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

## Layer 0: BASE (QWERTY)

```
┌─────┬─────┬─────┬─────┬─────┬─────┐                    ┌─────┬─────┬─────┬─────┬─────┬─────┐
│ ESC │  1  │  2  │  3  │  4  │  5  │                    │  6  │  7  │  8  │  9  │  0  │  `  │
├─────┼─────┼─────┼─────┼─────┼─────┤                    ├─────┼─────┼─────┼─────┼─────┼─────┤
│ ESC │  Q  │  W  │  E  │  R  │  T  │                    │  Y  │  U  │  I  │  O  │  P  │BSPC │
├─────┼─────┼─────┼─────┼─────┼─────┤                    ├─────┼─────┼─────┼─────┼─────┼─────┤
│ TAB │  A  │  S  │  D  │  F  │  G  │                    │  H  │  J  │  K  │  L  │  ;  │  '  │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┐        ┌─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│LSFT │  Z  │  X  │  C  │  V  │  B  │VOL- │        │VOL+ │  N  │  M  │  ,  │  .  │  /  │RSFT │
└─────┴─────┴─────┼─────┼─────┼─────┼─────┤        ├─────┼─────┼─────┼─────┼─────┴─────┴─────┘
                  │LGUI │LALT │LCTL │ LT1 │        │ LT2 │RCTL │RALT │RGUI │
                  └─────┴─────┴─────┴─────┘        └─────┴─────┴─────┴─────┘
                        │ SPC │              │ ENT │
                        └─────┘              └─────┘
```

**Key Features:**
- Standard QWERTY layout with number row on top (like Corne)
- Duplicate ESC keys on top-left positions for Vim users  
- TAB for IDE workflow
- LT1 (Layer 1 when held) on left thumb cluster
- LT2 (Layer 2 when held) on right thumb cluster
- Space key accessible next to left thumb cluster
- Enter key accessible next to right thumb cluster
- Volume controls integrated into encoder positions (VOL-/VOL+)
- Standard modifier key placement matching Corne layout

## Layer 1: SYMBOLS & NUMBERS (LT1 Hold)

```
┌─────┬─────┬─────┬─────┬─────┬─────┐                    ┌─────┬─────┬─────┬─────┬─────┬─────┐
│ --- │ --- │ --- │ --- │ --- │ --- │                    │ --- │ --- │ --- │ --- │ --- │ --- │
├─────┼─────┼─────┼─────┼─────┼─────┤                    ├─────┼─────┼─────┼─────┼─────┼─────┤
│ --- │  1  │  2  │  3  │  4  │  5  │                    │  6  │  7  │  8  │  9  │  0  │ --- │
├─────┼─────┼─────┼─────┼─────┼─────┤                    ├─────┼─────┼─────┼─────┼─────┼─────┤
│ --- │  !  │  _  │  @  │  ^  │  $  │                    │  ~  │  }  │  \  │  "  │  |  │ --- │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┐        ┌─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ --- │  +  │  =  │  –  │  |  │  &  │ ENC │        │ ENC │  -  │  -  │  *  │  /  │  )  │  %  │
└─────┴─────┴─────┼─────┼─────┼─────┼─────┤        ├─────┼─────┼─────┼─────┼─────┴─────┴─────┘
                  │ --- │ --- │ --- │ --- │        │ --- │ --- │ --- │ --- │
                  └─────┴─────┴─────┴─────┘        └─────┴─────┴─────┴─────┘
```

**Key Features:**
- Regular numbers (1-9,0) matching Corne layout
- Programming symbols: `! _ @ ^ $ ~ } \ " |`
- Math operators: `+ = – | & - * / ) %`
- Nordic character access via RALT combinations (@ $ – ~ | etc.)
- Layout optimized for programming and symbol access

## Layer 2: FUNCTIONS & NAVIGATION (LT2 Hold)

```
┌─────┬─────┬─────┬─────┬─────┬─────┐                    ┌─────┬─────┬─────┬─────┬─────┬─────┐
│ --- │ --- │ --- │ --- │ --- │ --- │                    │ --- │ --- │ --- │ --- │ --- │ --- │
├─────┼─────┼─────┼─────┼─────┼─────┤                    ├─────┼─────┼─────┼─────┼─────┼─────┤
│ --- │ F1  │ F2  │ F3  │ F4  │ F5  │                    │ F6  │ F7  │ F8  │ F9  │ INS │ DEL │
├─────┼─────┼─────┼─────┼─────┼─────┤                    ├─────┼─────┼─────┼─────┼─────┼─────┤
│ --- │  (  │  )  │  [  │  ]  │  /  │                    │  ←  │  ↓  │  ↑  │  →  │PGUP │PGDN │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┐        ┌─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ --- │  {  │  }  │  <  │  >  │  )  │ ENC │        │ ENC │ F10 │ F11 │ F12 │HOME │ END │ --- │
└─────┴─────┴─────┼─────┼─────┼─────┼─────┤        ├─────┼─────┼─────┼─────┼─────┴─────┴─────┘
                  │ --- │ --- │ --- │ --- │        │ --- │ --- │ --- │ --- │
                  └─────┴─────┴─────┴─────┘        └─────┴─────┴─────┴─────┘
```

**Key Features:**
- Function keys F1-F12 distributed for IDE workflow (matching Corne layout)
- All bracket types: `( ) [ ] { } < >`
- Arrow keys in inverted-T layout (right side, matching Corne)
- Page navigation: Insert, Delete, Page Up/Down
- Home/End for line navigation
- Nordic angle brackets (<>) accessible via special keys

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

- **BASE**: Default typing layer
- **LAYER 1**: Hold LT1 for symbols and numbers  
- **LAYER 2**: Hold LT2 for functions and navigation
- **GAMING**: Toggle via 4-key combo for gaming optimization

## Special Features

### Combo Sequences:
- **Gaming Layer Toggle**: ESC + ` + 1 + 0 (4-key combo sequence)

### Nordic Character Support:
- **Nordic characters** accessible via RALT combinations
- **RALT mappings** integrated into symbol layers (@ $ – ~ | etc.)
- Requires OS set to Nordic keyboard layout

### Unique Layout Characteristics:
- **Number row on top** matching Corne layout structure
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
- **Additional thumb positions** for complex layer access
- **Dual encoder functionality** for media control
- **Gaming layer optimization** for FPS/competitive gaming
- **Number row placement** matches Corne structure (top row)

This layout maximizes the Sofle's additional keys and encoders while maintaining compatibility with the Corne layout for shared key positions, ensuring a consistent typing experience across both keyboards.