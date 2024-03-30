import pygame
from pygame import *
from player import Player
from player1 import Pogonec










window = pygame.display.set_mode((700,500))
fps = pygame.time.Clock()

backround = pygame.transform.scale(
    pygame.image.load("foto/background.png"),(700,500)
)

roma = Player(100,100,50,50, "foto/sprite1.png", 10)

sofia = Pogonec(200,100,50,50, "foto/sprite2.png", 10)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    if roma.hitbox.colliderect(sofia.hitbox):
        print("Програв")

    sofia.move1()
    roma.move()
    window.blit(backround, (0,0) )
    sofia.draw(window)
    roma.draw(window)
    pygame.display.flip()
    fps.tick(60)