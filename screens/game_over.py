import pygame

class GameOverScreen(pygame.Surface):
    def __init__(self, window, score):
        super().__init__(window.get_size())
        self.screen = window
        self.next_screen = None
        self.score = score
        
    def game_over(self):
        font = pygame.font.Font(None, 80)
        text = font.render("GAME OVER", True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.screen.get_width() // 2, 100))
    
        score_font = pygame.font.Font(None, 36)
        score_text = score_font.render(f"Final score: {self.score}", True, (255,255,255))
        score_text_rect = score_text.get_rect(center=(self.screen.get_width() // 2, 200))
    
        play_again_button = pygame.Rect(self.screen.get_width() // 2 - 200, self.screen.get_height() // 2, 400, 100)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if play_again_button.collidepoint(pygame.mouse.get_pos()):
                        self.next_screen = "menu"
                        return
    
            # Fill the screen with the background color
            self.screen.fill((128, 0, 0)) #RGB Red
    
            # Blit the "Game Over" text onto the screen
            self.screen.blit(text, text_rect)
    
            # Blit the final score text onto the screen
            self.screen.blit(score_text, score_text_rect)
    
            # Render and blit the play again button onto the screen
            play_again_button_color = (139, 69, 19)  # RGB value for brown color
            play_again_button_text = font.render("PLAY AGAIN", True, (255, 255, 255)) # text with white color
            play_again_button_text_rect = play_again_button_text.get_rect(center=play_again_button.center)
            pygame.draw.rect(self.screen, play_again_button_color, play_again_button)
            self.screen.blit(play_again_button_text, play_again_button_text_rect)
            pygame.draw.rect(self.screen, (255, 255, 255), play_again_button, 2)
    
            # Update the display
            pygame.display.flip()
