"""
User interface system
"""

import pygame
from .constants import *

class UI:
    """Handles all user interface elements"""
    
    def __init__(self):
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        
    def render_hud(self, screen, game_state):
        """Render the heads-up display"""
        # Health bar
        health_text = f"Health: {game_state.player.health}/{game_state.player.max_health}"
        health_surface = self.small_font.render(health_text, True, WHITE)
        screen.blit(health_surface, (10, 10))
        
        # Score
        score_text = f"Score: {game_state.score}"
        score_surface = self.small_font.render(score_text, True, WHITE)
        screen.blit(score_surface, (10, 35))
        
        # Level
        level_text = f"Level: {game_state.level}"
        level_surface = self.small_font.render(level_text, True, WHITE)
        screen.blit(level_surface, (10, 60))
        
        # Controls hint
        controls_text = "WASD: Move | SPACE: Attack | ESC: Pause"
        controls_surface = self.small_font.render(controls_text, True, WHITE)
        screen.blit(controls_surface, (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 30))
        
    def render_pause_menu(self, screen):
        """Render the pause menu"""
        # Semi-transparent overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(128)
        overlay.fill(BLACK)
        screen.blit(overlay, (0, 0))
        
        # Pause text
        pause_text = "PAUSED"
        pause_surface = self.font.render(pause_text, True, WHITE)
        pause_rect = pause_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        screen.blit(pause_surface, pause_rect)
        
        # Instructions
        resume_text = "Press ESC to resume"
        resume_surface = self.small_font.render(resume_text, True, WHITE)
        resume_rect = resume_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20))
        screen.blit(resume_surface, resume_rect)
        
    def render_main_menu(self, screen):
        """Render the main menu"""
        # Title
        title_text = "8-bit Adventure"
        title_surface = self.font.render(title_text, True, WHITE)
        title_rect = title_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100))
        screen.blit(title_surface, title_rect)
        
        # Menu options
        options = ["Start Game", "Options", "Quit"]
        for i, option in enumerate(options):
            option_surface = self.small_font.render(option, True, WHITE)
            option_rect = option_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + i * 40))
            screen.blit(option_surface, option_rect)
            
    def render_game_over(self, screen, game_state):
        """Render the game over screen"""
        # Game over text
        game_over_text = "GAME OVER"
        game_over_surface = self.font.render(game_over_text, True, RED)
        game_over_rect = game_over_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        screen.blit(game_over_surface, game_over_rect)
        
        # Final score
        final_score_text = f"Final Score: {game_state.score}"
        final_score_surface = self.small_font.render(final_score_text, True, WHITE)
        final_score_rect = final_score_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(final_score_surface, final_score_rect)
        
        # Restart instruction
        restart_text = "Press R to restart"
        restart_surface = self.small_font.render(restart_text, True, WHITE)
        restart_rect = restart_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
        screen.blit(restart_surface, restart_rect) 