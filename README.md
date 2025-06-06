# ZMK Config - Corne Choc Pro

[![Build ZMK firmware](https://github.com/mkajander/zmk-config/actions/workflows/build.yml/badge.svg?branch=main)](https://github.com/mkajander/zmk-config/actions/workflows/build.yml)

Personal ZMK config for the Corne Choc Pro. Designed for programming in C#, TypeScript, and JavaScript with Finnish character support.
All docs are AI generated, so they may be incorrect somewhere.

## Layout

### Base Layer
QWERTY layout with Finnish Ö and Ä characters. ESC in top-left, standard modifiers.

### Number Layer (toggle)
Numbers 0-9 with math operators: `+ - * / = % ^ & | ( ) < >`
Includes comparison macros: `<=`, `>=`, `!=`

### Function Layer (hold)
Function keys F1-F12, arrow keys, page navigation, and basic punctuation: `? : ; ' " < >`

### Programming Layer (hold)  
All programming symbols: `{ } [ ] ( ) \ ` ~ ! @ # " ' : ; ? $ % ^ & * | + - =`

### Keyboard Layer (3-key combo)
Bluetooth management, RGB controls, system reset functions.

## Layer Access

```
| GUI | PROG | SPC |             | ENT | FUNCTION | NUMBER |
```

- **PROG** - Hold for programming symbols
- **FUNCTION** - Hold for F-keys and navigation  
- **NUMBER** - Toggle for numbers and math
- **Keyboard** - Hold PROG + FUNCTION + NUMBER simultaneously

## Hardware

Preserves all encoder functions: volume, page scroll, media control, brightness.

## Setup

Standard ZMK build. Set your OS keyboard layout to Finnish for Ö/Ä support. 