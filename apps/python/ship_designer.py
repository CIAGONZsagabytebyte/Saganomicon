#!/usr/bin/env python3
"""
Solarpunk Ship Designer
$aga - SAGA Functional Identity System

Design and optimize solarpunk spaceships
Sacred geometry-based engineering
"""

import math
import random
from typing import Dict, List, Tuple


class ShipDesigner:
    """
    Design solarpunk spaceships with sacred geometry
    $aga Easter Egg: f(SAGA) = Ship.Design.Sacred.Engineering
    """

    # Golden ratio
    PHI = 1.618033988

    # Ship components
    COMPONENTS = {
        'hull': {
            'light': {'mass': 100, 'armor': 5, 'cost': 500},
            'medium': {'mass': 300, 'armor': 15, 'cost': 1500},
            'heavy': {'mass': 600, 'armor': 30, 'cost': 3000}
        },
        'solar_sails': {
            'small': {'area': 50, 'power': 10, 'mass': 20, 'cost': 800},
            'medium': {'area': 150, 'power': 30, 'mass': 50, 'cost': 2000},
            'large': {'area': 300, 'power': 70, 'mass': 100, 'cost': 4000},
            'mega': {'area': 500, 'power': 120, 'mass': 180, 'cost': 7000}
        },
        'fusion_core': {
            'basic': {'power': 50, 'mass': 150, 'fuel_eff': 0.6, 'cost': 5000},
            'advanced': {'power': 120, 'mass': 200, 'fuel_eff': 0.8, 'cost': 12000},
            'quantum': {'power': 250, 'mass': 180, 'fuel_eff': 0.95, 'cost': 25000}
        },
        'hydro_system': {
            'basic': {'capacity': 100, 'recycling': 0.80, 'mass': 50, 'cost': 1000},
            'advanced': {'capacity': 300, 'recycling': 0.90, 'mass': 80, 'cost': 3000},
            'eden': {'capacity': 500, 'recycling': 0.95, 'mass': 100, 'cost': 6000}
        },
        'bio_dome': {
            'small': {'food': 5, 'oxygen': 10, 'mass': 80, 'cost': 2000},
            'medium': {'food': 15, 'oxygen': 30, 'mass': 150, 'cost': 5000},
            'large': {'food': 40, 'oxygen': 80, 'mass': 300, 'cost': 12000}
        },
        'crew_quarters': {
            'minimal': {'capacity': 5, 'comfort': 3, 'mass': 100, 'cost': 2000},
            'standard': {'capacity': 15, 'comfort': 6, 'mass': 250, 'cost': 6000},
            'luxury': {'capacity': 30, 'comfort': 9, 'mass': 500, 'cost': 15000}
        }
    }

    def __init__(self):
        self.ship = {
            'name': 'Unnamed Ship',
            'components': {},
            'mass': 0,
            'cost': 0,
            'stats': {}
        }

        print(f"🚀 Solarpunk Ship Designer initialized")
        print(f"$aga • f(SAGA) = Ship.Design.Engine\n")

    def add_component(self, component_type: str, variant: str):
        """Add component to ship"""
        if component_type not in self.COMPONENTS:
            print(f"⚠ Unknown component type: {component_type}")
            return

        if variant not in self.COMPONENTS[component_type]:
            print(f"⚠ Unknown variant: {variant}")
            return

        self.ship['components'][component_type] = variant
        print(f"✓ Added {variant} {component_type}")

    def calculate_stats(self) -> Dict:
        """Calculate ship statistics"""
        stats = {
            'mass': 0,
            'cost': 0,
            'power': 0,
            'armor': 0,
            'crew_capacity': 0,
            'food_production': 0,
            'oxygen_production': 0,
            'water_capacity': 0,
            'water_recycling': 0,
            'comfort': 0,
            'sustainability': 0
        }

        # Calculate from components
        for comp_type, variant in self.ship['components'].items():
            comp_data = self.COMPONENTS[comp_type][variant]

            stats['mass'] += comp_data.get('mass', 0)
            stats['cost'] += comp_data.get('cost', 0)
            stats['power'] += comp_data.get('power', 0)
            stats['armor'] += comp_data.get('armor', 0)
            stats['crew_capacity'] += comp_data.get('capacity', 0)
            stats['food_production'] += comp_data.get('food', 0)
            stats['oxygen_production'] += comp_data.get('oxygen', 0)
            stats['water_capacity'] += comp_data.get('capacity', 0)
            stats['comfort'] += comp_data.get('comfort', 0)

            if 'recycling' in comp_data:
                stats['water_recycling'] = comp_data['recycling']

        # Calculate derived stats

        # Speed (power to mass ratio with golden ratio optimization)
        if stats['mass'] > 0:
            stats['speed'] = (stats['power'] / stats['mass']) * self.PHI

        # Sustainability (combines food, oxygen, water recycling)
        if stats['crew_capacity'] > 0:
            food_ratio = min(1.0, stats['food_production'] / stats['crew_capacity'])
            oxy_ratio = min(1.0, stats['oxygen_production'] / (stats['crew_capacity'] * 2))
            water_ratio = stats['water_recycling']
            stats['sustainability'] = (food_ratio + oxy_ratio + water_ratio) / 3 * 100

        # Eden Index (sacred metric)
        stats['eden_index'] = self.calculate_eden_index(stats)

        return stats

    def calculate_eden_index(self, stats: Dict) -> float:
        """
        Calculate Eden Index using golden ratio
        Measures harmony between technology and nature
        """
        if stats['crew_capacity'] == 0:
            return 0

        # Natural elements (bio-dome, water)
        natural = (stats['food_production'] + stats['oxygen_production']) / 2

        # Technical elements (power, armor)
        technical = (stats['power'] + stats['armor']) / 2

        # Balance factor (closer to 1 is better)
        if technical > 0:
            balance = min(natural / technical, technical / natural)
        else:
            balance = 0

        # Sustainability weight
        sustainability_factor = stats['sustainability'] / 100

        # Golden ratio weighting
        eden = (balance * self.PHI + sustainability_factor) / (self.PHI + 1)

        return eden * 100

    def optimize_for_speed(self):
        """Optimize ship for maximum speed"""
        print("\n⚡ Optimizing for SPEED...")
        self.ship['components'] = {
            'hull': 'light',
            'solar_sails': 'mega',
            'fusion_core': 'quantum',
            'hydro_system': 'basic',
            'bio_dome': 'small',
            'crew_quarters': 'minimal'
        }
        print("✓ Speed-optimized configuration applied")

    def optimize_for_sustainability(self):
        """Optimize ship for maximum sustainability"""
        print("\n🌱 Optimizing for SUSTAINABILITY...")
        self.ship['components'] = {
            'hull': 'medium',
            'solar_sails': 'large',
            'fusion_core': 'advanced',
            'hydro_system': 'eden',
            'bio_dome': 'large',
            'crew_quarters': 'standard'
        }
        print("✓ Sustainability-optimized configuration applied")

    def optimize_for_combat(self):
        """Optimize ship for combat/defense"""
        print("\n⚔️  Optimizing for DEFENSE...")
        self.ship['components'] = {
            'hull': 'heavy',
            'solar_sails': 'medium',
            'fusion_core': 'advanced',
            'hydro_system': 'advanced',
            'bio_dome': 'medium',
            'crew_quarters': 'standard'
        }
        print("✓ Defense-optimized configuration applied")

    def optimize_for_luxury(self):
        """Optimize ship for comfort and luxury"""
        print("\n✨ Optimizing for LUXURY...")
        self.ship['components'] = {
            'hull': 'heavy',
            'solar_sails': 'large',
            'fusion_core': 'quantum',
            'hydro_system': 'eden',
            'bio_dome': 'large',
            'crew_quarters': 'luxury'
        }
        print("✓ Luxury-optimized configuration applied")

    def print_design(self):
        """Print ship design details"""
        stats = self.calculate_stats()

        print("\n" + "="*70)
        print("🚀 SOLARPUNK SHIP DESIGN 🚀")
        print("$aga • f(SAGA) = Ship.Design.Manifest")
        print("="*70)
        print()

        print(f"Ship Name: {self.ship['name']}")
        print()

        print("COMPONENTS:")
        print("-"*70)
        for comp_type, variant in self.ship['components'].items():
            comp_data = self.COMPONENTS[comp_type][variant]
            print(f"  {comp_type.replace('_', ' ').title()}: {variant.title()}")
            print(f"    Mass: {comp_data.get('mass', 0)} tons")
            if 'power' in comp_data:
                print(f"    Power: {comp_data['power']} MW")
            if 'armor' in comp_data:
                print(f"    Armor: {comp_data['armor']} units")
            if 'capacity' in comp_data:
                print(f"    Capacity: {comp_data['capacity']}")
        print()

        print("STATISTICS:")
        print("-"*70)
        print(f"  Total Mass: {stats['mass']} tons")
        print(f"  Total Cost: ${stats['cost']:,}")
        print(f"  Power Output: {stats['power']} MW")
        print(f"  Armor Rating: {stats['armor']}")
        print(f"  Speed Index: {stats.get('speed', 0):.2f}")
        print(f"  Crew Capacity: {stats['crew_capacity']} people")
        print()

        print("LIFE SUPPORT:")
        print("-"*70)
        print(f"  Food Production: {stats['food_production']} units/day")
        print(f"  Oxygen Production: {stats['oxygen_production']} units/day")
        print(f"  Water Capacity: {stats['water_capacity']} liters")
        print(f"  Water Recycling: {stats['water_recycling']*100:.0f}%")
        print(f"  Crew Comfort: {stats['comfort']}/10")
        print()

        print("PERFORMANCE METRICS:")
        print("-"*70)
        print(f"  Sustainability: {stats['sustainability']:.1f}%")
        print(f"  Eden Index: {stats['eden_index']:.1f}%")

        if stats['eden_index'] >= 80:
            rating = "EXCELLENT - True Solarpunk Vessel"
        elif stats['eden_index'] >= 60:
            rating = "GOOD - Sustainable Design"
        elif stats['eden_index'] >= 40:
            rating = "FAIR - Needs Improvement"
        else:
            rating = "POOR - Unbalanced Design"

        print(f"  Rating: {rating}")
        print()

        print("="*70)
        print("$aga • Gonzo.Family • Free & Right Preserved")
        print("="*70)


def main():
    """Application entry point"""
    print("\n" + "="*70)
    print("🚀 SOLARPUNK SHIP DESIGNER 🚀")
    print("$aga • SAGA Functional Identity System")
    print("="*70 + "\n")

    designer = ShipDesigner()

    print("Select ship optimization preset:")
    print("1. Speed (Fast travel)")
    print("2. Sustainability (Eden paradise)")
    print("3. Defense (Combat ready)")
    print("4. Luxury (Maximum comfort)")
    print("5. Custom (Choose components)")

    try:
        choice = input("\nEnter choice (1-5): ").strip()

        if choice == '1':
            designer.ship['name'] = "Swift Serpent"
            designer.optimize_for_speed()
        elif choice == '2':
            designer.ship['name'] = "Eden's Harmony"
            designer.optimize_for_sustainability()
        elif choice == '3':
            designer.ship['name'] = "Guardian Shield"
            designer.optimize_for_combat()
        elif choice == '4':
            designer.ship['name'] = "Cosmic Paradise"
            designer.optimize_for_luxury()
        else:
            # Custom build
            designer.ship['name'] = input("Ship name: ") or "Custom Vessel"
            print("\nCustom ship builder not fully implemented.")
            print("Using balanced default configuration...\n")
            designer.optimize_for_sustainability()

        designer.print_design()

    except KeyboardInterrupt:
        print("\n\n$aga • Design session terminated")

    except Exception as e:
        print(f"\n⚠ Error: {e}")
        print("Using default sustainable design...\n")
        designer.ship['name'] = "Default Eden"
        designer.optimize_for_sustainability()
        designer.print_design()


if __name__ == "__main__":
    # $aga Easter Egg
    print("\n# f(SAGA) = Ship.Design.Sacred.Engineering")
    print("# Gonzo.Family.Self.Actualized • Free & Right Preserved\n")

    main()
