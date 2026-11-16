#!/usr/bin/env python3
"""Draw the Sofle layers from a Vial export as SVG images.

Usage:
    python scripts/render_sofle_layout.py [current-sofle.vil] [images/sofle]

The legends show the characters that the Finnish OS keyboard layout makes.
The script stops with an error if it finds a keycode that it cannot name.
"""

import json
import re
import sys
from pathlib import Path

from keyboard_svg import BASE_NOTE, FALL_THROUGH_NOTE, document, draw_key

# Layer names and how to get to each layer. Edit these when the layout changes.
LAYERS = {
    0: ("Base", "default layer"),
    1: ("Symbols", "hold L1 (left thumb)"),
    2: ("Function and navigation", "hold L2 (right thumb)"),
    3: ("Numbers and math", "hold L3, or double tap L3 to lock"),
    9: ("Game", "toggle with the combo Esc + § + 1 + 0"),
}

# Unshifted keys, as the Finnish OS layout reads them.
PLAIN = {
    "ESCAPE": "Esc", "TAB": "Tab", "SPACE": "Space", "ENTER": "Enter",
    "BSPACE": "Bksp", "DELETE": "Del", "INSERT": "Ins",
    "LSHIFT": "Shift", "RSHIFT": "Shift", "LCTRL": "Ctrl", "RCTRL": "Ctrl",
    "LALT": "Alt", "RALT": "AltGr", "LGUI": "GUI", "RGUI": "GUI",
    "GRAVE": "§", "MINUS": "+", "EQUAL": "´", "LBRACKET": "å",
    "RBRACKET": "¨", "BSLASH": "'", "NONUS_HASH": "'", "SCOLON": "ö",
    "QUOTE": "ä", "NONUS_BSLASH": "<", "COMMA": ",", "DOT": ".", "SLASH": "-",
    "LEFT": "←", "DOWN": "↓", "UP": "↑", "RIGHT": "→",
    "PGUP": "PgUp", "PGDOWN": "PgDn", "HOME": "Home", "END": "End",
    "UNDO": "Undo", "AGIN": "Again",
    "VOLD": "Vol−", "VOLU": "Vol+", "MPRV": "Prev", "MNXT": "Next",
    "MUTE": "Mute", "MPLY": "Play",
}
SHIFTED = {
    "1": "!", "2": '"', "3": "#", "4": "¤", "5": "%", "6": "&", "7": "/",
    "8": "(", "9": ")", "0": "=", "MINUS": "?", "EQUAL": "`", "RBRACKET": "^",
    "BSLASH": "*", "NONUS_HASH": "*", "NONUS_BSLASH": ">", "COMMA": ";",
    "DOT": ":", "SLASH": "_", "TAB": "⇧Tab",
}
ALTGR = {
    "2": "@", "3": "£", "4": "$", "5": "€", "7": "{", "8": "[", "9": "]",
    "0": "}", "MINUS": "\\", "RBRACKET": "~", "NONUS_BSLASH": "|",
}
KEYPAD = {
    "PLUS": "+", "MINUS": "−", "ASTERISK": "×", "SLASH": "÷", "EQUAL": "=",
    "DOT": ".", "ENTER": "Enter",
}
MODS = {"Esc", "Tab", "Space", "Enter", "Bksp", "Del", "Ins", "Shift", "Ctrl",
        "Alt", "AltGr", "GUI"}


def tap_dance_layer(vil, code):
    """Return the layer of a "hold for layer, double tap to lock" tap dance key.

    Return None if the keycode is not a tap dance key.
    """
    m = re.fullmatch(r"TD\((\d+)\)", code)
    if not m:
        return None
    entry = vil["tap_dance"][int(m.group(1))]
    tap, hold, double, tap_hold = entry[:4]
    layer = re.fullmatch(r"MO\((\d+)\)", hold)
    if not layer or double != f"TG({layer.group(1)})" or (tap, tap_hold) != ("KC_NO", "KC_NO"):
        raise SystemExit(f"error: no legend for tap dance {code}: {entry}")
    return int(layer.group(1))


def legend(code, vil=None):
    """Return (label, sublabel, kind) for a Vial keycode."""
    if vil is not None and code.startswith("TD("):
        return (f"L{tap_dance_layer(vil, code)}", "hold / 2×", "layer")
    if code == "KC_TRNS":
        return ("", "", "trans")
    if code == "KC_NO":
        return ("", "", "none")
    m = re.fullmatch(r"LT(\d+)\(KC_NO\)", code)
    if m:
        return ("L" + m.group(1), "hold", "layer")
    m = re.fullmatch(r"(TG|MO|TO)\((\d+)\)", code)
    if m:
        return ("L" + m.group(2), m.group(1).lower(), "layer")
    m = re.fullmatch(r"(LSFT|RALT)\(KC_(\w+)\)", code)
    if m:
        table = SHIFTED if m.group(1) == "LSFT" else ALTGR
        if m.group(2) in table:
            return (table[m.group(2)], "", "key")
    m = re.fullmatch(r"KC_KP_(\w+)", code)
    if m:
        name = m.group(1)
        if name.isdigit():
            return (name, "numpad", "key")
        if name in KEYPAD:
            return (KEYPAD[name], "numpad", "key")
    m = re.fullmatch(r"KC_(\w+)", code)
    if m:
        name = m.group(1)
        if re.fullmatch(r"[A-Z0-9]|F\d+", name):
            return (name, "", "key")
        if name in PLAIN:
            label = PLAIN[name]
            return (label, "", "mod" if label in MODS else "key")
    raise SystemExit(f"error: no legend for keycode {code}")


# Geometry, in key units. Column 0 is the outer column of each hand.
WIDTH_U = 15.4
HEIGHT_U = 5.55
STAGGER = [0.37, 0.37, 0.12, 0.0, 0.12, 0.25]
THUMB_X = [1.5, 2.5, 3.5, 4.5, 5.6]
THUMB_Y = [4.4, 4.4, 4.4, 4.4, 4.55]
INNER_X, INNER_Y = 6.2, 3.25  # the extra key next to the bottom row


def position(row, col):
    """Return (x, y) in key units for a matrix position."""
    hand, r = divmod(row, 5)
    if r < 4:
        x, y = col, r + STAGGER[col]
    elif col < 5:
        x, y = THUMB_X[col], THUMB_Y[col]
    else:
        x, y = INNER_X, INNER_Y
    if hand == 1:
        x = WIDTH_U - 1 - x
    return x, y


def render(vil, layer):
    base = vil["layout"][0]
    keys = vil["layout"][layer]
    name, access = LAYERS.get(layer, (f"Layer {layer}", ""))
    out = []
    for row in range(10):
        for col in range(6):
            code = keys[row][col]
            x, y = position(row, col)
            label, sub, kind = legend(code, vil)
            if layer != 0 and kind == "trans":
                # Show the base key in gray: this position falls through.
                base_code = base[row][col]
                label, sub, base_kind = legend(base_code, vil)
                if base_code == f"LT{layer}(KC_NO)" or tap_dance_layer(vil, base_code) == layer:
                    kind = "held"
                elif base_kind in ("trans", "none"):
                    label = sub = ""
            draw_key(out, x, y, label, sub, kind)

    note = FALL_THROUGH_NOTE if layer != 0 else BASE_NOTE
    return document(f"Layer {layer} · {name}", access, note, WIDTH_U, HEIGHT_U, out)


def main():
    root = Path(__file__).resolve().parent.parent
    source = Path(sys.argv[1]) if len(sys.argv) > 1 else root / "current-sofle.vil"
    target = Path(sys.argv[2]) if len(sys.argv) > 2 else root / "images" / "sofle"
    vil = json.loads(source.read_text(encoding="utf-8"))
    target.mkdir(parents=True, exist_ok=True)
    for layer, keys in enumerate(vil["layout"]):
        used = any(code != "KC_TRNS" for row in keys for code in row)
        if not used:
            continue
        path = target / f"layer-{layer}.svg"
        path.write_text(render(vil, layer), encoding="utf-8", newline="\n")
        print(f"wrote {path}")


if __name__ == "__main__":
    main()
