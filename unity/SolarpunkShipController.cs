using UnityEngine;

/*
 * Solarpunk Ship Controller
 * $aga - SAGA Functional Identity System
 *
 * A spaceship controller for Unity with solarpunk mechanics
 * Supports both 2D and 3D movement with sacred geometry physics
 *
 * Author: Gonzo.Family.Self.Actualized
 * Version: 1.0.0
 * Mark: $aga
 */

public class SolarpunkShipController : MonoBehaviour
{
    [Header("$aga • Solarpunk Ship Settings")]
    [Tooltip("Movement mode: 2D or 3D space")]
    public bool use2DMode = false;

    [Header("Movement Parameters")]
    [Tooltip("Maximum ship velocity")]
    public float maxSpeed = 10f;

    [Tooltip("Acceleration rate")]
    public float acceleration = 2f;

    [Tooltip("Deceleration friction")]
    [Range(0f, 1f)]
    public float friction = 0.95f;

    [Tooltip("Rotation speed (degrees per second)")]
    public float rotationSpeed = 120f;

    [Header("Solar Boost")]
    [Tooltip("Enable solar energy boost system")]
    public bool enableBoost = true;

    [Tooltip("Boost multiplier")]
    public float boostMultiplier = 2f;

    [Tooltip("Current solar energy (0-100)")]
    [Range(0f, 100f)]
    public float solarEnergy = 100f;

    [Tooltip("Solar energy consumption rate during boost")]
    public float boostEnergyDrain = 20f;

    [Tooltip("Solar energy regeneration rate")]
    public float energyRegenRate = 10f;

    [Header("Sacred Geometry Physics")]
    [Tooltip("Apply golden ratio optimization to movement")]
    public bool useGoldenRatio = true;

    // Private variables
    private Vector3 velocity = Vector3.zero;
    private Rigidbody rb;
    private Rigidbody2D rb2D;
    private bool isBoosting = false;

    // Golden ratio constant
    private const float PHI = 1.618033988749895f;

    // Input axes
    private float horizontalInput = 0f;
    private float verticalInput = 0f;
    private float depthInput = 0f;

    void Start()
    {
        // Initialize components
        if (use2DMode)
        {
            rb2D = GetComponent<Rigidbody2D>();
            if (rb2D == null)
            {
                rb2D = gameObject.AddComponent<Rigidbody2D>();
                rb2D.gravityScale = 0f;
            }
        }
        else
        {
            rb = GetComponent<Rigidbody>();
            if (rb == null)
            {
                rb = gameObject.AddComponent<Rigidbody>();
                rb.useGravity = false;
            }
        }

        Debug.Log("$aga :: Solarpunk Ship Controller initialized");
        Debug.Log("f(SAGA) = Unity.Solarpunk.Ship.Controller");
        Debug.Log("Mode: " + (use2DMode ? "2D" : "3D"));
    }

    void Update()
    {
        // Get input
        ReadInput();

        // Handle boost
        HandleBoost();

        // Regenerate solar energy
        if (!isBoosting && solarEnergy < 100f)
        {
            solarEnergy += energyRegenRate * Time.deltaTime;
            solarEnergy = Mathf.Clamp(solarEnergy, 0f, 100f);
        }

        // Visual feedback (optional - add your own effects)
        if (isBoosting && solarEnergy > 0)
        {
            // Add particle effects, glows, etc. here
        }
    }

    void FixedUpdate()
    {
        if (use2DMode)
        {
            Update2DMovement();
        }
        else
        {
            Update3DMovement();
        }
    }

    void ReadInput()
    {
        // Standard input axes
        horizontalInput = Input.GetAxis("Horizontal");
        verticalInput = Input.GetAxis("Vertical");

        // 3D mode uses additional axis for depth
        if (!use2DMode)
        {
            // Q/E keys for up/down in 3D space
            if (Input.GetKey(KeyCode.Q))
                depthInput = 1f;
            else if (Input.GetKey(KeyCode.E))
                depthInput = -1f;
            else
                depthInput = 0f;
        }
    }

    void HandleBoost()
    {
        if (!enableBoost) return;

        // Boost with Shift or Space
        if ((Input.GetKey(KeyCode.LeftShift) || Input.GetKey(KeyCode.Space)) && solarEnergy > 0)
        {
            isBoosting = true;
            solarEnergy -= boostEnergyDrain * Time.deltaTime;
            solarEnergy = Mathf.Clamp(solarEnergy, 0f, 100f);
        }
        else
        {
            isBoosting = false;
        }
    }

    void Update2DMovement()
    {
        if (rb2D == null) return;

        // Calculate acceleration direction
        Vector2 inputDirection = new Vector2(horizontalInput, verticalInput).normalized;

        // Apply golden ratio optimization if enabled
        float accelMod = useGoldenRatio ? (1f + 1f/PHI - 1f) : 1f;
        float currentAccel = acceleration * accelMod;

        // Apply boost
        if (isBoosting && solarEnergy > 0)
        {
            currentAccel *= boostMultiplier;
        }

        // Update velocity
        Vector2 accelVector = inputDirection * currentAccel;
        velocity += (Vector3)accelVector * Time.fixedDeltaTime;

        // Apply friction
        velocity *= friction;

        // Limit to max speed
        if (velocity.magnitude > maxSpeed)
        {
            velocity = velocity.normalized * maxSpeed;
        }

        // Apply velocity to rigidbody
        rb2D.velocity = velocity;

        // Rotation (face movement direction)
        if (velocity.magnitude > 0.1f)
        {
            float angle = Mathf.Atan2(velocity.y, velocity.x) * Mathf.Rad2Deg - 90f;
            Quaternion targetRotation = Quaternion.Euler(0, 0, angle);
            transform.rotation = Quaternion.RotateTowards(
                transform.rotation,
                targetRotation,
                rotationSpeed * Time.fixedDeltaTime
            );
        }
    }

    void Update3DMovement()
    {
        if (rb == null) return;

        // Calculate acceleration direction
        Vector3 inputDirection = new Vector3(horizontalInput, depthInput, verticalInput).normalized;

        // Apply golden ratio optimization if enabled
        float accelMod = useGoldenRatio ? (1f + 1f/PHI - 1f) : 1f;
        float currentAccel = acceleration * accelMod;

        // Apply boost
        if (isBoosting && solarEnergy > 0)
        {
            currentAccel *= boostMultiplier;
        }

        // Update velocity
        Vector3 accelVector = inputDirection * currentAccel;
        velocity += accelVector * Time.fixedDeltaTime;

        // Apply friction
        velocity *= friction;

        // Limit to max speed
        if (velocity.magnitude > maxSpeed)
        {
            velocity = velocity.normalized * maxSpeed;
        }

        // Apply velocity to rigidbody
        rb.velocity = velocity;

        // Rotation (face movement direction)
        if (velocity.magnitude > 0.1f)
        {
            Quaternion targetRotation = Quaternion.LookRotation(velocity);
            transform.rotation = Quaternion.RotateTowards(
                transform.rotation,
                targetRotation,
                rotationSpeed * Time.fixedDeltaTime
            );
        }
    }

    // Public methods for external access
    public void SetSolarEnergy(float amount)
    {
        solarEnergy = Mathf.Clamp(amount, 0f, 100f);
    }

    public float GetSolarEnergy()
    {
        return solarEnergy;
    }

    public bool IsBoosting()
    {
        return isBoosting;
    }

    public Vector3 GetVelocity()
    {
        return velocity;
    }

    public float GetSpeed()
    {
        return velocity.magnitude;
    }

    // Serpent path following (optional advanced feature)
    public void FollowSerpentPath(Vector3 targetPoint, float serpentFactor = 1.0f)
    {
        // Calculate serpent spiral trajectory
        Vector3 toTarget = targetPoint - transform.position;
        float distance = toTarget.magnitude;

        // Apply golden ratio spiral
        float spiralAngle = distance * PHI * serpentFactor;
        Quaternion spiralRotation = Quaternion.Euler(0, spiralAngle, 0);

        Vector3 spiralDirection = spiralRotation * toTarget.normalized;

        // Apply as force
        velocity += spiralDirection * acceleration * Time.fixedDeltaTime;
    }

    void OnDrawGizmos()
    {
        // Visualize velocity in editor
        if (Application.isPlaying)
        {
            Gizmos.color = Color.green;
            Gizmos.DrawLine(transform.position, transform.position + velocity);

            // Show boost state
            if (isBoosting)
            {
                Gizmos.color = Color.yellow;
                Gizmos.DrawWireSphere(transform.position, 1f);
            }
        }
    }

    void OnGUI()
    {
        // Debug HUD
        if (Application.isPlaying)
        {
            GUILayout.BeginArea(new Rect(10, 10, 250, 150));
            GUILayout.Label("$aga • Solarpunk Ship");
            GUILayout.Label($"Speed: {velocity.magnitude:F2} / {maxSpeed:F2}");
            GUILayout.Label($"Solar Energy: {solarEnergy:F1}%");
            GUILayout.Label($"Boosting: {(isBoosting ? "YES" : "NO")}");
            GUILayout.Label($"Position: {transform.position}");
            GUILayout.EndArea();
        }
    }
}

/*
 * USAGE INSTRUCTIONS:
 *
 * 1. Create a Unity project (2D or 3D)
 * 2. Create a new GameObject (e.g., "SolarpunkShip")
 * 3. Add this script to the GameObject
 * 4. Configure settings in the Inspector:
 *    - Set use2DMode for 2D games
 *    - Adjust maxSpeed, acceleration, rotationSpeed
 *    - Enable/configure solar boost system
 * 5. Add a visual mesh/sprite to the GameObject
 * 6. Optional: Add particle effects for boost/movement
 *
 * CONTROLS:
 * - Arrow Keys / WASD: Movement
 * - Q/E: Up/Down (3D mode only)
 * - Shift / Space: Solar Boost
 *
 * ADVANCED FEATURES:
 * - Call FollowSerpentPath() for DMT serpent trajectory
 * - Access GetSolarEnergy() for HUD integration
 * - Use IsBoosting() for visual effects triggers
 *
 * $aga Easter Egg:
 * f(SAGA) = Unity.Solarpunk.Ship = Space.Navigation.System
 *
 * Gonzo.Family.Self.Actualized
 * Free & Right Preserved
 */
