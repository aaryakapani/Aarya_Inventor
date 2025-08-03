"""
Main game engine that coordinates all game systems
"""

import pygame
from .constants import *
from .ui import UI

class GameEngine:
    """Main game engine that handles rendering and input"""
    
    def __init__(self, game_state):
        self.game_state = game_state
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.ui = UI()
        
    def handle_event(self, event):
        """Handle pygame events"""
        if event.type == pygame.KEYDOWN:
            self.handle_keydown(event.key)
        elif event.type == pygame.KEYUP:
            self.handle_keyup(event.key)
            
    def handle_keydown(self, key):
        """Handle key press events"""
        if self.game_state.state == STATE_PLAYING:
            if key == pygame.K_ESCAPE:
                self.game_state.change_state(STATE_PAUSED)
            elif key == pygame.K_w or key == pygame.K_UP:
                self.game_state.player.start_moving(UP)
            elif key == pygame.K_s or key == pygame.K_DOWN:
                self.game_state.player.start_moving(DOWN)
            elif key == pygame.K_a or key == pygame.K_LEFT:
                self.game_state.player.start_moving(LEFT)
            elif key == pygame.K_d or key == pygame.K_RIGHT:
                self.game_state.player.start_moving(RIGHT)
            elif key == pygame.K_SPACE:
                self.game_state.player.attack()
        elif self.game_state.state == STATE_PAUSED:
            if key == pygame.K_ESCAPE:
                self.game_state.change_state(STATE_PLAYING)
                
    def handle_keyup(self, key):
        """Handle key release events"""
        if self.game_state.state == STATE_PLAYING:
            if key in [pygame.K_w, pygame.K_UP, pygame.K_s, pygame.K_DOWN,
                      pygame.K_a, pygame.K_LEFT, pygame.K_d, pygame.K_RIGHT]:
                self.game_state.player.stop_moving()
                
    def update(self):
        """Update game logic"""
        self.game_state.update()
        
    def render(self):
        """Render the game"""
        self.screen.fill(BLACK)
        
        if self.game_state.state == STATE_PLAYING:
            # Render world with camera offset
            self.game_state.world.render(self.screen, self.game_state.camera)
            self.game_state.player.render(self.screen, self.game_state.camera)
            self.ui.render_hud(self.screen, self.game_state)
        elif self.game_state.state == STATE_PAUSED:
            self.ui.render_pause_menu(self.screen)
        elif self.game_state.state == STATE_MENU:
            self.ui.render_main_menu(self.screen)
            
        pygame.display.flip() 