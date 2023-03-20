import pygame
import os


#Defining some colors to use and refer to at a later time
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ANTIFLASHWHITE = (235, 235, 235)
PUMPKIN = (255, 103, 0)
SILVER = (192, 192, 192)
BICEBLUE = (58, 110, 165)
POLYNESIANBLUE = (0, 78, 152)
main = True
velocity = 10

#Player Class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('images',img)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Player(Sprite):
    pass

class Jarheads(Sprite):
    pass

#pygame setup
pygame.init()
screen = pygame.display.set_mode((900, 700))
#sprite stuff
toastysource = pygame.image.load("./assets/toastman.png").convert_alpha()
jellysource = pygame.image.load("./assets/jellyjar.png").convert_alpha()
peanutjarsource = pygame.image.load("./assets/pjar.png").convert_alpha()
#resize source sprites
toasty = pygame.transform.scale(toastysource, (100, 100))
jelly = pygame.transform.scale(jellysource, (30,50))
peanutjar = pygame.transform.scale(peanutjarsource, (30, 50))

pygame.display.set_caption("Bullet Hell")
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
pjarpos = pygame.Vector2(100, 100)
jjarpos = pygame.Vector2(200, 200)
pygame.display.flip()
clock = pygame.time.Clock()

#Main game loop
while main:
    enemy_vel = 10
    enemy_vel += 1
    #If game is exited
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main = False
    screen.fill(BICEBLUE)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_pos.x -= velocity#Moves left
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_pos.x += velocity#Moves right
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player_pos.y -= velocity  #Moves up
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player_pos.y += velocity  #Moves down
    screen.blit(toasty, (player_pos.x, player_pos.y))
    screen.blit(peanutjar, (enemy_vel, player_pos.y)), 60
    screen.blit(jelly, (enemy_vel, player_pos.y+20)), 60
    pygame.display.flip()
    clock.tick(60)

