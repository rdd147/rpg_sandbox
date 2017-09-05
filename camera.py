import pygame

import monster_main

class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = pygame.Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state, self.width, self.height = self.camera_func(self.state, target.rect)


def complex_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t, _, _ = -l + monster_main.HALF_WIDTH, -t + monster_main.HALF_HEIGHT, w, h  # center player

    l = min(0, l)  # stop scrolling at the left edge
    l = max(-(camera.width - monster_main.WIN_WIDTH), l)  # stop scrolling at the right edge
    t = max(-(camera.height - monster_main.WIN_HEIGHT), t)  # stop scrolling at the bottom
    t = min(0, t)  # stop scrolling at the top

    return monster_main.Rect(l, t, w, h) , t, l