"""Visualizing gameplay"""
import pygame


class GameplayView:
    """Visualizing gameplay: rolling balls"""

    def __init__(self, color, models):
        ball = models["Field"].ball
        img = pygame.image.load("ball.gif")
        radius = int(ball.radius)
        pos = map(int, ball.position)

        self.color = color
        self.size = map(int, models["Field"].size)
        self.screen = pygame.display.set_mode(self.size)

        self.ball = dict(image=None, rect=None, model=None)
        self.ball["model"] = ball
        self.ball["image"] = pygame.transform.scale(img, (radius * 2, radius * 2))
        self.ball["rect"] = self.ball["image"].get_rect(center=pos)

    def update(self):
        """Update view content"""
        self.ball["rect"].center = map(int, self.ball["model"].position)
        self.screen.fill(self.color)
        self.screen.blit(self.ball["image"], self.ball["rect"])
        pygame.display.flip()
