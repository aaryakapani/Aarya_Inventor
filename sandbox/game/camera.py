"""
Camera system for following the player and managing the viewport
"""

from .constants import *

class Camera:
    """Camera that follows the player and manages the viewport"""
    
    def __init__(self):
        self.x = 0
        self.y = 0
        self.target_x = 0
        self.target_y = 0
        
    def update(self, player):
        """Update camera position to follow the player"""
        # Center the camera on the player
        self.target_x = player.x - SCREEN_WIDTH // 2
        self.target_y = player.y - SCREEN_HEIGHT // 2
        
        # Smooth camera movement (optional)
        self.x = self.target_x
        self.y = self.target_y
        
        # Keep camera within world bounds
        max_x = MAP_WIDTH * TILE_SIZE - SCREEN_WIDTH
        max_y = MAP_HEIGHT * TILE_SIZE - SCREEN_HEIGHT
        
        self.x = max(0, min(self.x, max_x))
        self.y = max(0, min(self.y, max_y)) 