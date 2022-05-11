from turtle import back
import pygame
from objects import Ball, Paddle


class Game:
    def __init__(self, size: tuple[int, int]):
        self.display = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.background_colour = (26, 26, 64)
        self.ball = Ball((32, 32), (64, 64))
        self.paddleOne = Paddle((10, 100), (10, 10))
        self.paddleTwo = Paddle((10, 100), (size[0] - 20, 10))
        pygame.display.set_caption("Pong")

    def render(self):
        self.display.fill(self.background_colour)
        self.ball.draw(self.display)
        self.paddleOne.draw(self.display)
        self.paddleTwo.draw(self.display)
        pygame.display.update()
        self.clock.tick(self.fps)

    def run(self):
        shouldContinue = True
        self.ball.set_speed((1, 1))

        while shouldContinue:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    shouldContinue = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.paddleOne.move(self.display, -5)
            if keys[pygame.K_DOWN]:
                self.paddleOne.move(self.display, 5)
            if keys[pygame.K_w]:
                self.paddleTwo.move(self.display, -5)
            if keys[pygame.K_s]:
                self.paddleTwo.move(self.display, 5)

            self.ball.move(self.display)
            self.render()


if __name__ == "__main__":
    pygame.init()
    game = Game((800, 600))
    game.run()
