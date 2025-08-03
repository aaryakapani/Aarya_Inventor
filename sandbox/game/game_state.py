"""
Game state management
"""

from .constants import *
from .player import Player
from .world import World
from .camera import Camera

class GameState:
    """Manages the overall state of the game"""
    
    def __init__(self):
        self.state = STATE_PLAYING
        self.player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.world = World()
        self.camera = Camera()
        self.score = 0
        self.level = 1
        
    def update(self):
        """Update game state"""
        if self.state == STATE_PLAYING:
            self.player.update()
            self.world.update()
            self.camera.update(self.player)
            
    def change_state(self, new_state):
        """Change the current game state"""
        self.state = new_state
        
    def reset(self):
        """Reset game state"""
        self.player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.world = World()
        self.camera = Camera()
        self.score = 0
        self.level = 1
        self.state = STATE_PLAYING 