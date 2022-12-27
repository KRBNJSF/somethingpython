import sys

import pygame

import Settings
from utils import SpriteSheetConverter

# img
sheet_bg = (0, 255, 255)
animationList = []
last_update = 0
animation_cooldown = 200
frame = 0

# basic
isRunning = True
pygame.init()
screen = pygame.display.set_mode([pygame.display.Info().current_w, pygame.display.Info().current_h],
                                 pygame.FULLSCREEN)


def init_animation_images(animation_steps):
    for x in range(animation_steps):
        animationList.append(sprite_sheet.getImage(x, 30, 31, Settings.SCALE, sheet_bg))


def initGame():
    global sprite_sheet
    pygame.display.set_caption("Something")

    sprite_sheet_image = pygame.image.load("img/spritesheetImage.png").convert_alpha()
    sprite_sheet = SpriteSheetConverter.SpriteSheet(sprite_sheet_image)

    init_animation_images(2)


def animate(last_update=None):
    global frame
    # Updating animation
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time

    # Showing image
    screen.blit(animationList[frame], (600, 300))


def gameLoop():
    global isRunning, frame, last_update

    while isRunning:
        # Updating screen background
        screen.fill((60, 60, 0))

        # Animation
        # Updating ticks
        current_time = pygame.time.get_ticks()
        # Changing image every 500 mils
        if current_time - last_update >= animation_cooldown:
            frame += 1
            last_update = current_time
            if frame >= len(animationList):
                frame = 0

        # Showing image
        screen.blit(animationList[frame], (600, 300))

        # Click events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False

        # Key events
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            isRunning = False

        # Invalidating screen
        pygame.display.update()
    pygame.quit()
    sys.exit(1)


if __name__ == '__main__':
    initGame()
    gameLoop()
