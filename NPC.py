from player import Human
from text_box import *
class Npc(Human):

    def __init__(self, centerPoint, image, **kwargs):
        Human.__init__(self, centerPoint, image)
        for key, value in kwargs.items():
            if key == 'talk_text':
                self.talk_text = value

    def script(self):
        return self.talk_text
