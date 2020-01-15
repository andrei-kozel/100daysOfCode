import pygame.camera


class Rocket():
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/rocket.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new rocket at the center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the rocket's posittion based on the movement flag"""
        # Update the rocket's center value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.rocket_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.rocket_speed_factor
        elif self.moving_up and self.rect.top > 0:
            self.centery -= self.ai_settings.rocket_speed_factor
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.rocket_speed_factor

        # Update rect object from self.center
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        """Draw the rocket at its current location"""
        self.screen.blit(self.image, self.rect)
