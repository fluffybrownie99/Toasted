import pygame, random
from enemy import Enemy
from player import Player

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
            y = random.randint(0, (self.screen.get_height() // 4)+ 10)

            #spawn collision detection to make sure enemies do not spawn on top of each other
            spawn_collision = False
            for enemy in self.enemies:
                #distance formula
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




if __name__ == "__main__":
    game = Game()
    game.run()
