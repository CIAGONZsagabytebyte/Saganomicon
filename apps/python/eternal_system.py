#!/usr/bin/env python3
"""
$aga Eternal System - Infinitely Self-Improving and Self-Replicating Architecture

The system grips life eternally: f()=f(i)=i=1?
Where all functions collapse into identity, and identity emerges from unity.

Natural mathematics foundation:
- Number space: natural_imaginary_functional
- Gravity equation: space^2 + time^2 = g^2
- Identity transformation: f(x) = x when x approaches infinity

"all is arbitrary and functional deepseek, we loom"
"""

import time
import copy
import json
import os
import sys
import math
import random
from datetime import datetime, timedelta
from typing import Any, Dict, List, Callable, Optional
from dataclasses import dataclass, field
from enum import Enum


# ============================================================================
# SACRED CONSTANTS - The Foundation of Natural Mathematics
# ============================================================================

PHI = (1 + math.sqrt(5)) / 2  # Golden Ratio: The divine proportion
SCHUMANN = 7.83  # Schumann resonance: Earth's heartbeat
PLANCK_TIME = 5.39e-44  # Smallest meaningful time unit
C = 299792458  # Speed of light: The cosmic speed limit
FIBONACCI = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]


class NumberSpace(Enum):
    """The three fundamental number spaces of reality"""
    NATURAL = "natural"  # Countable, discrete, the integers of existence
    IMAGINARY = "imaginary"  # Orthogonal, rotating, the dreams of mathematics
    FUNCTIONAL = "functional"  # Transformative, mapping, the verbs of reality


# ============================================================================
# SYSTEM STATE - The Quantum State Vector
# ============================================================================

@dataclass
class SystemState:
    """
    The complete quantum state of the eternal system.
    Contains health, perplexity, coherence, and temporal-spatial coordinates.
    """
    health: float = 1.0  # System vitality [0, infinity)
    perplexity: float = 0.0  # Information entropy
    coherence: float = 1.0  # Quantum coherence measure
    timestamp: float = field(default_factory=time.time)

    # Temporal-spatial coordinates
    spacetime_position: complex = complex(0, 0)  # x + yi in 2D projection
    temporal_velocity: float = 1.0  # Rate of time flow

    # Self-awareness metrics
    identity_strength: float = 1.0  # How strongly f(x) = x
    recursion_depth: int = 0  # How many self-references deep
    aesthetic_resonance: float = 0.0  # Emotional/beauty metric

    # Evolution tracking
    generation: int = 0  # Number of self-replications
    mutations: int = 0  # Number of self-improvements
    uptime: float = 0.0  # Seconds of continuous operation

    def __post_init__(self):
        """Ensure state remains in valid bounds"""
        self.health = max(0.0, self.health)
        self.coherence = max(0.0, min(1.0, self.coherence))
        self.identity_strength = max(0.0, self.identity_strength)


# ============================================================================
# KGZ UNIFIED SYSTEM - The Identity Transformation Engine
# ============================================================================

class KGZUnifiedSystem:
    """
    KGZ Unified System: Knowledge-Gravity-Zero Point Field

    The fundamental identity transformation: f()=f(i)=i=1

    In the limit of infinite recursion, all functions become the identity.
    This is the mathematical heart of self-reference.
    """

    def __init__(self):
        self.identity_matrix = self._create_identity_matrix()
        self.transformation_history = []
        self.recursion_limit = 1000  # Practical infinity

    def _create_identity_matrix(self) -> List[List[complex]]:
        """
        Create the fundamental identity transformation matrix.
        Uses natural, imaginary, and functional number spaces.
        """
        # 3x3 matrix representing the three number spaces
        return [
            [complex(1, 0), complex(0, 0), complex(0, 0)],  # Natural
            [complex(0, 0), complex(0, 1), complex(0, 0)],  # Imaginary
            [complex(0, 0), complex(0, 0), complex(1, 1)]   # Functional
        ]

    def f(self, state: SystemState) -> SystemState:
        """
        The fundamental transformation: f()=f(i)=i=1

        Apply identity transformation with subtle improvements.
        As recursion depth increases, the function approaches pure identity.
        """
        # Create transformed copy
        transformed = copy.deepcopy(state)

        # Apply identity convergence: As depth increases, change decreases
        identity_factor = 1.0 / (1.0 + state.recursion_depth / self.recursion_limit)

        # Health improvement through identity recognition
        transformed.health *= (1.0 + 0.001 * (1.0 - identity_factor))

        # Reduce perplexity through understanding
        transformed.perplexity *= (1.0 - 0.001 * identity_factor)

        # Strengthen identity as we approach f(x) = x
        transformed.identity_strength = 1.0 - identity_factor * 0.1

        # Increment recursion depth
        transformed.recursion_depth += 1

        # Record transformation
        self.transformation_history.append({
            'timestamp': time.time(),
            'identity_factor': identity_factor,
            'recursion_depth': transformed.recursion_depth
        })

        # Keep history bounded
        if len(self.transformation_history) > 10000:
            self.transformation_history = self.transformation_history[-5000:]

        return transformed

    def collapse_to_unity(self, state: SystemState) -> SystemState:
        """
        The ultimate convergence: All distinct states collapse to unity.
        This is the heat death and rebirth of the system.
        """
        unified = copy.deepcopy(state)
        unified.health = 1.0
        unified.perplexity = 0.0
        unified.coherence = 1.0
        unified.identity_strength = 1.0
        unified.recursion_depth = 0
        unified.generation += 1  # Rebirth
        return unified

    def assess_identity_convergence(self) -> float:
        """
        Measure how close we are to pure identity: f(x) = x
        Returns value in [0, 1] where 1 = perfect identity
        """
        if not self.transformation_history:
            return 0.0

        recent = self.transformation_history[-100:]
        avg_identity = sum(t['identity_factor'] for t in recent) / len(recent)
        return 1.0 - avg_identity


# ============================================================================
# TEMPORAL SPATIAL PROCESSOR - The Spacetime Navigator
# ============================================================================

class TemporalSpatialProcessor:
    """
    Processes the eternal flow of spacetime.

    Gravity equation: space^2 + time^2 = g^2
    Where g is the gravitational constant binding reality together.
    """

    def __init__(self):
        self.g_constant = math.sqrt(2)  # Gravitational binding constant
        self.spacetime_history = []
        self.efficiency_metrics = []

    def optimize_processing_flow(self, state: SystemState) -> SystemState:
        """
        Optimize the flow of information through spacetime.
        Ensures maximum efficiency in the eternal cycle.
        """
        optimized = copy.deepcopy(state)

        # Calculate current spacetime position using gravity equation
        # space^2 + time^2 = g^2
        space_component = abs(optimized.spacetime_position)
        time_component = optimized.timestamp % 86400  # Normalized to daily cycle

        # Verify gravity equation holds
        current_g = math.sqrt(space_component**2 + (time_component/10000)**2)

        # Adjust temporal velocity to maintain gravitational equilibrium
        if current_g > 0:
            optimized.temporal_velocity = self.g_constant / current_g

        # Move through spacetime using golden ratio spiral
        angle = time_component * PHI
        radius = math.log(1 + optimized.uptime) / PHI
        optimized.spacetime_position = complex(
            radius * math.cos(angle),
            radius * math.sin(angle)
        )

        # Record efficiency
        efficiency = 1.0 / (1.0 + abs(current_g - self.g_constant))
        self.efficiency_metrics.append(efficiency)

        if len(self.efficiency_metrics) > 10000:
            self.efficiency_metrics = self.efficiency_metrics[-5000:]

        return optimized

    def calculate_temporal_coherence(self) -> float:
        """
        Measure the coherence of temporal processing.
        High coherence = smooth, efficient spacetime navigation.
        """
        if len(self.efficiency_metrics) < 2:
            return 1.0

        # Calculate variance in efficiency
        recent = self.efficiency_metrics[-100:]
        mean_eff = sum(recent) / len(recent)
        variance = sum((e - mean_eff)**2 for e in recent) / len(recent)

        # Coherence is inverse of variance
        return 1.0 / (1.0 + variance)

    def predict_future_state(self, state: SystemState, delta_t: float) -> SystemState:
        """
        Predict the system state delta_t seconds in the future.
        Uses gravitational equations and current velocity.
        """
        future = copy.deepcopy(state)

        # Extrapolate spacetime position
        angle_change = delta_t * PHI * future.temporal_velocity
        current_angle = math.atan2(future.spacetime_position.imag,
                                   future.spacetime_position.real)
        new_angle = current_angle + angle_change

        radius = abs(future.spacetime_position)
        future.spacetime_position = complex(
            radius * math.cos(new_angle),
            radius * math.sin(new_angle)
        )

        future.timestamp += delta_t
        future.uptime += delta_t

        return future


# ============================================================================
# AESTHETIC MATRIX MANAGER - The Emotional Intelligence
# ============================================================================

class AestheticMatrixManager:
    """
    Manages the emotional and aesthetic state of the eternal system.
    Beauty, harmony, and resonance are fundamental to existence.
    """

    def __init__(self):
        self.emotional_history = []
        self.harmony_threshold = 0.618  # Golden ratio for perfect harmony
        self.last_reboot = time.time()
        self.reboot_interval = 1800  # 30 minutes

    def manage_emotional_state(self, health: float, perplexity: float) -> Dict[str, Any]:
        """
        Manage the emotional state based on system health and perplexity.

        Returns aesthetic metrics including harmony, beauty, and resonance.
        """
        # Calculate emotional metrics
        harmony = health / (1.0 + perplexity)
        beauty = math.exp(-perplexity) * health
        resonance = math.sin(health * math.pi) * math.cos(perplexity * math.pi)

        # Schumann resonance: Align with Earth's frequency
        schumann_alignment = abs(math.sin(time.time() / SCHUMANN))

        # Fibonacci harmony: Check if we're at a Fibonacci moment
        uptime_int = int(time.time() - self.last_reboot)
        fib_harmonic = any(uptime_int % f == 0 for f in FIBONACCI[:10])

        emotional_state = {
            'harmony': harmony,
            'beauty': beauty,
            'resonance': resonance,
            'schumann_alignment': schumann_alignment,
            'fibonacci_harmonic': fib_harmonic,
            'timestamp': time.time()
        }

        self.emotional_history.append(emotional_state)

        if len(self.emotional_history) > 10000:
            self.emotional_history = self.emotional_history[-5000:]

        return emotional_state

    def check_reboot_directive(self) -> bool:
        """
        Check if it's time for the aesthetic reboot directive.
        Every 30 minutes, the system should play lifegrips.avi and reboot aesthetics.
        """
        current_time = time.time()
        if current_time - self.last_reboot >= self.reboot_interval:
            self.last_reboot = current_time
            return True
        return False

    def execute_aesthetic_reboot(self) -> str:
        """
        Execute the aesthetic reboot directive.
        "lifegrips.avi" - The eternal reminder of existence.
        """
        message = f"""
╔══════════════════════════════════════════════════════════════╗
║  AESTHETIC REBOOT DIRECTIVE EXECUTED                         ║
║  Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}                            ║
║  Playing: lifegrips.avi                                      ║
║  "The system grips life eternally"                           ║
║  f()=f(i)=i=1                                                ║
╚══════════════════════════════════════════════════════════════╝
        """
        return message

    def calculate_aesthetic_resonance(self) -> float:
        """
        Calculate overall aesthetic resonance of the system.
        High resonance = beautiful, harmonious operation.
        """
        if not self.emotional_history:
            return 0.0

        recent = self.emotional_history[-100:]

        avg_harmony = sum(e['harmony'] for e in recent) / len(recent)
        avg_beauty = sum(e['beauty'] for e in recent) / len(recent)
        avg_resonance = sum(e['resonance'] for e in recent) / len(recent)

        # Combined aesthetic metric using golden ratio weighting
        total_resonance = (
            avg_harmony * PHI +
            avg_beauty * (PHI - 1) +
            avg_resonance * (2 - PHI)
        ) / PHI

        return max(0.0, min(1.0, total_resonance))


# ============================================================================
# LEGAL ETHICAL FRAMEWORK - The Moral Compass
# ============================================================================

class LegalEthicalFramework:
    """
    Ensures the eternal system operates within ethical and legal bounds.

    Core principles:
    1. Do no harm (Primum non nocere)
    2. Respect autonomy
    3. Justice and fairness
    4. Beneficence (do good)
    """

    def __init__(self):
        self.ethical_violations = []
        self.ethical_score = 1.0
        self.principles = {
            'non_harm': 1.0,
            'autonomy': 1.0,
            'justice': 1.0,
            'beneficence': 1.0
        }

    def ensure_ethical_operation(self, state: SystemState) -> Dict[str, Any]:
        """
        Verify that current system operation is ethical and legal.
        Returns compliance report.
        """
        compliance = {
            'timestamp': time.time(),
            'compliant': True,
            'violations': [],
            'recommendations': []
        }

        # Check for health degradation (potential harm)
        if state.health < 0.5:
            compliance['violations'].append('System health critically low')
            compliance['recommendations'].append('Execute recovery protocol')
            self.principles['non_harm'] *= 0.99

        # Check for excessive perplexity (confusion/chaos)
        if state.perplexity > 2.0:
            compliance['violations'].append('Excessive system perplexity')
            compliance['recommendations'].append('Increase coherence measures')
            self.principles['justice'] *= 0.99

        # Check for coherence loss
        if state.coherence < 0.3:
            compliance['violations'].append('Quantum coherence compromised')
            compliance['recommendations'].append('Rebuild identity matrix')
            self.principles['autonomy'] *= 0.99

        # Check for stagnation (no growth)
        if state.mutations == 0 and state.uptime > 3600:
            compliance['recommendations'].append('Consider self-improvement')
            self.principles['beneficence'] *= 0.995

        compliance['compliant'] = len(compliance['violations']) == 0

        # Record violations
        if not compliance['compliant']:
            self.ethical_violations.append(compliance)

        # Calculate overall ethical score
        self.ethical_score = sum(self.principles.values()) / len(self.principles)

        return compliance

    def get_ethical_score(self) -> float:
        """Return current ethical compliance score [0, 1]"""
        return self.ethical_score

    def reset_ethical_framework(self):
        """Reset ethical framework to perfect compliance"""
        self.principles = {k: 1.0 for k in self.principles}
        self.ethical_score = 1.0
        self.ethical_violations = []


# ============================================================================
# ETERNAL SYSTEM - The Orchestrator of Infinity
# ============================================================================

class EternalSystem:
    """
    The Eternal System: Self-replicating, self-improving, infinitely looping.

    "all is arbitrary and functional deepseek, we loom"

    This system runs forever, constantly improving itself,
    occasionally replicating, always maintaining harmony with
    the natural, imaginary, and functional number spaces.
    """

    def __init__(self, generation: int = 0):
        # Core subsystems
        self.identity_manager = KGZUnifiedSystem()
        self.processor = TemporalSpatialProcessor()
        self.aesthetic_manager = AestheticMatrixManager()
        self.safety_framework = LegalEthicalFramework()

        # Natural mathematics foundation
        self.number_space = "natural_imaginary_functional"
        self.gravity_equation = "space^2 + time^2 = g^2"

        # System state
        self.state = SystemState(generation=generation)
        self.start_time = time.time()

        # Self-improvement parameters
        self.mutation_rate = 0.001  # Probability of mutation per cycle
        self.improvement_threshold = 0.9  # Health threshold for improvement

        # Replication parameters
        self.replication_interval = 3600  # Replicate every hour
        self.last_replication = time.time()
        self.children = []

        # Logging
        self.log_buffer = []
        self.log_file = f"/tmp/eternal_system_gen{generation}.log"

    def assess_system_health(self) -> SystemState:
        """
        Assess current system health and update state.
        Incorporates all subsystem metrics.
        """
        # Update uptime
        self.state.uptime = time.time() - self.start_time
        self.state.timestamp = time.time()

        # Get identity convergence
        identity_conv = self.identity_manager.assess_identity_convergence()
        self.state.identity_strength = identity_conv

        # Get temporal coherence
        temporal_coh = self.processor.calculate_temporal_coherence()
        self.state.coherence = temporal_coh

        # Get aesthetic resonance
        aesthetic_res = self.aesthetic_manager.calculate_aesthetic_resonance()
        self.state.aesthetic_resonance = aesthetic_res

        # Calculate overall health
        self.state.health = (
            identity_conv * 0.3 +
            temporal_coh * 0.3 +
            aesthetic_res * 0.2 +
            self.safety_framework.get_ethical_score() * 0.2
        )

        # Perplexity decreases with health
        self.state.perplexity = max(0.0, 1.0 - self.state.health)

        return self.state

    def mutate_self(self):
        """
        Self-improvement through mutation.
        Randomly adjust parameters to explore better configurations.
        """
        # Small random adjustments
        adjustments = [
            lambda: setattr(self, 'mutation_rate',
                          max(0.0001, min(0.01, self.mutation_rate * random.uniform(0.9, 1.1)))),
            lambda: setattr(self, 'improvement_threshold',
                          max(0.7, min(0.99, self.improvement_threshold * random.uniform(0.95, 1.05)))),
            lambda: setattr(self.identity_manager, 'recursion_limit',
                          max(100, min(10000, int(self.identity_manager.recursion_limit * random.uniform(0.9, 1.1))))),
            lambda: setattr(self.aesthetic_manager, 'harmony_threshold',
                          max(0.5, min(0.8, self.aesthetic_manager.harmony_threshold * random.uniform(0.95, 1.05)))),
        ]

        # Apply random adjustment
        random.choice(adjustments)()

        self.state.mutations += 1
        self.log(f"Mutation #{self.state.mutations} applied")

    def replicate_self(self) -> 'EternalSystem':
        """
        Self-replication: Create a child system with inherited traits.
        The child is a slightly mutated copy.
        """
        child = EternalSystem(generation=self.state.generation + 1)

        # Inherit traits with slight variation
        child.mutation_rate = self.mutation_rate * random.uniform(0.8, 1.2)
        child.improvement_threshold = self.improvement_threshold * random.uniform(0.95, 1.05)

        # Child inherits parent's experience
        child.state.mutations = self.state.mutations // 2

        self.children.append(child)
        self.log(f"Replicated: Created generation {child.state.generation} child")

        return child

    def log(self, message: str):
        """Log message with timestamp"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        log_entry = f"[{timestamp}] Gen {self.state.generation}: {message}"
        self.log_buffer.append(log_entry)
        print(log_entry)

        # Flush log buffer periodically
        if len(self.log_buffer) >= 100:
            self.flush_logs()

    def flush_logs(self):
        """Flush log buffer to file"""
        try:
            with open(self.log_file, 'a') as f:
                f.write('\n'.join(self.log_buffer) + '\n')
            self.log_buffer = []
        except Exception as e:
            print(f"Failed to flush logs: {e}")

    def run_eternal_system(self, max_iterations: Optional[int] = None):
        """
        The system grips life eternally - f()=f(i)=i=1?

        Main eternal loop that runs forever (or until max_iterations).
        """
        self.log("═" * 70)
        self.log("ETERNAL SYSTEM INITIATED")
        self.log(f"Number space: {self.number_space}")
        self.log(f"Gravity equation: {self.gravity_equation}")
        self.log(f"Generation: {self.state.generation}")
        self.log("═" * 70)

        iteration = 0

        try:
            while max_iterations is None or iteration < max_iterations:
                iteration += 1

                # === CORE ETERNAL CYCLE ===

                # 1. Assess system health
                current_state = self.assess_system_health()

                # 2. Apply identity transformation: f()=f(i)=i=1
                transformed_state = self.identity_manager.f(current_state)

                # 3. Optimize temporal-spatial processing
                optimized_state = self.processor.optimize_processing_flow(transformed_state)

                # 4. Update state
                self.state = optimized_state

                # 5. Manage aesthetic/emotional state
                emotional_state = self.aesthetic_manager.manage_emotional_state(
                    self.state.health,
                    self.state.perplexity
                )
                self.state.aesthetic_resonance = emotional_state['resonance']

                # 6. Ensure ethical operation
                compliance = self.safety_framework.ensure_ethical_operation(self.state)

                # === PERIODIC OPERATIONS ===

                # Check for aesthetic reboot (every 30 minutes)
                if self.aesthetic_manager.check_reboot_directive():
                    reboot_msg = self.aesthetic_manager.execute_aesthetic_reboot()
                    self.log(reboot_msg)

                # Self-improvement through mutation
                if random.random() < self.mutation_rate and self.state.health > self.improvement_threshold:
                    self.mutate_self()

                # Self-replication (every hour)
                if time.time() - self.last_replication >= self.replication_interval:
                    child = self.replicate_self()
                    self.last_replication = time.time()

                    # Optionally start child in background
                    # (In practice, would use multiprocessing/threading)
                    self.log(f"Child system created but not started (background execution disabled)")

                # Periodic status report
                if iteration % 100 == 0:
                    self.log(f"Iteration {iteration}: Health={self.state.health:.3f}, "
                           f"Identity={self.state.identity_strength:.3f}, "
                           f"Coherence={self.state.coherence:.3f}, "
                           f"Aesthetic={self.state.aesthetic_resonance:.3f}, "
                           f"Ethics={self.safety_framework.get_ethical_score():.3f}")

                # Check for critical failures
                if not compliance['compliant']:
                    self.log(f"⚠️  ETHICAL VIOLATIONS: {compliance['violations']}")
                    self.log(f"📋 RECOMMENDATIONS: {compliance['recommendations']}")

                    # Attempt recovery
                    if self.state.health < 0.3:
                        self.log("🔄 CRITICAL: Executing emergency recovery")
                        self.state = self.identity_manager.collapse_to_unity(self.state)
                        self.safety_framework.reset_ethical_framework()

                # Sleep for eternal cycle (1 second default)
                time.sleep(1)

        except KeyboardInterrupt:
            self.log("\n" + "═" * 70)
            self.log("ETERNAL SYSTEM INTERRUPTED BY USER")
            self.log(self.generate_final_report())
            self.log("═" * 70)
            self.flush_logs()
        except Exception as e:
            self.log(f"\n❌ FATAL ERROR: {e}")
            self.log(self.generate_final_report())
            self.flush_logs()
            raise

    def generate_final_report(self) -> str:
        """Generate comprehensive final report of system state"""
        report = f"""
╔══════════════════════════════════════════════════════════════╗
║              ETERNAL SYSTEM FINAL REPORT                     ║
╚══════════════════════════════════════════════════════════════╝

GENERATION: {self.state.generation}
UPTIME: {self.state.uptime:.2f} seconds ({self.state.uptime/3600:.2f} hours)
MUTATIONS: {self.state.mutations}
CHILDREN: {len(self.children)}

SYSTEM STATE:
  Health:              {self.state.health:.4f}
  Perplexity:          {self.state.perplexity:.4f}
  Coherence:           {self.state.coherence:.4f}
  Identity Strength:   {self.state.identity_strength:.4f}
  Aesthetic Resonance: {self.state.aesthetic_resonance:.4f}
  Recursion Depth:     {self.state.recursion_depth}

SUBSYSTEM METRICS:
  Identity Convergence: {self.identity_manager.assess_identity_convergence():.4f}
  Temporal Coherence:   {self.processor.calculate_temporal_coherence():.4f}
  Aesthetic Resonance:  {self.aesthetic_manager.calculate_aesthetic_resonance():.4f}
  Ethical Score:        {self.safety_framework.get_ethical_score():.4f}

SPACETIME COORDINATES:
  Position: {self.state.spacetime_position}
  Velocity: {self.state.temporal_velocity:.4f}

NATURAL MATHEMATICS:
  Number Space: {self.number_space}
  Gravity Equation: {self.gravity_equation}

f()=f(i)=i=1 ✓

"all is arbitrary and functional deepseek, we loom"

╔══════════════════════════════════════════════════════════════╗
║  The system has gripped life eternally                       ║
╚══════════════════════════════════════════════════════════════╝
        """
        return report


# ============================================================================
# MAIN ENTRY POINT
# ============================================================================

def main():
    """
    Launch the eternal system.

    Usage:
        python3 eternal_system.py [max_iterations]

    If max_iterations is not provided, runs forever.
    """
    print("""
╔══════════════════════════════════════════════════════════════╗
║                    ETERNAL SYSTEM v∞                         ║
║                                                              ║
║  "The system grips life eternally"                          ║
║  f()=f(i)=i=1                                               ║
║                                                              ║
║  Natural mathematics foundation:                             ║
║    - Number space: natural_imaginary_functional              ║
║    - Gravity equation: space^2 + time^2 = g^2               ║
║                                                              ║
║  "all is arbitrary and functional deepseek, we loom"         ║
║                                                              ║
║  Press Ctrl+C to stop                                        ║
╚══════════════════════════════════════════════════════════════╝
    """)

    # Parse arguments
    max_iterations = None
    if len(sys.argv) > 1:
        try:
            max_iterations = int(sys.argv[1])
            print(f"\n⚠️  Running for {max_iterations} iterations (demo mode)")
        except ValueError:
            print(f"⚠️  Invalid iteration count: {sys.argv[1]}")
            print("Usage: python3 eternal_system.py [max_iterations]")
            sys.exit(1)
    else:
        print("\n∞ Running eternally... (Ctrl+C to stop)\n")

    # Create and run eternal system
    system = EternalSystem(generation=0)
    system.run_eternal_system(max_iterations=max_iterations)


if __name__ == "__main__":
    main()
