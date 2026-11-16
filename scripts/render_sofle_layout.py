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
from html import escape
from pathlib import Path

# Layer names and how to get to each layer. Edit these when the layout changes.
LAYERS = {
    0: ("Base", "default layer"),
    1: ("Symbols", "hold L1 (left thumb)"),
    2: ("Function and navigation", "hold L2 (right thumb)"),
    3: ("Numbers and math", "hold L3 (right thumb)"),
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


def legend(code):
    """Return (label, sublabel, kind) for a Vial keycode."""
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
U = 62
KEY = 56
PAD = 24
TOP = 58
WIDTH_U = 15.4
STAGGER = [0.37, 0.37, 0.12, 0.0, 0.12, 0.25]
THUMB_X = [1.5, 2.5, 3.5, 4.5, 5.6]
THUMB_Y = [4.4, 4.4, 4.4, 4.4, 4.55]
ENC_X, ENC_Y = 6.2, 3.25


def position(row, col):
    """Return (x, y, is_encoder) in key units for a matrix position."""
    hand, r = divmod(row, 5)
    if r < 4:
        x, y, enc = col, r + STAGGER[col], False
    elif col < 5:
        x, y, enc = THUMB_X[col], THUMB_Y[col], False
    else:
        x, y, enc = ENC_X, ENC_Y, True
    if hand == 1:
        x = WIDTH_U - 1 - x
    return x, y, enc


STYLE = {
    "key":   ("#ffffff", "#afb8c1", "#1f2328", ""),
    "mod":   ("#eaeef2", "#afb8c1", "#424a53", ""),
    "layer": ("#ddf4ff", "#54aeff", "#0550ae", ""),
    "held":  ("#0969da", "#0969da", "#ffffff", ""),
    "trans": ("none", "#d0d7de", "#8c959f", ' stroke-dasharray="4 3"'),
    "none":  ("none", "#d0d7de", "#8c959f", ' stroke-dasharray="4 3"'),
}


def font_size(label):
    return {1: 22, 2: 19, 3: 16, 4: 14}.get(len(label), 12)


def draw_key(out, x, y, enc, label, sub, kind):
    fill, stroke, ink, dash = STYLE[kind]
    px = PAD + x * U + (U - KEY) / 2
    py = TOP + y * U + (U - KEY) / 2
    cx, cy = px + KEY / 2, py + KEY / 2
    if enc:
        out.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{KEY / 2:.1f}" '
                   f'fill="{fill}" stroke="{stroke}" stroke-width="1.5"{dash}/>')
    else:
        out.append(f'<rect x="{px:.1f}" y="{py:.1f}" width="{KEY}" height="{KEY}" rx="8" '
                   f'fill="{fill}" stroke="{stroke}" stroke-width="1.5"{dash}/>')
    if not label:
        return
    size = font_size(label)
    if kind in ("trans", "none"):
        size = min(size, 14)
    weight = "400" if kind in ("trans", "none", "mod") else "600"
    ty = cy + size * 0.36 - (6 if sub else 0)
    out.append(f'<text x="{cx:.1f}" y="{ty:.1f}" font-size="{size}" font-weight="{weight}" '
               f'fill="{ink}" text-anchor="middle">{escape(label)}</text>')
    if sub:
        out.append(f'<text x="{cx:.1f}" y="{py + KEY - 8:.1f}" font-size="9.5" '
                   f'fill="{ink}" opacity="0.75" text-anchor="middle">{escape(sub)}</text>')


def render(vil, layer):
    base = vil["layout"][0]
    keys = vil["layout"][layer]
    name, access = LAYERS.get(layer, (f"Layer {layer}", ""))
    width = WIDTH_U * U + 2 * PAD
    height = TOP + 5.55 * U + PAD + 16
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width:.0f} {height:.0f}" '
        f'width="{width:.0f}" height="{height:.0f}" '
        'font-family="-apple-system, \'Segoe UI\', Helvetica, Arial, sans-serif">',
        f'<rect x="0.5" y="0.5" width="{width - 1:.0f}" height="{height - 1:.0f}" rx="14" '
        'fill="#f6f8fa" stroke="#d0d7de"/>',
        f'<text x="{PAD + 4}" y="38" font-size="20" font-weight="600" fill="#1f2328">'
        f'Layer {layer} · {escape(name)}</text>',
        f'<text x="{width - PAD - 4:.0f}" y="38" font-size="14" fill="#57606a" '
        f'text-anchor="end">{escape(access)}</text>',
    ]
    for row in range(10):
        for col in range(6):
            code = keys[row][col]
            x, y, enc = position(row, col)
            label, sub, kind = legend(code)
            if layer != 0 and kind == "trans":
                # Show the base key in gray: this position falls through.
                label, sub, base_kind = legend(base[row][col])
                if base[row][col] == f"LT{layer}(KC_NO)":
                    kind = "held"
                elif base_kind in ("trans", "none"):
                    label = sub = ""
            draw_key(out, x, y, enc, label, sub, kind)

    # Encoder rotation, written under each encoder.
    for index, enc_x in enumerate((ENC_X, WIDTH_U - 1 - ENC_X)):
        pair = vil["encoder_layout"][layer][index]
        gray = layer != 0 and pair == ["KC_TRNS", "KC_TRNS"]
        if gray:
            pair = vil["encoder_layout"][0][index]
        ccw, cw = (legend(code)[0] for code in pair)
        cx = PAD + enc_x * U + U / 2
        cy = TOP + ENC_Y * U - 4
        out.append(f'<text x="{cx:.1f}" y="{cy:.1f}" font-size="11" '
                   f'fill="{"#8c959f" if gray else "#424a53"}" text-anchor="middle">'
                   f'↺ {escape(ccw)} · {escape(cw)} ↻</text>')

    note = ("Gray keys with a dashed outline fall through to the base layer."
            if layer != 0 else
            "Round keys are the encoder push switches. The text above each one shows the rotation.")
    out.append(f'<text x="{width / 2:.0f}" y="{height - 14:.0f}" font-size="12" '
               f'fill="#57606a" text-anchor="middle">{escape(note)}</text>')
    out.append("</svg>")
    return "\n".join(out) + "\n"


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
