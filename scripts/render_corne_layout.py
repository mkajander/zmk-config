#!/usr/bin/env python3
"""Draw the Corne Choc Pro layers from the ZMK keymap as SVG images.

Usage:
    python scripts/render_corne_layout.py

The script reads config/corne_choc_pro.keymap for the bindings and
config/corne_choc_pro.json for the key positions. It writes one image for
each Windows/Linux layer and one for the keyboard layer to images/corne/.

The Mac layers must make the same characters as the Windows/Linux layers.
The script compares them and stops with an error if they are different.
The script also stops if it finds a binding that it cannot name.
"""

import json
import re
from pathlib import Path

from keyboard_svg import BASE_NOTE, FALL_THROUGH_NOTE, document, draw_key

# Layer index: (title, how to get to the layer). Only these layers get an image.
LAYERS = {
    0: ("Base", "default layer"),
    1: ("Number", "hold Num, or double tap Num to lock"),
    2: ("Function", "hold Func (right thumb)"),
    3: ("Programming", "hold Prog (left thumb)"),
    8: ("Keyboard", "press all three thumb keys of one hand"),
}
# Mac layer: the Windows/Linux layer that it must match.
MAC_TWIN = {4: 0, 5: 1, 6: 2, 7: 3}
# Short names for the layer keys.
LAYER_KEY = {"NUMBER": "Num", "FUNCTION": "Func", "PROG": "Prog",
             "BASE": "Win", "KEYBOARD": "Kbd"}

SYMBOL = {
    "O_UMLAUT": "ö", "A_UMLAUT": "ä", "COMMA": ",", "DOT": ".", "MINUS": "-",
    "PLUS": "+", "ASTRK": "*", "FSLH": "/", "EQUAL": "=", "PRCNT": "%",
    "CARET": "^", "AMPS": "&", "PIPE": "|", "LPAR": "(", "RPAR": ")",
    "LT": "<", "GT": ">", "EURO": "€", "DLLR": "$", "SECT": "§",
    "QMARK": "?", "COLON": ":", "SEMI": ";", "SQT": "'", "DQT": '"',
    "LBRC": "{", "RBRC": "}", "LBKT": "[", "RBKT": "]", "BSLH": "\\",
    "GRAVE": "`", "TILDE": "~", "UNDER": "_", "EXCL": "!", "AT": "@", "HASH": "#",
}
PLAIN = {
    "ESC": "Esc", "TAB": "Tab", "BSPC": "Bksp", "RET": "Enter", "DEL": "Del",
    "SPACE": "Space", "LSHFT": "Shift", "RSHFT": "Shift", "LCTRL": "Ctrl",
    "RCTRL": "Ctrl", "LALT": "Alt", "RALT": "AltGr", "LGUI": "GUI",
    "LEFT": "←", "DOWN": "↓", "UP": "↑", "RIGHT": "→",
    "PG_UP": "PgUp", "PG_DN": "PgDn", "HOME": "Home", "END": "End",
    "K_UNDO": "Undo", "K_REDO": "Redo", "LS(TAB)": "⇧Tab",
    # The Mac layers send Cmd+Z and Cmd+Shift+Z for undo and redo.
    "LG(Z)": "Undo", "LG(LS(Z))": "Redo",
    "C_VOL_DN": "Vol−", "C_VOL_UP": "Vol+", "C_PREV": "Prev", "C_NEXT": "Next",
    "C_BRI_DN": "Bri−", "C_BRI_UP": "Bri+",
}
MODS = {"Esc", "Tab", "Bksp", "Enter", "Del", "Space", "Shift", "Ctrl", "Alt",
        "AltGr", "GUI"}
OTHER = {
    "trans": ("", "", "trans"),
    "arrow": ("=>", "macro", "key"),
    "td_num": ("Num", "hold / 2×", "layer"),
    "bt BT_CLR": ("BT clr", "", "sys"),
    "rgb_ug RGB_TOG": ("RGB", "on/off", "sys"),
    "sys_reset": ("Reset", "", "sys"),
    "bootloader": ("Boot", "loader", "sys"),
    "studio_unlock": ("Unlock", "Studio", "sys"),
    "layer_indicator_win": ("Win", "+ type text", "layer"),
    "layer_indicator_mac": ("Mac", "+ type text", "layer"),
}


def legend(binding):
    """Return (label, sublabel, kind) for one ZMK binding, without the '&'."""
    # The Mac names make the same characters, so drop the Mac marker.
    text = re.sub(r"\bFI_MAC_", "FI_", binding)
    text = re.sub(r"\bmac_arrow\b", "arrow", text)
    text = text.replace("td_num_mac", "td_num").replace("_MAC", "")
    if text in OTHER:
        return OTHER[text]
    name, _, arg = text.partition(" ")
    if name == "kp":
        key = re.sub(r"\bFI_", "", arg)
        if key in PLAIN:
            label = PLAIN[key]
            return (label, "", "mod" if label in MODS else "key")
        if arg.startswith("FI_"):
            if re.fullmatch(r"[A-Z]|F\d+", key):
                return (key, "", "key")
            if re.fullmatch(r"N\d", key):
                return (key[1], "", "key")
            if key in SYMBOL:
                return (SYMBOL[key], "", "key")
        if re.fullmatch(r"F\d+", arg):
            return (arg, "", "key")
    if name in ("mo", "tog", "to") and arg in LAYER_KEY:
        sub = {"mo": "hold", "tog": "on/off", "to": "mode"}[name]
        label = "Mac" if binding.endswith("BASE_MAC") else LAYER_KEY[arg]
        return (label, sub, "layer")
    m = re.fullmatch(r"bt BT_SEL (\d)", text)
    if m:
        return (f"BT {int(m.group(1)) + 1}", "", "sys")
    raise SystemExit(f"error: no legend for binding &{binding}")


def parse_keymap(path):
    """Return a list of layers. Each layer is (bindings, sensor bindings)."""
    text = re.sub(r"//[^\n]*", "", path.read_text(encoding="utf-8"))
    text = text[text.index('compatible = "zmk,keymap"'):]
    layers = []
    for block in re.finditer(r"\w+\s*\{[^{}]*?\bbindings\s*=\s*<([^;]*?)>\s*;([^{}]*)\}", text):
        sensors = re.search(r"sensor-bindings\s*=\s*<([^;]*?)>\s*;", block.group(2))
        split = lambda s: [" ".join(b.split()) for b in s.split("&") if b.strip()]
        layers.append((split(block.group(1)), split(sensors.group(1)) if sensors else []))
    return layers


def render(layers, positions, index):
    title, access = LAYERS[index]
    base = layers[0][0]
    keys = layers[index][0]
    out = []
    for i, pos in enumerate(positions):
        label, sub, kind = legend(keys[i])
        if index != 0 and kind == "trans":
            label, sub, base_kind = legend(base[i])
            hold = {1: "td_num", 2: "mo FUNCTION", 3: "mo PROG"}.get(index)
            kind = "held" if base[i] == hold else "trans"
        rotate = (pos["r"], pos["rx"], pos["ry"]) if "r" in pos else None
        draw_key(out, pos["x"], pos["y"], label, sub, kind,
                 h=pos.get("h", 1.0), rotate=rotate)

    note = FALL_THROUGH_NOTE if index != 0 else BASE_NOTE
    return document(f"Layer {index} · {title}", access, note, 15, 4.6, out)


def main():
    root = Path(__file__).resolve().parent.parent
    layers = parse_keymap(root / "config" / "corne_choc_pro.keymap")
    layout = json.loads((root / "config" / "corne_choc_pro.json").read_text(encoding="utf-8"))
    positions = layout["layouts"]["default_layout"]["layout"]
    for index, (keys, _) in enumerate(layers):
        if len(keys) != len(positions):
            raise SystemExit(f"error: layer {index} has {len(keys)} bindings, "
                             f"but the layout has {len(positions)} keys")

    for mac, win in MAC_TWIN.items():
        for i, (a, b) in enumerate(zip(layers[mac][0], layers[win][0])):
            if legend(a) != legend(b):
                raise SystemExit(f"error: layer {mac} key {i} (&{a}) does not match "
                                 f"layer {win} (&{b})")

    target = root / "images" / "corne"
    target.mkdir(parents=True, exist_ok=True)
    for index in LAYERS:
        path = target / f"layer-{index}.svg"
        path.write_text(render(layers, positions, index), encoding="utf-8", newline="\n")
        print(f"wrote {path}")


if __name__ == "__main__":
    main()
