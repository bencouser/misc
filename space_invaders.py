import pygame

#initilize the pygame
pygame.init()

#create screen
screen = pygame.display.set_mode((800,600))

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
