#! /usr/bin/env python

#import levelBase
from helpers import *
import monster_main
from group_overload import Group_off
import basicSprite
from player import Player
from NPC import Npc
import camera


class Level():
    """Level class of the Game"""
    def __init__(self, level=1):
        self.level = level

    def getLayout(self):
        if self.level == 1:
            self.GRASS = 0
            self.BLOCK = 1
            self.PLAYER = 2
            self.NPC = 3
            return [
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], \
                    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], \
                    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], \
                    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], \
                    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 1, 1],\
                    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 1, 1],\
                    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],\
                    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 1, 1],\
                    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 1, 1],\
                    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],\
                    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],\
                    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 1],\
                    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 1],\
                    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 1],\
                    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 1],\
                    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 1],\
                    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 1],\
                    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 1],\
                    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 1],\
                    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 1],\
                    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 1],\
                    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 1],\
                    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 1],\
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 1]]


    def getSprites(self):
        player, rect = load_image('images/player.gif', -1)
        ss = spritesheet('images/tiles_2.png')
        grass = ss.image_at((0,480,32,32))
        block = ss.image_at((0,576,32,32))
        npc, rect = load_image('images/npc.gif', -1)
        return [grass,block,player, npc]

    def LoadSprites(self):
        """Load all of the sprites that we need"""
        """calculate the center point offset"""
        x_offset = (monster_main.BLOCK_SIZE/2)
        y_offset = (monster_main.BLOCK_SIZE/2)

        img_list = self.getSprites()
        self.layout = self.getLayout()

        self.block_sprites = Group_off()
        self.grass_sprites = Group_off()
        self.npc_sprites = Group_off()
        self.everything = Group_off()

        self.npc = []
        self.grass = []
        self.block = []

        """Iterate through the layout of the level"""
        for y in xrange(len(self.layout)):
            for x in xrange(len(self.layout[y])):
                """Get the center point for the rects"""
                centerPoint = [(x*monster_main.BLOCK_SIZE)+x_offset,(y*monster_main.BLOCK_SIZE+y_offset)]
                """Determine what each position is, load the correct image at the center point and assign to a sprite group"""
                if self.layout[y][x]==self.BLOCK:
                    self.block.append(basicSprite.Sprite(centerPoint, img_list[self.BLOCK]))
                elif self.layout[y][x]==self.PLAYER:
                    self.grass.append(basicSprite.Sprite(centerPoint, img_list[self.GRASS]))
                    self.player = Player(centerPoint,img_list[self.PLAYER])
                elif self.layout[y][x]==self.GRASS:
                    self.grass.append(basicSprite.Sprite(centerPoint, img_list[self.GRASS]))
                elif self.layout[y][x]==self.NPC:
                    self.grass.append(basicSprite.Sprite(centerPoint, img_list[self.GRASS]))
                    self.npc.append(Npc(centerPoint, img_list[self.NPC], talk_text = ['I just met you And this is crazy So'
                                                                                   ' heres my number So call me maybe!!!!'
                                                                                    , "Who said I can't sing..."]))
        for npc in self.npc:
            self.npc_sprites.add(npc)
        for grass in self.grass:
            self.grass_sprites.add(grass)
        for block in self.block:
            self.block_sprites.add(block)
        self.player_sprites = Group_off(self.player)

        """Make a 'camera' to follow the player and update the world accordingly"""
        total_level_width = len(self.layout[0]) * 32  # calculate size of level in pixels
        total_level_height = len(self.layout) * 32  # maybe make 32 an constant
        camera_x = camera.Camera(camera.complex_camera, total_level_width, total_level_height)

        return self.block_sprites, self.grass_sprites, self.npc_sprites, self.player_sprites, self.player, camera_x
        