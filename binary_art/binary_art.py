#!/usr/bin/env python3
"""
Binary Art Generator
$aga - SAGA Functional Identity System

Generate procedural tilemaps and textures from binary patterns
Sacred geometry meets digital manifestation
"""

import os
import random
import math
from PIL import Image, ImageDraw, ImageFont
from typing import Tuple, List


class BinaryArtGenerator:
    """
    Generate sacred geometry art from binary patterns
    $aga Easter Egg: f(SAGA) = Binary.Dimensional.Art
    """

    # Golden ratio
    PHI = 1.618033988

    # Color palettes (solarpunk + space)
    PALETTES = {
        'solarpunk': [
            (0, 255, 136),      # Eden green
            (127, 255, 170),    # Light green
            (255, 200, 0),      # Solar gold
            (45, 90, 61),       # Deep green
            (255, 255, 100)     # Light gold
        ],
        'space': [
            (10, 15, 30),       # Deep space
            (100, 100, 255),    # Cosmic blue
            (200, 100, 255),    # Nebula purple
            (255, 200, 100),    # Star light
            (50, 50, 80)        # Space gray
        ],
        'quantum': [
            (0, 255, 255),      # Cyan
            (255, 0, 255),      # Magenta
            (255, 255, 0),      # Yellow
            (0, 0, 0),          # Void
            (255, 255, 255)     # Light
        ]
    }

    def __init__(self, output_dir='output'):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        print(f"🎨 Binary Art Generator initialized")
        print(f"$aga • f(SAGA) = Binary.Art.Generator")
        print(f"Output directory: {output_dir}\n")

    def binary_to_pattern(self, value: int, size: int = 8) -> List[int]:
        """Convert integer to binary pattern"""
        binary = format(value, f'0{size}b')
        return [int(b) for b in binary]

    def generate_binary_tilemap(self, width: int = 32, height: int = 32,
                                palette: str = 'solarpunk') -> Image.Image:
        """
        Generate tilemap from binary patterns
        Each tile is derived from binary representation
        """
        tile_size = 16
        img = Image.new('RGB', (width * tile_size, height * tile_size))
        draw = ImageDraw.Draw(img)

        colors = self.PALETTES[palette]

        for y in range(height):
            for x in range(width):
                # Generate binary pattern for this tile
                seed = (x * self.PHI + y) % 256
                pattern = self.binary_to_pattern(int(seed))

                # Draw tile
                for i in range(8):
                    bit = pattern[i]
                    color_idx = bit * (len(colors) - 1)

                    # Create checkerboard sub-tiles
                    sub_x = (i % 4) * (tile_size // 4)
                    sub_y = (i // 4) * (tile_size // 2)

                    tile_x = x * tile_size + sub_x
                    tile_y = y * tile_size + sub_y

                    draw.rectangle([
                        tile_x, tile_y,
                        tile_x + tile_size // 4, tile_y + tile_size // 2
                    ], fill=colors[color_idx])

        return img

    def generate_quantum_noise(self, width: int = 256, height: int = 256,
                               palette: str = 'quantum') -> Image.Image:
        """
        Generate quantum-inspired noise texture
        Using binary randomness with sacred patterns
        """
        img = Image.new('RGB', (width, height))
        pixels = img.load()

        colors = self.PALETTES[palette]

        for y in range(height):
            for x in range(width):
                # Quantum interference pattern
                value1 = int((x * self.PHI + y) % 256)
                value2 = int((x + y * self.PHI) % 256)

                # Binary XOR for quantum superposition
                quantum_value = value1 ^ value2

                # Map to color
                color_idx = (quantum_value % len(colors))
                pixels[x, y] = colors[color_idx]

        return img

    def generate_sacred_grid(self, width: int = 512, height: int = 512,
                            palette: str = 'solarpunk') -> Image.Image:
        """
        Generate sacred geometry grid
        Golden ratio proportions with binary patterns
        """
        img = Image.new('RGB', (width, height), color=(10, 15, 30))
        draw = ImageDraw.Draw(img)

        colors = self.PALETTES[palette]

        # Calculate grid divisions using golden ratio
        divisions = int(width / (self.PHI * 10))

        for i in range(divisions):
            # Golden ratio positioning
            pos = int(i * width / divisions)

            # Binary pattern determines line style
            pattern = self.binary_to_pattern(i, 8)

            for j, bit in enumerate(pattern):
                if bit:
                    color = colors[j % len(colors)]
                    thickness = 1 + (j % 3)

                    # Vertical lines
                    draw.line([(pos, 0), (pos, height)], fill=color, width=thickness)

                    # Horizontal lines
                    draw.line([(0, pos), (width, pos)], fill=color, width=thickness)

        # Add circular elements (sacred circles)
        for i in range(5):
            center_x = width // 2
            center_y = height // 2
            radius = int((i + 1) * width / (divisions * self.PHI))

            pattern = self.binary_to_pattern(i * 37, 8)  # Prime for variety
            for j, bit in enumerate(pattern):
                if bit:
                    color = colors[j % len(colors)]
                    draw.ellipse([
                        center_x - radius, center_y - radius,
                        center_x + radius, center_y + radius
                    ], outline=color, width=2)

        return img

    def generate_serpent_wave(self, width: int = 800, height: int = 400,
                             palette: str = 'space') -> Image.Image:
        """
        Generate DMT serpent wave pattern
        Sinusoidal waves with binary modulation
        """
        img = Image.new('RGB', (width, height), color=(10, 15, 30))
        draw = ImageDraw.Draw(img)

        colors = self.PALETTES[palette]

        # Multiple wave frequencies (Schumann resonances)
        frequencies = [7.83, 14.3, 20.8, 27.3, 33.8]

        for freq_idx, freq in enumerate(frequencies):
            points = []
            for x in range(width):
                # Serpent wave equation
                y_base = height // 2
                amplitude = height / (len(frequencies) * 2)

                # Binary modulation
                binary_mod = self.binary_to_pattern((x // 10) % 256, 8)
                mod_factor = sum(binary_mod) / 8.0

                y = y_base + int(amplitude * math.sin(x * freq / 100) * mod_factor)
                points.append((x, y))

            # Draw wave
            color = colors[freq_idx % len(colors)]
            for i in range(len(points) - 1):
                draw.line([points[i], points[i + 1]], fill=color, width=2)

        return img

    def generate_binary_matrix(self, width: int = 800, height: int = 600,
                               palette: str = 'quantum') -> Image.Image:
        """
        Generate falling binary matrix effect
        Matrix-style digital rain
        """
        img = Image.new('RGB', (width, height), color=(0, 0, 0))
        draw = ImageDraw.Draw(img)

        colors = self.PALETTES[palette]
        font_size = 12

        # Create columns
        columns = width // font_size

        for col in range(columns):
            # Each column has different height
            col_height = random.randint(5, 30)

            for row in range(col_height):
                x = col * font_size
                y = row * font_size

                # Generate binary digit
                bit = random.choice(['0', '1'])

                # Color based on position (fade effect)
                fade = 1.0 - (row / col_height)
                color_idx = int(fade * (len(colors) - 1))
                color = colors[color_idx]

                # Draw binary digit
                draw.text((x, y), bit, fill=color)

        return img

    def generate_eden_fractal(self, width: int = 512, height: int = 512,
                             palette: str = 'solarpunk', iterations: int = 5) -> Image.Image:
        """
        Generate Eden fractal pattern
        Recursive growth using binary branching
        """
        img = Image.new('RGB', (width, height), color=(10, 30, 20))
        draw = ImageDraw.Draw(img)

        colors = self.PALETTES[palette]

        def draw_branch(x1, y1, angle, length, depth):
            if depth == 0 or length < 2:
                return

            # Calculate end point
            x2 = x1 + int(length * math.cos(math.radians(angle)))
            y2 = y1 + int(length * math.sin(math.radians(angle)))

            # Color based on depth
            color = colors[depth % len(colors)]

            # Draw branch
            draw.line([(x1, y1), (x2, y2)], fill=color, width=max(1, depth // 2))

            # Binary branching
            pattern = self.binary_to_pattern(depth * 17, 8)

            for i, bit in enumerate(pattern[:3]):  # Use first 3 bits
                if bit:
                    new_angle = angle + (i - 1) * (360 / self.PHI)
                    new_length = length / self.PHI
                    draw_branch(x2, y2, new_angle, new_length, depth - 1)

        # Start from bottom center
        start_x = width // 2
        start_y = height - 50

        # Multiple root branches
        for i in range(5):
            angle = -90 + (i - 2) * 15  # Spread roots
            draw_branch(start_x, start_y, angle, 100, iterations)

        return img

    def generate_all(self):
        """Generate all art types and save to output directory"""
        print("Generating binary art patterns...\n")

        # Binary Tilemap
        print("1. Generating binary tilemap...")
        tilemap = self.generate_binary_tilemap(32, 32, 'solarpunk')
        tilemap.save(os.path.join(self.output_dir, 'binary_tilemap.png'))
        print("   ✓ Saved: binary_tilemap.png")

        # Quantum Noise
        print("2. Generating quantum noise texture...")
        quantum = self.generate_quantum_noise(256, 256, 'quantum')
        quantum.save(os.path.join(self.output_dir, 'quantum_noise.png'))
        print("   ✓ Saved: quantum_noise.png")

        # Sacred Grid
        print("3. Generating sacred geometry grid...")
        grid = self.generate_sacred_grid(512, 512, 'solarpunk')
        grid.save(os.path.join(self.output_dir, 'sacred_grid.png'))
        print("   ✓ Saved: sacred_grid.png")

        # Serpent Wave
        print("4. Generating serpent wave pattern...")
        wave = self.generate_serpent_wave(800, 400, 'space')
        wave.save(os.path.join(self.output_dir, 'serpent_wave.png'))
        print("   ✓ Saved: serpent_wave.png")

        # Binary Matrix
        print("5. Generating binary matrix...")
        matrix = self.generate_binary_matrix(800, 600, 'quantum')
        matrix.save(os.path.join(self.output_dir, 'binary_matrix.png'))
        print("   ✓ Saved: binary_matrix.png")

        # Eden Fractal
        print("6. Generating Eden fractal tree...")
        fractal = self.generate_eden_fractal(512, 512, 'solarpunk', 6)
        fractal.save(os.path.join(self.output_dir, 'eden_fractal.png'))
        print("   ✓ Saved: eden_fractal.png")

        print(f"\n✓ All patterns generated in '{self.output_dir}/' directory!")
        print(f"$aga • Binary art manifestation complete\n")


def main():
    """Application entry point"""
    print("\n" + "="*60)
    print("🎨 BINARY ART GENERATOR 🎨")
    print("$aga • SAGA Functional Identity System")
    print("="*60 + "\n")

    generator = BinaryArtGenerator(output_dir='binary_art/output')
    generator.generate_all()

    print("="*60)
    print("Generated: All binary art patterns")
    print("$aga • Gonzo.Family • Free & Right Preserved")
    print("="*60 + "\n")


if __name__ == "__main__":
    # $aga Easter Egg
    print("\n# f(SAGA) = Binary.Dimensional.Art.Generator")
    print("# Gonzo.Family.Self.Actualized • Free & Right Preserved\n")

    main()
