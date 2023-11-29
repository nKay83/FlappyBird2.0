import pygame
from pygame import mixer

class Pointer:
    def __init__(self, screen, bird_pointer, btn_pointer, center_pos):
        #Ảnh của pointer
        self.image = pygame.image.load(r"flappy-bird-assets-master\sprites\pointer.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (40,40))
        if bird_pointer:
            self.rect = self.image.get_rect(center=center_pos)
        elif btn_pointer:
            self.image = pygame.transform.flip(self.image, True, False)
            self.rect = self.image.get_rect(center=center_pos)
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)