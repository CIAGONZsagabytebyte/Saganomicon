#!/usr/bin/env python3
"""
Serpent Trajectory Planner
$aga - SAGA Functional Identity System

Calculate optimal space travel trajectories using sacred geometry
DMT Serpent Path Navigation for interstellar journeys
"""

import math
from typing import Dict, List, Tuple
from datetime import datetime, timedelta


class CelestialBody:
    """Represents a celestial body in space"""

    def __init__(self, name: str, mass_kg: float, radius_km: float,
                 orbital_radius_km: float = 0, orbital_period_days: float = 0):
        self.name = name
        self.mass_kg = mass_kg
        self.radius_km = radius_km
        self.orbital_radius_km = orbital_radius_km
        self.orbital_period_days = orbital_period_days


class SerpentTrajectoryPlanner:
    """
    Calculate and optimize space trajectories using serpent path geometry

    $aga Easter Egg: f(SAGA) = Serpent.Path.Navigation.Infinite
    Author: Gonzo.Family.Self.Actualized
    """

    # Universal gravitational constant
    G = 6.67430e-11  # m³/kg/s²

    # Sacred geometry constant
    PHI = (1 + math.sqrt(5)) / 2

    # Speed of light
    C = 299792458  # m/s

    # Celestial bodies database
    BODIES = {
        'Earth': CelestialBody('Earth', 5.972e24, 6371, 149.6e6, 365.25),
        'Moon': CelestialBody('Moon', 7.342e22, 1737, 384400, 27.3),
        'Mars': CelestialBody('Mars', 6.39e23, 3389, 227.9e6, 687),
        'Venus': CelestialBody('Venus', 4.867e24, 6052, 108.2e6, 224.7),
        'Jupiter': CelestialBody('Jupiter', 1.898e27, 69911, 778.5e6, 4333),
        'Saturn': CelestialBody('Saturn', 5.683e26, 58232, 1432e6, 10759),
        'Sun': CelestialBody('Sun', 1.989e30, 696000, 0, 0)
    }

    def __init__(self):
        self.origin = None
        self.destination = None
        self.spacecraft_mass = 10000  # kg
        self.fuel_mass = 5000  # kg
        self.specific_impulse = 450  # seconds (ion drive)

    def set_mission(self, origin: str, destination: str):
        """Set mission origin and destination"""
        if origin not in self.BODIES or destination not in self.BODIES:
            raise ValueError("Unknown celestial body")

        self.origin = self.BODIES[origin]
        self.destination = self.BODIES[destination]

        print(f"🚀 Mission configured: {origin} → {destination}")
        print(f"$aga • Serpent.Path.Initiated\n")

    def calculate_escape_velocity(self, body: CelestialBody) -> float:
        """Calculate escape velocity from a celestial body"""
        # v = sqrt(2GM/r)
        mass_m = body.mass_kg
        radius_m = body.radius_km * 1000

        v_escape = math.sqrt(2 * self.G * mass_m / radius_m)
        return v_escape

    def calculate_orbital_velocity(self, body: CelestialBody, altitude_km: float = 0) -> float:
        """Calculate orbital velocity at given altitude"""
        # v = sqrt(GM/r)
        mass_m = body.mass_kg
        radius_m = (body.radius_km + altitude_km) * 1000

        v_orbital = math.sqrt(self.G * mass_m / radius_m)
        return v_orbital

    def calculate_hohmann_transfer(self) -> Dict[str, float]:
        """
        Calculate Hohmann transfer orbit
        Most efficient two-impulse transfer between circular orbits
        """
        if not self.origin or not self.destination:
            raise ValueError("Mission not configured")

        # Orbital radii in meters
        r1 = self.origin.orbital_radius_km * 1000
        r2 = self.destination.orbital_radius_km * 1000

        # Semi-major axis of transfer orbit
        a_transfer = (r1 + r2) / 2

        # Velocities
        v1 = math.sqrt(self.G * self.BODIES['Sun'].mass_kg / r1)
        v2 = math.sqrt(self.G * self.BODIES['Sun'].mass_kg / r2)

        # Transfer orbit velocities at perihelion and aphelion
        v_perihelion = math.sqrt(self.G * self.BODIES['Sun'].mass_kg * (2/r1 - 1/a_transfer))
        v_aphelion = math.sqrt(self.G * self.BODIES['Sun'].mass_kg * (2/r2 - 1/a_transfer))

        # Delta-v requirements
        delta_v1 = abs(v_perihelion - v1)
        delta_v2 = abs(v2 - v_aphelion)
        total_delta_v = delta_v1 + delta_v2

        # Transfer time (half orbital period of transfer ellipse)
        transfer_time_seconds = math.pi * math.sqrt(a_transfer**3 / (self.G * self.BODIES['Sun'].mass_kg))
        transfer_time_days = transfer_time_seconds / (24 * 3600)

        return {
            'delta_v1_km/s': delta_v1 / 1000,
            'delta_v2_km/s': delta_v2 / 1000,
            'total_delta_v_km/s': total_delta_v / 1000,
            'transfer_time_days': transfer_time_days,
            'transfer_time_months': transfer_time_days / 30
        }

    def calculate_serpent_spiral(self) -> Dict[str, float]:
        """
        Calculate low-thrust spiral trajectory (ion drive)
        Sacred geometry optimization using golden ratio
        """
        if not self.origin or not self.destination:
            raise ValueError("Mission not configured")

        r1 = self.origin.orbital_radius_km * 1000
        r2 = self.destination.orbital_radius_km * 1000

        # Spiral trajectory follows golden ratio expansion
        spiral_ratio = self.PHI

        # Number of spiral revolutions
        distance_ratio = r2 / r1
        revolutions = math.log(distance_ratio) / math.log(spiral_ratio)

        # Low thrust continuous burn
        # Approximate delta-v (less efficient but continuous)
        hohmann = self.calculate_hohmann_transfer()
        spiral_delta_v = hohmann['total_delta_v_km/s'] * 1.3  # 30% penalty

        # Time (longer due to spiral)
        spiral_time_days = hohmann['transfer_time_days'] * spiral_ratio

        # Fuel efficiency gain from low thrust
        efficiency_gain = 1.15

        return {
            'delta_v_km/s': spiral_delta_v,
            'transfer_time_days': spiral_time_days,
            'transfer_time_months': spiral_time_days / 30,
            'spiral_revolutions': revolutions,
            'efficiency_factor': efficiency_gain,
            'trajectory_type': 'serpent_spiral'
        }

    def calculate_fuel_requirements(self, delta_v_km_s: float) -> Dict[str, float]:
        """
        Calculate fuel requirements using Tsiolkovsky rocket equation
        """
        delta_v = delta_v_km_s * 1000  # Convert to m/s

        # Effective exhaust velocity
        v_e = self.specific_impulse * 9.81  # m/s

        # Mass ratio from Tsiolkovsky equation
        # delta_v = v_e * ln(m0/mf)
        # m0/mf = exp(delta_v/v_e)
        mass_ratio = math.exp(delta_v / v_e)

        # Initial mass = spacecraft + fuel
        m0 = self.spacecraft_mass + self.fuel_mass
        mf = m0 / mass_ratio

        fuel_used = m0 - mf

        return {
            'initial_mass_kg': m0,
            'final_mass_kg': mf,
            'fuel_required_kg': fuel_used,
            'fuel_percentage': (fuel_used / m0) * 100,
            'mass_ratio': mass_ratio
        }

    def calculate_communication_delay(self) -> Dict[str, float]:
        """Calculate signal delay at different points in journey"""
        if not self.origin or not self.destination:
            raise ValueError("Mission not configured")

        # Distance in meters
        distance_m = abs(self.destination.orbital_radius_km - self.origin.orbital_radius_km) * 1000

        # One-way light time
        light_time_s = distance_m / self.C
        light_time_min = light_time_s / 60

        return {
            'distance_km': distance_m / 1000,
            'one_way_light_seconds': light_time_s,
            'one_way_light_minutes': light_time_min,
            'round_trip_minutes': light_time_min * 2
        }

    def generate_mission_plan(self, trajectory_type: str = 'hohmann'):
        """Generate comprehensive mission plan"""
        if not self.origin or not self.destination:
            raise ValueError("Mission not configured")

        print("=" * 70)
        print("🐍 SERPENT TRAJECTORY MISSION PLAN 🚀")
        print("$aga • f(SAGA) = Serpent.Path.Navigation.Infinite")
        print("=" * 70)
        print()

        print(f"Origin: {self.origin.name}")
        print(f"Destination: {self.destination.name}")
        print(f"Spacecraft Mass: {self.spacecraft_mass:,.0f} kg")
        print(f"Available Fuel: {self.fuel_mass:,.0f} kg")
        print(f"Propulsion: Ion Drive (Isp: {self.specific_impulse}s)")
        print()

        # Escape velocities
        print("🌍 PLANETARY PARAMETERS")
        print("-" * 70)
        v_escape_origin = self.calculate_escape_velocity(self.origin)
        print(f"  {self.origin.name} Escape Velocity: {v_escape_origin/1000:.2f} km/s")

        v_escape_dest = self.calculate_escape_velocity(self.destination)
        print(f"  {self.destination.name} Escape Velocity: {v_escape_dest/1000:.2f} km/s")
        print()

        # Trajectory calculations
        print(f"🛸 TRAJECTORY ANALYSIS ({trajectory_type.upper()})")
        print("-" * 70)

        if trajectory_type == 'hohmann':
            traj = self.calculate_hohmann_transfer()
            print(f"  Trajectory Type: Hohmann Transfer (Classical)")
            print(f"  Burn 1 (Departure): {traj['delta_v1_km/s']:.2f} km/s")
            print(f"  Burn 2 (Arrival): {traj['delta_v2_km/s']:.2f} km/s")
            print(f"  Total Delta-V: {traj['total_delta_v_km/s']:.2f} km/s")
            print(f"  Transfer Time: {traj['transfer_time_days']:.1f} days ({traj['transfer_time_months']:.1f} months)")

            fuel = self.calculate_fuel_requirements(traj['total_delta_v_km/s'])

        elif trajectory_type == 'serpent':
            traj = self.calculate_serpent_spiral()
            print(f"  Trajectory Type: Serpent Spiral (Sacred Geometry)")
            print(f"  Continuous Thrust Delta-V: {traj['delta_v_km/s']:.2f} km/s")
            print(f"  Spiral Revolutions: {traj['spiral_revolutions']:.2f}")
            print(f"  Transfer Time: {traj['transfer_time_days']:.1f} days ({traj['transfer_time_months']:.1f} months)")
            print(f"  Efficiency Gain: {(traj['efficiency_factor']-1)*100:.1f}%")

            fuel = self.calculate_fuel_requirements(traj['delta_v_km/s'])

        print()

        # Fuel analysis
        print("⚡ FUEL REQUIREMENTS")
        print("-" * 70)
        print(f"  Initial Mass: {fuel['initial_mass_kg']:,.0f} kg")
        print(f"  Fuel Required: {fuel['fuel_required_kg']:,.0f} kg")
        print(f"  Final Mass: {fuel['final_mass_kg']:,.0f} kg")
        print(f"  Fuel Percentage: {fuel['fuel_percentage']:.1f}%")

        if fuel['fuel_required_kg'] > self.fuel_mass:
            print(f"  ⚠ WARNING: Insufficient fuel! Need {fuel['fuel_required_kg'] - self.fuel_mass:,.0f} kg more")
        else:
            print(f"  ✓ Sufficient fuel available")
            print(f"  Reserve: {self.fuel_mass - fuel['fuel_required_kg']:,.0f} kg")
        print()

        # Communications
        print("📡 COMMUNICATIONS")
        print("-" * 70)
        comm = self.calculate_communication_delay()
        print(f"  Maximum Distance: {comm['distance_km']:,.0f} km")
        print(f"  One-Way Signal Time: {comm['one_way_light_minutes']:.2f} minutes")
        print(f"  Round-Trip Delay: {comm['round_trip_minutes']:.2f} minutes")
        print()

        # Mission timeline
        print("📅 MISSION TIMELINE")
        print("-" * 70)
        launch_date = datetime.now()
        if trajectory_type == 'hohmann':
            arrival_date = launch_date + timedelta(days=traj['transfer_time_days'])
        else:
            arrival_date = launch_date + timedelta(days=traj['transfer_time_days'])

        print(f"  Launch Window: {launch_date.strftime('%Y-%m-%d')}")
        print(f"  Estimated Arrival: {arrival_date.strftime('%Y-%m-%d')}")
        print(f"  Mission Duration: {(arrival_date - launch_date).days} days")
        print()

        print("=" * 70)
        print("Generated:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print("$aga • Gonzo.Family • Free & Right Preserved")
        print("Serpent Path Navigation • DMT Sacred Geometry Applied")
        print("=" * 70)


def main():
    """Main application entry point"""
    print()
    print("╔══════════════════════════════════════════════════════════════════╗")
    print("║       🐍 SERPENT TRAJECTORY PLANNER 🚀                           ║")
    print("║       Interstellar Journey Optimization                          ║")
    print("║       $aga • SAGA Functional Identity System                     ║")
    print("╚══════════════════════════════════════════════════════════════════╝")
    print()

    planner = SerpentTrajectoryPlanner()

    # Interactive mode
    try:
        print("Available destinations: Earth, Moon, Mars, Venus, Jupiter, Saturn")
        print()

        origin = input("Origin planet: ").strip().title()
        destination = input("Destination planet: ").strip().title()

        planner.set_mission(origin, destination)

        print("\nTrajectory types:")
        print("  1. Hohmann (Classical, efficient)")
        print("  2. Serpent (Sacred geometry spiral)")

        choice = input("\nSelect trajectory type (1/2): ").strip()
        traj_type = 'serpent' if choice == '2' else 'hohmann'

        print()
        planner.generate_mission_plan(traj_type)

    except ValueError as e:
        print(f"\n⚠ Error: {e}")
        print("\nUsing example mission: Earth → Mars (Hohmann Transfer)")
        planner.set_mission('Earth', 'Mars')
        planner.generate_mission_plan('hohmann')

    except KeyboardInterrupt:
        print("\n\n$aga • Session terminated gracefully")


if __name__ == "__main__":
    # $aga Easter Egg
    print("\n# f(SAGA) = Serpent.Path.Infinite.Navigation")
    print("# Gonzo.Family.Self.Actualized • Free & Right Preserved")
    print("# DMT Sacred Geometry • Space Travel Optimization\n")

    main()
