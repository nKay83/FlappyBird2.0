import pygame
from pygame import mixer
from src.Pointer import Pointer

pygame.init()
font = pygame.font.Font(r'flappy-bird-assets-master\04B_19__.TTF', 20)
# Lớp Button
class Button:
    size = (110, 40)   #Kích thước nút
    position = (0, 0)  #Vị trí của Button 
    text = ""          #Nội dung
    rect = None        #Rectangle
    color = (0, 0, 0)  #Màu của Button
    text_color = (0, 0, 0)  #Màu của text
    clicked = False         #Button đã được click hay chưa
    pointed = False

    def __init__(self, screen, position, color, text, text_color, state, pointer_center_pos):
        self.text = text
        self.color = color
        self.text_color = text_color
        self.position = position
        self.rect = pygame.rect.Rect(self.position, self.size)
        self.clicked = False
        pointer_center_pos = (self.rect.centerx - 80, self.rect.centery)
        self.pointer = Pointer(screen, False, True, pointer_center_pos)
        self.pointed = state

    def draw(self, screen):
        the_text = font.render(self.text, True, self.text_color)
        text_rec = the_text.get_rect(center = (self.position[0] + self.size[0]/2, self.position[1] + self.size[1]/2))
        if self.hover_check():
            pygame.draw.rect(screen, (138, 51, 36), self.rect, 0, 5)
        else:
            pygame.draw.rect(screen, self.color, self.rect, 0, 5)
        pygame.draw.rect(screen, "white", self.rect, 1, 5)
        screen.blit(the_text, text_rec)
        if self.pointed:
            screen.blit(self.pointer.image, self.pointer.rect)

    def hover_check(self):
        if self.pointed:
            return True
        else: return False
    
    def click(self):
        self.clicked = True