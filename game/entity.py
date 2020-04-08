import pygame

class PlayerEntity:
    __slots__ = ["_x", "_y", "_name", "_is_blue"]
    def __init__(self, name):
        self._x, self._y, self._name = 0, 0, name
        self._is_blue = True

    def update(self, data):
        pass

    def __repr__(self):
        return "{}{}{}".format(self._x, self._y, self._name)

    def render(self, screen, time):
        if self._is_blue: color = (0, 128, 255)
        else: color = (255, 100, 0)
        pygame.draw.rect(screen, color, pygame.Rect(self._x, self._y, 60, 60))
        print(self)