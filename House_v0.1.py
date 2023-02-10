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


WIDTH = 661
HEIGHT = 400
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
        self.speed = 2
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
        self.speed = 2
        self.width = 16
        self.height = 16
        self.color = (255, 50, 37)
        self.rect = pygame.Rect(15,330, 20, 20)

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


def dSR(surface,x,y,w,h): 
    pygame.draw.rect(surface, Bluegrey, (x,y,w,h),5)

#r1 deco
Bread = pygame.Rect(25,135,10,10)
Dresser1 = pygame.Rect(126, 5, 20, 60)
Nightstand1 = pygame.Rect(45, 5, 20, 20)
Bed1 = pygame.Rect(5, 5, 38, 80)
Pillow1 = pygame.Rect(10, 10, 26, 20)
#r2 deco
Dresser2 = pygame.Rect(86, 375, 60, 20)
Nightstand2 = pygame.Rect(45, 320, 20, 25)
Bed2 = pygame.Rect(5, 315, 38, 80)
Pillow2 = pygame.Rect(10, 320, 26, 20)
objects = [Dresser1,Nightstand1,Bed1,Pillow1,Bread]

# this is the main code part and everything that runs needs to be inside this loop to be shown on the screen
while not loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = True
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
    Main.fill((0, 0, 0))

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
    label = myfont.render("Bread.", 1, (255,255,255))
    Main.blit(label, (10, 115))
    label = myfont.render("Dresser", 1, (255,255,255))
    Main.blit(label, (80, 75))
    label = myfont.render("Night", 1, (255,255,255))
    Main.blit(label, (50, 35))
    label = myfont.render("Stand", 1, (255,255,255))
    Main.blit(label, (50, 45))
    label = myfont.render("Bed", 1, (255,255,255))
    Main.blit(label, (10, 90))
    label = myfont.render("Dresser", 1, (255,255,255))
    Main.blit(label, (81, 355))
    label = myfont.render("Nightstand", 1, (255,255,255))
    Main.blit(label, (45, 345))
    label = myfont.render("Bed", 1, (255,255,255))
    Main.blit(label, (10, 295))
#--------------------------------------------------------------
    pygame.draw.rect(Main,bread,Bread)
    # these actually place the items and player on the screen
    pygame.draw.rect(Main,brown,Dresser1)
    pygame.draw.rect(Main,brown,Nightstand1)
    pygame.draw.rect(Main,grey,Bed1)
    pygame.draw.rect(Main,white,Pillow1)
    # this is for the walls and to help me code these
#room2 
    pygame.draw.rect(Main,brown,Dresser2)
    pygame.draw.rect(Main,brown,Nightstand2)
    pygame.draw.rect(Main,grey,Bed2)
    pygame.draw.rect(Main,white,Pillow2)
#--------------------------------------------------------------
    char2.draw()
    char1.draw()
#---------------------------------------------------------------
    #up
    #Bedroom
    dSR(Main,0,0,151,150)
    #Bathroom
    dSR(Main,151,0,68,110)
    #Closet (Right)
    dSR(Main,76,150,75,104)
    #Cabnet
    dSR(Main,220,70,25,25)
#----------------------------------------------------------------
    #down
    #Bedroom
    dSR(Main,0,254,151,146)
    #Bathroom
    dSR(Main,151,295,68,106)
    #Closet (Left)
    dSR(Main,0,150,76,104)
    #Cabnet
    dSR(Main,220,70,25,25)
    
#    for rect in objects:
#        if char1.colliderect(rect) or char2.colliderect(rect):
#            if rect == Bread:
#                print("bread")
#            elif rect == Dresser:
#                print("Dresser")
#            elif rect == Nightstand:
#                print("Nightstand")
#            elif rect == Bed:
#                print("Bed")
#            elif rect == Pillow:
#                print("Pillow")
    pygame.display.flip()
    # This specifies how many times the window updates per second
    clock.tick(60)