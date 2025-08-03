"""
Example enemy class to demonstrate framework extension
"""

import pygame
import random
from .constants import *
from .sprite import Sprite

class Enemy(Sprite):
    """Basic enemy class with simple AI"""
    
    def __init__(self, x, y, enemy_type="basic"):
        super().__init__(x, y, 32, 32)
        self.enemy_type = enemy_type
        self.health = 50
        self.max_health = 50
        self.speed = 1
        self.direction = random.randint(0, 3)
        self.move_timer = 0
        self.move_duration = 60  # frames
        
        # Set properties based on enemy type
        if enemy_type == "fast":
            self.speed = 2
            self.health = 30
        elif enemy_type == "tank":
            self.speed = 0.5
            self.health = 100
            
    def update(self):
        """Update enemy AI and movement"""
        self.move_timer += 1
        
        # Change direction periodically
        if self.move_timer >= self.move_duration:
            self.direction = random.randint(0, 3)
            self.move_timer = 0
            
        # Move in current direction
        dx, dy = 0, 0
        if self.direction == UP:
            dy = -self.speed
        elif self.direction == DOWN:
            dy = self.speed
        elif self.direction == LEFT:
            dx = -self.speed
        elif self.direction == RIGHT:
            dx = self.speed
            
        self.x += dx
        self.y += dy
        
        # Keep enemy within world bounds
        self.x = max(0, min(MAP_WIDTH * TILE_SIZE - self.width, self.x))
        self.y = max(0, min(MAP_HEIGHT * TILE_SIZE - self.height, self.y))
        
    def render(self, screen, camera):
        """Render the enemy"""
        screen_x = self.x - camera.x
        screen_y = self.y - camera.y
        
        # Choose color based on enemy type
        if self.enemy_type == "fast":
            color = YELLOW
        elif self.enemy_type == "tank":
            color = GRAY
        else:
            color = RED
            
        # Draw enemy
        pygame.draw.rect(screen, color, (screen_x, screen_y, self.width, self.height))
        
        # Draw health bar
        health_width = (self.width * self.health) // self.max_health
        pygame.draw.rect(screen, RED, (screen_x, screen_y - 10, self.width, 5))
        pygame.draw.rect(screen, GREEN, (screen_x, screen_y - 10, health_width, 5))
        
    def take_damage(self, damage):
        """Take damage from player attack"""
        self.health -= damage
        return self.health <= 0  # Return True if enemy is defeated 