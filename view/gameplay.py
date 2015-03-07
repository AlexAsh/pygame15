"""Visualizing gameplay"""
import pygame


class GameplayView:
    """Visualizing gameplay: rolling balls"""

    def __init__(self, color, models):
        self.color = color
        self.size = map(int, models["Field"].size)
        self.screen = pygame.display.set_mode(self.size)

        balls = models["Field"].balls
        img = pygame.image.load("ball.gif")
        self.balls = [None] * len(balls)

        for i in range(0, len(balls)):
            img_size = int(balls[i].radius * 2), int(balls[i].radius * 2)
            pos = map(int, balls[i].position)

            self.balls[i] = dict(image=None, rect=None, model=None)
            self.balls[i]["model"] = balls[i]
            self.balls[i]["image"] = pygame.transform.scale(img, img_size)
            self.balls[i]["rect"] = self.balls[i]["image"].get_rect(center=pos)

    def update(self):
        """Update view content"""
        self.screen.fill(self.color)
        for i in range(0, len(self.balls)):
            self.balls[i]["rect"].center = map(int, self.balls[i]["model"].position)
            self.screen.blit(
                pygame.transform.rotate(self.balls[i]["image"],
                                        int(self.balls[i]["model"].rotated)),
                self.balls[i]["rect"])
        pygame.display.flip()
