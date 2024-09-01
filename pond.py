# Example file showing a basic pygame "game loop"
import pygame
import sys

from settings import Settings
from fish import Fish

class Pond:
    """A class for all game component and methods"""

    def __init__(self):
        """Initialize varialbles"""
        pygame.init()
        self.settings = Settings()


        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Space War")
        self.clock = pygame.time.Clock()
        self.fish = Fish(self)        
        self.running = True
    
    def _check_events(self):
        """To check events and update variable"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    
    def _check_keydown_events(self, event):
        """Check which key is down and response"""
        if event.key == pygame.K_RIGHT:
            self.fish.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.fish.moving_left = True
        elif event.key == pygame.K_UP:
            self.fish.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.fish.moving_down = True
    
    def _check_keyup_events(self, event):
        """Check which key is up and response"""
        if event.key == pygame.K_RIGHT:
            self.fish.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.fish.moving_left = False
        elif event.key == pygame.K_UP:
            self.fish.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.fish.moving_down = False
    


            
    
    def _update_screen(self):
        """To update screen with latest component"""
        self.screen.fill(self.settings.bg_color)
        self.fish.blitme()
        pygame.display.flip()
    
    def run_game(self):
        """Main loop running repeatedly"""
        while True:
            self._check_events()
            # fill the screen with a color to wipe away anything from last frame
            self.fish.update()
            self._update_screen()
            self.clock.tick(60)  # limits FPS to 60


if __name__ == "__main__":
    sw = Pond()
    sw.run_game()