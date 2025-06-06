# Corne Choc Pro - Layout Visualization

## Physical Layout Overview

```
┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐
│     │     │     │     │     │     │ENC1 │ENC3 │     │     │     │     │     │     │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│     │     │     │     │     │     │ENC2 │ENC4 │     │     │     │     │     │     │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┴─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│     │     │     │     │     │     │           │     │     │     │     │     │     │
└─────┴─────┴─────┼─────┼─────┼─────│           │─────┼─────┼─────┼─────┴─────┴─────┘
                  │     │     │     │           │     │     │     │
                  └─────┴─────┴─────┘           └─────┴─────┴─────┘

        ENC1: VOL±     ENC2: PG±     ENC3: TRACK±     ENC4: BRIGHT±
```

## Layer 0: BASE (Default)

```
┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐
│ ESC │  Q  │  W  │  E  │  R  │  T  │LALT │RALT │  Y  │  U  │  I  │  O  │  P  │BSPC │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ TAB │  A  │  S  │  D  │  F  │  G  │LCTRL│RCTRL│  H  │  J  │  K  │  L  │  Ö  │  Ä  │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┴─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│SHIFT│  Z  │  X  │  C  │  V  │  B  │           │  N  │  M  │  ,  │  .  │  -  │SHIFT│
└─────┴─────┴─────┼─────┼─────┼─────│           │─────┼─────┼─────┼─────┴─────┴─────┘
                  │ GUI │PROG │ SPC │           │ ENT │FUNC │ NUM │
                  └─────┴─────┴─────┘           └─────┴─────┴─────┘
```

**Key Features:**
- Standard QWERTY layout with Finnish characters Ö and Ä
- Modifier keys in encoder positions: LALT/RALT (top), LCTRL/RCTRL (middle)
- ESC in top-left, TAB for IDE work
- Shift keys on both outer edges

## Layer 1: NUMBER (Toggle)

```
┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐
│ --- │  1  │  2  │  3  │  4  │  5  │ --- │ --- │  6  │  7  │  8  │  9  │  0  │ --- │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ --- │  +  │  -  │  *  │  /  │  =  │ --- │ --- │  %  │  ^  │  &  │  |  │  (  │  )  │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┴─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ --- │  <  │  >  │ <=  │ >=  │ !=  │           │ --- │ --- │ --- │ --- │ --- │ --- │
└─────┴─────┴─────┼─────┼─────┼─────│           │─────┼─────┼─────┼─────┴─────┴─────┘
                  │ --- │ --- │ --- │           │ --- │ --- │ --- │
                  └─────┴─────┴─────┘           └─────┴─────┴─────┘
```

**Key Features:**
- Numbers 0-9 in standard layout
- Mathematical operators: + - * / = % ^ & | ( )
- Comparison operators: < > <= >= !=
- Toggle layer - tap NUM to enter/exit

## Layer 2: FUNCTION (Hold)

```
┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐
│ --- │ F1  │ F2  │ F3  │ F4  │ F5  │ --- │ --- │ F6  │ F7  │ F8  │ F9  │ F10 │ DEL │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ --- │ F11 │ F12 │  ?  │  :  │  ;  │ --- │ --- │  ←  │  ↓  │  ↑  │  →  │PGUP │PGDN │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┴─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ --- │  '  │  "  │  <  │  >  │  "  │           │HOME │ END │UNDO │REDO │S+TAB│ --- │
└─────┴─────┴─────┼─────┼─────┼─────│           │─────┼─────┼─────┼─────┴─────┴─────┘
                  │ --- │ --- │ --- │           │ --- │---  │ --- │
                  └─────┴─────┴─────┘           └─────┴─────┴─────┘
```

**Key Features:**
- Function keys F1-F12
- Arrow key navigation
- Home/End, Page Up/Down
- Undo/Redo, Shift+Tab
- Basic punctuation: ? : ; ' "

## Layer 3: PROGRAMMING (Hold)

```
┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐
│ --- │  {  │  }  │  [  │  ]  │  \  │ --- │ --- │  `  │  ~  │  !  │  @  │  #  │ --- │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ --- │  (  │  )  │  <  │  >  │  /  │ --- │ --- │  "  │  '  │  :  │  ;  │  ?  │ --- │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┴─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ --- │  $  │  %  │  ^  │  &  │  *  │           │  |  │  \  │  +  │  -  │  =  │ --- │
└─────┴─────┴─────┼─────┼─────┼─────│           │─────┼─────┼─────┼─────┴─────┴─────┘
                  │ --- │PROG │ --- │           │ --- │ --- │ --- │
                  └─────┴─────┴─────┘           └─────┴─────┴─────┘
```

**Key Features:**
- All bracket types: { } [ ] ( ) < >
- Programming symbols: $ @ # | \ ` ~ !
- String delimiters: " ' 
- Mathematical operators: + - * / = ^ % &
- Hold PROG key to access

## Layer 4: KEYBOARD (3-Key Combo: PROG+FUNC+NUM)

```
┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐
│ --- │ BT1 │ BT2 │ BT3 │ BT4 │ BT5 │ --- │ --- │ --- │ --- │ --- │ --- │ --- │ --- │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ --- │BTCLR│RGBTG│ RST │BOOT │UNLCK│ --- │ --- │  ←  │  ↓  │  ↑  │  →  │ --- │ --- │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┴─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ --- │ --- │ --- │ --- │ --- │ --- │           │ --- │ --- │ --- │ --- │ --- │ --- │
└─────┴─────┴─────┼─────┼─────┼─────│           │─────┼─────┼─────┼─────┴─────┴─────┘
                  │ --- │ --- │ --- │           │ --- │ --- │ --- │
                  └─────┴─────┴─────┘           └─────┴─────┴─────┘
```

**Key Features:**
- Bluetooth device selection (BT1-BT5)
- Bluetooth clear (BTCLR)
- RGB toggle (RGBTG)
- System reset (RST) and bootloader (BOOT)
- Studio unlock (UNLCK)
- Safety: Requires holding PROG+FUNC+NUM simultaneously

## Encoder Functions (All Layers)

- **Encoder 1 (Left-Top)**: Volume Down/Up
- **Encoder 2 (Left-Middle)**: Page Up/Down  
- **Encoder 3 (Right-Middle)**: Previous/Next Track
- **Encoder 4 (Right-Top)**: Brightness Down/Up

## Layer Access Summary

```
| GUI | PROG | SPC |             | ENT | FUNC | NUM |
```

- **BASE**: Default QWERTY + Finnish characters
- **PROG**: Hold for programming symbols (left thumb)
- **FUNC**: Hold for function keys and navigation (right thumb)  
- **NUM**: Toggle for numbers and math (right thumb)
- **KEYBOARD**: Hold PROG+FUNC+NUM simultaneously for system functions

## Finnish Character Support

- **Ö**: Accessed via `FI_O_UMLAUT` (semicolon position with Finnish OS layout)
- **Ä**: Accessed via `FI_A_UMLAUT` (quote position with Finnish OS layout)

**Important**: Requires OS keyboard layout set to Finnish for proper character output.

## Macros

Three comparison operators use Finnish keys:
- **<=**: `FI_LT` + `FI_EQUAL`
- **>=**: `FI_GT` + `FI_EQUAL` 
- **!=**: `FI_EXCL` + `FI_EQUAL` 