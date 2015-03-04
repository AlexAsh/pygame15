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

        self.models = None
        self.views = None
        self.controllers = None
        self.router = None
        self.app = None

        self._setup_models()
        self._setup_views()
        self._setup_controllers()
        self._setup_router()
        self._setup_application()

    def _setup_models(self):
        """Prepare Field and Ball models by settings"""
        size = settings["models"]["size"]
        speed = settings["models"]["speed"]
        radius = settings["models"]["radius"]

        self.models = models
        self.models["Field"] = Field(size)
        self.models["Ball"] = Ball(radius, models["Field"])
        self.models["Ball"].position = map(2.0.__rdiv__, models["Field"].size)
        self.models["Ball"].speed = list(speed)

    def _setup_views(self):
        """Prepare Gameplay view by color and models"""
        color = settings["views"]["color"]

        self.views = views
        self.views["GameplayView"] = GameplayView(color, self.models)

    def _setup_controllers(self):
        """Prepare General and Mouse controllers by models, views and application"""
        self.controllers = controllers
        self.controllers["GeneralController"] = GeneralController(self.models, self.views, self)
        self.controllers["MouseController"] = MouseController()

    def _setup_router(self):
        """Prepare router by controllers"""
        self.router = Router(self.controllers)

    def _setup_application(self):
        """Setup application cycle tools"""
        self.app = {
            "play": False,
            "tick_time": settings["cycle"]["tick"],
            "frame_rate": 1000 / settings["cycle"]["tick"],
            "clock": pygame.time.Clock()

        }

    def run(self):
        """Run application main cycle"""
        self.app["play"] = True
        pygame.time.set_timer(pygame.USEREVENT, self.app["tick_time"])

        while self.app["play"]:
            for event in pygame.event.get():
                self.router.route(event)
            self.app["clock"].tick(self.app["frame_rate"])

        self._quit()

    def finish(self):
        """Finish application main cycle"""
        self.app["play"] = False

    @staticmethod
    def _quit():
        """Release pygame resources"""
        pygame.time.set_timer(pygame.USEREVENT, 0)
        pygame.quit()
