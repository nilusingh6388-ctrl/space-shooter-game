import random
import sys

import pygame


WIDTH = 600
HEIGHT = 600
FPS = 60
MAX_BULLETS = 5
WHITE = (245, 245, 245)
BLACK = (15, 18, 30)
BLUE = (65, 155, 255)
YELLOW = (255, 220, 70)
RED = (235, 75, 75)


class Ship:
    def __init__(self):
        self.width = 50
        self.height = 50
        self.speed = 8
        self.rect = pygame.Rect(275, 520, self.width, self.height)

    def move(self, direction):
        self.rect.x += direction * self.speed
        self.rect.x = max(0, min(self.rect.x, WIDTH - self.width))

    def draw(self, surface):
        points = [
            (self.rect.centerx, self.rect.top),
            (self.rect.left, self.rect.bottom),
            (self.rect.centerx, self.rect.bottom - 12),
            (self.rect.right, self.rect.bottom),
        ]
        pygame.draw.polygon(surface, BLUE, points)


class Bullet:
    def __init__(self, x, y):
        self.width = 5
        self.height = 10
        self.speed = 10
        self.x = x  # Center x, so firing from the default ship is (300, 520).
        self.rect = pygame.Rect(x - self.width // 2, y, self.width, self.height)

    def update(self):
        self.rect.y -= self.speed

    def draw(self, surface):
        pygame.draw.rect(surface, YELLOW, self.rect)


class Enemy:
    def __init__(self, x=None, y=0, speed=None):
        self.width = 40
        self.height = 40
        self.speed = speed if speed is not None else random.randint(2, 4)
        if x is None:
            x = random.randint(0, WIDTH - self.width)
        self.rect = pygame.Rect(x, y, self.width, self.height)

    def update(self):
        self.rect.y += self.speed

    def draw(self, surface):
        pygame.draw.rect(surface, RED, self.rect, border_radius=8)
        pygame.draw.circle(surface, WHITE, (self.rect.centerx - 8, self.rect.centery), 3)
        pygame.draw.circle(surface, WHITE, (self.rect.centerx + 8, self.rect.centery), 3)


class SpaceShooter:
    def __init__(self):
        self.font = pygame.font.Font(None, 30)
        self.large_font = pygame.font.Font(None, 64)
        self.reset()

    def reset(self):
        self.ship = Ship()
        self.bullets = []
        self.enemies = []
        self.score = 0
        self.lives = 3
        self.game_over = False
        self.last_enemy_spawn = pygame.time.get_ticks()

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type != pygame.KEYDOWN:
            return

        if self.game_over:
            if event.key == pygame.K_r:
                self.reset()
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            return

        if event.key == pygame.K_LEFT:
            self.ship.move(-1)
        elif event.key == pygame.K_RIGHT:
            self.ship.move(1)
        elif event.key == pygame.K_SPACE and len(self.bullets) < MAX_BULLETS:
            self.bullets.append(Bullet(self.ship.rect.centerx, self.ship.rect.y))

    def update(self):
        if self.game_over:
            return

        now = pygame.time.get_ticks()
        if now - self.last_enemy_spawn >= 900:
            self.enemies.append(Enemy())
            self.last_enemy_spawn = now

        for bullet in self.bullets:
            bullet.update()
        self.bullets = [bullet for bullet in self.bullets if bullet.rect.bottom > 0]

        for enemy in self.enemies:
            enemy.update()

        for bullet in self.bullets[:]:
            for enemy in self.enemies[:]:
                if bullet.rect.colliderect(enemy.rect):
                    self.bullets.remove(bullet)
                    self.enemies.remove(enemy)
                    self.score += 10
                    break

        escaped = [enemy for enemy in self.enemies if enemy.rect.y >= HEIGHT]
        for enemy in escaped:
            self.enemies.remove(enemy)
            self.lives = max(0, self.lives - 1)

        if self.lives == 0:
            self.game_over = True

    def draw(self, surface):
        surface.fill(BLACK)

        self.ship.draw(surface)
        for bullet in self.bullets:
            bullet.draw(surface)
        for enemy in self.enemies:
            enemy.draw(surface)

        status = self.font.render(
            f"Score: {self.score}    Lives: {self.lives}    Bullets: {len(self.bullets)}",
            True,
            WHITE,
        )
        surface.blit(status, (12, 12))

        if self.game_over:
            title = self.large_font.render("Game Over", True, WHITE)
            final_score = self.font.render(f"Final score: {self.score}", True, WHITE)
            restart = self.font.render("Press R to restart or ESC to quit", True, WHITE)
            surface.blit(title, title.get_rect(center=(WIDTH // 2, 250)))
            surface.blit(final_score, final_score.get_rect(center=(WIDTH // 2, 310)))
            surface.blit(restart, restart.get_rect(center=(WIDTH // 2, 355)))


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Space Shooter")
    clock = pygame.time.Clock()
    game = SpaceShooter()

    while True:
        for event in pygame.event.get():
            game.handle_event(event)

        game.update()
        game.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()