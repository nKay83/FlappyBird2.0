import pygame
from pygame import mixer

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

    def __init__(self, position, color, text, text_color):
        self.text = text
        self.color = color
        self.text_color = text_color
        self.position = position
        self.rect = pygame.rect.Rect(self.position, self.size)
        self.clicked = False

    def draw(self, screen):
        the_text = font.render(self.text, True, self.text_color)
        text_rec = the_text.get_rect(center = (self.position[0] + self.size[0]/2, self.position[1] + self.size[1]/2))
        if self.hover_check():
            pygame.draw.rect(screen, (138, 51, 36), self.rect, 0, 5)
        else:
            pygame.draw.rect(screen, self.color, self.rect, 0, 5)
        pygame.draw.rect(screen, "white", self.rect, 1, 5)
        screen.blit(the_text, text_rec)

    def hover_check(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos) and not self.clicked:
            if pygame.mouse.get_pressed()[0]:
                self.clicked = True
            return True
        else: return False
            