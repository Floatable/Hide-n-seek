#----------------------------------------------------------------------------------------------------
# Imports The Pygame Library
# Download link: https://pypi.org/project/pygame/
# Created By The Python Community 
import pygame
from pygame import *
#----------------------------------------------------------------------------------------------------
# Some code used from user underscoreC on stack overflow
# Link: https://stackoverflow.com/questions/43179682/how-can-i-create-an-interactive-object-in-pygame
#----------------------------------------------------------------------------------------------------
# Some code used from online python game tutorial 
# Link to code: https://pastebin.com/embed_js/jB6k06hG
# Link to Video: https://www.youtube.com/watch?v=XGf2GcyHPhc&list=PLWKjhJtqVAbnqBxcdjVGgT3uVR10bzTEB&t=4734s
# Timestamp: (45:35)
#----------------------------------------------------------------------------------------------------

# Starts and keeps the code running 
pygame.init()
#defines how big the window is
pygame.init()


WIDTH = 1040
HEIGHT = 876
Main = pygame.display.set_mode((WIDTH, HEIGHT))

#used to tell the program how many times to update AKA frames per second
clock = pygame.time.Clock()
#used to open and close the main loop
loop = False
# Creates and places character
x=100
y=50
class Player1:
    def __init__(self):
        self.speed = 4
        self.width = 16
        self.height = 16
        self.color = (0,51,102)
        self.rect = pygame.Rect(15,25, 20, 20,)

    def up(self):
        self.rect.y = max([self.rect.y - self.speed, 0])
        
    def down(self):
        self.rect.y = min([self.rect.y + self.speed, HEIGHT - self.height])
        
    def left(self):
        self.rect.x = max([self.rect.x - self.speed, 0])
        
    def right(self):
        self.rect.x = min([self.rect.x + self.speed, WIDTH - self.width])
        
    def draw(self):
        pygame.draw.rect(Main, self.color, self.rect)
class Player2:
    def __init__(self):
        self.speed = 4
        self.width = 16
        self.height = 16
        self.color = (255, 50, 37)
        self.rect = pygame.Rect(15,273, 20, 20)

    def up(self):
        self.rect.y = max([self.rect.y - self.speed, 0])
        
    def down(self):
        self.rect.y = min([self.rect.y + self.speed, HEIGHT - self.height])
        
    def left(self):
        self.rect.x = max([self.rect.x - self.speed, 0])
        
    def right(self):
        self.rect.x = min([self.rect.x + self.speed, WIDTH - self.width])
        
    def draw(self):
        pygame.draw.rect(Main, self.color, self.rect)
char1 = Player1()
char2 = Player2()


def DoorH(surface,x,y): 
    pygame.draw.rect(surface, grey, (x,y,30,9))
def DoorV(surface,x,y): 
    pygame.draw.rect(surface, grey, (x,y,9,30))
def Black(surface,x,y,w,h): 
    pygame.draw.rect(surface, black, (x,y,w,h))
def dSR(surface,x,y,w,h): 
    pygame.draw.rect(surface, Bluegrey, (x,y,w,h),5)

#r1 deco
Bread = pygame.Rect(25,135,10,10)
Dresser1 = pygame.Rect(126, 5, 20, 60)
Nightstand1 = pygame.Rect(45, 5, 20, 20)
Bed1 = pygame.Rect(5, 5, 38, 80)
Pillow1 = pygame.Rect(10, 10, 26, 20)
#r2 deco
Dresser2 = pygame.Rect(86, 318, 60, 20)
Nightstand2 = pygame.Rect(45, 263, 20, 25)
Bed2 = pygame.Rect(5, 258, 38, 80)
Pillow2 = pygame.Rect(10, 263, 26, 20)
objects = [Dresser1,Nightstand1,Bed1,Pillow1,Bread]

# this is the main code part and everything that runs needs to be inside this loop to be shown on the screen
while not loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = True
        elif event.type == pygame.MOUSEBUTTONDOWN:  # or MOUSEBUTTONDOWN depending on what you want.
            print(pygame.mouse.get_pos())


    # this defines how the player moves

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        char1.up()
    if pressed[pygame.K_DOWN]:
        char1.down()
    if pressed[pygame.K_LEFT]:
        char1.left()
    if pressed[pygame.K_RIGHT]:
        char1.right()
    
    if pressed[pygame.K_w]:
        char2.up()
    if pressed[pygame.K_s]:
        char2.down()
    if pressed[pygame.K_a]:
        char2.left()
    if pressed[pygame.K_d]:
        char2.right()

    pygame.display.update()
    # Main.fill((0, 0, 0))

    # this is an interesting piece of code as it is constantly updating the player by deleting it after it detects movement 
    # so while the player moves it creates a new player while the old player is left in its posistion creating a snake like entity
    # this prevents that from happening   

    # tells the program how to define certain colors used later
    brown = (102,51,0)
    grey = (54,69,79)
    white = (255,255,255)
    Bluegrey = (137, 148, 153)
    black = (0,0,0)
    bread = (198,137,88)
    # sets the font
    myfont = pygame.font.SysFont("monospace", 15)

    # Creates the labels for items or the text that appears on the screen
    # The Bread doesnt do anything and is there souly for my entertainment
#-----------------------------------------------------------------

#--------------------------------------------------------------
    # pygame.draw.rect(Main,bread,Bread)
    # # these actually place the items and player on the screen
    # pygame.draw.rect(Main,brown,Dresser1)
    # pygame.draw.rect(Main,brown,Nightstand1)
    # pygame.draw.rect(Main,grey,Bed1)
    # pygame.draw.rect(Main,white,Pillow1)
    # # this is for the walls and to help me code these

#--------------------------------------------------------------

# Garage 
    dSR(Main,x,y,298,396)

# Storage(down)
    dSR(Main,x,y,166,56)

# Storage(up)
    dSR(Main,x,y,138,86)

# Bedroom 2
    dSR(Main,x,y,166,144)

# Bath 3
    dSR(Main,x,y,64,100)

# Closet (bath 3)
    dSR(Main,x,y,46,100)

# Bedroom 3
    dSR(Main,x,y,166,144)

# Bathroom 2
    dSR(Main,x,y,84,100)

# Closet (Bath 2)
    dSR(Main,x,y,48,100)

# Game room
    dSR(Main,x,y,200,172)

# Powder room
    dSR(Main,x,y,78,84)

# Mud room
    dSR(Main,x,y,78,136)

# Utility
    dSR(Main,x,y,152,82)

# Pantry
    dSR(Main,x,y,78,102)

# Foyer
    dSR(Main,x,y,92,130)

# Study
    dSR(Main,x,y,150,134)

# Kitchen/Dining
    dSR(Main,x,y,184,384)

# Great room
    dSR(Main,x,y,220,224)

# Primary bedroom
    dSR(Main,x,y,180,188)

# Main bath
    dSR(Main,x,y,152,200)

# Main Bath Shower
    dSR(Main,x,y,40,68)

# Main Closet
    dSR(Main,x,y,158,88)

#--------------------------------------------------------------
    
    char2.draw()
    char1.draw()


    
    pygame.display.flip()
    # This specifies how many times the window updates per second
    clock.tick(60)