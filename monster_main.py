from monster_generation import *
from level001 import *
from player import Player
from camera import *
from group_overload import Group_off
from NPC import Npc

import os, sys
import pygame
from pygame.locals import *
import basicSprite
from text_box import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

'''Global constants'''

BLOCK_SIZE = 32
WIN_WIDTH = 800
WIN_HEIGHT = 640
HALF_WIDTH = int(WIN_WIDTH / 2)
HALF_HEIGHT = int(WIN_HEIGHT / 2)
movement_buttons = [K_d, K_w, K_a, K_s]

"""
TODO: Make a text widget for displaying text when Player interacts with things (NPCs etc.)
In Progress: Make an action button for the main character to interact with objects, NPCs
Complete: Make an NPC class
TODO: Update the level code to support more than 1 level gracefully
TODO: Make an environment layer to every level to add other static sprites for better atmosphere
TODO: Make an overall scene class to organize scene sequencing, control game flow
TODO: Make a pokemon class and define all aspects that every Pokemon needs
TODO: Make individual pokemon that inherit from the pokemon class
TODO: Make an item system and storage
TODO: Make a game menu and grant access to available stuff like items and pokemon
TODO: Make a save system that can store every aspect of the game
TODO: Prototype a music player that can be accessed based on level and/or scene class
TODO: Make a battle 'mode' where pokemon can be encountered in the wild and/or with NPCs
TODO: Make an algorithim to gradually and randomly encounter pokemon in the wild based on tile
TODO: Be able to load 1 larger enviormental sprite (like a tree) and block off multiple tiles as the player can't walk through
TODO: Make a 'move' class that defines the attributes that every move needs to have
TODO: Make a suite of individual moves (like tackle or electrocute) that attach to certain Pokemon
TODO: Create scene animations such as what to show when the player tranisitions to battle mode and perhaps attacking
"""

class Main_poke:
    """The Main Pokemon Class - This class handles the main
    initialization and creating of the Game."""

    def __init__(self, width, height):
        """Initialize"""
        """Initialize PyGame"""
        pygame.init()
        """Initalize the font"""
        pygame.font.init()
        """Set the window Size"""
        self.width = width
        self.height = height
        """Create the Screen"""
        self.screen = pygame.display.set_mode((self.width
                                               , self.height))
        self.entities = pygame.sprite.Group()


    def MainLoop(self):
        """This is the Main Loop of the Game"""

        """Load All of our Sprites"""
        self.LoadSprites();

        """Create the background"""
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0, 0, 0))
        """Create the game clock to manage framerate"""
        self.timer = pygame.time.Clock()

        """Make a 'camera' to follow the player and update the world accordingly"""
        total_level_width = len(self.layout[0]) * 32  # calculate size of level in pixels
        total_level_height = len(self.layout) * 32  # maybe make 32 an constant
        camera = Camera(complex_camera, total_level_width, total_level_height)

        while 1:
            """clear all surfaces at begininng of loop"""
            self.everything.clear(self.screen, self.background)
            #self.monster_sprites.clear(self.screen, self.background)

            """Event loop"""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == KEYDOWN:
                    """Detect any movement buttons and pass to player function to handle movement"""
                    if event.key in movement_buttons:
                        self.player.MoveKeyDown(event.key)
                        move_keydown = True
                    if event.key == K_SPACE:
                        self.player.interact(event.key, self.player, self.npc, self.screen)
                        #test = Pane()
                        #self.screen, self.player = test.displayText(self.screen, self.player, 'Hope this works....')
                        #pygame.event.set_allowed(None)
                        #pygame.event.set_allowed(KEYDOWN)

                elif event.type == KEYUP:
                    if event.key in movement_buttons:
                        """Detect any removal of movement buttons and pass to player function to turn off movement"""
                        self.player.MoveKeyUp(event.key)
                        move_keydown = False


            """Update the camera based on the players new position in the level"""
            camera.update(self.player)

            """Draw the enviorment sprites with respect to the cameras offset from the players movement"""
            self.block_sprites.draw(self.screen , [camera.height, camera.width])
            self.grass_sprites.draw(self.screen, [camera.height, camera.width])

            """Update and draw the player with respect to the enviorment"""
            self.player_sprites.update(self.block_sprites, self.grass_sprites, self.npc_sprites)
            self.player_sprites.draw(self.screen, [camera.height, camera.width])

            self.npc_sprites.draw(self.screen, [camera.height, camera.width])

            """Actually draw everything"""
            pygame.display.flip()

            """Limit FPS"""
            self.timer.tick(30)

    def LoadSprites(self):
        """Load all of the sprites that we need"""
        """calculate the center point offset"""
        x_offset = (BLOCK_SIZE/2)
        y_offset = (BLOCK_SIZE/2)
        """Load the level"""
        level1 = level()
        self.layout = level1.getLayout()
        img_list = level1.getSprites()

        self.block_sprites = Group_off()
        self.grass_sprites = Group_off()
        self.npc_sprites = Group_off()
        self.everything = Group_off()

        """Iterate through the layout of the level"""
        for y in xrange(len(self.layout)):
            for x in xrange(len(self.layout[y])):
                """Get the center point for the rects"""
                centerPoint = [(x*BLOCK_SIZE)+x_offset,(y*BLOCK_SIZE+y_offset)]
                """Determine what each position is, load the correct image at the center point and assign to a sprite group"""
                if self.layout[y][x]==level1.BLOCK:
                    block = basicSprite.Sprite(centerPoint, img_list[level1.BLOCK])
                    self.block_sprites.add(block)
                    self.everything.add(block)
                elif self.layout[y][x]==level1.PLAYER:
                    grass = basicSprite.Sprite(centerPoint, img_list[level1.GRASS])
                    self.player = Player(centerPoint,img_list[level1.PLAYER])
                    self.grass_sprites.add(grass)
                    self.everything.add(self.player)
                    self.everything.add(grass)
                elif self.layout[y][x]==level1.GRASS:
                    grass = basicSprite.Sprite(centerPoint, img_list[level1.GRASS])
                    self.grass_sprites.add(grass)
                    self.everything.add(grass)
                elif self.layout[y][x]==level1.NPC:
                    grass = basicSprite.Sprite(centerPoint, img_list[level1.GRASS])
                    self.npc = Npc(centerPoint, img_list[level1.NPC], talk_text = ['I just met you And this is crazy So'
                                                                                   ' heres my number So call me maybe!!!!', "Who said I can't sing..."])
                    self.grass_sprites.add(grass)
                    self.npc_sprites.add(self.npc)
                    self.everything.add(self.npc)
                    self.everything.add(grass)
        self.player_sprites = Group_off(self.player)


if __name__ == '__main__':
    print 'it ran!!'
    squirt = Water_monster(1)
    charm = Fire_monster(2)
    squirt.attack()
    squirt.talk()
    charm.blurb()
    loop = Main_poke(WIN_WIDTH,WIN_HEIGHT)
    loop.MainLoop()