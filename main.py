from turtle import back
import pygame
from objects import Ball


class Game:
    def __init__(self, size: tuple[int, int]):
        self.display = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.background_colour = (26, 26, 64)
        self.ball = Ball((32, 32), (64, 64))
        pygame.display.set_caption("Pong")

    def render(self):
        self.display.fill(self.background_colour)
        self.ball.draw(self.display)
        # pygame.display.flip()
        pygame.display.update()
        self.clock.tick(self.fps)

    def run(self):
        shouldContinue = True
        self.ball.set_speed((1, 1))

        while shouldContinue:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    shouldContinue = False
            self.ball.move(self.display)
            self.render()


if __name__ == "__main__":
    pygame.init()
    game = Game((800, 600))
    game.run()
