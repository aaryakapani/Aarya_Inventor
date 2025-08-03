"""
Player character class
"""

import pygame
from .constants import *
from .sprite import Sprite

class Player(Sprite):
    """Player character with movement, combat, and animation"""
    
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_SIZE, PLAYER_SIZE)
        self.health = PLAYER_HEALTH
        self.max_health = PLAYER_HEALTH
        self.speed = PLAYER_SPEED
        self.direction = DOWN
        self.moving = False
        self.attacking = False
        self.attack_cooldown = 0
        self.animation_frame = 0
        self.animation_timer = 0
        
        # Movement state
        self.moving_directions = set()
        
    def start_moving(self, direction):
        """Start moving in a direction"""
        self.moving_directions.add(direction)
        self.moving = True
        self.direction = direction
        
    def stop_moving(self):
        """Stop moving"""
        self.moving_directions.clear()
        self.moving = False
        
    def attack(self):
        """Perform an attack"""
        if self.attack_cooldown <= 0:
            self.attacking = True
            self.attack_cooldown = 20  # frames
            
    def update(self):
        """Update player state"""
        # Handle movement
        if self.moving:
            dx, dy = 0, 0
            
            if UP in self.moving_directions:
                dy = -self.speed
            elif DOWN in self.moving_directions:
                dy = self.speed
            if LEFT in self.moving_directions:
                dx = -self.speed
            elif RIGHT in self.moving_directions:
                dx = self.speed
                
            self.x += dx
            self.y += dy
            
            # Keep player on screen
            self.x = max(0, min(SCREEN_WIDTH - self.width, self.x))
            self.y = max(0, min(SCREEN_HEIGHT - self.height, self.y))
            
        # Update attack cooldown
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1
        else:
            self.attacking = False
            
        # Update animation
        self.animation_timer += 1
        if self.animation_timer >= ANIMATION_SPEED:
            self.animation_timer = 0
            if self.moving:
                self.animation_frame = (self.animation_frame + 1) % 4
                
    def render(self, screen, camera):
        """Render the player"""
        # Calculate screen position with camera offset
        screen_x = self.x - camera.x
        screen_y = self.y - camera.y
        
        # Draw player as a colored rectangle (placeholder for sprites)
        color = BLUE
        if self.attacking:
            color = RED
        elif self.moving:
            color = LIGHT_BLUE
            
        pygame.draw.rect(screen, color, (screen_x, screen_y, self.width, self.height))
        
        # Draw direction indicator
        if self.direction == UP:
            pygame.draw.polygon(screen, WHITE, [(screen_x + 16, screen_y), 
                                               (screen_x + 8, screen_y + 8), 
                                               (screen_x + 24, screen_y + 8)])
        elif self.direction == DOWN:
            pygame.draw.polygon(screen, WHITE, [(screen_x + 16, screen_y + 32), 
                                               (screen_x + 8, screen_y + 24), 
                                               (screen_x + 24, screen_y + 24)])
        elif self.direction == LEFT:
            pygame.draw.polygon(screen, WHITE, [(screen_x, screen_y + 16), 
                                               (screen_x + 8, screen_y + 8), 
                                               (screen_x + 8, screen_y + 24)])
        elif self.direction == RIGHT:
            pygame.draw.polygon(screen, WHITE, [(screen_x + 32, screen_y + 16), 
                                               (screen_x + 24, screen_y + 8), 
                                               (screen_x + 24, screen_y + 24)])
        
        # Draw health bar
        health_width = (self.width * self.health) // self.max_health
        pygame.draw.rect(screen, RED, (screen_x, screen_y - 10, self.width, 5))
        pygame.draw.rect(screen, GREEN, (screen_x, screen_y - 10, health_width, 5)) 