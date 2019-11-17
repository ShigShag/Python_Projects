import pygame
import random


class Player_class:

    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0
        self.image = pygame.image.load(image)


def player_move(playerImg, xcordinate, ycordinate):
    screen.blit(playerImg, (xcordinate, ycordinate))


pygame.init()
xborder = 3000
yborder = 2000
screen = pygame.display.set_mode((xborder, yborder))


#Title and Icon
pygame.display.set_caption("Tower Defense")
icon = pygame.image.load(r"Icons\icon.png")
pygame.display.set_icon(icon)


player = Player_class(400, 700, r"Icons\african-mask 64 px.png")
enemy = Player_class(400, 200, r"Icons\soldier.png")

running = True
background = pygame.image.load(r"Icons\2860990.jpg")
while running:
    #above everything
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    player_move(player.image, player.x, player.y)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.x_change = -3
            if event.key == pygame.K_RIGHT:
                player.x_change = 3
            if event.key == pygame.K_UP:
                player.y_change = -3
            if event.key == pygame.K_DOWN:
                player.y_change = 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.x_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player.y_change = 0

    playerXTEMP = player.x
    playerYTEMP = player.y
    player.x += player.x_change
    player.y += player.y_change

    #Rahmenbeschränkung
    if player.x < 0 or player.x > xborder - 64:
        player.x = playerXTEMP
    if player.y < 0 or player.y > yborder - 64:
        player.y = playerYTEMP

    player_move(player.image, player.x, player.y)
    player_move(enemy.image, enemy.x, enemy.y)
    pygame.display.update()



