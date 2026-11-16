"""Shared SVG drawing code for the layout images."""

from html import escape

U = 62      # one key unit, in pixels
KEY = 56    # key cap size, in pixels
PAD = 24
TOP = 58

# kind: (fill, outline, text color, extra outline attributes)
STYLE = {
    "key":   ("#ffffff", "#afb8c1", "#1f2328", ""),
    "mod":   ("#eaeef2", "#afb8c1", "#424a53", ""),
    "layer": ("#ddf4ff", "#54aeff", "#0550ae", ""),
    "held":  ("#0969da", "#0969da", "#ffffff", ""),
    "sys":   ("#fff8c5", "#d4a72c", "#7d4e00", ""),
    "trans": ("none", "#d0d7de", "#8c959f", ' stroke-dasharray="4 3"'),
    "none":  ("none", "#d0d7de", "#8c959f", ' stroke-dasharray="4 3"'),
}

FALL_THROUGH_NOTE = "Gray keys with a dashed outline fall through to the base layer."


def font_size(label):
    return {1: 22, 2: 19, 3: 16, 4: 14}.get(len(label), 12)


def draw_key(out, x, y, label, sub, kind, round_key=False, h=1.0, rotate=None):
    """Draw one key. x, y and h are in key units. rotate is (degrees, cx, cy)."""
    fill, stroke, ink, dash = STYLE[kind]
    gap = (U - KEY) / 2
    px, py = PAD + x * U + gap, TOP + y * U + gap
    height = h * U - 2 * gap
    cx, cy = px + KEY / 2, py + height / 2
    if rotate:
        deg, rx, ry = rotate
        out.append(f'<g transform="rotate({deg} {PAD + rx * U:.1f} {TOP + ry * U:.1f})">')
    if round_key:
        out.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{KEY / 2:.1f}" '
                   f'fill="{fill}" stroke="{stroke}" stroke-width="1.5"{dash}/>')
    else:
        out.append(f'<rect x="{px:.1f}" y="{py:.1f}" width="{KEY}" height="{height:.1f}" rx="8" '
                   f'fill="{fill}" stroke="{stroke}" stroke-width="1.5"{dash}/>')
    if label:
        size = font_size(label)
        faint = kind in ("trans", "none")
        if faint:
            size = min(size, 14)
        weight = "400" if faint or kind == "mod" else "600"
        ty = cy + size * 0.36 - (6 if sub else 0)
        out.append(f'<text x="{cx:.1f}" y="{ty:.1f}" font-size="{size}" font-weight="{weight}" '
                   f'fill="{ink}" text-anchor="middle">{escape(label)}</text>')
        if sub:
            out.append(f'<text x="{cx:.1f}" y="{cy + 20:.1f}" font-size="9.5" '
                       f'fill="{ink}" opacity="0.75" text-anchor="middle">{escape(sub)}</text>')
    if rotate:
        out.append("</g>")


def draw_rotation(out, x, y, ccw, cw, gray=False, below=False, dx=0):
    """Write what an encoder sends when you turn it, above or below the key at x, y.

    dx moves the text sideways, in pixels.
    """
    cx = PAD + x * U + U / 2 + dx
    cy = TOP + y * U + (U + 9 if below else -4)
    out.append(f'<text x="{cx:.1f}" y="{cy:.1f}" font-size="10.5" '
               f'fill="{"#8c959f" if gray else "#424a53"}" text-anchor="middle">'
               f'↺ {escape(ccw)} · {escape(cw)} ↻</text>')


def document(title, access, note, width_u, height_u, body):
    """Wrap the key drawings in an SVG document with a title bar and a note."""
    width = width_u * U + 2 * PAD
    height = TOP + height_u * U + PAD + 16
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width:.0f} {height:.0f}" '
        f'width="{width:.0f}" height="{height:.0f}" '
        'font-family="-apple-system, \'Segoe UI\', Helvetica, Arial, sans-serif">',
        f'<rect x="0.5" y="0.5" width="{width - 1:.0f}" height="{height - 1:.0f}" rx="14" '
        'fill="#f6f8fa" stroke="#d0d7de"/>',
        f'<text x="{PAD + 4}" y="38" font-size="20" font-weight="600" fill="#1f2328">'
        f'{escape(title)}</text>',
        f'<text x="{width - PAD - 4:.0f}" y="38" font-size="14" fill="#57606a" '
        f'text-anchor="end">{escape(access)}</text>',
    ]
    out.extend(body)
    out.append(f'<text x="{width / 2:.0f}" y="{height - 14:.0f}" font-size="12" '
               f'fill="#57606a" text-anchor="middle">{escape(note)}</text>')
    out.append("</svg>")
    return "\n".join(out) + "\n"
