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
```

**Features:**
- **6×4 key matrix per hand** (58 keys total)
- **2 rotary encoders** with click functions
- **4 thumb keys per hand**
- **10 layers** defined
- **Nordic character support** via RALT combos

## Layer 0: BASE (QWERTY + Finnish)

```
┌─────┬─────┬─────┬─────┬─────┬─────┐                    ┌─────┬─────┬─────┬─────┬─────┬─────┐
│ ESC │  Q  │  W  │  E  │  R  │  T  │                    │  Y  │  U  │  I  │  O  │  P  │BSPC │
├─────┼─────┼─────┼─────┼─────┼─────┤                    ├─────┼─────┼─────┼─────┼─────┼─────┤
│ TAB │  A  │  S  │  D  │  F  │  G  │                    │  H  │  J  │  K  │  L  │  Ö  │  Ä  │
├─────┼─────┼─────┼─────┼─────┼─────┤                    ├─────┼─────┼─────┼─────┼─────┼─────┤
│LSFT │  Z  │  X  │  C  │  V  │  B  │                    │  N  │  M  │  ,  │  .  │  -  │RSFT │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┐        ┌─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│LALT │LCTL │ --- │ --- │ --- │ --- │VOL- │        │VOL+ │ --- │ --- │ --- │ --- │RCTL │RALT │
└─────┴─────┴─────┼─────┼─────┼─────┼─────┤        ├─────┼─────┼─────┼─────┼─────┴─────┴─────┘
                  │LGUI │LALT │LCTL │ LT1 │        │ LT2 │RCTL │RALT │RGUI │
                  └─────┴─────┴─────┴─────┘        └─────┴─────┴─────┴─────┘
                        │ SPC │              │ ENT │
                        └─────┘              └─────┘
```

**Key Features:**
- Standard QWERTY layout with Finnish characters Ö and Ä
- ESC in top-left for Vim users, TAB for IDE workflow
- LALT/RALT in encoder positions (top), LCTRL/RCTRL (middle)
- Numbers accessed via Layer 1 (no dedicated number row)
- LT1 (Layer 1 when held) on left thumb cluster
- LT2 (Layer 2 when held) on right thumb cluster
- Space key accessible next to left thumb cluster
- Enter key accessible next to right thumb cluster
- Volume controls integrated into encoder positions (VOL-/VOL+)
- Requires OS keyboard layout set to Finnish for proper character output

## Layer 1: NUMBER (Toggle)

```
┌─────┬─────┬─────┬─────┬─────┬─────┐                    ┌─────┬─────┬─────┬─────┬─────┬─────┐
│ --- │  1  │  2  │  3  │  4  │  5  │                    │  6  │  7  │  8  │  9  │  0  │ --- │
├─────┼─────┼─────┼─────┼─────┼─────┤                    ├─────┼─────┼─────┼─────┼─────┼─────┤
│ --- │  +  │  -  │  *  │  /  │  =  │                    │  %  │  ^  │  &  │  |  │  (  │  )  │
├─────┼─────┼─────┼─────┼─────┼─────┤                    ├─────┼─────┼─────┼─────┼─────┼─────┤
│ --- │  <  │  >  │ <=  │ >=  │ !=  │                    │ --- │ --- │ --- │ --- │ --- │ --- │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┐        ┌─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ --- │ --- │ --- │ --- │ --- │ --- │ ENC │        │ ENC │ --- │ --- │ --- │ --- │ --- │ --- │
└─────┴─────┴─────┼─────┼─────┼─────┼─────┤        ├─────┼─────┼─────┼─────┼─────┴─────┴─────┘
                  │ --- │ --- │ --- │ --- │        │ --- │ --- │ --- │ --- │
                  └─────┴─────┴─────┴─────┘        └─────┴─────┴─────┴─────┘
```

**Key Features:**
- Numbers 0-9 in standard layout
- Basic math operators: + - * / = % ^ & | ( )
- Comparison macros: < > <= >= !=
- Toggle layer - numbers accessible when LT1 is held

## Layer 2: FUNCTION (Hold)

```
┌─────┬─────┬─────┬─────┬─────┬─────┐                    ┌─────┬─────┬─────┬─────┬─────┬─────┐
│ --- │ F1  │ F2  │ F3  │ F4  │ F5  │                    │ F6  │ F7  │ F8  │ F9  │ F10 │ DEL │
├─────┼─────┼─────┼─────┼─────┼─────┤                    ├─────┼─────┼─────┼─────┼─────┼─────┤
│ --- │ F11 │ F12 │  ?  │  :  │  ;  │                    │  ←  │  ↓  │  ↑  │  →  │PGUP │PGDN │
├─────┼─────┼─────┼─────┼─────┼─────┤                    ├─────┼─────┼─────┼─────┼─────┼─────┤
│ --- │  '  │  "  │  <  │  >  │  "  │                    │HOME │ END │UNDO │REDO │STAB │ --- │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┐        ┌─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ --- │ --- │ --- │ --- │ --- │ --- │ ENC │        │ ENC │ --- │ --- │ --- │ --- │ --- │ --- │
└─────┴─────┴─────┼─────┼─────┼─────┼─────┤        ├─────┼─────┼─────┼─────┼─────┴─────┴─────┘
                  │ --- │ --- │ --- │ --- │        │ --- │ --- │ --- │ --- │
                  └─────┴─────┴─────┴─────┘        └─────┴─────┴─────┴─────┘
```

**Key Features:**
- Function keys F1-F12
- Arrow keys and navigation (←, ↓, ↑, →)  
- Basic punctuation: ? : ; ' "
- Editing functions: HOME, END, PGUP, PGDN, UNDO, REDO, Shift+TAB
- Hold LT2 to access

## Layer 3: PROGRAMMING (Hold)

```
┌─────┬─────┬─────┬─────┬─────┬─────┐                    ┌─────┬─────┬─────┬─────┬─────┬─────┐
│ --- │  {  │  }  │  [  │  ]  │  \  │                    │  `  │  ~  │  !  │  @  │  #  │ --- │
├─────┼─────┼─────┼─────┼─────┼─────┤                    ├─────┼─────┼─────┼─────┼─────┼─────┤
│ --- │  (  │  )  │  <  │  >  │  /  │                    │  "  │  '  │  :  │  ;  │  ?  │ --- │
├─────┼─────┼─────┼─────┼─────┼─────┤                    ├─────┼─────┼─────┼─────┼─────┼─────┤
│ --- │  $  │  %  │  ^  │  &  │  *  │                    │  |  │  \  │  +  │  -  │  =  │ --- │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┐        ┌─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ --- │ --- │ --- │ --- │ --- │ --- │ ENC │        │ ENC │ --- │ --- │ --- │ --- │ --- │ --- │
└─────┴─────┴─────┼─────┼─────┼─────┼─────┤        ├─────┼─────┼─────┼─────┼─────┴─────┴─────┘
                  │ --- │ --- │ --- │ --- │        │ --- │ --- │ --- │ --- │
                  └─────┴─────┴─────┴─────┘        └─────┴─────┴─────┴─────┘
```

**Key Features:**
- All bracket types: { } [ ] ( ) < >
- Quotes and punctuation: " ' : ; ? ! ` ~
- Programming symbols: @ # $ % ^ & * | \ + - =
- Hold programming layer key to access

## Layer 9: GAMING (Combo Toggle: ESC+`+1+0)

```
┌─────┬─────┬─────┬─────┬─────┬─────┐                    ┌─────┬─────┬─────┬─────┬─────┬─────┐
│ ESC │ --- │ --- │ --- │ --- │ --- │                    │ --- │ --- │ --- │ --- │ --- │ --- │
├─────┼─────┼─────┼─────┼─────┼─────┤                    ├─────┼─────┼─────┼─────┼─────┼─────┤
│ TAB │ --- │ --- │ --- │ --- │ --- │                    │ --- │ --- │ --- │ --- │ --- │ --- │
├─────┼─────┼─────┼─────┼─────┼─────┤                    ├─────┼─────┼─────┼─────┼─────┼─────┤
│ --- │ --- │ --- │ --- │ --- │ --- │                    │ --- │ --- │ --- │ --- │ --- │ --- │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┐        ┌─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ --- │ --- │ --- │ --- │ --- │ --- │ ENC │        │ ENC │ --- │ --- │ --- │ --- │ --- │ --- │
└─────┴─────┴─────┼─────┼─────┼─────┼─────┤        ├─────┼─────┼─────┼─────┼─────┴─────┴─────┘
                  │LALT │LALT │LCTL │LCTL │        │ --- │ --- │ --- │ --- │
                  └─────┴─────┴─────┴─────┘        └─────┴─────┴─────┴─────┘
```

**Key Features:**
- Dedicated ESC and TAB for gaming (matching Corne gaming philosophy)
- Duplicate ALT and CTRL on left thumb cluster for gaming combinations
- Space key accessible for gaming
- Most keys transparent (inherit from base layer)
- **Toggle Access**: ESC + ` + 1 + 0 combo sequence

## Encoder Functions

### All Layers:
- **Left Encoder**: Volume Down/Up
- **Right Encoder**: Previous Track/Next Track

### Encoder Click Functions:
- **Left Click**: Mute/Unmute
- **Right Click**: Play/Pause

## Layer Access Summary

```
│LGUI │LALT │LCTL │ LT1 │        │ LT2 │RCTL │RALT │RGUI │
```

- **BASE**: Default QWERTY + Finnish characters (Ö, Ä)
- **LAYER 1**: Hold LT1 for numbers and math operators
- **LAYER 2**: Hold LT2 for function keys and navigation
- **LAYER 3**: Hold programming layer key for programming symbols
- **GAMING**: Toggle via 4-key combo for gaming optimization

## Special Features

### Combo Sequences:
- **Gaming Layer Toggle**: ESC + ` + 1 + 0 (4-key combo sequence)

### Finnish Character Support:
- **Ö**: Accessed in semicolon position with Finnish OS layout
- **Ä**: Accessed in quote position with Finnish OS layout
- Requires OS keyboard layout set to Finnish for proper character output

### Unique Layout Characteristics:
- **NO dedicated number row** - numbers accessed via Layer 1 only
- **Finnish characters (Ö, Ä)** in standard positions
- **Dedicated Space and Enter keys** in thumb clusters
- **Extended thumb cluster** with 4 keys per side
- **Dual encoder control** for media and volume
- **Consistent keymapping** with Corne for overlapping keys

## Layout Philosophy

### Design Principles:
1. **Corne compatibility** - Same keys in same positions where applicable
2. **Layer-based access** - Multiple functions per key position
3. **Gaming optimization** - Dedicated layer for gaming workflow
4. **Media integration** - Encoder controls for multimedia
5. **Programming focus** - Comprehensive symbol access
6. **Nordic support** - Built-in Nordic character handling

### Ergonomic Considerations:
- **Thumb cluster heavy usage** for layer switching
- **Logical symbol grouping** by function type
- **Arrow keys in standard position** for familiar navigation (matching Corne)
- **Function keys distributed** across accessible positions

### Comparison to Corne Layout:
- **Additional keys available** compared to Corne (58 vs 42 keys)
- **Same core layout** for overlapping key positions
- **Same layer structure** - numbers only via Layer 1, not dedicated row
- **Finnish character support** - Ö and Ä in standard positions
- **Additional thumb positions** for complex layer access
- **Dual encoder functionality** for media control
- **Gaming layer optimization** for FPS/competitive gaming
- **Layers are the same** - Sofle just has some extra transitive keys

This layout maintains exact consistency with the Corne layout structure while utilizing the Sofle's additional keys and encoders for enhanced functionality.