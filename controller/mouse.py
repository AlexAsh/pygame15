"""Handling mouse application actions"""


class MouseController:
    """Handling mouse application actions: press, release and move"""

    def __init__(self):
        self.status = ""

    def release(self, event):
        """Handle mouse button release"""
        self.status = ("mouse button release " +
                       str(event.pos) + " " +
                       str(event.button))
        return self.status

    def press(self, event):
        """Handle mouse button press"""
        self.status = ("mouse button press " +
                       str(event.pos) + " " +
                       str(event.button))
        return self.status

    def move(self, event):
        """Handle mouse move"""
        self.status = ("mouse move " +
                       str(event.pos) + " " +
                       str(event.rel) + " " +
                       str(event.buttons))
        return self.status
