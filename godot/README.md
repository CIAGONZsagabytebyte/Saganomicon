# Godot Solarpunk Ship Prototype

## $aga - SAGA Functional Identity System

This directory contains a Godot Engine prototype for a solarpunk space ship game.

## Files

- `SolarpunkShip.gd` - Main ship controller script (GDScript)

## Setup Instructions

### 1. Install Godot Engine
Download Godot 4.x from: https://godotengine.org/

### 2. Create New Project
1. Open Godot
2. Create new 2D project
3. Import the `SolarpunkShip.gd` script

### 3. Create Ship Scene
1. Create a new Scene
2. Add `CharacterBody2D` as root node
3. Rename to "SolarpunkShip"
4. Attach `SolarpunkShip.gd` script
5. Add child nodes:
   - `Sprite2D` (add your ship sprite)
   - `CollisionShape2D` (set shape to capsule or polygon)

### 4. Configure Input
Go to Project Settings → Input Map and ensure these are configured:
- `ui_left` - Left Arrow / A
- `ui_right` - Right Arrow / D
- `ui_up` - Up Arrow / W
- `ui_down` - Down Arrow / S
- `ui_select` - Space (for boost)

### 5. Run!
Press F5 to run the scene.

## Features

- **Physics-based movement** with acceleration and friction
- **Solar boost system** - Hold Space to boost (drains energy)
- **Golden ratio optimization** - Sacred geometry physics
- **Serpent path navigation** - Advanced pathfinding
- **Energy regeneration** - Solar panels recharge over time

## Controls

- **Arrow Keys / WASD** - Move ship
- **Space** - Solar boost

## Sacred Geometry

The ship uses golden ratio (Φ = 1.618...) for movement optimization and serpent spiral navigation.

---

**$aga** • Gonzo.Family.Self.Actualized • Free & Right Preserved
