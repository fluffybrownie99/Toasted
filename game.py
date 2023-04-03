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
        pygame.display.set_caption("Toasted")
        # Set up the player object
        self.player = Player(self.screen)
        # Set up the player's health with a heart image
        self.heart_image = pygame.image.load("./assets/heart.png")
        self.heart = pygame.transform.scale(self.heart_image, (30, 30))
        # Set up the enemy list to load with the get_enemies() function
        self.enemies = []
        # Set up the clock and score
        self.clock = pygame.time.Clock()
        self.score = 0
        self.score_font = pygame.font.Font(None, 36)
        self.menu_screen = MenuScreen(self.screen)
        self.state = "menu"
    
    def get_enemies(self):
    # This function initializes the enemies list with enemies that are placed randomly 
        self.enemies = [] #this is for clearing the list after trying the game again
        margin = 40 #this is for making sure the enemies spawn within the margins of the display
        min_distance = 80 #this is so that the enemies have a minimum distance of 80 between spawning
        random_enemy_png_paths = ["./assets/pjar.png", "./assets/jellyjar.png", "./assets/shema.png", "./assets/tim.png"]
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
            random_enemy_type = random.choice(random_enemy_png_paths)
            if not spawn_collision:
                self.enemies.append(Enemy(self.screen, random_enemy_type, (x, y)))
    
    
    def draw_hearts(self):
    #this function is for drawing the hearts on the screen that represents the player health
        for i in range(self.player.health):
            x_position = 10 + (i * (self.heart.get_width()+ 10))
            self.screen.blit(self.heart, (x_position, 50))
    
    def handle_quit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

    def handle_collisions(self):
        #handles collisions and player health based on collision detection
        collided_enemies = [enemy for enemy in self.enemies if self.player.collides_with(enemy)]
        for enemy in collided_enemies:
            self.enemies.remove(enemy)
            if self.player.health == 1:
                return self.score
            else:
                self.player.health -= 1
                self.player.update()
        return None
    

    def run(self):
        # Main game loop
        while True:
            # Handle exit events
            self.handle_quit()
            # Handles game states
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
                
            # update score based on elapsed time
            elapsed_time = pygame.time.get_ticks() - start_time
            self.score = elapsed_time // 10
            
            #handle collisions and player health with self.handle_collisions
            final_score = self.handle_collisions()
            if final_score is not None:
                self.state = "game_over"
            
            # draw the game background and objects
            self.screen.fill((58, 110, 165)) #RGB value that fills the background
            self.player.draw()
            for enemy in self.enemies:
                enemy.draw()
            # draws hearts on the screen
            self.draw_hearts()
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
