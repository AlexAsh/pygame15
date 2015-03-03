"""Game field logic"""


class Field:
    """Game field logic"""

    def __init__(self, size):
        self.size = map(float, size)

    def get_size(self):
        """Get field size"""
        return self.size
