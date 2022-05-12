import pygame


class Drawable:
    def __init__(self, window: pygame.Surface, size: tuple[int, int], position: tuple[int, int], colour: tuple[int, int, int] = (122, 11, 192)):
        self.window = window
        self.size = size
        self.colour = colour
        self.surface = pygame.Surface(size, pygame.SRCALPHA)
        self.rect = self.surface.get_rect(x=position[0], y=position[1])

    def draw(self):
        self.window.blit(self.surface, self.rect)


class Paddle(Drawable):
    def __init__(self, window: pygame.Surface, size: tuple[int, int], position: tuple[int, int], colour: tuple[int, int, int] = (250, 88, 182)):
        super().__init__(window, size, position, colour)
        self.surface.fill(colour)

    def move(self, speed: int):
        self.rect.y += speed
        self.rect.y = min(max(self.rect.y, 0), self.window.get_height() - self.size[1])


class Ball(Drawable):
    def __init__(self, window: pygame.Surface, size: tuple[int, int], position: tuple[int, int], colour: tuple[int, int, int] = (250, 88, 182)):
        super().__init__(window, size, position, colour)
        pygame.draw.ellipse(self.surface, self.colour, [0, 0, self.size[0], self.size[1]])
        self.speed = (0, 0)

    def set_speed(self, speed: tuple[int, int]):
        self.speed = speed

    def move(self, paddles: list[Paddle]) -> int:
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]

        if self.rect.x not in range(0, (self.window.get_width() - self.size[0])):
            self.speed = (-self.speed[0], self.speed[1])
            if self.rect.x <= 0:
                return -1
            if self.rect.x >= (self.window.get_width() - self.size[0]):
                return 1
        if self.rect.y not in range(0, (self.window.get_height() - self.size[1])):
            self.speed = (self.speed[0], -self.speed[1])
        for paddle in paddles:
            if self.rect.colliderect(paddle.rect):
                self.speed = (-self.speed[0], self.speed[1])
        return 0


class TextLabel(Drawable):
    def __init__(self, window: pygame.Surface, text: str, size: tuple[int, int] = None, position: tuple[int, int] = None, colour: tuple[int, int, int] = (122, 11, 192), font_size: int = 200):
        super().__init__(window, size if size is not None else (0, 0), position if position is not None else (0, 0), colour)
        self.text = text
        self.font = pygame.font.Font(None, font_size)
        self.surface = self.font.render(self.text, True, self.colour)
        if position is None:
            self.rect.x = self.window.get_width() // 2 - self.surface.get_width() // 2
            self.rect.y = self.window.get_height() // 2 - self.surface.get_height() // 2

    def set_text(self, text):
        self.text = text
        self.surface = self.font.render(text, True, self.colour)
