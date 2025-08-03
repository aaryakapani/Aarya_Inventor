"""
World management and tile system
"""

import pygame
from .constants import *
from .tile import Tile

class World:
    """Manages the game world, tiles, and environment"""
    
    def __init__(self):
        self.tiles = []
        self.entities = []
        self.generate_world()
        
    def generate_world(self):
        """Generate the initial world"""
        self.tiles = []
        
        # Generate a simple world with grass and some obstacles
        for y in range(MAP_HEIGHT):
            row = []
            for x in range(MAP_WIDTH):
                # Create grass tiles by default
                tile_type = "grass"
                
                # Add some water and trees for variety
                if (x == 5 and y == 5) or (x == 10 and y == 8) or (x == 15 and y == 12):
                    tile_type = "water"
                elif (x == 3 and y == 3) or (x == 8 and y == 10) or (x == 12 and y == 15):
                    tile_type = "tree"
                elif (x == 7 and y == 7) or (x == 13 and y == 13):
                    tile_type = "rock"
                    
                tile = Tile(x * TILE_SIZE, y * TILE_SIZE, tile_type)
                row.append(tile)
            self.tiles.append(row)
            
    def get_tile_at(self, x, y):
        """Get tile at world coordinates"""
        tile_x = x // TILE_SIZE
        tile_y = y // TILE_SIZE
        
        if 0 <= tile_x < MAP_WIDTH and 0 <= tile_y < MAP_HEIGHT:
            return self.tiles[tile_y][tile_x]
        return None
        
    def is_walkable(self, x, y):
        """Check if a position is walkable"""
        tile = self.get_tile_at(x, y)
        if tile:
            return tile.walkable
        return False
        
    def update(self):
        """Update world state"""
        # Update entities
        for entity in self.entities:
            entity.update()
            
    def render(self, screen, camera):
        """Render the world"""
        # Calculate visible tile range
        start_x = max(0, camera.x // TILE_SIZE)
        end_x = min(MAP_WIDTH, (camera.x + SCREEN_WIDTH) // TILE_SIZE + 1)
        start_y = max(0, camera.y // TILE_SIZE)
        end_y = min(MAP_HEIGHT, (camera.y + SCREEN_HEIGHT) // TILE_SIZE + 1)
        
        # Render visible tiles
        for y in range(start_y, end_y):
            for x in range(start_x, end_x):
                tile = self.tiles[y][x]
                tile.render(screen, camera)
                
        # Render entities
        for entity in self.entities:
            entity.render(screen, camera) 