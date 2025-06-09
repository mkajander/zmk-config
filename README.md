# ZMK Config - Corne Choc Pro

[![Build ZMK firmware](https://github.com/mkajander/zmk-config/actions/workflows/build.yml/badge.svg?branch=main)](https://github.com/mkajander/zmk-config/actions/workflows/build.yml)

Personal ZMK config for the Corne Choc Pro. Designed for programming in C#, TypeScript, and JavaScript with Finnish character support.

**Now supports both Windows/Linux AND Mac!** Just switch between OS modes when you need to.

## Dual OS Support

This keyboard has separate layers for different operating systems:

### Windows/Linux Mode (Layers 0-3)
- Uses AltGr for special characters (like @ = AltGr+2)
- Standard Finnish layout symbols
- Works with Windows or Linux set to Finnish keyboard layout

### Mac Mode (Layers 4-7) 
- Uses Option key for special characters (like @ = Option+2)
- Mac Finnish layout symbols  
- Works with macOS set to Finnish keyboard layout

**Both modes produce identical results** - just optimized for how each OS handles key combinations.

## Layout

### Base Layer / Base Mac
QWERTY layout with Finnish Ö and Ä characters. ESC in top-left, standard modifiers.
Mac version uses Cmd instead of Ctrl keys where appropriate.

### Number Layer / Number Mac (toggle)
Numbers 0-9 with math operators: `+ - * / = % ^ & | ( ) < >`
Includes comparison macros: `<=`, `>=`, `!=`
Also has: `€ $ §` symbols

### Function Layer / Function Mac (hold)
Function keys F1-F12, arrow keys, page navigation, and basic punctuation: `? : ; ' " < >`
Mac version uses proper Cmd+Z/Cmd+Shift+Z for undo/redo.

### Programming Layer / Programming Mac (hold)  
All programming symbols: `{ } [ ] ( ) \ ` ~ ! @ # " ' : ; ? $ % ^ & * | + - =`

### Keyboard Layer (3-key combo)
Bluetooth management, RGB controls, system reset functions.
**Plus OS switching buttons and layer test macros.**

## Switching Between OS Modes

1. **Access keyboard layer**: Hold 3 keys simultaneously:
   - Left combo: `GUI + PROG + SPACE` 
   - Right combo: `ENT + FUNCTION + NUMBER`

2. **Switch OS mode**:
   - Press **WIN/L** button → Switch to Windows/Linux mode
   - Press **MAC** button → Switch to Mac mode

3. **Test which mode you're in**:
   - Press **WTEST** → Goes to Windows mode and types "win-mode"
   - Press **MTEST** → Goes to Mac mode and types "mac-mode"

Once you switch modes, it stays that way until you manually change it.

## Layer Access

```
| GUI | PROG | SPC |             | ENT | FUNCTION | NUMBER |
```

- **PROG** - Hold for programming symbols (PROG or PROG_MAC depending on mode)
- **FUNCTION** - Hold for F-keys and navigation (FUNCTION or FUNCTION_MAC)
- **NUMBER** - Toggle for numbers and math (NUMBER or NUMBER_MAC)
- **Keyboard** - Hold any 3-key combo above for system controls

## Hardware

Preserves all encoder functions: volume, page scroll, media control, brightness.

## Setup

1. Flash the firmware to your keyboard
2. Set your OS keyboard layout to Finnish 
3. Use the keyboard layer to switch to your OS mode (Windows/Linux or Mac)
4. Start typing!

The keyboard remembers which OS mode you selected, so you only need to switch when changing computers. 