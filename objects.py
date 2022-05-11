import pygame


class Drawable:
    def __init__(self, size: tuple[int, int], position: tuple[int, int], colour: tuple[int, int, int] = (122, 11, 192)):
        self.size = size
        self.colour = colour
        self.surface = pygame.Surface(size, pygame.SRCALPHA)
        self.rect = self.surface.get_rect(x=position[0], y=position[1])

    def draw(self, surface: pygame.Surface):
        surface.blit(self.surface, self.rect)


class Ball(Drawable):
    def __init__(self, size: tuple[int, int], position: tuple[int, int], colour: tuple[int, int, int] = (122, 11, 192)):
        super().__init__(size, position, colour)
        pygame.draw.ellipse(self.surface, self.colour, [0, 0, self.size[0], self.size[1]])
        self.speed = (0, 0)

    def set_speed(self, speed: tuple[int, int]):
        self.speed = speed

    def move(self, surface: pygame.Surface):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]

        if self.rect.x not in range(0, (surface.get_width() - self.size[0])):
            self.speed = (-self.speed[0], self.speed[1])
        if self.rect.y not in range(0, (surface.get_height() - self.size[1])):
            self.speed = (self.speed[0], -self.speed[1])


class Paddle(Drawable):
    def __init__(self, size: tuple[int, int], position: tuple[int, int], colour: tuple[int, int, int] = (122, 11, 192)):
        super().__init__(size, position, colour)
        self.surface.fill(colour)

    def move(self, surface: pygame.Surface, speed: int):
        self.rect.y += speed
        self.rect.y = min(max(self.rect.y, 0), surface.get_height() - self.size[1])
