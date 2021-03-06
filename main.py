import pygame
from objects import Ball, Paddle, TextLabel
from physics import MagneticField
from config import CHARGE, FPS, INDUCTION, MASS, WINDOW_SIZE


class Game:
    def __init__(self, size: tuple[int, int]):
        self.display = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()
        self.fps = FPS
        self.background_colour = (26, 26, 64)
        self.ball = Ball(self.display, (32, 32), (64, 64))
        self.paddleOne = Paddle(self.display, (20, 100), (0, 0))
        self.paddleTwo = Paddle(self.display, (20, 100), (size[0] - 20, 0))
        self.field = MagneticField(INDUCTION)
        self.score = (0, 0)
        self.score_label = TextLabel(self.display, str(self.score[0])+" : "+str(self.score[1]))
        pygame.display.set_caption("Pong")

    def render(self):
        self.display.fill(self.background_colour)
        self.score_label.draw()
        self.ball.draw()
        self.paddleOne.draw()
        self.paddleTwo.draw()
        pygame.display.update()
        self.clock.tick(self.fps)

    def set_score(self, score: int):
        if score == 0:
            return
        if score < 0:
            self.score = (self.score[0], self.score[1] + 1)
        if score > 0:
            self.score = (self.score[0] + 1, self.score[1])
        self.score_label.set_text(str(self.score[0])+" : "+str(self.score[1]))

    def run(self):
        shouldContinue = True
        self.ball.set_speed((4, 4))
        paddleSpeed = 5
        isPaused = False

        while shouldContinue:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    shouldContinue = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        isPaused = not isPaused

            if not isPaused:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_UP]:
                    self.paddleTwo.move(-paddleSpeed)
                if keys[pygame.K_DOWN]:
                    self.paddleTwo.move(paddleSpeed)
                if keys[pygame.K_w]:
                    self.paddleOne.move(-paddleSpeed)
                if keys[pygame.K_s]:
                    self.paddleOne.move(paddleSpeed)

                self.set_score(self.ball.move([self.paddleOne, self.paddleTwo]))
                self.ball.set_speed(self.field.apply(self.ball.speed, CHARGE, MASS, 1 / self.fps))
            self.render()


if __name__ == "__main__":
    pygame.init()
    game = Game(WINDOW_SIZE)
    game.run()
