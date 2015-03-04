"""Routing events to controller's actions"""

import pygame


class Router:
    """Resolves events to controller's actions, handling mapping table"""

    def __init__(self, controllers):
        self.controllers = controllers
        self.mapping = {
            pygame.ACTIVEEVENT: ("GeneralController", "toggle_focus"),
            pygame.USEREVENT:   ("GeneralController", "tick"),
            pygame.QUIT:        ("GeneralController", "quit"),

            pygame.MOUSEBUTTONDOWN: ("MouseController",   "down"),
            pygame.MOUSEBUTTONUP:   ("MouseController",   "up"),
            pygame.MOUSEMOTION:     ("MouseController",   "move")
        }

    def route(self, event):
        """Get controller and action by event"""
        if event.type in self.mapping:
            route = self.mapping[event.type]
            getattr(self.controllers[route[0]], route[1])(event)
