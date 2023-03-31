import pygame
import random
class Enemy:
    def __init__(self, screen, image_path, position):
        self.screen = screen
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 50))
        self.rect = self.image.get_rect(topleft=position)
        self.speed = [4, 4]
        self.stuck_timer = 0

    def update(self, enemies):
        on_screen_enemies = [enemy for enemy in enemies if enemy.rect.colliderect(self.screen.get_rect()) and enemy != self]
        for enemy in on_screen_enemies:
            if enemy == self:
                continue
            if self.rect.colliderect(enemy.rect):
                self.speed[0] = -self.speed[0]
                self.speed[1] = -self.speed[1]
                self.stuck_timer += 1
                break
            else:
                self.stuck_timer = 0
            
            if self.stuck_timer > 5*60:  # change velocity after 5 seconds of being stuck
                self.speed[0] = random.randint(-5, 5)
                self.speed[1] = random.randint(-5, 5)
                self.stuck_timer = 0
            

        if self.rect.left < 0 or self.rect.right > self.screen.get_width():
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > self.screen.get_height():
            self.speed[1] = -self.speed[1]

        self.rect.move_ip(self.speed)

    def draw(self):
        self.screen.blit(self.image, self.rect)
