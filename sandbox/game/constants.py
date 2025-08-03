"""
Game constants and configuration
"""

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors (8-bit palette)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BROWN = (139, 69, 19)
GRAY = (128, 128, 128)
DARK_GREEN = (0, 100, 0)
LIGHT_BLUE = (173, 216, 230)

# Player settings
PLAYER_SPEED = 3
PLAYER_SIZE = 32
PLAYER_HEALTH = 100

# Tile settings
TILE_SIZE = 32
MAP_WIDTH = 25  # tiles
MAP_HEIGHT = 19  # tiles

# Game states
STATE_MENU = "menu"
STATE_PLAYING = "playing"
STATE_PAUSED = "paused"
STATE_GAME_OVER = "game_over"

# Direction constants
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

# Animation settings
ANIMATION_SPEED = 8  # frames per animation cycle 