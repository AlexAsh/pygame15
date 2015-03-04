"""Visualizing gameplay"""
import pygame


class GameplayView:
    """Visualizing gameplay: rolling balls"""

    def __init__(self, color, models):
        self.color = color
        self.size = map(int, models["Field"].get_size())
        self.screen = pygame.display.set_mode(self.size)
        self.ball = dict(image=None, rect=None, model=None)
        self.ball["model"] = models["Ball"]
        self.ball["image"] = pygame.transform.scale(
            pygame.image.load("ball.gif"),
            (int(self.ball["model"].radius) * 2, int(self.ball["model"].radius) * 2))
        self.ball["rect"] = self.ball["image"].get_rect(
            center=map(int, self.ball["model"].position))

    def update(self):
        """Update view content"""
        self.ball["rect"].center = map(int, self.ball["model"].position)
        self.screen.fill(self.color)
        self.screen.blit(self.ball["image"], self.ball["rect"])
        pygame.display.flip()
