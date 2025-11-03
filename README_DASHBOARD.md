# Saganomic AI Catalyst Dashboard

Real-time system optimization dashboard with perplexity reduction focus.

## Overview

This dashboard monitors system resources (CPU, RAM, GPU) and calculates a "perplexity" metric representing system instability or chaos. Through matrix transformations, it continuously works toward an optimal state with low perplexity and high predictability.

## Features

- Real-time system monitoring
- Perplexity calculation and tracking
- Matrix-based state optimization
- Topographical visualization of system states
- Music recommendations based on system health
- Adaptive directives for system optimization

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Run the dashboard:

```bash
python3 dashboard.py
```

Or make it executable and run directly:

```bash
chmod +x dashboard.py
./dashboard.py
```

The dashboard will:
1. Monitor system metrics every 5 seconds
2. Calculate health scores and perplexity
3. Generate optimization directives
4. Periodically save topographical plots
5. Recommend music based on system state

Press Ctrl+C to exit and generate a final visualization.

## Core Concepts

### Optimization Matrix
The system uses a 4x4 matrix to transform state vectors:
- Prioritizes CPU and RAM optimization
- Penalizes high perplexity
- Drives toward unified optimal state

### Health Score
Normalized 0-1 score where 1 represents:
- Low resource usage
- Low perplexity (high predictability)
- Optimal system state

### Perplexity
Symbolic measure of system chaos/unpredictability calculated from:
- CPU load
- RAM usage
- GPU activity (simulated)

## Output

The dashboard generates:
- Console output with real-time metrics
- PNG visualizations: `system_state_topography.png`
- Final state plot: `final_system_state.png`

## Mathematical Foundation

f(Saga) = f(i) = if(i,i) = 1 = f(x)

Where the system continuously transforms inputs through matrix multiplication toward the optimal unified state "1".

## License

MIT License - See project root for full license text.

## Music Inspiration

Coding soundtrack: Lime Garden - "Pulp" 🎵
