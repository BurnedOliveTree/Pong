import pygame


class Window:
    def __init__(self, dimensions: tuple[int, int]):
        self.display = pygame.display.set_mode(dimensions)
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.background_colour = (26, 26, 64)
        pygame.display.set_caption("Pong")

    def render(self):
        self.display.fill(self.background_colour)
        pygame.display.flip()
        # pygame.display.update()
        self.clock.tick(self.fps)

    def run(self):
        shouldContinue = True

        while shouldContinue:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    shouldContinue = False

            window.render()


if __name__ == "__main__":
    pygame.init()
    window = Window((800, 600))
    window.run()
