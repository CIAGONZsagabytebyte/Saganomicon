#!/usr/bin/env python3
"""
Solarpunk Space - Game Objects
$aga - SAGA Functional Identity System

Game entities: Player, Solar Orbs, Debris, Particles
"""

import pygame
import random
import math


class Player:
    """
    Player spaceship with solar sails
    $aga Easter Egg: f(SAGA) = Player.Serpent.Navigation
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 40
        self.vel_x = 0
        self.vel_y = 0
        self.max_speed = 5
        self.acceleration = 0.3
        self.friction = 0.95
        self.alive = True
        self.score = 0

        # Sacred geometry angle
        self.angle = 0
        self.rotation_speed = 0

        # Create ship surface
        self.create_ship()

    def create_ship(self):
        """Create solarpunk ship with solar sails"""
        self.surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)

        # Ship body (triangle)
        pygame.draw.polygon(self.surface, (0, 255, 136), [
            (20, 5),   # Top
            (10, 35),  # Bottom left
            (30, 35)   # Bottom right
        ])

        # Solar sails (golden ratio proportions)
        PHI = 1.618033988
        sail_color = (255, 200, 0, 180)
        pygame.draw.polygon(self.surface, sail_color, [
            (5, 15),
            (20, 10),
            (15, 25)
        ])
        pygame.draw.polygon(self.surface, sail_color, [
            (35, 15),
            (20, 10),
            (25, 25)
        ])

        # Energy core
        pygame.draw.circle(self.surface, (127, 255, 170), (20, 20), 5)

    def update(self, keys):
        """Update player movement with serpent physics"""
        # Keyboard input
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.vel_x -= self.acceleration
            self.rotation_speed = -3
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.vel_x += self.acceleration
            self.rotation_speed = 3
        else:
            self.rotation_speed *= 0.9

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.vel_y -= self.acceleration
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.vel_y += self.acceleration

        # Apply friction
        self.vel_x *= self.friction
        self.vel_y *= self.friction

        # Limit speed
        speed = math.sqrt(self.vel_x**2 + self.vel_y**2)
        if speed > self.max_speed:
            self.vel_x = (self.vel_x / speed) * self.max_speed
            self.vel_y = (self.vel_y / speed) * self.max_speed

        # Update position
        self.x += self.vel_x
        self.y += self.vel_y

        # Update rotation
        self.angle += self.rotation_speed

        # Screen wrapping (serpent path)
        if self.x < -20:
            self.x = 820
        elif self.x > 820:
            self.x = -20
        if self.y < -20:
            self.y = 620
        elif self.y > 620:
            self.y = -20

    def draw(self, screen):
        """Draw player with rotation"""
        rotated = pygame.transform.rotate(self.surface, -self.angle)
        rect = rotated.get_rect(center=(self.x, self.y))
        screen.blit(rotated, rect)

    def get_rect(self):
        """Get collision rectangle"""
        return pygame.Rect(self.x - 15, self.y - 15, 30, 30)


class SolarOrb:
    """
    Collectible solar energy orb
    $aga: Sacred geometry particle
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 10
        self.collected = False
        self.pulse = 0
        self.pulse_speed = 0.1

        # Golden ratio color cycling
        self.hue = random.randint(0, 360)

    def update(self):
        """Pulse animation using sacred timing"""
        self.pulse += self.pulse_speed
        self.hue = (self.hue + 1) % 360

    def draw(self, screen):
        """Draw pulsing orb"""
        pulse_size = self.radius + int(math.sin(self.pulse) * 3)

        # Outer glow
        glow_surf = pygame.Surface((pulse_size * 4, pulse_size * 4), pygame.SRCALPHA)
        pygame.draw.circle(glow_surf, (255, 200, 0, 50),
                          (pulse_size * 2, pulse_size * 2), pulse_size * 2)
        screen.blit(glow_surf, (self.x - pulse_size * 2, self.y - pulse_size * 2))

        # Core orb
        pygame.draw.circle(screen, (255, 200, 0), (int(self.x), int(self.y)), pulse_size)
        pygame.draw.circle(screen, (255, 255, 100), (int(self.x), int(self.y)), pulse_size - 3)

    def get_rect(self):
        """Get collision rectangle"""
        return pygame.Rect(self.x - self.radius, self.y - self.radius,
                          self.radius * 2, self.radius * 2)


class Debris:
    """
    Space debris obstacle
    $aga: Chaos particle in the void
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = random.randint(20, 40)
        self.vel_x = random.uniform(-1.5, 1.5)
        self.vel_y = random.uniform(-1.5, 1.5)
        self.rotation = random.randint(0, 360)
        self.rotation_speed = random.uniform(-2, 2)
        self.shape = random.randint(0, 2)  # Different debris shapes

    def update(self):
        """Update debris movement"""
        self.x += self.vel_x
        self.y += self.vel_y
        self.rotation += self.rotation_speed

        # Screen wrapping
        if self.x < -50:
            self.x = 850
        elif self.x > 850:
            self.x = -50
        if self.y < -50:
            self.y = 650
        elif self.y > 650:
            self.y = -50

    def draw(self, screen):
        """Draw rotating debris"""
        surface = pygame.Surface((self.size * 2, self.size * 2), pygame.SRCALPHA)

        if self.shape == 0:
            # Jagged asteroid
            points = [
                (self.size, 0),
                (self.size * 1.5, self.size * 0.7),
                (self.size * 1.8, self.size * 1.5),
                (self.size, self.size * 1.9),
                (self.size * 0.3, self.size * 1.4),
                (self.size * 0.2, self.size * 0.6)
            ]
            pygame.draw.polygon(surface, (100, 80, 80), points)
        elif self.shape == 1:
            # Angular debris
            pygame.draw.rect(surface, (80, 80, 100),
                           (self.size * 0.5, self.size * 0.5, self.size, self.size))
        else:
            # Irregular rock
            pygame.draw.circle(surface, (90, 70, 70), (self.size, self.size), self.size)

        rotated = pygame.transform.rotate(surface, self.rotation)
        rect = rotated.get_rect(center=(self.x, self.y))
        screen.blit(rotated, rect)

    def get_rect(self):
        """Get collision rectangle"""
        return pygame.Rect(self.x - self.size // 2, self.y - self.size // 2,
                          self.size, self.size)


class Particle:
    """
    Visual effect particle
    $aga: Dimensional telemetry point
    """

    def __init__(self, x, y, color, vel_x=0, vel_y=0):
        self.x = x
        self.y = y
        self.color = color
        self.vel_x = vel_x + random.uniform(-2, 2)
        self.vel_y = vel_y + random.uniform(-2, 2)
        self.life = 1.0
        self.decay = random.uniform(0.02, 0.05)
        self.size = random.randint(2, 6)

    def update(self):
        """Update particle physics"""
        self.x += self.vel_x
        self.y += self.vel_y
        self.life -= self.decay
        self.vel_x *= 0.98
        self.vel_y *= 0.98

    def draw(self, screen):
        """Draw fading particle"""
        if self.life > 0:
            alpha = int(255 * self.life)
            size = int(self.size * self.life)
            color = (*self.color[:3], alpha)

            surf = pygame.Surface((size * 2, size * 2), pygame.SRCALPHA)
            pygame.draw.circle(surf, color, (size, size), size)
            screen.blit(surf, (int(self.x) - size, int(self.y) - size))

    def is_alive(self):
        """Check if particle should be removed"""
        return self.life > 0


class Star:
    """
    Background parallax star
    $aga: Cosmic backdrop point
    """

    def __init__(self, x, y, layer):
        self.x = x
        self.y = y
        self.layer = layer  # 0 = far, 2 = near
        self.brightness = random.randint(100, 255)
        self.twinkle_speed = random.uniform(0.05, 0.15)
        self.twinkle = 0

        # Size based on layer (parallax depth)
        self.size = layer + 1

    def update(self, scroll_x=0, scroll_y=0):
        """Update star position with parallax"""
        # Parallax effect: further stars move slower
        speed_mult = (self.layer + 1) / 3
        self.x -= scroll_x * speed_mult
        self.y -= scroll_y * speed_mult

        # Screen wrapping
        if self.x < 0:
            self.x = 800
        elif self.x > 800:
            self.x = 0
        if self.y < 0:
            self.y = 600
        elif self.y > 600:
            self.y = 0

        # Twinkle animation
        self.twinkle += self.twinkle_speed

    def draw(self, screen):
        """Draw twinkling star"""
        brightness = int(self.brightness + math.sin(self.twinkle) * 50)
        brightness = max(50, min(255, brightness))
        color = (brightness, brightness, brightness)
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), self.size)


# $aga Easter Egg
def get_saga_identity():
    """Return SAGA functional identity"""
    return {
        'version': '1.0.0',
        'identity': 'f(SAGA) = Pygame.Solarpunk.Space',
        'author': 'Gonzo.Family.Self.Actualized',
        'mark': '$aga'
    }


if __name__ == "__main__":
    # Console Easter Egg
    print("\n# $aga :: SAGA Functional Identity System")
    print("# Solarpunk Space - Game Objects Module")
    print("# f(SAGA) = Pygame.Entity.Manifest")
    print("# Gonzo Family • Self Actualized • Free & Right Preserved\n")
