"""Handling mouse application actions"""


class MouseController:
    """Handling mouse application actions: press, release and move"""

    MOUSE_BUTTON_LEFT = 1

    def __init__(self, models):
        self.status = ""
        self.models = models

    def release(self, event):
        """Handle mouse button release"""
        self.status = ("mouse button release " +
                       str(event.pos) + " " +
                       str(event.button))
        if event.button == self.MOUSE_BUTTON_LEFT:
            self.models["Field"].release(map(float, event.pos))
        return self.status

    def press(self, event):
        """Handle mouse button press"""
        self.status = ("mouse button press " +
                       str(event.pos) + " " +
                       str(event.button))
        if event.button == self.MOUSE_BUTTON_LEFT:
            self.models["Field"].freeze(map(float, event.pos))
        return self.status

    def move(self, event):
        """Handle mouse move"""
        self.status = ("mouse move " +
                       str(event.pos) + " " +
                       str(event.rel) + " " +
                       str(event.buttons))
        return self.status
