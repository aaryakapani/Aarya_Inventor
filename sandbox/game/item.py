"""
Item system for collectibles and power-ups
"""

import pygame
from .constants import *
from .sprite import Sprite

class Item(Sprite):
    """Base class for all collectible items"""
    
    def __init__(self, x, y, item_type):
        super().__init__(x, y, 16, 16)
        self.item_type = item_type
        self.collected = False
        self.animation_timer = 0
        self.set_properties()
        
    def set_properties(self):
        """Set item properties based on type"""
        if self.item_type == "health_potion":
            self.color = RED
            self.value = 25
        elif self.item_type == "coin":
            self.color = YELLOW
            self.value = 10
        elif self.item_type == "sword":
            self.color = GRAY
            self.value = 50
        else:
            self.color = WHITE
            self.value = 1
            
    def update(self):
        """Update item animation"""
        self.animation_timer += 1
        
    def render(self, screen, camera):
        """Render the item with floating animation"""
        if self.collected:
            return
            
        screen_x = self.x - camera.x
        screen_y = self.y - camera.y
        
        # Floating animation
        float_offset = int(3 * pygame.math.sin(self.animation_timer * 0.1))
        
        # Draw item
        if self.item_type == "coin":
            # Draw coin as circle
            pygame.draw.circle(screen, self.color, 
                             (screen_x + 8, screen_y + 8 + float_offset), 6)
            pygame.draw.circle(screen, BLACK, 
                             (screen_x + 8, screen_y + 8 + float_offset), 6, 1)
        else:
            # Draw other items as rectangles
            pygame.draw.rect(screen, self.color, 
                           (screen_x, screen_y + float_offset, self.width, self.height))
            pygame.draw.rect(screen, BLACK, 
                           (screen_x, screen_y + float_offset, self.width, self.height), 1)
            
    def collect(self, player):
        """Collect the item and apply its effect"""
        if self.collected:
            return False
            
        self.collected = True
        
        if self.item_type == "health_potion":
            player.health = min(player.max_health, player.health + self.value)
        elif self.item_type == "coin":
            # Add to score (handled by game state)
            pass
        elif self.item_type == "sword":
            # Increase attack power (could be implemented)
            pass
            
        return True

class ItemManager:
    """Manages all items in the world"""
    
    def __init__(self):
        self.items = []
        
    def add_item(self, x, y, item_type):
        """Add an item to the world"""
        item = Item(x, y, item_type)
        self.items.append(item)
        
    def update(self):
        """Update all items"""
        for item in self.items:
            item.update()
            
    def render(self, screen, camera):
        """Render all items"""
        for item in self.items:
            item.render(screen, camera)
            
    def check_collisions(self, player):
        """Check for collisions between player and items"""
        collected_items = []
        for item in self.items:
            if not item.collected and player.collides_with(item):
                if item.collect(player):
                    collected_items.append(item)
        return collected_items 