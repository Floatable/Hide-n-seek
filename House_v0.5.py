#----------------------------------------------------------------------------------------------------
# Imports The Pygame Library
# Download link: https://pypi.org/project/py/
# Created By The Python Community 
import pygame as py
#----------------------------------------------------------------------------------------------------
# Some code used from user underscoreC on stack overflow
# Link: https://stackoverflow.com/questions/43179682/how-can-i-create-an-interactive-object-in-py
#----------------------------------------------------------------------------------------------------
# Some code used from online python game tutorial 
# Link to code: https://pastebin.com/embed_js/jB6k06hG
# Link to Video: https://www.youtube.com/watch?v=XGf2GcyHPhc&list=PLWKjhJtqVAbnqBxcdjVGgT3uVR10bzTEB&t=4734s
# Timestamp: (45:35)
#----------------------------------------------------------------------------------------------------

# Starts and keeps the code running 
py.init()
#defines how big the window is


WIDTH = 1000
HEIGHT = 850
Main = py.display.set_mode((WIDTH, HEIGHT))

background = py.image.load("Houseplan.png")
#used to tell the program how many times to update AKA frames per second
clock = py.time.Clock()
#used to open and close the main loop
loop = False
# Creates and places character
x=100
y=50
brown = (102,51,0)
grey = (54,69,79)
white = (255,255,255)
bluegrey = (137, 148, 153)
black = (0,0,0)
bread = (198,137,88)
#--------------------------------------------------------------
timer = 1
font = py.font.SysFont(None, 72)
title_font = py.font.SysFont("serif typeface", 90)

second_font = py.font.SysFont(None, 50)
next_font = py.font.SysFont("serif typeface", 70)
again_font = py.font.SysFont("serif typeface", 40)

player_info = None
player_size = 20

class Player(py.sprite.Sprite):
  
  def __init__(self, player_x, player_y, RGB):

    py.sprite.Sprite.__init__(self)

    self.image = py.Surface([player_size, player_size])
    self.rect = self.image.get_rect()
    self.image.fill(RGB)
    self.rect.x = player_x
    self.rect.y = player_y
    self.p_vel = 3
    self.tagged = False

   
#CONTROLS
  def move_up(self):
    self.rect.y -= self.p_vel
    
  def move_down(self):
    self.rect.y += self.p_vel
    
  def move_left(self):
    self.rect.x -= self.p_vel
    
  def move_right(self):
    self.rect.x += self.p_vel
  
  
  # DETECTS THE PLAYER COLLISION WITH THE BORDER
  def player_border_collision(self):
    if self.rect.x < 0:
        self.rect.x = 0
    if self.rect.x > WIDTH - player_size - 1:
        self.rect.x = WIDTH - player_size -1
    if self.rect.y < 0:
        self.rect.y = 0
    if self.rect.y > HEIGHT - player_size - 1:
        self.rect.y = HEIGHT - player_size - 1

  # DETECTS COLLISION WITH THE WALLS
  def player_wall_right_x(self, player):
    if py.sprite.spritecollideany(player, wall_sprites):
      self.rect.x -= self.p_vel
  def player_wall_up_y(self, player):
    if py.sprite.spritecollideany(player, wall_sprites):
      self.rect.y += self.p_vel
  def player_wall_left_x(self, player):
    if py.sprite.spritecollideany(player, wall_sprites):
      self.rect.x += self.p_vel
  def player_wall_down_y(self, player):
    if py.sprite.spritecollideany(player, wall_sprites):
      self.rect.y -= self.p_vel

  
  #DETECTS COLLISION WITH SLOW WALLS
  #right
  def player_slow_wall_right_x(self, player):
    if py.sprite.spritecollideany(player, door_sprites):
      self.rect.x -= self.p_vel-1
  #left
  def player_slow_wall_left_x(self, player):
    if py.sprite.spritecollideany(player, door_sprites):
      self.rect.x += self.p_vel-1
  #up    
  def player_slow_wall_up_y(self, player):
    if py.sprite.spritecollideany(player, door_sprites):
      self.rect.y += self.p_vel-1
  #down
  def player_slow_wall_down_y(self, player):
    if py.sprite.spritecollideany(player, door_sprites):
      self.rect.y -= self.p_vel-1

class Wall(py.sprite.Sprite):
  def __init__(self, wall_x, wall_y, wall_width, wall_height, color):

    py.sprite.Sprite.__init__(self)

    self.image = py.Surface([wall_width, wall_height])
    self.rect = self.image.get_rect()
    self.image.fill(color)
    self.rect.x = wall_x
    self.rect.y = wall_y


color = bluegrey 

wall_sprites = py.sprite.Group()
wall_1 = Wall(45, 52, 3, 213, color)
wall_2 = Wall(45, 52, 173, 4, color)
wall_3 = Wall(217, 52, 4, 182, color)
wall_4 = Wall(45, 236, 35, 4, color)
wall_5 = Wall(115,234,57,4,color)
wall_6 = Wall(205,234,95,4,color)
wall_7 = Wall(157,238,4,80,color)
wall_8 = Wall(10,264,60,4,color)
wall_9 = Wall(10,264,4,135,color)
wall_10 = Wall(10,395,60,4,color)
wall_11 = Wall(52,296,4,72,color)
wall_12 = Wall(136,307,66,4,color)
wall_13 = Wall(157,346,4,85,color)
wall_14 = Wall(137,355,23,4,color)
wall_15 = Wall(45,399,4,118,color)
wall_16 = Wall(45,426,40,4,color)
wall_17 = Wall(118,426,43,4,color)
wall_18 = Wall(46,513,152,3,color)
wall_19 = Wall(197,287,5,295,color)
wall_20 = Wall(160,385,39,5,color)
wall_21 = Wall(185,426,14,4,color)
wall_22 = Wall(197,287,27,3,color)
wall_23 = Wall(217,238,8,7,color)
wall_24 = Wall(226,454,134,4,color)
#https://coolors.co/818479-b5cbb7-d2e4c4-e4e9b2-e7e08b

wall_sprites.add(wall_1,wall_2,wall_3,
wall_4,wall_5,wall_6,
wall_7,wall_8,wall_9,
wall_10,wall_11,wall_12,
wall_13,wall_14,wall_15,
wall_16,wall_17,wall_18,
wall_19,wall_20,wall_21,
wall_22,wall_23,wall_24)


dcolor = grey
door_sprites = py.sprite.Group()
door_1 = Wall(79,236,35,4,dcolor)
door_2 = Wall(172,235,35,4,dcolor)
door_3 = Wall(157,318,4,29,dcolor)
door_4 = Wall(85,427,32,4,dcolor)
door_5 = Wall(161,426,24,4,dcolor)
door_6 = Wall(162,288,39,1,dcolor)
door_sprites.add(door_1,door_2,door_3,
door_4,door_5)

player_1_sprite = py.sprite.Group()
player_1 = Player(100,100,black)
player_1_sprite.add(player_1)

player_2_sprite = py.sprite.Group()
player_2 = Player(584, 288, white)
player_2_sprite.add(player_2)

player_sprites = py.sprite.Group()
player_sprites.add(player_1_sprite, player_2_sprite)
#--------------------------------------------------------------

all_sprites = py.sprite.Group()
all_sprites.add(player_1_sprite, player_2_sprite, wall_sprites, door_sprites)

# this is the main code part and everything that runs needs to be inside this loop to be shown on the Main
while not loop:
    for event in py.event.get():
        if event.type == py.QUIT:
            loop = True
        elif event.type == py.MOUSEBUTTONDOWN:  # or MOUSEBUTTONDOWN depending on what you want.
            print(py.mouse.get_pos())
    if event.type == py.KEYDOWN:
      if event.key == py.K_q:
        x1input = input("X1: ")
        y1input = input("Y1: ")
        x2input = input("X2: ")
        y2input = input("Y2: ")
        xdiff = x1input - x2input
        ydiff = y1input - y2input
        print(f"Wall({x1input},{y1input},{xdiff},{ydiff},color)")


    # this defines how the player moves

    pressed = py.key.get_pressed()
    if pressed[py.K_UP]:
        player_1.move_up()
        player_1.player_wall_up_y(player_1)
        player_1.player_slow_wall_up_y(player_1)
    if pressed[py.K_DOWN]:
        player_1.move_down()
        player_1.player_wall_down_y(player_1)
        player_1.player_slow_wall_down_y(player_1)
    if pressed[py.K_LEFT]:
        player_1.move_left()
        player_1.player_wall_left_x(player_1)
        player_1.player_slow_wall_left_x(player_1)
    if pressed[py.K_RIGHT]:
        player_1.move_right()
        player_1.player_wall_right_x(player_1)
        player_1.player_slow_wall_right_x(player_1)
    
    # if pressed[py.K_w]:
    #     char2.up()
    # if pressed[py.K_s]:
    #     char2.down()
    # if pressed[py.K_a]:
    #     char2.left()
    # if pressed[py.K_d]:
    #     char2.right()

    # Main.fill((0, 0, 0))
    py.display.update()
    all_sprites.update()
    Main.blit(background,(0,0))
    # this is an interesting piece of code as it is constantly updating the player by deleting it after it detects movement 
    # so while the player moves it creates a new player while the old player is left in its posistion creating a snake like entity
    # this prevents that from happening   

    # tells the program how to define certain colors used later

    # sets the font
    # Creates the labels for items or the text that appears on the Main
    # The Bread doesnt do anything and is there souly for my entertainment
#-----------------------------------------------------------------

#--------------------------------------------------------------
    # py.draw.rect(Main,bread,Bread)
    # # these actually place the items and player on the Main
    # py.draw.rect(Main,brown,Dresser1)
    # py.draw.rect(Main,brown,Nightstand1)
    # py.draw.rect(Main,grey,Bed1)
    # py.draw.rect(Main,white,Pillow1)
    # # this is for the walls and to help me code these
#--------------------------------------------------------------

#--------------------------------------------------------------

#--------------------------------------------------------------
    
    # char2.draw()
    # char1.draw()
    #DRAWING THE WALLS
    wall_sprites.draw(Main)
    door_sprites.draw(Main)

    #DRAWING THE PLAYERS
    player_1_sprite.draw(Main)
    player_1.player_border_collision()

    player_2_sprite.draw(Main)
    player_2.player_border_collision()

    first_time = py.time.get_ticks()
    py.display.flip()
    # This specifies how many times the window updates per second
    clock.tick(60)

# while loop:
#     clock.tick(60)

#     for event in py.event.get():

#         if event.type == py.QUIT:
#             run = False
#         if event.type == py.KEYDOWN:
#             if event.key == py.K_ESCAPE:
#                 run = False

#     keys = py.key.get_pressed()

#     Main.fill(grey)

#     second_time = (py.time.get_ticks() - first_time)
#      # mainloop
#     seconds= int((second_time) / 1000)
#     calculate_time = (timer - seconds)
#     # time = font.render(str(calculate_time))
#     Main.blit(time, (10, 10))

#     if calculate_time <= 0:
#         run = False
#         final_screen = True
