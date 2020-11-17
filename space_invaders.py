import pygame

#initilize the pygame
pygame.init()

#create screen
screen = pygame.display.set_mode((800,600)) #((width,height))

# make a fullscreen:
#screen = pygame.display.set_mode((0,0))
#print('height: %s' % screen.get_height())
#print('width: %s' % screen.get_width())


#Title & Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#player
playerImg = pygame.image.load('001-spaceship.png')
playerX = 370
playerY = 480

def player():
    screen.blit(playerImg, (playerX, playerY))


# the game loop (keeps window open until we quit) 
running = True
while running:
     
    screen.fill((0,0,0)) #((R,G,B))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
   
    player() #player called after screen as player must be on top of screen.
    pygame.display.update()
