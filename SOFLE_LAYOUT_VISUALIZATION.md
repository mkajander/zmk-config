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
- **6×4 key matrix per hand** (60 keys total + 2 encoders)
- **Number row** that Corne doesn't have (12 additional keys)
- **2 rotary encoders** with click functions
- **4 thumb keys per hand**
- **10 layers** defined
- **Nordic character support** via Finnish OS layout
- **Corne-compatible layer structure** for overlapping functionality

## Layer 0: BASE (QWERTY + Finnish)

```
┌─────┬─────┬─────┬─────┬─────┬─────┐                    ┌─────┬─────┬─────┬─────┬─────┬─────┐
│ ??? │ ??? │ ??? │ ??? │ ??? │ ??? │                    │ ??? │ ??? │ ??? │ ??? │ ??? │ ??? │ ← NUMBER ROW (exists physically, configure as needed)
├─────┼─────┼─────┼─────┼─────┼─────┤                    ├─────┼─────┼─────┼─────┼─────┼─────┤
│ ESC │  Q  │  W  │  E  │  R  │  T  │                    │  Y  │  U  │  I  │  O  │  P  │BSPC │
├─────┼─────┼─────┼─────┼─────┼─────┤                    ├─────┼─────┼─────┼─────┼─────┼─────┤
│ TAB │  A  │  S  │  D  │  F  │  G  │                    │  H  │  J  │  K  │  L  │  Ö  │  Ä  │
├─────┼─────┼─────┼─────┼─────┼─────┤                    ├─────┼─────┼─────┼─────┼─────┼─────┤
│LSFT │  Z  │  X  │  C  │  V  │  B  │                    │  N  │  M  │  ,  │  .  │  -  │RSFT │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┐        ┌─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│LALT │LCTL │ ??? │ ??? │ ??? │ ??? │VOL- │        │VOL+ │ ??? │ ??? │ ??? │ ??? │RCTL │RALT │
└─────┴─────┴─────┼─────┼─────┼─────┼─────┤        ├─────┼─────┼─────┼─────┼─────┴─────┴─────┘
                  │ GUI │PROG │ SPC │     │        │     │ ENT │FUNC │ NUM │
                  └─────┴─────┴─────┴─────┘        └─────┴─────┴─────┴─────┘
```

**Target Layout Features (to match Corne exactly):**
- **NUMBER ROW**: Sofle has this extra row that Corne lacks - can be configured as needed
- **QWERTY section**: Exactly matches Corne layout structure
  - ESC, Q,W,E,R,T | Y,U,I,O,P, BSPC
  - TAB, A,S,D,F,G | H,J,K,L, Ö, Ä  
  - SHIFT, Z,X,C,V,B | N,M,comma,period, -, SHIFT
- **Encoder positions**: LALT/RALT (top row), LCTRL/RCTRL (middle row) to match Corne
- **Bottom row**: Additional Sofle keys can be configured as needed
- **Thumb cluster**: GUI, PROG, SPACE | ENTER, FUNC, NUM (matching Corne structure)
- **Finnish characters**: Ö and Ä in semicolon/quote positions
- **Dash character**: - (dash) instead of / (slash) in bottom-right position

**Note**: This shows the TARGET layout to exactly match Corne structure. The Sofle's additional number row provides extra functionality while maintaining perfect compatibility with Corne layer behavior.

## Layer 1: NUMBER (Toggle)

```
┌─────┬─────┬─────┬─────┬─────┬─────┐                    ┌─────┬─────┬─────┬─────┬─────┬─────┐
│ --- │ --- │ --- │ --- │ --- │ --- │                    │ --- │ --- │ --- │ --- │ --- │ --- │ ← Number row (transparent)
├─────┼─────┼─────┼─────┼─────┼─────┤                    ├─────┼─────┼─────┼─────┼─────┼─────┤
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
- **Number row transparent** - numbers accessed through Layer 1 functionality, not the physical number row
- Numbers 1-9,0 positioned in QWERTY row when Layer 1 is active (matching Corne layout)
- Basic math operators: + - * / = % ^ & | ( )
- Comparison macros: < > <= >= !=
- Toggle layer - numbers accessible when LT1 is held
- **Maintains Corne compatibility** - numbers in same positions as Corne Layer 1

## Layer 2: FUNCTION (Hold)

```
┌─────┬─────┬─────┬─────┬─────┬─────┐                    ┌─────┬─────┬─────┬─────┬─────┬─────┐
│ --- │ --- │ --- │ --- │ --- │ --- │                    │ --- │ --- │ --- │ --- │ --- │ --- │ ← Number row (transparent)
├─────┼─────┼─────┼─────┼─────┼─────┤                    ├─────┼─────┼─────┼─────┼─────┼─────┤
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
- **Number row transparent** - function keys positioned in main area to match Corne
- Function keys F1-F12
- Arrow keys and navigation (←, ↓, ↑, →)  
- Basic punctuation: ? : ; ' "
- Editing functions: HOME, END, PGUP, PGDN, UNDO, REDO, Shift+TAB
- Hold LT2 to access
- **Same layout as Corne Layer 2** for all overlapping positions

## Layer 3: PROGRAMMING (Hold)

```
┌─────┬─────┬─────┬─────┬─────┬─────┐                    ┌─────┬─────┬─────┬─────┬─────┬─────┐
│ --- │ --- │ --- │ --- │ --- │ --- │                    │ --- │ --- │ --- │ --- │ --- │ --- │ ← Number row (transparent)
├─────┼─────┼─────┼─────┼─────┼─────┤                    ├─────┼─────┼─────┼─────┼─────┼─────┤
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
- **Number row transparent** - programming symbols positioned in main area to match Corne
- All bracket types: { } [ ] ( ) < >
- Quotes and punctuation: " ' : ; ? ! ` ~
- Programming symbols: @ # $ % ^ & * | \ + - =
- Hold programming layer key to access
- **Exact match with Corne Layer 3** for all overlapping positions

## Layer 9: GAMING (Combo Toggle: ESC+`+1+0)

```
┌─────┬─────┬─────┬─────┬─────┬─────┐                    ┌─────┬─────┬─────┬─────┬─────┬─────┐
│ ESC │ --- │ --- │ --- │ --- │ --- │                    │ --- │ --- │ --- │ --- │ --- │ --- │ ← Number row (ESC active, others transparent)
├─────┼─────┼─────┼─────┼─────┼─────┤                    ├─────┼─────┼─────┼─────┼─────┼─────┤
│ TAB │ --- │ --- │ --- │ --- │ --- │                    │ --- │ --- │ --- │ --- │ --- │ --- │
├─────┼─────┼─────┼─────┼─────┼─────┤                    ├─────┼─────┼─────┼─────┼─────┼─────┤
│ --- │ --- │ --- │ --- │ --- │ --- │                    │ --- │ --- │ --- │ --- │ --- │ --- │
├─────┼─────┼─────┼─────┼─────┼─────┤                    ├─────┼─────┼─────┼─────┼─────┼─────┤
│ --- │ --- │ --- │ --- │ --- │ --- │                    │ --- │ --- │ --- │ --- │ --- │ --- │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┐        ┌─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│LALT │LALT │LCTL │LCTL │ SPC │ --- │ ENC │        │ ENC │ --- │ ENT │ --- │ --- │ --- │ --- │
└─────┴─────┴─────┼─────┼─────┼─────┼─────┤        ├─────┼─────┼─────┼─────┼─────┴─────┴─────┘
                  │ SPC │     │     │     │        │     │     │     │ ENT │
                  └─────┘     └─────┴─────┘        └─────┴─────┘     └─────┘
```

**Key Features:**
- **Number row available** - includes ESC for gaming, other keys transparent
- Dedicated ESC and TAB for gaming (matching Corne gaming philosophy)
- Duplicate ALT and CTRL on left thumb cluster for gaming combinations
- Space and Enter keys accessible for gaming
- Most keys transparent (inherit from base layer)
- **Toggle Access**: ESC + ` + 1 + 0 combo sequence (using number row keys)
- **Extra functionality** compared to Corne due to additional physical keys

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
- **Physical number row exists** but layer behavior matches Corne (numbers via Layer 1)
- **Finnish characters (Ö, Ä)** in standard semicolon/quote positions
- **Dedicated Space and Enter keys** in thumb clusters
- **Extended thumb cluster** with 4 keys per side
- **Dual encoder control** for media and volume
- **18 additional keys** compared to Corne for extended functionality
- **Consistent layer mappings** with Corne for overlapping keys

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
- **Additional number row** - Sofle has 60 keys vs Corne's 42 keys (18 additional keys)
- **Same core layout structure** for all overlapping key positions 
- **Same layer mappings** - numbers accessed via Layer 1, functions via Layer 2, programming via Layer 3
- **Finnish character support** - Ö and Ä in same relative positions as Corne
- **Additional thumb positions** for complex layer access and media control
- **Dual encoder functionality** for media/volume control
- **Gaming layer optimization** with number row accessibility
- **"Layers are the same"** - Sofle adds physical keys but maintains Corne compatibility

**Key Principle**: The Sofle maintains exact consistency with Corne layer behavior while providing additional physical keys that extend functionality without breaking compatibility. Users can transition seamlessly between keyboards.

This layout maintains exact consistency with the Corne layout structure while utilizing the Sofle's additional number row and encoder functionality for enhanced capabilities. The Sofle has 60 keys compared to Corne's 42 keys, with the extra 18 keys being the number row that the Corne lacks.