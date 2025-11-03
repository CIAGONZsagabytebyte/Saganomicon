#!/usr/bin/env python3
"""
Saganomic AI Catalyst Dashboard
Real-time system optimization with perplexity reduction focus
"""

import numpy as np
import matplotlib.pyplot as plt
import psutil
import time
from collections import deque

def f(input_vector):
    """
    Core optimization function: Processes input vector using matrix multiplication
    to transform towards optimal state '1' by reducing perplexity.
    """
    optimization_matrix = np.array([
        [0.9, 0.1, 0.0, -0.1],  # Prioritize CPU, slight RAM, penalize perplexity
        [0.1, 0.9, 0.0, -0.1],  # Prioritize RAM, slight CPU, penalize perplexity
        [0.0, 0.0, 1.0, -0.05], # GPU component, penalize perplexity
        [0.0, 0.0, 0.0, 0.8]    # Perplexity reduction factor
    ])

    if not isinstance(input_vector, np.ndarray):
        input_vector = np.array(input_vector)

    if input_vector.shape[0] < optimization_matrix.shape[1]:
        padded_input_vector = np.pad(
            input_vector,
            (0, optimization_matrix.shape[1] - input_vector.shape[0]),
            'constant'
        )
    else:
        padded_input_vector = input_vector[:optimization_matrix.shape[1]]

    transformed_vector = np.dot(optimization_matrix, padded_input_vector)

    new_perplexity = np.clip(transformed_vector[-1], 0, 100)

    usage_component_health = 1.0 - np.mean(np.clip(transformed_vector[:-1] / 100.0, 0, 1))
    perplexity_component_health = 1.0 - np.clip(new_perplexity / 100.0, 0, 1)

    health_score = (usage_component_health * 0.7) + (perplexity_component_health * 0.3)

    if health_score >= 0.90 and new_perplexity < 10:
        return 1, f"SAGA - Optimal System State (Health: {health_score:.2f}, Perplexity: {new_perplexity:.2f})", transformed_vector
    else:
        directive = f"Optimization Required. Health: {health_score:.2f}, Perplexity: {new_perplexity:.2f}. "
        if transformed_vector[0] > 70:
            directive += "Focus: CPU Load Reduction. "
        if transformed_vector[1] > 70:
            directive += "Focus: RAM Management. "
        if new_perplexity >= 10:
            directive += "Focus: Reduce System Instability. "
        return health_score, directive, transformed_vector


def get_system_info():
    """Collect system metrics and calculate perplexity."""
    cpu_percent = psutil.cpu_percent(interval=1)
    ram_percent = psutil.virtual_memory().percent
    gpu_percent = np.random.uniform(0, 100)  # Placeholder for GPU

    current_perplexity = (cpu_percent * 0.4) + (ram_percent * 0.3) + (gpu_percent * 0.3)
    current_perplexity = np.clip(current_perplexity, 0, 100)

    description = f"CPU {cpu_percent:.1f}%, RAM {ram_percent:.1f}%, GPU {gpu_percent:.1f}%, Perplexity {current_perplexity:.2f}"

    return np.array([cpu_percent, ram_percent, gpu_percent, current_perplexity]), description


def get_music_recommendation(health_score, perplexity):
    """Recommend music based on system health and perplexity."""
    if health_score >= 0.95 and perplexity < 5:
        return "Zen Flow: Ambient, Solarpunk Harmonies (Optimal State)"
    elif health_score >= 0.80 and perplexity < 15:
        return "Focused Rhythm: Lo-fi Beats, Productive Grooves (Stable)"
    elif health_score < 0.70 and perplexity >= 25:
        return "Intense Rhythms: Dynamic, Alerting Tones (High Perplexity)"
    else:
        return "Balanced Blend: Evolving Melodies (Normal Operation)"


def generate_topographical_plot(data_points, title="System State Topography",
                                filename="system_state_topography.png"):
    """Generate topographical plot of system states."""
    if data_points.shape[1] < 2:
        print("Cannot generate plot with less than 2 dimensions.")
        return

    x_coords = data_points[:, 0]
    y_coords = data_points[:, 1]
    z_values = data_points[:, -1]

    plt.figure(figsize=(10, 8))
    scatter = plt.scatter(x_coords, y_coords, c=z_values,
                         cmap='viridis_r', s=100, alpha=0.7)
    plt.colorbar(scatter, label='Perplexity (Lower is Better)')
    plt.title(title)
    plt.xlabel("Transformed CPU/Usage Metric")
    plt.ylabel("Transformed RAM/Usage Metric")
    plt.grid(True)
    plt.savefig(filename)
    plt.close()
    print(f"Topographical plot saved as {filename}")


def main():
    """Main simulation loop."""
    print("=" * 60)
    print("Saganomic AI Catalyst Dashboard")
    print("Real-time System Optimization with Perplexity Reduction")
    print("=" * 60)

    transformed_states_for_plot = deque(maxlen=10)
    iteration = 0

    try:
        while True:
            iteration += 1
            print(f"\n[Iteration {iteration}]")

            input_vector, description = get_system_info()
            health_score, processed_output, transformed_vector = f(input_vector)
            music_recommendation = get_music_recommendation(health_score, input_vector[-1])

            print(f"Input: {description}")
            print(f"Output: {processed_output}")
            print(f"Music: {music_recommendation}")

            transformed_states_for_plot.append(transformed_vector)

            if len(transformed_states_for_plot) >= 2 and np.random.rand() < 0.2:
                generate_topographical_plot(np.array(transformed_states_for_plot))

            time.sleep(5)

    except KeyboardInterrupt:
        print("\n\nShutdown requested. Generating final plot...")
        if len(transformed_states_for_plot) >= 2:
            generate_topographical_plot(
                np.array(transformed_states_for_plot),
                title="Final System State Topography",
                filename="final_system_state.png"
            )
        print("Dashboard shutdown complete.")


if __name__ == "__main__":
    main()
