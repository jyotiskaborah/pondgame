import pygame


class Fish:
    """Class for ship and methods"""
    def __init__(self, SW_game):
        """Initialize all items"""
        self.screen = SW_game.screen
        self.settings = SW_game.settings
        self.screen_rect = SW_game.screen.get_rect()


        self.image_org = pygame.image.load('images/fish.bmp')
        self.image = self.image_org
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect()

        self.facing = "left"

        self.rect.center = self.screen_rect.center

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        """Move the position according to flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.speed
            self.facing = "right"
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.speed
            self.facing = "left"
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.speed
        
        self.rect.x = self.x
        self.rect.y = self.y

        if self.facing == "left":
            self.image = self.image_org
        elif self.facing == "right":
            self.image = pygame.transform.flip(self.image_org, True, False)



    def blitme(self):
        """show the image on screen"""
        self.screen.blit(self.image, self.rect)

