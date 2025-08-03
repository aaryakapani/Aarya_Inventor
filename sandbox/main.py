#!/usr/bin/env python3
"""
8-bit Zelda-like Game Framework
Main entry point for the game
"""

import pygame
import sys
from game.game_state import GameState
from game.game_engine import GameEngine
from game.constants import *

def main():
    """Main game loop"""
    pygame.init()
    pygame.display.set_caption("8-bit Adventure")
    
    # Initialize game state and engine
    game_state = GameState()
    game_engine = GameEngine(game_state)
    
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