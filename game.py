import pygame
import random

class Game:
    def __init__(self):
        # initialize pygame and create the window
        pygame.init()
        self.screen = pygame.display.set_mode((700, 900))
        pygame.display.set_caption("Bullet Hell")

        # set up the game objects
        self.player = Player(self.screen)
        self.enemies = []
        for i in range(2):
            x = random.randint(0, self.screen.get_width() - 30)
            y = random.randint(0, self.screen.get_height() // 2)
            self.enemies.append(Enemy(self.screen, "./assets/pjar.png", (x, y)))
            self.enemies.append(Enemy(self.screen, "./assets/jellyjar.png", (y, x)))


        # set up the clock and velocity
        self.clock = pygame.time.Clock()
        self.velocity = 10


    def run(self):
        # main game loop
        while True:
            # handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            # update the game objects
            self.player.update()

            for enemy in self.enemies:
                enemy.update()

                if self.player.collides_with(enemy):
                    pygame.quit()
                    return

            # draw the game objects
            self.screen.fill((58, 110, 165))
            self.player.draw()
            for enemy in self.enemies:
                enemy.draw()
            # update the screen
            pygame.display.flip()

            # limit the frame rate
            self.clock.tick(60)


class Player:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("./assets/toastman.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect(center=(screen.get_width() / 2, screen.get_height() - 50))
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
        #Jumping mechanics
        if keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_SPACE]:
            if not self.is_jumping:
                self.is_jumping = True
        
        if self.is_jumping:
            if self.jump_count >= self.jump_height:
                self.is_jumping = False
                self.jump_count = 0
            else:
                self.rect.y -= 10
                self.jump_count += 1
                
        # handle gravity
        if not self.is_jumping and self.rect.bottom < self.screen.get_height():
            self.rect.y += 10
        # if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        #     if self.rect.bottom < self.screen.get_height():
        #         self.rect.y += self.velocity

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def collides_with(self, other):
        return self.rect.colliderect(other.rect)

class Enemy:
    def __init__(self, screen, image_path, position):
        self.screen = screen
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 50))
        self.rect = self.image.get_rect(topleft=position)
        self.speed = [4,4]

    def update(self):
        if self.rect.left < 0 or self.rect.right > self.screen.get_width():
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > self.screen.get_height():
            self.speed[1] = -self.speed[1]
        
        self.rect.move_ip(self.speed)
        # elif self.rect.right < self.screen.get_width():
        #     self.rect.x += self.velocity
        # elif self.rect.top > 0:
        #     self.rect.y -= self.velocity
        # elif self.rect.bottom < self.screen.get_height():
        #     self.rect.y += self.velocity
    
    def draw(self):
        self.screen.blit(self.image, self.rect)


if __name__ == "__main__":
    game = Game()
    game.run()
