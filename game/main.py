import pygame

white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128) 

class PlayerEntity:
    __slots__ = ["_x", "_y", "_name", "_is_blue"]
    def __init__(self, name):
        self._x, self._y, self._name = 0, 0, name
        self._is_blue = True

    def update(self, x, y):
        self._x = x
        self._y = y

    def __repr__(self):
        return "{}{}{}".format(self._x, self._y, self._name)

    def render(self, screen, time):
        font = pygame.font.Font('freesansbold.ttf', 10)
        text = font.render('{}'.format(self._name), True, green, blue)
        textRect = text.get_rect() 
        textRect.center = (self._x, self._y - 20)
        screen.blit(text, textRect)
        pygame.draw.rect(screen, blue, pygame.Rect(self._x, self._y, 60, 60))


def main():
        pygame.init()
        screen = pygame.display.set_mode((400, 300))
        done = False
        clock = pygame.time.Clock()
        p1 = PlayerEntity("marcius")
        x, y = 30, 30
        while not done:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                done = True
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                                is_blue = not is_blue
                
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_UP]: y -= 3
                if pressed[pygame.K_DOWN]: y += 3
                if pressed[pygame.K_LEFT]: x -= 3
                if pressed[pygame.K_RIGHT]: x += 3
                p1.update(x, y)
                screen.fill((0, 0, 0))
                p1.render(screen, clock)
                pygame.display.flip()
                clock.tick(60)
if __name__ == "__main__":
        main()