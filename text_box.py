# draw some text into an area of a surface
# automatically wraps words
import pygame
from pygame.locals import *
import sys


green = (25,125,0)
blue = (0,25,125)
movement_buttons = [K_d, K_w, K_a, K_s]


class Pane(object):
    def __init__(self):
        pygame.init()
        '''Set font, font color, and different surfaces and fill colors to make a text box'''
        self.font = pygame.font.SysFont('Arial', 40)
        pygame.display.set_caption('Box Test')
        self.text_rect = Rect(0,0,750,150)
        self.color = (255,0,0)
        self.surface = pygame.Surface((800, 200))
        self.surface2 = pygame.Surface((775, 175))
        self.surface.fill(blue)
        self.surface2.fill(green)
        pygame.display.update()


    def displayText(self, screen, player, text_list):
        """Loop over all text in list, action buttons hit in between"""
        for text in text_list:
            '''function to call to make text in a rect, return surface to draw with text on it'''
            self.text_surface = self.render_textrect(text,self.font,self.text_rect,self.color,(0,0,0))
            '''Blit all surfaces to screen at different offsets'''
            screen.blit(self.surface, (0,0))
            screen.blit(self.surface2, (12, 12))
            screen.blit(self.text_surface, (25, 25))
            #screen.blit(self.font.render(text, True, (255,0,0)), (25, 25))
            #self.rect = pygame.draw.rect(self.surface, (black), (175, 75, 200, 100), 2)
            '''Event loop to wait for keydown space event and constant redrawing'''
            while True:
                pygame.display.update()
                event = pygame.event.wait()
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == KEYDOWN and event.key == K_SPACE:
                    '''Once the space bar is pressed, get the entire keyboards state'''
                    after = pygame.key.get_pressed()
                    '''Break out of first loop'''
                    break
        '''function to set player movement properly'''
        player = self.set_player_speeds(player,after)
        return screen , player

    def set_player_speeds(self,player,after):
        '''zero out players currrent movement'''
        player.xMove = 0
        player.yMove = 0
        '''depending on what keys are currently pressed, set the movement levels appropriately'''
        if after[K_w] == 1:
            player.yMove -= 4
        if after[K_s] == 1:
            player.yMove += 4
        if after[K_a] == 1:
            player.xMove -= 4
        if after[K_d] == 1:
            player.xMove += 4
        return player


    def render_textrect(self, string, font, rect, text_color, background_color, justification=0):
        """Returns a surface containing the passed text string, reformatted
        to fit within the given rect, word-wrapping as necessary. The text
        will be anti-aliased.

        Takes the following arguments:

        string - the text you wish to render. \n begins a new line.
        font - a Font object
        rect - a rectstyle giving the size of the surface requested.
        text_color - a three-byte tuple of the rgb value of the
                     text color. ex (0, 0, 0) = BLACK
        background_color - a three-byte tuple of the rgb value of the surface.
        justification - 0 (default) left-justified
                        1 horizontally centered
                        2 right-justified

        Returns the following values:

        Success - a surface object with the text rendered onto it.
        Failure - raises a TextRectException if the text won't fit onto the surface.
        """

        final_lines = []

        requested_lines = string.splitlines()

        # Create a series of lines that will fit on the provided
        # rectangle.

        for requested_line in requested_lines:
            if font.size(requested_line)[0] > rect.width:
                words = requested_line.split(' ')
                # if any of our words are too long to fit, return.
                for word in words:
                    if font.size(word)[0] >= rect.width:
                        raise TextRectException, "The word " + word + " is too long to fit in the rect passed."
                # Start a new line
                accumulated_line = ""
                for word in words:
                    test_line = accumulated_line + word + " "
                    # Build the line while the words fit.
                    if font.size(test_line)[0] < rect.width:
                        accumulated_line = test_line
                    else:
                        final_lines.append(accumulated_line)
                        accumulated_line = word + " "
                final_lines.append(accumulated_line)
            else:
                final_lines.append(requested_line)

        # Let's try to write the text out on the surface.

        surface = pygame.Surface(rect.size)
        surface.fill(background_color)

        accumulated_height = 0
        for line in final_lines:
            if accumulated_height + font.size(line)[1] >= rect.height:
                raise TextRectException, "Once word-wrapped, the text string was too tall to fit in the rect."
            if line != "":
                tempsurface = font.render(line, 1, text_color)
                if justification == 0:
                    surface.blit(tempsurface, (0, accumulated_height))
                elif justification == 1:
                    surface.blit(tempsurface, ((rect.width - tempsurface.get_width()) / 2, accumulated_height))
                elif justification == 2:
                    surface.blit(tempsurface, (rect.width - tempsurface.get_width(), accumulated_height))
                else:
                    raise TextRectException, "Invalid justification argument: " + str(justification)
            accumulated_height += font.size(line)[1]

        return surface


class TextRectException:
    def __init__(self, message=None):
        self.message = message

    def __str__(self):
        return self.message