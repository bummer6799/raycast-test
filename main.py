import random

import pygame
import pygame.freetype

import time
import math

pygame.init()

windowX = 600
windowY = windowX
window = pygame.display.set_mode((windowX, windowY))

# timer
clock = pygame.time.Clock()

# player
# playerImg = pygame.image.load('player.png')
playerX = windowX / 2
playerY = windowY / 2
playerX_change = 0
playerY_change = 0
player_angle = math.pi

# icon
pygame.display.set_caption('GunSoundSimulator')
icon = pygame.image.load('GunSoundSimulatorIcon.png')
pygame.display.set_icon(icon)

# walls
# wallImg = pygame.image.load('wall.png')
# wallX = 450
# wallY = 350

# map
map_size = 12

map = (
    '############'
    '#          #'
    '#          #'
    '#          #'
    '#          #'
    '#          #'
    '#          #'
    '#          #'
    '#          #'
    '#          #'
    '#          #'
    '############'
)

# sensors
# off = pygame.image.load('off.png')
# on = pygame.image.load('on.png')


# def wall(x, y):
#     window.blit(wallImg, (x, y))

FOV = 360
half_FOV = FOV / 2
casted_rays = 120
step_angle = FOV / casted_rays
tile_size = int((windowX / 1) / map_size)
max_depth = int(map_size * tile_size)

# draw map
def draw_map():
    for row in range(12):
        for col in range(12):
            # calculate square index
            square = row * map_size + col
            pygame.draw.rect(
                window,
                (255, 255, 255) if map[square] == '#' else (100, 100, 100),
                (col * tile_size, row * tile_size, tile_size - 2, tile_size - 2)
            )
    pygame.draw.circle(window, (255, 255, 255), (int(playerX), int(playerY)), 12)

    pygame.draw.line(window, (0, 255, 0), (playerX, playerY),
                     (playerX - math.sin(player_angle) * 50,
                      playerY + math.cos(player_angle) * 50), 3)

    pygame.draw.line(window, (0, 255, 0), (playerX, playerY),
                     (playerX - math.sin(player_angle - half_FOV) * 50,
                      playerY + math.cos(player_angle - half_FOV) * 50), 3)

    pygame.draw.line(window, (0, 255, 0), (playerX, playerY),
                     (playerX - math.sin(player_angle + half_FOV) * 50,
                      playerY + math.cos(player_angle + half_FOV) * 50), 3)

def raycast():
    # define left most angle of FOV
    start_angle = player_angle - half_FOV

    for ray in range(casted_rays):
        for depth in range(max_depth):

            # get ray target coordinates
            target_x = playerX - math.sin(start_angle) * depth
            target_y = playerX + math.cos(start_angle) * depth

            # covert target X, Y coordinate to map col, row
            col = int(target_x / tile_size)
            row = int(target_y / tile_size)

            # calculate map square index
            square = row * map_size + col

            # ray hits the condition
            if map[square] == '#':
                # highlight wall that has been hit by a casted ray
                pygame.draw.rect(window, (0, 255, 0), (col * tile_size,
                                                    row * tile_size,
                                                    tile_size - 2,
                                                    tile_size - 2))

                # draw casted ray
                pygame.draw.line(window, (255, 255, 0), (playerX, playerY), (target_x, target_y))

                break


def player(x, y):
    window.blit(playerImg, (x, y))

# def isCollision(wallX, wallY, playerX, playerY):
#     global distanceX
#     global distanceY
#     distanceX = wallX - playerX
#     distanceY = wallY - playerY
#     distance = math.sqrt((math.pow(wallX - playerX, 2)) + (math.pow(wallY - playerY, 2)))
#     if distanceX < 48 or distanceX < -48:
#         return True
#     elif distanceY < 24 or distanceY < -24:
#         return True
#     else:
#         return False
#     if distance < 32:
#         return True
#     else:
#         return False


running = True

while running:

    window.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # stops automatically quitting
            running = False

        # if event.type == pygame.KEYDOWN:  # movement
        #     if event.key == pygame.K_LEFT:
        #         print("Left Pressed")
        #         playerX_change = -0.15
        #         print(playerX, playerY)
        #     if event.key == pygame.K_RIGHT:
        #         print("Right Pressed")
        #         playerX_change = 0.15
        #         print(playerX, playerY)
        #     if event.key == pygame.K_UP:
        #         print("Up Pressed")
        #         playerY_change = -0.15
        #         print(playerX, playerY)
        #     if event.key == pygame.K_DOWN:
        #         print("Down Pressed")
        #         playerY_change = 0.15
        #         print(playerX, playerY)
        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        #         print("Key Released")
        #         playerX_change = 0
        #     if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
        #         print("Key Released")
        #         playerY_change = 0

    playerX += playerX_change
    playerY += playerY_change

    # border collisions
    if playerX <= -1:
        playerX = 0
        # print("Boundaries Reached")
    elif playerX >= 769:
        playerX = 768
        # print("Boundaries Reached")
    elif playerY <= 0:
        playerY = 0
        # print("Boundaries Reached")
    elif playerY >= 568:
        playerY = 568
        # print("Boundaries Reached")

    # collision = isCollision(wallX, wallY, playerX, playerY)  # collisons
    # window.blit(off, (8, 576))
    # if collision:
    #     print("Collision Detected")
    #     window.blit(on, (8, 576))

    # insert collision code

    # font = pygame.freetype.Font("pixelfont.ttf", 20)  # font
    # pX = str(round(playerX, 2))  # text
    # pY = str(round(playerY, 2))
    # text_surface1, rect1 = font.render(pX, (255, 255, 255))
    # text_surface2, rect2 = font.render(pY, (255, 255, 255))
    # window.blit(text_surface1, (5, 5))
    # window.blit(text_surface2, (5, 30))

    # dX = str(round(distanceX, 2))
    # dY = str(round(distanceY, 2))
    # distanceX_text, rect3 = font.render(dX, (127.5, 255, 255))
    # distanceY_text, rect4 = font.render(dY, (127.5, 255, 255))
    # window.blit(distanceX_text, (5, 55))
    # window.blit(distanceY_text, (5, 80))

    # player(playerX, playerY)
    # wall(wallX, wallY)
#    clock.tick(60)

    col = int(playerX / tile_size)
    row = int(playerY / tile_size)

    square = row * map_size + col

    forward = True

    if map[square] == '#':
        if forward:
            playerX -= -math.sin(player_angle) * 5
            playerY -= math.cos(player_angle) * 5
        else:
            playerX += -math.sin(player_angle) * 5
            playerY += math.cos(player_angle) * 5

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]: player_angle -= 0.1
    if keys[pygame.K_RIGHT]: player_angle += 0.1
    if keys[pygame.K_UP]:
        forward = True
        playerX += -math.sin(player_angle) * 5
        playerY += math.cos(player_angle) * 5
    if keys[pygame.K_DOWN]:
        forward = False
        playerX -= -math.sin(player_angle) * 5
        playerY -= math.cos(player_angle) * 5

    # update 2D background
    pygame.draw.rect(window, (0, 0, 0), (0, 0, windowX, windowY))

    draw_map()
    raycast()
    pygame.display.update()

