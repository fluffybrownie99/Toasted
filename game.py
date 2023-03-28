import pygame

class Game:
    def __init__(self):
        # initialize pygame and create the window
        pygame.init()
        self.screen = pygame.display.set_mode((700, 900))
        pygame.display.set_caption("Bullet Hell")

        # set up the game objects
        self.player = Player(self.screen)
        self.enemies = [Enemy(self.screen, "./assets/pjar.png", (100, 100)), 
                        Enemy(self.screen, "./assets/jellyjar.png", (200, 100)),
                        Enemy(self.screen, "./assets/pjar.png", (300, 100)),
                        Enemy(self.screen, "./assets/jellyjar.png", (400, 100))
                        ]

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

    def update(self):
        # handle player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if self.rect.left > 0:
                self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if self.rect.right < self.screen.get_width():
                self.rect.x += self.velocity
        # if keys[pygame.K_UP] or keys[pygame.K_w]:
        #     if self.rect.top > 0:
        #         self.rect.y -= self.velocity
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
