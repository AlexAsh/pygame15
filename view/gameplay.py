"""Visualizing gameplay"""
import pygame


class GameplayView:
    """Visualizing gameplay: rolling balls"""

    def __init__(self, color, field):
        self.color = color
        self.size = map(int, field.get_size())
        self.screen = pygame.display.set_mode(self.size)

    def update(self):
        """Update view content"""
        self.screen.fill(self.color)
        pygame.display.flip()
