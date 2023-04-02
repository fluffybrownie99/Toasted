import pygame, random
from enemy import Enemy
from player import Player
from screens.menu import MenuScreen
from screens.game_over import GameOverScreen

class Game:
    def __init__(self):
        # Initialize pygame and create the window
        pygame.init()
        self.screen = pygame.display.set_mode((500, 700))
        pygame.display.set_caption("Bullet Hell")

        # Set up the player object
        self.player = Player(self.screen)
        # Set up the enemies object with more logic
        self.enemies = []
        # Set up the clock and score
        self.clock = pygame.time.Clock()
        self.score = 0
        self.score_font = pygame.font.Font(None, 36)
        self.menu_screen = MenuScreen(self.screen)
        self.state = "menu"
    
    def get_enemies(self):
        self.enemies = []
        margin = 40
        min_distance = 80
        # While loop for declaring number of enemy spawns with random coordinates for each spawn
        while len(self.enemies) < 9:
            x = random.randint(0, (self.screen.get_width() - margin))
            y = random.randint(0, (self.screen.get_height() // 4) - margin)
            # Spawn collision detection to make sure enemies do not spawn on top of each other
            spawn_collision = False
            for enemy in self.enemies:
                # Distance formula
                distance = ((x - enemy.rect.centerx)**2 + (y - enemy.rect.centery)**2)**0.5
                if distance < min_distance:
                    spawn_collision = True
            random_enemy_png_path = ["./assets/pjar.png", "./assets/jellyjar.png", "./assets/shema.png"]
            random_enemy_type = random.choice(random_enemy_png_path)
            if not spawn_collision:
                self.enemies.append(Enemy(self.screen, random_enemy_type, (x, y)))
    
    def run(self):
        # Main game loop
        while True:
            # Handle exit events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            if self.state =="menu":
                self.menu_screen.menu()
                self.state = "play"
                self.player.health = 3
                self.get_enemies()
                start_time = pygame.time.get_ticks()
            if self.state == "game_over":
                game_over_screen = GameOverScreen(self.screen, final_score)
                game_over_screen.game_over()
                self.state = "menu"
            # update the game objects
            self.player.update()
            for enemy in self.enemies:
                enemy.update(self.enemies)
            # update score based on elapsded time
            elapsed_time = pygame.time.get_ticks() - start_time
            self.score = elapsed_time // 10
            
            collided_enemies = []
            for enemy in self.enemies:
                if self.player.collides_with(enemy):
                    collided_enemies.append(enemy)
            for enemy in collided_enemies:
                self.enemies.remove(enemy)
                if self.player.health == 1:
                    final_score = self.score
                    self.state = "game_over"
                else:
                    self.player.health -= 1
                    self.player.update()
            # draw the game objects
            self.screen.fill((58, 110, 165)) #RGB value that fills the background
            self.player.draw()
            for enemy in self.enemies:
                enemy.draw()
            #draw the score
            score_text = self.score_font.render(f"Score: {self.score}", True, (255,255,255))
            self.screen.blit(score_text, (10, 10))
            # update the screen
            pygame.display.flip()

            # limit the frame rate
            self.clock.tick(60)




if __name__ == "__main__":
    game = Game()
    game.run()
