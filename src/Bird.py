import pygame, sys, random
from pygame import mixer
pygame.init()
#Lớp chim
p = 0.15    #Trọng lực
class Bird:
    def __init__(self,screen):
        #Âm thanh bay của chim
        self.wing = pygame.mixer.Sound("flappy-bird-assets-master/audio/wing.wav")
        #Âm thanh di chuyển của pointer chọn skin chim
        self.move_pointer = pygame.mixer.Sound("flappy-bird-assets-master/audio/coin.wav")
        
        #Ảnh của chim
        self.bird_mid = pygame.image.load(r"flappy-bird-assets-master\sprites\bluebird-midflap.png").convert_alpha()
        self.bird_up = pygame.image.load(r"flappy-bird-assets-master\sprites\bluebird-upflap.png").convert_alpha()
        self.bird_down = pygame.image.load(r"flappy-bird-assets-master\sprites\bluebird-downflap.png").convert_alpha()
    
        self.bird_mid = pygame.transform.scale_by(self.bird_mid, 1.2)
        self.bird_up = pygame.transform.scale_by(self.bird_up, 1.2)
        self.bird_down = pygame.transform.scale_by(self.bird_down, 1.2)
        
        self.bird_list = [self.bird_down, self.bird_mid, self.bird_down]
        self.bird_index = 0
        self.bird = self.bird_list[self.bird_index]
        self.bird_rect = self.bird.get_rect(center = (50, (614 - 134)/2))
        self.bird_y = 0  #Biến y của chim
        
        #Taọ timer cho chim
        self.bird_flap = pygame.USEREVENT + 1
        pygame.time.set_timer(self.bird_flap, 200)
        
        #Khởi tạo các đối tượng màn hình chọn skin:
        self.red_bird = pygame.image.load(r"flappy-bird-assets-master\sprites\redbird-midflap.png").convert_alpha()
        self.red_bird = pygame.transform.scale_by(self.red_bird, 1.2)
        self.redbird_rect = self.red_bird.get_rect(center = (screen.get_rect().centerx, screen.get_rect().centery))

        self.blue_bird = pygame.image.load(r"flappy-bird-assets-master\sprites\bluebird-midflap.png").convert_alpha()
        self.blue_bird = pygame.transform.scale_by(self.blue_bird, 1.2)
        self.bluebird_rect = self.blue_bird.get_rect(center = (self.redbird_rect.centerx - 100, screen.get_rect().centery))

        self.yellow_bird = pygame.image.load(r"flappy-bird-assets-master\sprites\yellowbird-midflap.png").convert_alpha()
        self.yellow_bird = pygame.transform.scale_by(self.yellow_bird, 1.2)
        self.yellowbird_rect = self.yellow_bird.get_rect(center = (self.redbird_rect.centerx + 100, screen.get_rect().centery))

        self.pointer = pygame.image.load(r"flappy-bird-assets-master\sprites\pointer.png").convert_alpha()
        self.pointer = pygame.transform.scale(self.pointer, (40,40))
        self.pointer_rect = self.pointer.get_rect(center = (screen.get_rect().centerx + 5, screen.get_rect().centery + 40))
    
    #Hàm xoay chim
    def rotate_bird(self):
        new_bird = pygame.transform.rotozoom(self.bird, self.bird_y * 3, 1)
        return new_bird
    
    #Hàm tạo animation đập cánh
    def bird_animation(self):
        new_bird = self.bird_list[self.bird_index]
        new_bird_rect = new_bird.get_rect(center = (50, self.bird_rect.centery))
        return new_bird, new_bird_rect
    
    #Hàm chim đập cánh
    def Bird_Flap(self):
        if self.bird_index < 2:
            self.bird_index += 1
        else:
            self.bird_index = 0
        self.bird, self.bird_rect = self.bird_animation()
    
    #Hàm thêm chim vào game:
    def add_bird(self,screen):
        rotated_bird = self.rotate_bird()
        screen.blit(rotated_bird, self.bird_rect)
        self.bird_y += p #y của chim tăng theo p -> bị rớt xuống
        self.bird_rect.centery += self.bird_y
    
    #Hàm vẽ màn hình chọn skin chim
    def draw_choose_skin_screen(self,screen,game_font):
        screen.blit(self.red_bird, self.redbird_rect)
        screen.blit(self.blue_bird, self.bluebird_rect)
        screen.blit(self.yellow_bird, self.yellowbird_rect)
        screen.blit(self.pointer, self.pointer_rect)
        text_surface = game_font.render('Choose skin', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center = ((screen.get_rect().centerx), 200))
        screen.blit(text_surface, text_rect)
    
    #Hàm di chuyển pointer chọn skin chim sang phải
    def move_pointer_RIGHT(self):
        if self.pointer_rect.centerx != self.yellowbird_rect.centerx + 5:
            if self.pointer_rect.centerx == self.redbird_rect.centerx + 5:
                self.pointer_rect.centerx = self.yellowbird_rect.centerx + 5
            else: self.pointer_rect.centerx = self.redbird_rect.centerx + 5
    
    #Hàm di chuyển pointer chọn skin chim sang trái
    def move_pointer_LEFT(self):
        if self.pointer_rect.centerx != self.bluebird_rect.centerx + 5:
            if self.pointer_rect.centerx == self.redbird_rect.centerx + 5:
                self.pointer_rect.centerx = self.bluebird_rect.centerx + 5
            else: self.pointer_rect.centerx = self.redbird_rect.centerx + 5
    
    #Hàm chọn chim xanh
    def choose_bluebird(self):
        self.bird_mid = pygame.image.load(r"flappy-bird-assets-master\sprites\bluebird-midflap.png").convert_alpha()
        self.bird_up = pygame.image.load(r"flappy-bird-assets-master\sprites\bluebird-upflap.png").convert_alpha()
        self.bird_down = pygame.image.load(r"flappy-bird-assets-master\sprites\bluebird-downflap.png").convert_alpha()
        
        self.bird_mid = pygame.transform.scale_by(self.bird_mid, 1.2)
        self.bird_up = pygame.transform.scale_by(self.bird_up, 1.2)
        self.bird_down = pygame.transform.scale_by(self.bird_down, 1.2)

        self.bird_list = [self.bird_down, self.bird_mid, self.bird_down]
        self.bird_index = 0
        self.bird = self.bird_list[self.bird_index]
        self.bird_rect = self.bird.get_rect(center = (50, (614 - 134)/2))
    
    #Hàm chọn chim đỏ
    def choose_redbird(self):
        self.bird_mid = pygame.image.load(r"flappy-bird-assets-master\sprites\redbird-midflap.png").convert_alpha()
        self.bird_up = pygame.image.load(r"flappy-bird-assets-master\sprites\redbird-upflap.png").convert_alpha()
        self.bird_down = pygame.image.load(r"flappy-bird-assets-master\sprites\redbird-downflap.png").convert_alpha()
        
        self.bird_mid = pygame.transform.scale_by(self.bird_mid, 1.2)
        self.bird_up = pygame.transform.scale_by(self.bird_up, 1.2)
        self.bird_down = pygame.transform.scale_by(self.bird_down, 1.2)

        self.bird_list = [self.bird_down, self.bird_mid, self.bird_down]
        self.bird_index = 0
        self.bird = self.bird_list[self.bird_index]
        self.bird_rect = self.bird.get_rect(center = (50, (614 - 134)/2))
    
    #Hàm chọn chim vàng
    def choose_yellowbird(self):
        self.bird_mid = pygame.image.load(r"flappy-bird-assets-master\sprites\yellowbird-midflap.png").convert_alpha()
        self.bird_up = pygame.image.load(r"flappy-bird-assets-master\sprites\yellowbird-upflap.png").convert_alpha()
        self.bird_down = pygame.image.load(r"flappy-bird-assets-master\sprites\yellowbird-downflap.png").convert_alpha()
        
        self.bird_mid = pygame.transform.scale_by(self.bird_mid, 1.2)                   
        self.bird_up = pygame.transform.scale_by(self.bird_up, 1.2)
        self.bird_down = pygame.transform.scale_by(self.bird_down, 1.2)

        self.bird_list = [self.bird_down, self.bird_mid, self.bird_down]
        self.bird_index = 0
        self.bird = self.bird_list[self.bird_index]
        self.bird_rect = self.bird.get_rect(center = (50, (614 - 134)/2))     
