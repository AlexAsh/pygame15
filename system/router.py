"""Routing events to controller's actions"""

import pygame


class Router:
    """Resolves events to controller's actions, handling mapping table"""

    def __init__(self):
        self.mapping = {
            pygame.ACTIVEEVENT:     ("GeneralController", "toggle_focus"),
            pygame.QUIT:            ("GeneralController", "quit"),

            pygame.MOUSEBUTTONDOWN: ("MouseController",   "down"),
            pygame.MOUSEBUTTONUP:   ("MouseController",   "up"),
            pygame.MOUSEMOTION:     ("MouseController",   "move")
        }

    def route(self, event):
        """Get controller and action by event"""
        if event.type not in self.mapping:
            return None

        return self.mapping[event.type]
