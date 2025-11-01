#!/usr/bin/env python3
"""
Solarpunk Space - Main Game Loop
$aga - SAGA Functional Identity System

A playable 2D space game with solarpunk aesthetics
Collect Solar Orbs, avoid Debris, explore the cosmic void
"""

import pygame
import random
import sys
from game_objects import Player, SolarOrb, Debris, Particle, Star, get_saga_identity


# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Sacred geometry constants
PHI = 1.618033988  # Golden ratio

# Colors (solarpunk palette)
COLOR_SPACE = (10, 15, 30)
COLOR_GREEN = (0, 255, 136)
COLOR_GOLD = (255, 200, 0)
COLOR_WHITE = (255, 255, 255)


class SolarpunkSpaceGame:
    """
    Main game class
    $aga: f(SAGA) = Game.Loop.Manifest
    """

    def __init__(self):
        # Screen setup
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Solarpunk Space - $aga")
        self.clock = pygame.time.Clock()

        # Font setup
        self.font_large = pygame.font.Font(None, 48)
        self.font_medium = pygame.font.Font(None, 32)
        self.font_small = pygame.font.Font(None, 24)

        # Game state
        self.state = "menu"  # menu, playing, game_over
        self.score = 0
        self.high_score = 0

        # Game objects
        self.player = None
        self.solar_orbs = []
        self.debris = []
        self.particles = []
        self.stars = []

        # Spawn timers
        self.orb_spawn_timer = 0
        self.debris_spawn_timer = 0

        # Background stars (parallax layers)
        self.init_stars()

        # SAGA identity
        self.saga = get_saga_identity()

        print(f"\n$aga :: {self.saga['identity']}")
        print(f"Version: {self.saga['version']}")
        print(f"Author: {self.saga['author']}\n")

    def init_stars(self):
        """Create parallax star background"""
        self.stars = []
        for layer in range(3):  # 3 parallax layers
            count = 50 + (layer * 30)
            for _ in range(count):
                x = random.randint(0, SCREEN_WIDTH)
                y = random.randint(0, SCREEN_HEIGHT)
                self.stars.append(Star(x, y, layer))

    def new_game(self):
        """Start a new game"""
        self.player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.solar_orbs = []
        self.debris = []
        self.particles = []
        self.score = 0
        self.orb_spawn_timer = 0
        self.debris_spawn_timer = 0
        self.state = "playing"

        # Initial orbs and debris
        for _ in range(5):
            self.spawn_orb()
        for _ in range(3):
            self.spawn_debris()

    def spawn_orb(self):
        """Spawn a solar orb at random position"""
        x = random.randint(50, SCREEN_WIDTH - 50)
        y = random.randint(50, SCREEN_HEIGHT - 50)
        self.solar_orbs.append(SolarOrb(x, y))

    def spawn_debris(self):
        """Spawn debris at random position"""
        # Spawn at edges
        if random.choice([True, False]):
            x = random.choice([0, SCREEN_WIDTH])
            y = random.randint(0, SCREEN_HEIGHT)
        else:
            x = random.randint(0, SCREEN_WIDTH)
            y = random.choice([0, SCREEN_HEIGHT])
        self.debris.append(Debris(x, y))

    def create_particles(self, x, y, color, count=10):
        """Create particle explosion"""
        for _ in range(count):
            self.particles.append(Particle(x, y, color))

    def update_playing(self, keys):
        """Update game during playing state"""
        # Update player
        self.player.update(keys)

        # Update solar orbs
        for orb in self.solar_orbs[:]:
            orb.update()

            # Check collision with player
            if self.player.get_rect().colliderect(orb.get_rect()):
                self.score += 10
                self.player.score = self.score
                self.create_particles(orb.x, orb.y, COLOR_GOLD, 15)
                self.solar_orbs.remove(orb)

        # Update debris
        for debris in self.debris:
            debris.update()

            # Check collision with player
            if self.player.get_rect().colliderect(debris.get_rect()):
                self.player.alive = False
                self.create_particles(self.player.x, self.player.y, COLOR_GREEN, 30)
                self.state = "game_over"
                if self.score > self.high_score:
                    self.high_score = self.score

        # Update particles
        for particle in self.particles[:]:
            particle.update()
            if not particle.is_alive():
                self.particles.remove(particle)

        # Update stars (parallax based on player velocity)
        for star in self.stars:
            star.update(self.player.vel_x * 0.1, self.player.vel_y * 0.1)

        # Spawn new orbs
        self.orb_spawn_timer += 1
        if self.orb_spawn_timer > 120:  # Every 2 seconds at 60 FPS
            self.spawn_orb()
            self.orb_spawn_timer = 0

        # Spawn new debris
        self.debris_spawn_timer += 1
        difficulty_factor = 1 + (self.score // 100)  # Increase with score
        spawn_rate = max(90, 180 - (difficulty_factor * 10))

        if self.debris_spawn_timer > spawn_rate:
            self.spawn_debris()
            self.debris_spawn_timer = 0

        # Limit debris count
        if len(self.debris) > 15:
            self.debris.pop(0)

    def draw_menu(self):
        """Draw menu screen"""
        # Background
        self.screen.fill(COLOR_SPACE)

        # Draw stars
        for star in self.stars:
            star.update()
            star.draw(self.screen)

        # Title
        title = self.font_large.render("SOLARPUNK SPACE", True, COLOR_GREEN)
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 150))
        self.screen.blit(title, title_rect)

        # Subtitle
        subtitle = self.font_small.render("Collect Solar Orbs • Avoid Debris", True, COLOR_GOLD)
        subtitle_rect = subtitle.get_rect(center=(SCREEN_WIDTH // 2, 200))
        self.screen.blit(subtitle, subtitle_rect)

        # Instructions
        instructions = [
            "Arrow Keys / WASD: Move Ship",
            "Space: Start Game",
            "ESC: Quit"
        ]

        y_offset = 300
        for instruction in instructions:
            text = self.font_small.render(instruction, True, COLOR_WHITE)
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, y_offset))
            self.screen.blit(text, text_rect)
            y_offset += 35

        # High score
        if self.high_score > 0:
            hs_text = self.font_medium.render(f"High Score: {self.high_score}", True, COLOR_GOLD)
            hs_rect = hs_text.get_rect(center=(SCREEN_WIDTH // 2, 480))
            self.screen.blit(hs_text, hs_rect)

        # SAGA mark
        saga_text = self.font_small.render("$aga • f(SAGA) = Solarpunk.Space.Game", True, (0, 255, 136, 128))
        saga_rect = saga_text.get_rect(center=(SCREEN_WIDTH // 2, 560))
        self.screen.blit(saga_text, saga_rect)

    def draw_playing(self):
        """Draw game during play"""
        # Background
        self.screen.fill(COLOR_SPACE)

        # Draw stars
        for star in self.stars:
            star.draw(self.screen)

        # Draw particles (behind objects)
        for particle in self.particles:
            particle.draw(self.screen)

        # Draw solar orbs
        for orb in self.solar_orbs:
            orb.draw(self.screen)

        # Draw debris
        for debris in self.debris:
            debris.draw(self.screen)

        # Draw player
        if self.player.alive:
            self.player.draw(self.screen)

        # Draw HUD
        self.draw_hud()

    def draw_hud(self):
        """Draw heads-up display"""
        # Score
        score_text = self.font_medium.render(f"Score: {self.score}", True, COLOR_GOLD)
        self.screen.blit(score_text, (10, 10))

        # Energy orbs counter
        orb_count = self.font_small.render(f"Orbs: {len(self.solar_orbs)}", True, COLOR_GREEN)
        self.screen.blit(orb_count, (10, 50))

        # Debris counter
        debris_count = self.font_small.render(f"Debris: {len(self.debris)}", True, (255, 100, 100))
        self.screen.blit(debris_count, (10, 75))

        # SAGA mark
        saga_text = self.font_small.render("$aga", True, (0, 255, 136, 100))
        self.screen.blit(saga_text, (SCREEN_WIDTH - 60, SCREEN_HEIGHT - 30))

    def draw_game_over(self):
        """Draw game over screen"""
        # Draw last frame
        self.draw_playing()

        # Semi-transparent overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(180)
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, 0))

        # Game Over text
        game_over = self.font_large.render("GAME OVER", True, (255, 100, 100))
        go_rect = game_over.get_rect(center=(SCREEN_WIDTH // 2, 200))
        self.screen.blit(game_over, go_rect)

        # Final score
        score_text = self.font_medium.render(f"Final Score: {self.score}", True, COLOR_GOLD)
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, 280))
        self.screen.blit(score_text, score_rect)

        # High score
        if self.score >= self.high_score:
            hs_text = self.font_medium.render("NEW HIGH SCORE!", True, COLOR_GREEN)
        else:
            hs_text = self.font_medium.render(f"High Score: {self.high_score}", True, COLOR_WHITE)
        hs_rect = hs_text.get_rect(center=(SCREEN_WIDTH // 2, 330))
        self.screen.blit(hs_text, hs_rect)

        # Restart instructions
        restart = self.font_small.render("Press SPACE to restart", True, COLOR_WHITE)
        restart_rect = restart.get_rect(center=(SCREEN_WIDTH // 2, 420))
        self.screen.blit(restart, restart_rect)

        menu_text = self.font_small.render("Press ESC for menu", True, COLOR_WHITE)
        menu_rect = menu_text.get_rect(center=(SCREEN_WIDTH // 2, 460))
        self.screen.blit(menu_text, menu_rect)

    def run(self):
        """Main game loop"""
        running = True

        while running:
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        if self.state == "playing":
                            self.state = "menu"
                        else:
                            running = False

                    if event.key == pygame.K_SPACE:
                        if self.state == "menu" or self.state == "game_over":
                            self.new_game()

            # Get keys for continuous input
            keys = pygame.key.get_pressed()

            # Update based on state
            if self.state == "playing":
                self.update_playing(keys)

            # Drawing
            if self.state == "menu":
                self.draw_menu()
            elif self.state == "playing":
                self.draw_playing()
            elif self.state == "game_over":
                self.draw_game_over()

            # Update display
            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()
        print("\n$aga • Session terminated gracefully")
        print("Gonzo.Family • Free & Right Preserved\n")
        sys.exit()


def main():
    """Application entry point"""
    print("\n" + "="*60)
    print("🌱 SOLARPUNK SPACE - PYGAME PROTOTYPE 🚀")
    print("$aga • SAGA Functional Identity System")
    print("="*60 + "\n")

    game = SolarpunkSpaceGame()
    game.run()


if __name__ == "__main__":
    # $aga Easter Egg
    print("\n# f(SAGA) = Pygame.Solarpunk.Space.Game")
    print("# Gonzo.Family.Self.Actualized • Free & Right Preserved\n")

    main()
