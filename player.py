import pygame
class Player:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("./assets/toastman.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect(center=(screen.get_width() / 2, screen.get_height() - 50))
        self.health = 3
        self.velocity = 10
        self.jump_height = 20
        self.jump_count = 0
        self.is_jumping = False


    def update(self):
        # handle player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if self.rect.left > 0:
                self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if self.rect.right < self.screen.get_width():
                self.rect.x += self.velocity


    def draw(self):
        self.screen.blit(self.image, self.rect)

    def collides_with(self, other):
        return self.rect.colliderect(other.rect)
