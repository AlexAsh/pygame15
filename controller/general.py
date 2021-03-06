"""Handling general application actions"""


class GeneralController:
    """Handling general user actions: quit, loosing and gaining focus"""

    def __init__(self, models, views, app):
        self.status = ""
        self.models = models
        self.views = views
        self.app = app

    def quit(self, event):
        """Handle application quit"""
        self.status = "quit " + str(event.type)
        self.app.finish()
        return self.status

    def toggle_focus(self, event):
        """Handle focus loose and gain"""
        self.status = "toggle_focus " + str(event.gain) + " " + str(event.state)
        return self.status

    def tick(self, event):
        """Handle clock tick"""
        self.status = "tick " + str(event.code)
        self.models["Field"].motion()
        self.views["GameplayView"].update()
        return self.status
