#!/usr/bin/env python3
"""
Demo script showing how to extend the game framework
with enemies and items
"""

import pygame
import sys
from game.game_state import GameState
from game.game_engine import GameEngine
from game.enemy import Enemy
from game.item import ItemManager
from game.constants import *

class DemoGameState(GameState):
    """Extended game state with enemies and items"""
    
    def __init__(self):
        super().__init__()
        self.enemies = []
        self.item_manager = ItemManager()
        self.setup_demo()
        
    def setup_demo(self):
        """Setup demo enemies and items"""
        # Add some enemies
        self.enemies.append(Enemy(200, 200, "basic"))
        self.enemies.append(Enemy(400, 300, "fast"))
        self.enemies.append(Enemy(600, 400, "tank"))
        
        # Add some items
        self.item_manager.add_item(150, 150, "coin")
        self.item_manager.add_item(350, 250, "health_potion")
        self.item_manager.add_item(550, 350, "sword")
        
    def update(self):
        """Update game state with enemies and items"""
        super().update()
        
        # Update enemies
        for enemy in self.enemies:
            enemy.update()
            
        # Update items
        self.item_manager.update()
        
        # Check item collisions
        collected = self.item_manager.check_collisions(self.player)
        for item in collected:
            if item.item_type == "coin":
                self.score += item.value
                
    def render(self, screen, camera):
        """Render world with enemies and items"""
        # Render world and player (handled by parent)
        super().render(screen, camera)
        
        # Render enemies
        for enemy in self.enemies:
            enemy.render(screen, camera)
            
        # Render items
        self.item_manager.render(screen, camera)

class DemoGameEngine(GameEngine):
    """Extended game engine for demo"""
    
    def __init__(self, game_state):
        super().__init__(game_state)
        
    def render(self):
        """Render the demo game"""
        self.screen.fill(BLACK)
        
        if self.game_state.state == STATE_PLAYING:
            # Render world with camera offset
            self.game_state.world.render(self.screen, self.game_state.camera)
            self.game_state.player.render(self.screen, self.game_state.camera)
            
            # Render enemies and items
            for enemy in self.game_state.enemies:
                enemy.render(self.screen, self.game_state.camera)
            self.game_state.item_manager.render(self.screen, self.game_state.camera)
            
            self.ui.render_hud(self.screen, self.game_state)
        elif self.game_state.state == STATE_PAUSED:
            self.ui.render_pause_menu(self.screen)
            
        pygame.display.flip()

def main():
    """Demo main function"""
    pygame.init()
    pygame.display.set_caption("8-bit Adventure - Demo")
    
    # Initialize demo game state and engine
    game_state = DemoGameState()
    game_engine = DemoGameEngine(game_state)
    
    # Main game loop
    running = True
    clock = pygame.time.Clock()
    
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            game_engine.handle_event(event)
        
        # Update game state
        game_engine.update()
        
        # Render everything
        game_engine.render()
        
        # Cap the frame rate
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main() 