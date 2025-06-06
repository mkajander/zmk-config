# Sofle Keyboard - Layout Visualization

## Physical Layout Overview

```
┌─────┬─────┬─────┬─────┬─────┬─────┐                    ┌─────┬─────┬─────┬─────┬─────┬─────┐
│     │     │     │     │     │     │                    │     │     │     │     │     │     │
├─────┼─────┼─────┼─────┼─────┼─────┤                    ├─────┼─────┼─────┼─────┼─────┼─────┤
│     │     │     │     │     │     │                    │     │     │     │     │     │     │
├─────┼─────┼─────┼─────┼─────┼─────┤                    ├─────┼─────┼─────┼─────┼─────┼─────┤
│     │     │     │     │     │     │                    │     │     │     │     │     │     │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┐        ┌─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│     │     │     │     │     │     │ ENC │        │ ENC │     │     │     │     │     │     │
└─────┴─────┴─────┼─────┼─────┼─────┼─────┤        ├─────┼─────┼─────┼─────┼─────┴─────┴─────┘
                  │     │     │     │     │        │     │     │     │     │
                  └─────┴─────┴─────┴─────┘        └─────┴─────┴─────┴─────┘

          [LEFT ENC]                        [RIGHT ENC]
          VOL±                              TRACK±
```

**Features:**
- **6×4 key matrix per hand** (58 keys total)
- **2 rotary encoders** with click functions
- **4 thumb keys per hand**
- **10 layers** defined (3 main active layers)
- **Nordic character support** via RALT combos

## Layer 0: BASE (QWERTY)

```
┌─────┬─────┬─────┬─────┬─────┬─────┐                    ┌─────┬─────┬─────┬─────┬─────┬─────┐
│ ESC │  Q  │  W  │  E  │  R  │  T  │                    │  Y  │  U  │  I  │  O  │  P  │BSPC │
├─────┼─────┼─────┼─────┼─────┼─────┤                    ├─────┼─────┼─────┼─────┼─────┼─────┤
│ TAB │  A  │  S  │  D  │  F  │  G  │                    │  H  │  J  │  K  │  L  │  ;  │  '  │
├─────┼─────┼─────┼─────┼─────┼─────┤                    ├─────┼─────┼─────┼─────┼─────┼─────┤
│SHIFT│  Z  │  X  │  C  │  V  │  B  │                    │  N  │  M  │  ,  │  .  │  /  │SHIFT│
├─────┼─────┼─────┼─────┼─────┼─────┼─────┐        ┌─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ ESC │  1  │  2  │  3  │  4  │  5  │VOL- │        │VOL+ │  6  │  7  │  8  │  9  │  0  │  `  │
└─────┴─────┴─────┼─────┼─────┼─────┼─────┤        ├─────┼─────┼─────┼─────┼─────┴─────┴─────┘
                  │ GUI │ ALT │CTRL │ LT1 │        │ LT2 │CTRL │ ALT │ GUI │
                  └─────┴─────┴─────┴─────┘        └─────┴─────┴─────┴─────┘
```

**Key Features:**
- Standard QWERTY layout with number row on bottom
- ESC in top-left for Vim users
- TAB for IDE workflow
- LT1 (Layer 1 when held) on left thumb
- LT2 (Layer 2 when held) on right thumb
- Volume controls integrated into encoder positions
- **Note**: No dedicated Space key (accessed via layer)

## Layer 1: NUMBERS & SYMBOLS (LT1 Hold)

```
┌─────┬─────┬─────┬─────┬─────┬─────┐                    ┌─────┬─────┬─────┬─────┬─────┬─────┐
│ --- │ KP1 │ KP2 │ KP3 │ KP4 │ KP5 │                    │ KP6 │ KP7 │ KP8 │ KP9 │ KP0 │ --- │
├─────┼─────┼─────┼─────┼─────┼─────┤                    ├─────┼─────┼─────┼─────┼─────┼─────┤
│ --- │  !  │  _  │  @  │  ^  │  $  │                    │  ~  │  "  │  \  │  ]  │  }  │ NO  │
├─────┼─────┼─────┼─────┼─────┼─────┤                    ├─────┼─────┼─────┼─────┼─────┼─────┤
│ --- │  +  │  =  │  -  │  |  │  &  │                    │  -  │  /  │  *  │  -  │  %  │  %  │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┐        ┌─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ --- │ --- │ --- │ --- │ --- │ --- │ --- │        │ --- │ --- │ --- │ --- │ --- │ --- │ --- │
└─────┴─────┴─────┼─────┼─────┼─────┼─────┤        ├─────┼─────┼─────┼─────┼─────┴─────┴─────┘
                  │ --- │ --- │ --- │ --- │        │ --- │ --- │ --- │ --- │
                  └─────┴─────┴─────┴─────┘        └─────┴─────┴─────┴─────┘
```

**Key Features:**
- Keypad numbers (KP1-KP0) for numpad functionality
- Programming symbols: `! _ @ ^ $ ~ " \ ] }`
- Math operators: `+ = - | & / * %`
- Nordic character access via NO key (RALT combinations)
- Spaces for additional math/programming symbols

## Layer 2: FUNCTIONS & NAVIGATION (LT2 Hold)

```
┌─────┬─────┬─────┬─────┬─────┬─────┐                    ┌─────┬─────┬─────┬─────┬─────┬─────┐
│ --- │ F1  │ F2  │ F3  │ F4  │ F5  │                    │ F6  │ F7  │ F8  │ F9  │ INS │ DEL │
├─────┼─────┼─────┼─────┼─────┼─────┤                    ├─────┼─────┼─────┼─────┼─────┼─────┤
│ --- │  (  │  )  │  [  │  ]  │  /  │                    │  ←  │  ↓  │  ↑  │  →  │PGUP │PGDN │
├─────┼─────┼─────┼─────┼─────┼─────┤                    ├─────┼─────┼─────┼─────┼─────┼─────┤
│ --- │  {  │  }  │  <  │  >  │  )  │                    │ F10 │ F11 │ F12 │HOME │ END │ --- │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┐        ┌─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ --- │ --- │ --- │ --- │ --- │ --- │ --- │        │ --- │ --- │ --- │ --- │ --- │ --- │ --- │
└─────┴─────┴─────┼─────┼─────┼─────┼─────┤        ├─────┼─────┼─────┼─────┼─────┴─────┴─────┘
                  │ --- │ --- │ --- │ --- │        │ --- │ --- │ --- │ --- │
                  └─────┴─────┴─────┴─────┘        └─────┴─────┴─────┴─────┘
```

**Key Features:**
- Function keys F1-F12 distributed for IDE workflow
- All bracket types: `( ) [ ] { } < >`
- Arrow keys in inverted-T layout (right side)
- Page navigation: Insert, Delete, Page Up/Down
- Home/End for line navigation
- Additional F10-F12 on bottom row

## Layer 9: GAMING (Combo Toggle: ESC+`+1+0)

```
┌─────┬─────┬─────┬─────┬─────┬─────┐                    ┌─────┬─────┬─────┬─────┬─────┬─────┐
│ ESC │ --- │ --- │ --- │ --- │ --- │                    │ --- │ --- │ --- │ --- │ --- │ --- │
├─────┼─────┼─────┼─────┼─────┼─────┤                    ├─────┼─────┼─────┼─────┼─────┼─────┤
│ TAB │ --- │ --- │ --- │ --- │ --- │                    │ --- │ --- │ --- │ --- │ --- │ --- │
├─────┼─────┼─────┼─────┼─────┼─────┤                    ├─────┼─────┼─────┼─────┼─────┼─────┤
│ --- │ --- │ --- │ --- │ --- │ --- │                    │ --- │ --- │ --- │ --- │ --- │ --- │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┐        ┌─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ --- │ --- │ --- │ --- │ --- │ --- │ --- │        │ --- │ --- │ --- │ --- │ --- │ --- │ --- │
└─────┴─────┴─────┼─────┼─────┼─────┼─────┤        ├─────┼─────┼─────┼─────┼─────┴─────┴─────┘
                  │ ALT │ ALT │CTRL │CTRL │        │ --- │ --- │ --- │ --- │
                  └─────┴─────┴─────┴─────┘        └─────┴─────┴─────┴─────┘
```

**Key Features:**
- Dedicated ESC and TAB for gaming
- Duplicate ALT and CTRL on left thumb cluster
- Space key accessibility for gaming
- Most keys transparent (inherit from base)
- **Toggle Access**: ESC + ` + 1 + 0 combo

## Encoder Functions

### All Layers:
- **Left Encoder**: Volume Down/Up
- **Right Encoder**: Previous Track/Next Track

### Encoder Click Functions:
- **Left Click**: Mute/Unmute
- **Right Click**: Play/Pause

## Layer Access Summary

```
| GUI | ALT | CTRL | LT1 |        | LT2 | CTRL | ALT | GUI |
```

- **BASE**: Default typing layer
- **LAYER 1**: Hold LT1 for numbers and symbols
- **LAYER 2**: Hold LT2 for functions and navigation
- **GAMING**: Toggle via 4-key combo for gaming optimization

## Special Features

### Combo Sequences:
- **Gaming Layer Toggle**: ESC + ` + 1 + 0 (4-key combo)

### Nordic Character Support:
- **Nordic characters** accessible via RALT combinations
- **NO key** on Layer 1 provides RALT functionality
- Requires OS set to Nordic keyboard layout

### Unique Layout Characteristics:
- **Number row on bottom** instead of traditional top position
- **No dedicated Space key** on base layer (accessed via layers)
- **Extended thumb cluster** with 4 keys per side
- **Dual encoder control** for media and volume

## Layout Philosophy

### Design Principles:
1. **Layer-based access** - Multiple functions per key position
2. **Gaming optimization** - Dedicated layer for gaming workflow
3. **Media integration** - Encoder controls for multimedia
4. **Programming focus** - Comprehensive symbol access
5. **Nordic support** - Built-in Nordic character handling

### Ergonomic Considerations:
- **Thumb cluster heavy usage** for layer switching
- **Logical symbol grouping** by function type
- **Arrow keys in standard position** for familiar navigation
- **Function keys distributed** across accessible positions

### Comparison to Standard Layouts:
- **More keys available** than compact layouts (58 vs 42 on Corne)
- **Additional thumb positions** for complex layer access
- **Dual encoder functionality** for media control
- **Gaming layer optimization** for FPS/competitive gaming
- **Flexible number placement** (bottom row vs top row)

This layout maximizes the Sofle's additional keys and encoders while maintaining programming efficiency and gaming optimization. 