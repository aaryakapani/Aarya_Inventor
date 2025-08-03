"""
Tile system for the world
"""

import pygame
from .constants import *
from .sprite import Sprite

class Tile(Sprite):
    """Represents a single tile in the world"""
    
    def __init__(self, x, y, tile_type):
        super().__init__(x, y, TILE_SIZE, TILE_SIZE)
        self.tile_type = tile_type
        self.set_properties()
        
    def set_properties(self):
        """Set tile properties based on type"""
        if self.tile_type == "grass":
            self.color = GREEN
            self.walkable = True
        elif self.tile_type == "water":
            self.color = BLUE
            self.walkable = False
        elif self.tile_type == "tree":
            self.color = DARK_GREEN
            self.walkable = False
        elif self.tile_type == "rock":
            self.color = GRAY
            self.walkable = False
        else:
            self.color = BROWN
            self.walkable = True
            
    def render(self, screen, camera):
        """Render the tile"""
        # Calculate screen position with camera offset
        screen_x = self.x - camera.x
        screen_y = self.y - camera.y
        
        # Only render if tile is visible on screen
        if (screen_x + TILE_SIZE > 0 and screen_x < SCREEN_WIDTH and
            screen_y + TILE_SIZE > 0 and screen_y < SCREEN_HEIGHT):
            
            # Draw the tile
            pygame.draw.rect(screen, self.color, (screen_x, screen_y, TILE_SIZE, TILE_SIZE))
            
            # Draw tile border
            pygame.draw.rect(screen, BLACK, (screen_x, screen_y, TILE_SIZE, TILE_SIZE), 1)
            
            # Add some visual details based on tile type
            if self.tile_type == "grass":
                # Add some grass detail
                for i in range(3):
                    detail_x = screen_x + 5 + i * 8
                    detail_y = screen_y + 5 + i * 8
                    pygame.draw.circle(screen, DARK_GREEN, (detail_x, detail_y), 2)
            elif self.tile_type == "water":
                # Add wave effect
                wave_y = screen_y + 8 + (pygame.time.get_ticks() // 100) % 8
                pygame.draw.line(screen, LIGHT_BLUE, (screen_x, wave_y), 
                               (screen_x + TILE_SIZE, wave_y), 2)
            elif self.tile_type == "tree":
                # Draw tree trunk
                trunk_x = screen_x + TILE_SIZE // 2 - 2
                trunk_y = screen_y + TILE_SIZE // 2
                pygame.draw.rect(screen, BROWN, (trunk_x, trunk_y, 4, TILE_SIZE // 2))
            elif self.tile_type == "rock":
                # Add rock texture
                for i in range(4):
                    rock_x = screen_x + 4 + i * 6
                    rock_y = screen_y + 4 + i * 6
                    pygame.draw.circle(screen, BLACK, (rock_x, rock_y), 1) 