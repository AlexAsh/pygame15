"""Setup application"""
import pygame

from system.settings import settings

from model.field import Field
from model.ball import Ball
from model import models

from view.gameplay import GameplayView
from view import views

from controller.general import GeneralController
from controller.mouse import MouseController
from controller import controllers

from system.router import Router


class Application:
    """Setup application"""

    def __init__(self):
        pygame.init()

        self.play = False
        self._setup_models()
        self._setup_views()
        self._setup_controllers()
        self._setup_router()
        self._setup_application()

    def _setup_models(self):
        size = settings["models"]["size"]
        speed = settings["models"]["speed"]
        radius = settings["models"]["radius"]

        self.models = models
        self.models["Field"] = Field(size)
        self.models["Ball"] = Ball(radius, models["Field"])
        self.models["Ball"].position = map(2.0.__rdiv__, models["Field"].size)
        self.models["Ball"].speed = list(speed)

    def _setup_views(self):
        color = settings["views"]["color"]

        self.views = views
        self.views["GameplayView"] = GameplayView(color, self.models)

    def _setup_controllers(self):
        self.controllers = controllers
        self.controllers["GeneralController"] = GeneralController(self.models, self.views, self)
        self.controllers["MouseController"] = MouseController()

    def _setup_router(self):
        self.router = Router(self.controllers)

    def _setup_application(self):
        self.tick_time = settings["cycle"]["tick"]

        self.frame_rate = int(1000 / self.tick_time)
        self.clock = pygame.time.Clock()

    def run(self):
        """Run application main cycle"""
        self.play = True
        pygame.time.set_timer(pygame.USEREVENT, self.tick_time)

        while self.play:
            for event in pygame.event.get():
                self.router.route(event)
            self.clock.tick(self.frame_rate)

        self._quit()

    def finish(self):
        """Finish application main cycle"""
        self.play = False

    @staticmethod
    def _quit():
        pygame.time.set_timer(pygame.USEREVENT, 0)
        pygame.quit()

