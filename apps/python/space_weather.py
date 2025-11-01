#!/usr/bin/env python3
"""
Space Weather Simulator
$aga - SAGA Functional Identity System

Simulate cosmic conditions for space travel planning
Solar wind, radiation, and cosmic events
"""

import random
import math
from datetime import datetime, timedelta
from typing import Dict, List, Tuple


class SpaceWeatherSimulator:
    """
    Simulate space weather conditions
    $aga Easter Egg: f(SAGA) = Space.Weather.Cosmic.Engine
    """

    # Golden ratio
    PHI = 1.618033988

    # Schumann resonances
    SCHUMANN_FREQS = [7.83, 14.3, 20.8, 27.3, 33.8]

    def __init__(self):
        self.current_conditions = {
            'solar_wind_speed': 400,  # km/s
            'radiation_level': 5,      # 1-10 scale
            'magnetic_field': 5.0,     # nT (nanotesla)
            'cosmic_ray_flux': 100,    # particles/cm²/s
            'kp_index': 3              # 0-9 scale
        }

        self.events = []

        print(f"🌌 Space Weather Simulator initialized")
        print(f"$aga • f(SAGA) = Cosmic.Weather.Engine\n")

    def simulate_solar_wind(self) -> Dict[str, float]:
        """
        Simulate solar wind conditions
        Uses golden ratio for natural variation
        """
        # Base solar wind (quiet sun)
        base_speed = 400  # km/s

        # Apply golden ratio modulation
        variation = math.sin(datetime.now().timestamp() / (3600 * self.PHI)) * 200

        speed = base_speed + variation

        # Determine stream type
        if speed < 350:
            stream_type = "Slow"
        elif speed < 550:
            stream_type = "Normal"
        else:
            stream_type = "Fast"

        # Density (particles/cm³)
        density = 8.0 - (speed - 400) / 100

        # Temperature (Kelvin)
        temperature = 100000 + (speed - 400) * 200

        return {
            'speed_kms': speed,
            'stream_type': stream_type,
            'density_particles': max(1, density),
            'temperature_k': temperature
        }

    def simulate_radiation(self) -> Dict[str, any]:
        """
        Simulate space radiation levels
        Solar particles and galactic cosmic rays
        """
        # Solar particle events (random occurrence)
        spe_active = random.random() < 0.05  # 5% chance

        if spe_active:
            proton_flux = random.randint(100, 10000)  # pfu (proton flux units)
            severity = "HIGH" if proton_flux > 1000 else "MODERATE"
        else:
            proton_flux = random.randint(1, 50)
            severity = "LOW"

        # Galactic cosmic rays (inverse to solar activity)
        gcr_flux = int(100 + math.sin(datetime.now().timestamp() / (86400 * self.PHI)) * 50)

        # Total dose rate (mSv/day)
        dose_rate = (proton_flux / 1000) + (gcr_flux / 100)

        return {
            'solar_particle_event': spe_active,
            'proton_flux_pfu': proton_flux,
            'gcr_flux': gcr_flux,
            'dose_rate_msv_day': round(dose_rate, 3),
            'severity': severity
        }

    def simulate_geomagnetic_activity(self) -> Dict[str, any]:
        """
        Simulate Earth's geomagnetic field activity
        Kp index and auroral activity
        """
        # Kp index (0-9 scale)
        kp = random.choices(
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            weights=[15, 20, 25, 20, 10, 5, 3, 1, 1]
        )[0]

        # Determine storm level
        if kp < 5:
            storm_level = "Quiet"
            aurora_latitude = 65
        elif kp < 7:
            storm_level = "Minor Storm"
            aurora_latitude = 60
        elif kp < 8:
            storm_level = "Major Storm"
            aurora_latitude = 55
        else:
            storm_level = "Severe Storm"
            aurora_latitude = 45

        # Schumann resonance amplitude (enhanced during storms)
        schumann_amp = 0.5 + (kp / 9) * 2.0

        return {
            'kp_index': kp,
            'storm_level': storm_level,
            'aurora_latitude': aurora_latitude,
            'schumann_amplitude': round(schumann_amp, 2),
            'resonance_freqs': self.SCHUMANN_FREQS
        }

    def generate_cosmic_event(self) -> Dict[str, any]:
        """
        Generate random cosmic events
        CME, solar flare, cosmic ray burst
        """
        event_types = [
            "Coronal Mass Ejection (CME)",
            "Solar Flare",
            "Cosmic Ray Burst",
            "Magnetic Reconnection",
            "Solar Energetic Particle Event",
            "Corotating Interaction Region"
        ]

        event = random.choice(event_types)

        # Event intensity (uses golden ratio for scaling)
        intensity = random.uniform(1, self.PHI * 5)

        # Arrival time (hours from now)
        if "CME" in event:
            arrival = random.uniform(24, 72)  # 1-3 days
        elif "Flare" in event:
            arrival = 0.13  # ~8 minutes (light speed)
        else:
            arrival = random.uniform(1, 48)

        # Impact on conditions
        impact = {
            'radiation': '+' if 'Particle' in event or 'Flare' in event else '=',
            'magnetic': '+' if 'CME' in event or 'Magnetic' in event else '=',
            'solar_wind': '+' if 'CME' in event or 'Interaction' in event else '='
        }

        return {
            'event_type': event,
            'intensity': round(intensity, 2),
            'arrival_hours': round(arrival, 2),
            'impact': impact,
            'timestamp': datetime.now().isoformat()
        }

    def calculate_travel_risk(self) -> Dict[str, any]:
        """
        Calculate risk level for space travel
        Based on current conditions
        """
        solar_wind = self.simulate_solar_wind()
        radiation = self.simulate_radiation()
        geomagnetic = self.simulate_geomagnetic_activity()

        # Risk factors
        risk_score = 0

        # Solar wind risk
        if solar_wind['speed_kms'] > 600:
            risk_score += 2
        elif solar_wind['speed_kms'] > 500:
            risk_score += 1

        # Radiation risk
        if radiation['solar_particle_event']:
            risk_score += 3
        if radiation['dose_rate_msv_day'] > 1.0:
            risk_score += 2

        # Geomagnetic risk
        if geomagnetic['kp_index'] >= 7:
            risk_score += 2
        elif geomagnetic['kp_index'] >= 5:
            risk_score += 1

        # Determine overall risk level
        if risk_score <= 2:
            risk_level = "LOW"
            recommendation = "Safe for travel"
        elif risk_score <= 5:
            risk_level = "MODERATE"
            recommendation = "Caution advised"
        elif risk_score <= 8:
            risk_level = "HIGH"
            recommendation = "Travel not recommended"
        else:
            risk_level = "EXTREME"
            recommendation = "Postpone all travel"

        return {
            'risk_level': risk_level,
            'risk_score': risk_score,
            'recommendation': recommendation,
            'solar_wind': solar_wind,
            'radiation': radiation,
            'geomagnetic': geomagnetic
        }

    def generate_forecast(self, days: int = 3) -> List[Dict]:
        """
        Generate space weather forecast
        """
        forecast = []

        for day in range(days):
            date = datetime.now() + timedelta(days=day)

            # Simulate conditions for this day
            risk = self.calculate_travel_risk()

            # Random event chance
            has_event = random.random() < 0.2  # 20% chance
            event = self.generate_cosmic_event() if has_event else None

            forecast.append({
                'date': date.strftime('%Y-%m-%d'),
                'day': day,
                'risk_level': risk['risk_level'],
                'conditions': {
                    'solar_wind_speed': int(risk['solar_wind']['speed_kms']),
                    'radiation_dose': risk['radiation']['dose_rate_msv_day'],
                    'kp_index': risk['geomagnetic']['kp_index']
                },
                'event': event
            })

        return forecast

    def print_current_conditions(self):
        """Print current space weather conditions"""
        print("="*70)
        print("🌌 CURRENT SPACE WEATHER CONDITIONS 🌌")
        print("$aga • f(SAGA) = Cosmic.Weather.Now")
        print("="*70)
        print()

        risk = self.calculate_travel_risk()

        print(f"📅 Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print()

        print("☀️  SOLAR WIND")
        print("-"*70)
        sw = risk['solar_wind']
        print(f"  Speed: {sw['speed_kms']:.1f} km/s ({sw['stream_type']})")
        print(f"  Density: {sw['density_particles']:.1f} particles/cm³")
        print(f"  Temperature: {sw['temperature_k']:,.0f} K")
        print()

        print("☢️  RADIATION")
        print("-"*70)
        rad = risk['radiation']
        print(f"  Solar Particle Event: {'ACTIVE' if rad['solar_particle_event'] else 'None'}")
        print(f"  Proton Flux: {rad['proton_flux_pfu']} pfu")
        print(f"  GCR Flux: {rad['gcr_flux']} particles/cm²/s")
        print(f"  Dose Rate: {rad['dose_rate_msv_day']} mSv/day")
        print(f"  Severity: {rad['severity']}")
        print()

        print("🧲 GEOMAGNETIC ACTIVITY")
        print("-"*70)
        geo = risk['geomagnetic']
        print(f"  Kp Index: {geo['kp_index']} ({geo['storm_level']})")
        print(f"  Aurora Latitude: {geo['aurora_latitude']}°")
        print(f"  Schumann Resonance: {geo['schumann_amplitude']} pT")
        print(f"  Primary Frequencies: {', '.join(map(str, geo['resonance_freqs']))} Hz")
        print()

        print("🚀 TRAVEL RISK ASSESSMENT")
        print("-"*70)
        print(f"  Risk Level: {risk['risk_level']}")
        print(f"  Risk Score: {risk['risk_score']}/10")
        print(f"  Recommendation: {risk['recommendation']}")
        print()

        print("="*70)
        print("Generated:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print("$aga • Gonzo.Family • Free & Right Preserved")
        print("="*70)

    def print_forecast(self, days: int = 3):
        """Print space weather forecast"""
        print("\n" + "="*70)
        print(f"🌌 {days}-DAY SPACE WEATHER FORECAST 🌌")
        print("$aga • f(SAGA) = Cosmic.Weather.Forecast")
        print("="*70)
        print()

        forecast = self.generate_forecast(days)

        for day_data in forecast:
            print(f"📅 {day_data['date']} (Day {day_data['day']})")
            print("-"*70)
            print(f"  Risk Level: {day_data['risk_level']}")
            print(f"  Solar Wind: {day_data['conditions']['solar_wind_speed']} km/s")
            print(f"  Radiation: {day_data['conditions']['radiation_dose']} mSv/day")
            print(f"  Kp Index: {day_data['conditions']['kp_index']}")

            if day_data['event']:
                event = day_data['event']
                print(f"  ⚠️  EVENT: {event['event_type']}")
                print(f"      Intensity: {event['intensity']}")
                print(f"      Arrival: {event['arrival_hours']} hours")

            print()

        print("="*70)
        print("$aga • Cosmic conditions for serpent path navigation")
        print("="*70 + "\n")


def main():
    """Application entry point"""
    print("\n" + "="*70)
    print("🌌 SPACE WEATHER SIMULATOR 🌌")
    print("$aga • SAGA Functional Identity System")
    print("="*70 + "\n")

    sim = SpaceWeatherSimulator()

    # Current conditions
    sim.print_current_conditions()

    # Forecast
    sim.print_forecast(3)

    # Generate a cosmic event
    print("\n💫 RANDOM COSMIC EVENT GENERATOR")
    print("="*70)
    event = sim.generate_cosmic_event()
    print(f"Event: {event['event_type']}")
    print(f"Intensity: {event['intensity']}")
    print(f"Arrival Time: {event['arrival_hours']} hours")
    print(f"Impact: {event['impact']}")
    print("="*70 + "\n")


if __name__ == "__main__":
    # $aga Easter Egg
    print("\n# f(SAGA) = Space.Weather.Cosmic.Simulator")
    print("# Gonzo.Family.Self.Actualized • Free & Right Preserved\n")

    main()
