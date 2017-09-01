import basicSprite
from helpers import *
from text_box import Pane
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

    def MoveKeyDown(self, key):
        """This function sets the xMove or yMove variables that will
        then move the snake when update() function is called.  The
        xMove and yMove values will be returned to normal when this
        keys MoveKeyUp function is called."""

        if (key == K_d):
            self.xMove += self.x_dist
        elif (key == K_a):
            self.xMove += -self.x_dist
        elif (key == K_w):
            self.yMove += -self.y_dist
        elif (key == K_s):
            self.yMove += self.y_dist

    def MoveKeyUp(self, key):
        """This function resets the xMove or yMove variables that will
        then move the player when update() function is called.  The
        xMove and yMove values will be returned to normal when this
        keys MoveKeyUp function is called."""

        if (key == K_d):
            self.xMove += -self.x_dist
        elif (key == K_a):
            self.xMove += self.x_dist
        elif (key == K_w):
            self.yMove += self.y_dist
        elif (key == K_s):
            self.yMove += -self.y_dist

    def update(self, block_group, grass_group, npc_group):
        """Called when the Player sprit should update itself"""

        if (self.xMove == 0) and (self.yMove == 0):
            """If we arn'te moveing just get out of here"""
            return
        """All right we must be moving!"""
        self.rect.move_ip(self.xMove, self.yMove)

        if pygame.sprite.spritecollideany(self, block_group) or pygame.sprite.spritecollideany(self, npc_group):
            """IF we hit a block or an NPC, don't move - reverse the movement"""
            self.rect.move_ip(-self.xMove, -self.yMove)

    def interact(self, key, player, npc, screen):
        twice=pygame.sprite.collide_rect_ratio(1.5)
        if twice(player, npc):
            textbox = Pane()
            textbox.displayText(screen,player, npc.script())
            #npc.script()