import pygame
class Floor:
    #Floor game
    mode = pygame.display.set_mode((346, 614))
    floor = pygame.image.load(r"flappy-bird-assets-master\sprites\base.png").convert()
    floor = pygame.transform.scale(floor, (346, 134))
    def __init__(self) -> None:
        self.floor_x = 0 #Tọa độ x của floor

    #Hàm vẽ floor
    def draw_floor(self,screen):
        self.floor_x -= 1    #Biến x của floor giảm dần -> chạy sang trái
        screen.blit(self.floor, (self.floor_x, 614 - 134))
        screen.blit(self.floor, (self.floor_x + 346, 614 - 134))  #Thêm 1 floor nối tiếp cái ban đầu
        if self.floor_x == -346:     #Nếu floor đầu chạy hết (x của floor đầu ban đầu bằng 0) thì reset floor_x
            self.floor_x = 0

