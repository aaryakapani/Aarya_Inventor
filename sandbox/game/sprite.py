"""
Base sprite class for all game objects
"""

class Sprite:
    """Base class for all game sprites"""
    
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    def get_rect(self):
        """Get the sprite's rectangle for collision detection"""
        return (self.x, self.y, self.width, self.height)
        
    def collides_with(self, other):
        """Check collision with another sprite"""
        return (self.x < other.x + other.width and
                self.x + self.width > other.x and
                self.y < other.y + other.height and
                self.y + self.height > other.y) 