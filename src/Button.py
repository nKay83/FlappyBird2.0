import pygame
from pygame import mixer

pygame.init()
font = pygame.font.Font(r'flappy-bird-assets-master\04B_19__.TTF', 20)

move_pointer = pygame.mixer.Sound("flappy-bird-assets-master/audio/coin.wav")
class Button:
    size = (110, 40)
    position = (0, 0)
    text = ""
    rect = None
    color = (0, 0, 0)
    text_color = (0, 0, 0)
    '''pointer = pygame.image.load(r"flappy-bird-assets-master\sprites\pointer.png").convert()
    pointer = pygame.transform.scale(pointer, (40,40))
    pointer = pygame.transform.flip(pointer, True, False)
    pointer = pygame.transform.rotate(pointer, 100)
    pointer_rect = pointer.get_rect(center = (0,0))'''
    pointed = False
    clicked = False

    def __init__(self, position, color, text, text_color):
        self.text = text
        self.color = color
        self.text_color = text_color
        self.position = position
        self.rect = pygame.rect.Rect(self.position, self.size)
        self.clicked = False
        if self.text == "New Game":
            self.pointed = True
        else: self.pointed = False

    def draw(self, screen):
        the_text = font.render(self.text, True, self.text_color)
        text_rec = the_text.get_rect(center = (self.position[0] + self.size[0]/2, self.position[1] + self.size[1]/2))
        if self.hover_check():
            pygame.draw.rect(screen, (138, 51, 36), self.rect, 0, 5)
        else:
            pygame.draw.rect(screen, self.color, self.rect, 0, 5)
        pygame.draw.rect(screen, "white", self.rect, 1, 5)
        screen.blit(the_text, text_rec)
        '''if self.pointed:
            pointer_rect = self.pointer.get_rect(center=(self.rect.centerx - self.size[0], self.rect.centery))
            screen.blit(self.pointer, self.pointer_rect)'''

    def hover_check(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos) and not self.clicked:
            if pygame.mouse.get_pressed()[0]:
                self.clicked = True
            return True
        else: return False
            