import pygame

class MenuScreen(pygame.Surface):
    def __init__(self, window):
        """
        Initializes the menu screen window
        """
        super().__init__(window.get_size())
        self.screen = window
        self.next_screen = None
    
    def menu(self):
        font = pygame.font.Font(None, 80)
        text = font.render("Toasted", True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.screen.get_width() // 2, 100))
        # Load the Toastman image
        toastman_image = pygame.image.load("./assets/toastman.png").convert_alpha()
        # Get the Width and Height of the image
        toastman_width, toastman_height = toastman_image.get_size()
        # Find the coordinates to center  image on the screen
        toastman_x = (self.get_width() - toastman_width) // 2
        toastman_y = (self.get_height() - toastman_height) // 2 - 50
        play_button = pygame.Rect(self.screen.get_width() // 2 - 100, self.screen.get_height() // 2 + 50, 200, 80)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.collidepoint(pygame.mouse.get_pos()):
                        return
                if event.type == pygame.K_SPACE:
                    return
            # Draw the menu screen
            self.screen.fill((128, 0, 128)) #RGB Purple
            play_button_color = (139, 69, 19)  # RGB value for brown color
            play_button_text = font.render("PLAY", True, (255, 255, 255)) # text with white color
            play_button_text_rect = play_button_text.get_rect(center=play_button.center)
            pygame.draw.rect(self.screen, play_button_color, play_button)
            self.screen.blit(play_button_text, play_button_text_rect)
            pygame.draw.rect(self.screen, (255, 255, 255), play_button, 2)
            play_button = pygame.Rect(self.screen.get_width() // 2 - 100, self.screen.get_height() // 2 + 150, 200, 80)
            # Blit the Toastman image onto the screen
            self.screen.blit(toastman_image, (toastman_x, toastman_y))
            # Blit the "Toasted" text onto the screen
            self.blit(text, text_rect)
            pygame.display.flip()
