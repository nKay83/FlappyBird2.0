import pygame

font = pygame.font.Font(r'flappy-bird-assets-master\04B_19__.TTF', 15)
class Button:
    size = (80, 25)
    position = (0, 0)
    text = ""
    rect = None
    color = (0, 0, 0)
    text_color = (0, 0, 0)
    clicked = False

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
        self.click_check()
        pygame.draw.rect(screen, "white", self.rect, 1, 5)
        screen.blit(the_text, text_rec)

    def hover_check(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos) and not self.clicked:
            return True
        else: return False
    
    def click_check(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        if self.rect.collidepoint(mouse_pos) and not self.clicked and left_click:
            self.clicked = True




            