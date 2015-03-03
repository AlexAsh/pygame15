"""Handling general application actions"""


class GeneralController:
    """Handling general user actions: quit, loosing and gaining focus"""

    def __init__(self):
        self.status = ""

    def quit(self, event):
        """Handle application quit"""
        self.status = "quit"
        return self.status

    def toggle_focus(self, event):
        """Handling focus loose and gain"""
        self.status = "toggle_focus " + str(event.gain) + " " + str(event.state)

        return self.status
