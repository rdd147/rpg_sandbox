from monster_generation import *
import level001
from player import Player
import camera
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
In Progress: Make a text widget for displaying text when Player interacts with things (NPCs etc.)
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

class Main_game:
    """The Main Game Class - This class handles the main
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
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('RPG sandbox')

    def MainLoop(self):
        """This is the Main Loop of the Game"""

        """Create the background"""
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0, 0, 0))
        """Create the game clock to manage framerate"""
        self.timer = pygame.time.Clock()

        """Load the level"""
        level1 = level001.Level(1)
        self.block_sprites, self.grass_sprites, self.npc_sprites, self.player_sprites, self.player, camera_x = level1.LoadSprites()


        while True:

            """Event loop"""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == KEYUP:
                    pass
                elif event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        self.player.interact(event.key, self.player, self.npc_sprites, self.screen)

            """Update the camera based on the players new position in the level"""
            camera_x.update(self.player)

            """Draw the enviorment sprites with respect to the cameras offset from the players movement"""
            self.block_sprites.draw(self.screen , [camera_x.height, camera_x.width])
            self.grass_sprites.draw(self.screen, [camera_x.height, camera_x.width])

            """Update and draw the player with respect to the enviorment"""
            self.player_sprites.update(self.block_sprites, self.grass_sprites, self.npc_sprites)
            self.player_sprites.draw(self.screen, [camera_x.height, camera_x.width])

            self.npc_sprites.draw(self.screen, [camera_x.height, camera_x.width])

            """Actually draw everything"""
            pygame.display.flip()

            """Limit FPS"""
            self.timer.tick(30)




if __name__ == '__main__':
    print 'it ran!!'
    squirt = Water_monster(1)
    charm = Fire_monster(2)
    squirt.attack()
    squirt.talk()
    charm.blurb()
    loop = Main_game(WIN_WIDTH,WIN_HEIGHT)
    loop.MainLoop()