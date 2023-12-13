import pygame
from pygame import mixer
from src.Pointer import Pointer

font = pygame.font.Font(r'flappy-bird-assets-master\04B_19__.TTF', 20)
# Lớp Button
class Button:
    size = (110, 40)                #Kích thước nút
    position = (0, 0)               #Vị trí của Button 
    text = ""                       #Nội dung
    rect = None                     #Rectangle
    color = (255, 94, 14)           #Màu của Button
    pointing_color = (138, 51, 36)  #Màu của button khi được trỏ tới
    text_color = (255, 255, 255)    #Màu của text
    clicked = False                 #Button đã được click hay chưa
    pointed = False                 #Button có đang được trỏ tới hay không

    def __init__(self, screen, position, text, state, pointer_center_pos):
        self.text = text
        self.position = position
        self.rect = pygame.rect.Rect(self.position, self.size)
        self.clicked = False
        pointer_center_pos = (self.rect.centerx - 80, self.rect.centery)
        self.pointer = Pointer(screen, False, True, pointer_center_pos)
        self.pointed = state

    #Vẽ nút lên màn hình
    def draw(self, screen):
        the_text = font.render(self.text, True, self.text_color)
        text_rec = the_text.get_rect(center = (self.position[0] + self.size[0]/2, self.position[1] + self.size[1]/2))
        #Nếu nút được trỏ tới thì sẽ có màu khác so với bình thường
        if self.hover_check():
            pygame.draw.rect(screen, self.pointing_color, self.rect, 0, 5)
        else:
            pygame.draw.rect(screen, self.color, self.rect, 0, 5)
        pygame.draw.rect(screen, "white", self.rect, 1, 5)
        screen.blit(the_text, text_rec)
        #Nếu nút được trỏ tới thì con trỏ của nút sẽ được vẽ cùng
        if self.pointed:
            screen.blit(self.pointer.image, self.pointer.rect)
            
    #Kiểm tra xem nút có được trỏ tới hay không
    def hover_check(self):
        if self.pointed:
            return True
        else: return False
    #Hàm nhấn nút
    def click(self):
        self.clicked = True