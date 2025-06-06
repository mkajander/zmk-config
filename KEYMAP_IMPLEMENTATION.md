# Corne Choc Pro Keymap Implementation

## Layer Configuration

This keymap has 5 layers with the following access pattern:

```
Thumb cluster: | GUI | PROG | SPC |  | ENT | FUNCTION | NUMBER |
                     hold           hold    toggle
```

### Layer 0 - Base (QWERTY + Finnish)

```
| ESC  |  Q  |  W  |  E  |  R  |  T  |LALT|RALT|  Y  |  U  |   I  |  O  |  P  | BSPC |
| TAB  |  A  |  S  |  D  |  F  |  G  |LCTRL|RCTRL|  H  |  J  |   K  |  L  |  Ö  |  Ä   |
| SHFT |  Z  |  X  |  C  |  V  |  B  |     |     |  N  |  M  |   ,  |  .  |  -  | SHFT |
```

- Standard QWERTY with Ö and Ä in semicolon/quote positions
- Requires OS keyboard layout set to Finnish

### Layer 1 - Number (Toggle)

```
|TRANS|  1  |  2  |  3  |  4  |  5  |TRANS|TRANS|  6  |  7  |  8  |  9  |  0  |TRANS|
|TRANS|  +  |  -  |  *  |  /  |  =  |TRANS|TRANS|  %  |  ^  |  &  |  |  |  (  |  )  |
|TRANS|  <  |  >  | <=  | >=  | !=  |     |     |TRANS|TRANS|TRANS|TRANS|TRANS|TRANS|
```

- Numbers 0-9
- Basic math operators: + - * / = % ^ & | ( ) < >
- Comparison macros: <= >= !=

### Layer 2 - Function (Hold)

```
|TRANS| F1  | F2  | F3  | F4  | F5  |TRANS|TRANS| F6  | F7  | F8  | F9  | F10 | DEL  |
|TRANS| F11 | F12 |  ?  |  :  |  ;  |TRANS|TRANS|  ←  |  ↓  |  ↑  |  →  |PGUP |PGDN  |
|TRANS| '   | "   |  <  |  >  |  "  |     |     |HOME | END |UNDO |REDO |STAB |TRANS|
```

- Function keys F1-F12
- Arrow keys and navigation (HOME, END, PGUP, PGDN)
- Basic punctuation: ? : ; ' "
- Editing functions: UNDO, REDO, Shift+TAB

### Layer 3 - Programming (Hold)

```
|TRANS|  {  |  }  |  [  |  ]  |  \  |TRANS|TRANS|  `  |  ~  |  !  |  @  |  #  |TRANS|
|TRANS|  (  |  )  |  <  |  >  |  /  |TRANS|TRANS|  "  |  '  |  :  |  ;  |  ?  |TRANS|
|TRANS|  $  |  %  |  ^  |  &  |  *  |     |     |  |  |  \  |  +  |  -  |  =  |TRANS|
```

- All bracket types: { } [ ] ( ) < >
- Quotes and punctuation: " ' : ; ? ! ` ~
- Programming symbols: @ # $ % ^ & * | \ + - =

### Layer 4 - Keyboard (3-key combo: PROG + FUNCTION + NUMBER)

```
|TRANS| BT1 | BT2 | BT3 | BT4 | BT5 |TRANS|TRANS|     |     |     |     |     |TRANS|
|TRANS|BTCLR|RGBTG| RST |BOOT |UNLCK|TRANS|TRANS| ←   | ↓   | ↑   | →   |     |TRANS|
|TRANS|     |     |     |     |     |     |     |     |     |     |     |     |TRANS|
```

- Bluetooth device selection (BT1-BT5)
- Bluetooth clear (BTCLR)
- RGB toggle (RGBTG)
- System reset (RST)
- Bootloader mode (BOOT)
- Studio unlock (UNLCK)

## Macros

Three comparison operator macros using Finnish keys:

```c
less_equal: FI_LT + FI_EQUAL     // <=
greater_equal: FI_GT + FI_EQUAL  // >=
not_equal: FI_EXCL + FI_EQUAL    // !=
```

## Hardware Features

**Encoders (preserved):**
- Volume control
- Page up/down
- Media previous/next
- Brightness control

**Combo Access:**
- Keyboard layer requires holding thumb positions 41 + 44 + 45 simultaneously
- Prevents accidental system function activation

## Key Header

Uses `keys_fi.h` for Finnish keyboard layout support. All key references use `FI_*` prefixes to ensure correct character output when OS is set to Finnish layout.

## Build Requirements

- ZMK firmware
- OS keyboard layout set to Finnish
- Standard Corne Choc Pro board definition 