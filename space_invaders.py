import pygame

#initilize the pygame
pygame.init()

#create screen
#screen = pygame.display.set_mode((800,600))

# make a screen:
screen = pygame.display.set_mode((0,0))
print('height: %s' % screen.get_height())
print('width: %s' % screen.get_width())


#Title & Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# the game loop (keeps window open until we quit) 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0,0,0)) #((R,G,B))
    pygame.display.update()
