import pygame
import sys
from pygame.locals import *

pygame.init()
pygame.display.set_caption('Start Menu')
screen = pygame.display.set_mode((600, 300))
# Using default font for the menu text
font = pygame.font.SysFont(None, 30)
clock = pygame.time.Clock()
FPS = 60

# A function for drawing text onto the screen and onto buttons
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
# A variable to check if user pressed one of the buttons
click = False
# Container function that holds both the buttons function
# and the game function
def main_menu():
    while True:
        screen.fill((0,190,255))
        draw_text('Main Menu', font, (0,0,0), screen, 250, 40)
        mx, my = pygame.mouse.get_pos()
        # Creating buttons
        button_1 = pygame.Rect(200, 100, 200, 50)
        button_2 = pygame.Rect(200, 180, 200, 50)

        if button_1.collidepoint((mx, my)):
            if click:
                game()
                if button_2.collidepoint((mx, my)):
                    if click:
                        options()
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
        # Drawing text on top of the button

        draw_text('PLAY', font, (255,255,255), screen, 270, 115)
        draw_text('OPTIONS', font, (255,255,255), screen, 250, 195)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        clock.tick(FPS)
    # This function is called when the "PLAY" button is clicked.
        def game():
            running = True
            while running:
                screen.fill((0,0,0))
                draw_text('GAME SCREEN', font, (255, 255, 255), screen, 20, 20)
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()

                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            running = False
                pygame.display.update()
                clock.tick(FPS)
            # This function is called when the "OPTIONS" button is clicked
        def options():
            running = True
            while running:
                screen.fill((0,0,0))
                draw_text('OPTIONS SCREEN', font, (255, 255, 255), screen, 20, 20)
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()

                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            running = False
                pygame.display.update()

                clock.tick(60)
main_menu()