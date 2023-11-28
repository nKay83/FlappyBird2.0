import pygame, sys
from src.Bird import Bird
from src.PipeList import PipeList
from src.Score import Score
from src.Button import Button
from src.Floor import Floor
from pygame import mixer

window = (346, 614)

class FlappyBird:
    pygame.init()

    #Cửa sổ game
    screen = pygame.display.set_mode(window)

    #Tiêu đề game
    pygame.display.set_caption('Flappy Bird')

    #FPS game
    clock = pygame.time.Clock()

    #Các biến của game
    time_counter = 0
    p = 0.15    #Trọng lực
    start_time = pygame.time.get_ticks()
    game_font = pygame.font.Font(r'flappy-bird-assets-master\04B_19__.TTF', 40)

    #Các âm thanh game
    mixer.init()
    point = pygame.mixer.Sound("flappy-bird-assets-master/audio/point.wav")
    die = pygame.mixer.Sound("flappy-bird-assets-master/audio/die.wav")
    hit = pygame.mixer.Sound("flappy-bird-assets-master/audio/hit.wav")

    #Icon game
    icon = pygame.image.load(r"flappy-bird-assets-master\favicon.ico").convert()
    pygame.display.set_icon(icon)

    #Background game
    background = pygame.image.load(r"flappy-bird-assets-master\sprites\background-day.png").convert()
    #Chỉnh background size lớn hơn
    background = pygame.transform.scale(background, window)

    #Tạo timer
    spawn_pipe = pygame.USEREVENT
    pygame.time.set_timer(spawn_pipe, 1000)

    #Màn hình kết thúc game
    screen_over = pygame.image.load(r'flappy-bird-assets-master\sprites\gameover.png')
    screen_over = pygame.transform.scale_by(screen_over, 1.2)
    screen_over_rect = screen_over.get_rect(center = (screen.get_rect().center))

    #Màn hình bắt đầu game
    screen_start = pygame.image.load(r'flappy-bird-assets-master\sprites\message.png')
    screen_start = pygame.transform.scale_by(screen_start, 1.2)
    screen_start_rect = screen_start.get_rect(center = (window[0]/2, window[1]/2 - 100))

    #Các nút
    btn_x_pos = window[0]/2 - Button.size[0]/2
    new_game_btn = Button((btn_x_pos, window[1]/2 + 30), (255, 94, 14), "New Game", (255, 255, 255))
    continue_btn = Button((btn_x_pos, window[1]/2 + 100), (255, 94, 14), "Continue", (255, 255, 255))
    exit_btn = Button((btn_x_pos, window[1]/2 + 170), (255, 94, 14), "Quit", (255, 255, 255))
    restart_btn = Button((btn_x_pos, window[1]/2 + 100), (255, 94, 14), "Restart", (255, 255, 255))
    
    pipe_surface = pygame.image.load(r"flappy-bird-assets-master\sprites\pipe-red.png")
    pipe_surface = pygame.transform.scale_by(pipe_surface, 1.2)
    pipe_surface_rect = pipe_surface.get_rect(midtop = (500, 400))

    def __init__(self):
        self.game_play = True
        self.choose_skin = False
        self.show_start_screen = True
        self.show_choose_skin_screen = False
        self.is_day = True

    #Hàm xử lý va chạm
    def check_collision(self,bird,pipes):
        if (bird.bird_rect.bottom >= window[1] - 134):
            pygame.mixer.Sound.play(self.hit)
            return False
        for pipe in pipes:
            if bird.bird_rect.colliderect(pipe):
                pygame.mixer.Sound.play(self.hit)
                return True
        return True

    def runGame(self):
        
        #Khởi tạo chim của game
        bird = Bird(self.screen)
        pipe = PipeList()
        score = Score()
        floor = Floor()
        
        #Vòng lặp xử lí game
        while True:
            score.read_high_score('high_score.txt')

            for event in pygame.event.get():
                if event.type == pygame.QUIT or self.exit_btn.clicked:   #Event thoát game
                    pygame.quit()
                    sys.exit()
                    
                if event.type == self.spawn_pipe and self.choose_skin and self.game_play:    #Cho ống xuất hiện
                    pipe.create_pipe()
                    
                if event.type == bird.bird_flap and self.game_play:   #Chim đập cánh
                    bird.Bird_Flap()
                    
                if event.type == pygame.KEYDOWN:
                    '''if event.key == pygame.K_SPACE and self.show_start_screen:
                        self.screen_start_rect.centerx = 1000
                        self.screen_start_rect.centery = 1000
                        self.show_start_screen = False'''
                    
                    #Event bay của chim
                    if event.key == pygame.K_SPACE and self.game_play and self.choose_skin:
                        bird.bird_y = -5
                        pygame.mixer.Sound.play(bird.wing)

                    #Event di chuyển pointer chọn nút đầu game
                    if event.key == pygame.K_UP and self.show_start_screen:
                        pygame.mixer.Sound.play(bird.move_pointer)
                        bird.move_pointer_RIGHT()
                    
                    #Event di chuyển pointer chọn nút đầu game
                    if event.key == pygame.K_DOWN and self.show_start_screen:   
                        pygame.mixer.Sound.play(bird.move_pointer)
                        bird.move_pointer_LEFT()

                    #Event di chuyển pointer chọn skin chim sang phải
                    if event.key == pygame.K_RIGHT and self.choose_skin == False and self.show_start_screen == False and self.show_choose_skin_screen:
                        pygame.mixer.Sound.play(bird.move_pointer)
                        bird.move_pointer_RIGHT()
                    
                    #Event di chuyển pointer chọn skin chim sang trái
                    if event.key == pygame.K_LEFT and self.choose_skin == False and self.show_start_screen == False and self.show_choose_skin_screen:   
                        pygame.mixer.Sound.play(bird.move_pointer)
                        bird.move_pointer_LEFT()
                    
                    #Event chọn skin chim
                    if event.key == pygame.K_SPACE and self.show_choose_skin_screen:
                        if bird.pointer_rect.centerx == bird.bluebird_rect.centerx + 5: #Chọn chim xanh
                            bird.choose_bluebird()
                            self.choose_skin = True
                            self.show_choose_skin_screen = False
                        if bird.pointer_rect.centerx == bird.redbird_rect.centerx + 5:  #Chọn chim đỏ
                            bird.choose_redbird()
                            self.choose_skin = True
                            self.show_choose_skin_screen = False
                        if bird.pointer_rect.centerx == bird.yellowbird_rect.centerx + 5:   #Chọn chim vàng
                            bird.choose_yellowbird()
                            self.choose_skin = True
                            self.show_choose_skin_screen = False

            # Cập nhật thời gian
            self.time_counter += pygame.time.get_ticks() - self.start_time
            self.start_time = pygame.time.get_ticks()

            # Thay đổi background nếu đã đủ thời gian
            if self.time_counter >= 20000:
                if self.is_day:
                    self.background = pygame.image.load(r"flappy-bird-assets-master\sprites\background-night.png").convert()
                else:
                    self.background = pygame.image.load(r"flappy-bird-assets-master\sprites\background-day.png").convert()
                self.background = pygame.transform.scale(self.background, window)
                self.is_day = False
                self.time_counter = 0

            #Thêm background vào game
            self.screen.blit(self.background, (0, 0))

            #Thêm sàn    
            floor.draw_floor(self.screen)
            
            #Vẽ màn hình bắt đầu
            self.screen.blit(self.screen_start, self.screen_start_rect)

            #Vẽ các nút
            if self.show_start_screen:
                self.new_game_btn.draw(self.screen)
                self.continue_btn.draw(self.screen)
                self.exit_btn.draw(self.screen)

            #Xử lý việc ấn các nút New Game và Continue
            if self.show_start_screen and self.new_game_btn.clicked == False and self.continue_btn.clicked == False:
                if self.new_game_btn.clicked:
                    score.high_score = -1
                    score.update_hightScore()
                    self.new_game_btn.clicked = False
                elif self.continue_btn.clicked:
                    self.continue_btn.clicked = False
            if self.new_game_btn.clicked or self.continue_btn.clicked and self.show_start_screen:
                self.screen_start_rect.centerx = 1000
                self.screen_start_rect.centery = 1000
                self.show_start_screen = False

            #Vẽ màn hình chọn skin chim
            if self.choose_skin == False and self.show_start_screen == False:
                bird.draw_choose_skin_screen(self.screen,self.game_font)
                self.show_choose_skin_screen = True

            if self.game_play and self.show_start_screen == False and self.choose_skin:       
                #Thêm chim vào game:
                bird.add_bird(self.screen)
                
                #Vẽ ống
                pipe.draw_pipe(self.screen,score)
                # for i in range(10):
                # if(score.score < 1):
                # self.pipe_list_bot[i].blit(screen)
                    # self.screen.blit(self.pipe_surface, self.pipe_surface_rect)
                
                # Vẽ lại sàn
                floor.draw_floor(self.screen)
                
                #Xử lý ghi điểm
                bird_mid_pos = bird.bird_rect.x + bird.bird_rect.width / 2
                for eachPipe in pipe.pipe_list:
                    pipe_mid_pos = eachPipe.rect.x + eachPipe.rect.width / 2
                    if pipe_mid_pos <=  bird_mid_pos <=  pipe_mid_pos:
                        score.score += 0.5
                        pygame.mixer.Sound.play(self.point)
                        pipe.printlist()
                        
                #Cập nhật điểm cao nhất
                score.update_hightScore()
                #Thêm score vào màn hình
                score.score_view(self.screen,self.game_font,self.game_play)
                
                #Va chạm
                self.game_play = self.check_collision(bird,pipe.pipe_list)

            elif self.game_play == False and self.show_start_screen == False and self.choose_skin: 
                self.screen.blit(self.screen_over, self.screen_over_rect)
                score.score_view(self.screen,self.game_font,self.game_play)
                self.restart_btn.draw(self.screen)
                self.exit_btn.draw(self.screen)
                self.screen_start_rect.centerx = 1000
                self.screen_start_rect.centery = 1000

            if self.restart_btn.clicked and self.game_play == False:  #Cho phép chơi lại
                self.game_play = True
                self.restart_btn.clicked = False
                pipe.clear()
                bird.bird_y = 0
                bird.bird_rect.center = (50, (window[1] - 134)/2)
                score.score = 0
            
            pygame.display.update()
            
            #clock 120
            self.clock.tick(120)

