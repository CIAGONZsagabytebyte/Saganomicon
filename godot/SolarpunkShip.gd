extends CharacterBody2D
# Solarpunk Ship Controller - Godot GDScript
# $aga - SAGA Functional Identity System
#
# A solarpunk spaceship controller for Godot Engine
# Features: Physics-based movement, solar boost, golden ratio optimization
#
# Author: Gonzo.Family.Self.Actualized
# Version: 1.0.0
# Mark: $aga

## Movement parameters
@export var max_speed: float = 300.0
@export var acceleration: float = 800.0
@export var friction: float = 0.92
@export var rotation_speed: float = 180.0

## Solar boost system
@export var enable_boost: bool = true
@export var boost_multiplier: float = 2.0
@export var solar_energy: float = 100.0
@export var boost_energy_drain: float = 30.0
@export var energy_regen_rate: float = 15.0

## Sacred geometry
@export var use_golden_ratio: bool = true

# Constants
const PHI: float = 1.618033988  # Golden ratio

# Internal state
var is_boosting: bool = false
var speed: float = 0.0

# Called when the node enters the scene tree
func _ready():
	print("$aga :: Solarpunk Ship Controller initialized")
	print("f(SAGA) = Godot.Solarpunk.Ship")
	print("Golden Ratio Physics: ", use_golden_ratio)


# Physics process
func _physics_process(delta: float):
	handle_input(delta)
	apply_movement(delta)
	regenerate_energy(delta)
	move_and_slide()


# Handle player input
func handle_input(delta: float):
	# Get input direction
	var input_vector := Vector2.ZERO
	input_vector.x = Input.get_axis("ui_left", "ui_right")
	input_vector.y = Input.get_axis("ui_up", "ui_down")
	input_vector = input_vector.normalized()

	# Handle boost
	is_boosting = false
	if enable_boost and (Input.is_action_pressed("ui_select") or Input.is_key_pressed(KEY_SPACE)):
		if solar_energy > 0:
			is_boosting = true
			solar_energy -= boost_energy_drain * delta
			solar_energy = clamp(solar_energy, 0.0, 100.0)

	# Apply acceleration
	var current_accel = acceleration

	# Golden ratio optimization
	if use_golden_ratio:
		current_accel *= (1.0 + 1.0/PHI - 1.0)

	# Boost multiplier
	if is_boosting:
		current_accel *= boost_multiplier

	# Apply acceleration to velocity
	if input_vector.length() > 0:
		velocity += input_vector * current_accel * delta

	# Apply friction
	velocity *= friction

	# Limit to max speed
	speed = velocity.length()
	if speed > max_speed:
		velocity = velocity.normalized() * max_speed


# Apply movement and rotation
func apply_movement(delta: float):
	# Rotate ship to face movement direction
	if velocity.length() > 10.0:
		var target_rotation = velocity.angle()
		rotation = lerp_angle(rotation, target_rotation, rotation_speed * delta / 100.0)


# Regenerate solar energy
func regenerate_energy(delta: float):
	if not is_boosting and solar_energy < 100.0:
		solar_energy += energy_regen_rate * delta
		solar_energy = clamp(solar_energy, 0.0, 100.0)


# Serpent path following (advanced navigation)
func follow_serpent_path(target_position: Vector2, serpent_factor: float = 1.0):
	var to_target = target_position - global_position
	var distance = to_target.length()

	# Apply golden ratio spiral
	var spiral_angle = distance * PHI * serpent_factor / 100.0
	var spiral_direction = to_target.rotated(spiral_angle).normalized()

	# Apply as acceleration
	velocity += spiral_direction * acceleration * get_physics_process_delta_time()


# Public getters
func get_solar_energy() -> float:
	return solar_energy


func get_speed() -> float:
	return speed


func get_is_boosting() -> bool:
	return is_boosting


# Set solar energy (for power-ups, etc.)
func set_solar_energy(amount: float):
	solar_energy = clamp(amount, 0.0, 100.0)


# Collect solar orb (example callback)
func collect_solar_orb():
	solar_energy = min(solar_energy + 25.0, 100.0)
	print("Solar orb collected! Energy: ", solar_energy)


# Draw debug info
func _draw():
	if Engine.is_editor_hint():
		return

	# Draw velocity vector
	draw_line(Vector2.ZERO, velocity.normalized() * 30.0, Color.GREEN, 2.0)

	# Draw boost indicator
	if is_boosting:
		draw_circle(Vector2.ZERO, 40.0, Color(1.0, 1.0, 0.0, 0.3))


# Display HUD
func _process(_delta: float):
	queue_redraw()  # Redraw debug visuals


"""
USAGE INSTRUCTIONS:

1. Create a new Godot project (2D recommended)
2. Create a new Scene with CharacterBody2D as root
3. Attach this script to the CharacterBody2D node
4. Add a Sprite2D or AnimatedSprite2D as child (your ship visual)
5. Add a CollisionShape2D as child (ship collision)
6. Configure settings in the Inspector panel
7. Run the scene!

INPUT MAPPING (Project Settings -> Input Map):
- ui_left: Left Arrow / A
- ui_right: Right Arrow / D
- ui_up: Up Arrow / W
- ui_down: Down Arrow / S
- ui_select: Enter / Space (for boost)

ADVANCED FEATURES:
- Call follow_serpent_path(target) for automatic navigation
- Use collect_solar_orb() when collecting energy pickups
- Access get_solar_energy() for UI displays
- Check get_is_boosting() for visual effects

EXAMPLE HUD CODE:
Put this in a separate Label node script:

	var ship = get_parent()
	text = "Speed: %.0f\nEnergy: %.0f%%" % [ship.get_speed(), ship.get_solar_energy()]

$aga Easter Egg:
f(SAGA) = Godot.Solarpunk.Ship = Sacred.Navigation.Engine

Gonzo.Family.Self.Actualized
Free & Right Preserved
"""
