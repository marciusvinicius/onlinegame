import abc
import pygame

white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128) 


class Game:
    __slots__ = ["_entities", "_context", "_clock", "done"]

    def __init__(self, entities=[]):
        self._entities = entities

    def __list__(self):
        return self._entities

    def new(self):
        self.done = False
        self._clock = pygame.time.Clock()
        self._context = pygame.display.set_mode((400, 300))

    def add(self, entitie):
        self._entities.append(entitie)

    def update(self):
        for e in self._entities:
            e.update()

    def render(self):
        self._context.fill((0, 0, 0))
        for e in self._entities:
            e.render(self._context)
            
        self._clock.tick(60)
        pygame.display.flip()
        

    def handle(self, event):
        for e in self._entities:
            e.handle(event)
            yield

    def quit(self):
        #self.network.persist(self._entities)
        self.done = True

class State:
    __slots__ = ["x", "y"]

    def __init__(self, x, y):
        self.x = x
        self.y = y


class RenderEntity(abc.ABC):
    @abc.abstractmethod
    def update(self):
        raise NotImplementedError

    @abc.abstractmethod
    def render(self, screen):
        raise NotImplementedError

    @abc.abstractmethod
    def handle(self, event):
        raise NotImplementedError


class PlayerEntity(RenderEntity):
    __slots__ = ["state", "_name", "_is_blue"]
    def __init__(self, name):
        self.state = State(100, 100)
        self._name = name
        self._is_blue = True

    def update(self): pass

    def __repr__(self):
        return "{}{}".format(self.state, self._name)

    def render(self, screen):
        font = pygame.font.Font('freesansbold.ttf', 10)
        text = font.render('{}'.format(self._name), True, green, blue)
        textRect = text.get_rect() 
        textRect.center = (self.state.x, self.state.y - 20)
        screen.blit(text, textRect)
        pygame.draw.rect(screen, blue, pygame.Rect(self.state.x, self.state.y, 60, 60))

    def handle(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pressed = pygame.key.get_pressed()
            x, y = self.state.x, self.state.y
            if pressed[pygame.K_UP]: y -= 3
            if pressed[pygame.K_DOWN]: y += 3
            if pressed[pygame.K_LEFT]: x -= 3
            if pressed[pygame.K_RIGHT]: x += 3
            self.state.x, self.state.y = x, y


class Network:
    __slots__ = ["wserver", "gsession"]
    def __init__(self):
        pass

    def sync_entity(self):
        pass

def main():
        pygame.init()
        p1 = PlayerEntity("marcius")
        game = Game()
        game.add(p1)
        game.new()
        while not game.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game.quit()
                game.handle(event)
            game.update()
            game.render()
if __name__ == "__main__":
        main()