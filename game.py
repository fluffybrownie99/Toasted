import pygame
import random

class Game:
    def __init__(self):
        # initialize pygame and create the window
        pygame.init()
        self.screen = pygame.display.set_mode((500, 700))
        pygame.display.set_caption("Bullet Hell")

        # set up the game objects
        self.player = Player(self.screen)
        self.enemies = []
        min_distance = 80
        #for loop for declaring random x y coordinates for enemy spawns
        while len(self.enemies) < 9:
            x = random.randint(0, self.screen.get_width() - 30)
            y = random.randint(0, (self.screen.get_height() // 3)+ 10)

            #spawn collision detection to make sure enemies do not spawn on top of each other
            spawn_collision = False
            for enemy in self.enemies:
                distance = ((x - enemy.rect.centerx)**2 + (y - enemy.rect.centery)**2)**0.5
                if distance < min_distance:
                    spawn_collision = True
            random_enemy_png_path = ["./assets/pjar.png", "./assets/jellyjar.png", "./assets/brian.png", "./assets/shema.png"]
            random_enemy_type = random.choice(random_enemy_png_path)
            if not spawn_collision:
                self.enemies.append(Enemy(self.screen, random_enemy_type, (x, y)))
        # set up the clock and velocity
        self.clock = pygame.time.Clock()


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
                enemy.update(self.enemies)
                
            collided_enemies = []
            for enemy in self.enemies:
                if self.player.collides_with(enemy):
                    collided_enemies.append(enemy)
            for enemy in collided_enemies:
                self.enemies.remove(enemy)

                if self.player.health == 1:
                    print(self.player.health)
                    pygame.quit()
                    return
                else:
                    self.player.health -= 1
                    self.player.update()
            # draw the game objects
            self.screen.fill((58, 110, 165)) #RGB value that fills the background
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


if __name__ == "__main__":
    game = Game()
    game.run()
