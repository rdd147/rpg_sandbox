import basicSprite
from helpers import *
from text_box import Pane
import pygame
from time import sleep


class Human(basicSprite.Sprite):
    def __init__(self, centerPoint, image):
        basicSprite.Sprite.__init__(self, centerPoint, image)
        """Set the number of Pixels to move each time"""
        self.x_dist = 4
        self.y_dist = 4
        """Initialize how much we are moving"""
        self.xMove = 0
        self.yMove = 0

class Player(Human):

    def __init__(self, centerPoint, image):
        Human.__init__(self, centerPoint, image)

    def set_player_speeds(self):
        '''zero out players currrent movement'''
        after = pygame.key.get_pressed()
        self.xMove = 0
        self.yMove = 0
        '''depending on what keys are currently pressed, set the movement levels appropriately'''
        if after[K_w] == 1:
            self.yMove -= self.y_dist
        if after[K_s] == 1:
            self.yMove += self.y_dist
        if after[K_a] == 1:
            self.xMove -= self.x_dist
        if after[K_d] == 1:
            self.xMove += self.x_dist
        return

    def update(self, block_group, grass_group, npc_group):
        """Called when the Player sprite should update itself"""

        """function to set players movement based on what buttons are currently pressed"""
        self.set_player_speeds()
        if (self.xMove == 0) and (self.yMove == 0):
            """If we aren't moveing just get out of here"""
            return
        """All right we must be moving!"""
        self.rect.move_ip(self.xMove, self.yMove)

        if pygame.sprite.spritecollideany(self, block_group) or pygame.sprite.spritecollideany(self, npc_group):
            """IF we hit a block or an NPC, don't move - reverse the movement"""
            self.rect.move_ip(-self.xMove, -self.yMove)

    def interact(self, key, player, npcs, screen):
        """Function to define the spacebar interaction between the player and other things"""

        """Scale the collision rect up bu 1.5 times"""
        largerrect=pygame.sprite.collide_rect_ratio(1.5)

        """Loop over all NPCs and check to see if they collide with eaach other using the larger rect ratios"""
        for npc in npcs:
            if largerrect(player, npc):
                """Build a textbox and display the script that the NPC is constructed with"""
                textbox = Pane()
                textbox.displayText(screen, npc.script())