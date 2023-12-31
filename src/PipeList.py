import pygame, random
class Pipe:
    pipe_surface = pygame.image.load(r"flappy-bird-assets-master\sprites\pipe-green.png")
    pipe_surface = pygame.transform.scale_by(pipe_surface, 1.2)
    def __init__(self,pipe_pos,flagMove) -> None:
        self.flagStop = True
        self.flagMove = flagMove
        self.rect = self.pipe_surface.get_rect(midtop = (500, pipe_pos))
        self.anchor = self.rect.bottom

    def blit(self, screen):
        screen.blit(self.pipe_surface,self.rect)
    

class PipeTop(Pipe):
    def __init__(self,pipe_pos,flagMove) -> None:
        Pipe.__init__(self,pipe_pos,flagMove)
        self.pipe_surface = pygame.transform.flip(self.pipe_surface, False, True)
        self.bottomMost = 64

    
    def move_up_down(self):
        if(self.flagStop):
            self.move_down()
        else:
            self.move_up()
            
    
    def move_down(self):
        if(self.rect.bottom >= self.anchor + 30):
            self.flagStop = False
        else:
            self.rect.centery += 2

    def move_up(self):
        if(self.rect.bottom <= self.bottomMost ):
            self.flagStop = True
        else:
            self.rect.centery -= 2

class PipeBot(Pipe):
    def __init__(self,pipe_pos,flagMove) -> None:
        Pipe.__init__(self,pipe_pos,flagMove)
        self.bottomMost = 789

    def move_up_down(self):
        if(self.flagStop):
            self.move_down()
        else:
            self.move_up()
    
    def move_down(self):
        if(self.rect.bottom >= self.bottomMost ):
            self.flagStop = False
        else:
            self.rect.centery += 2

    def move_up(self):
        if(self.rect.bottom <= self.anchor - 30):
            self.flagStop = True
        else:
            self.rect.centery -= 2

    def move_up_with_anchor(self,anchor):
        if(self.rect.bottom <= anchor ):
            self.flagStop = True
        else:
            self.rect.centery -= 2


class PipeList:
    pipe_surface = pygame.image.load(r"flappy-bird-assets-master\sprites\pipe-green.png")
    pipe_surface = pygame.transform.scale_by(pipe_surface, 1.2)
    movable = False
    def __init__(self) :
        #Tạo ống
        self.pipe_list = []
        self.pipe_height = [230,255,280,305,330,355,380,405]
        # ,255,280,305,330,355,380,

    #Hàm tạo ống
    def create_pipe(self):
        random_pipePos = random.choice(self.pipe_height)
        if(not self.movable):
            self.pipe_list.append( PipeBot(random_pipePos,False))
            self.pipe_list.append(PipeTop(random_pipePos - 550,False))
        else:
            self.pipe_list.append( PipeBot(random_pipePos,self.coinflip()))
            self.pipe_list.append(PipeTop(random_pipePos - 550,self.coinflip()))

    def coinflip(self):
        return random.choice([0,1]) == 1
    
    def clear(self):
        self.pipe_list.clear()
    
    def printlist(self):
        for pipe in self.pipe_list:
            print("move: "+ str(pipe.flagMove))
        print("\n")

    #Hàm di chuyển ống
    def move_pipe_horizontally(self):
        for pipe in self.pipe_list:
            pipe.rect.centerx -= 2
    
    def move_synchronized(self, i):
        if(self.pipe_list[i].flagStop):
            self.pipe_list[i].move_down()
            self.pipe_list[i+1].rect.centery += 2
        else:
            self.pipe_list[i].move_up_with_anchor(600)
            self.pipe_list[i+1].rect.centery -= 2

    def draw_synchronized(self, i, screen):
        if(PipeBot.__instancecheck__(self.pipe_list[i])):
            self.move_synchronized(i)
            self.pipe_list[i].blit(screen)
            self.pipe_list[i+1].blit(screen)
    

    #Hàm vẽ ống
    def draw_pipe(self,screen,score):
        spacing = 0  #spacing phục vụ cho idea zic zac
        i = 0
        lvUp = 5
        self.move_pipe_horizontally()   #Important hàm luôn chạy để di chuyển ống xuất hiện sang ngang trên screen
        for pipe in self.pipe_list:
            i += 1
            if(score.score < lvUp):    #Điểm kích hoạt di chuyển ống
                pipe.blit(screen)
            elif(score.score < lvUp *2):
                # Di chuyển ống độc lập tự ống nào ống đó tự đi     ((foundation))
                # pipe.move_up_down() 
                # pipe.blit(screen)
                #Di chuyển ống random        ((done))
                self.movable = True         #((cờ hiệu cho phép pipe tạo sau sẽ random thuộc tính flagmove quyết định pipe có được di chuyển hay không))
                if(pipe.flagMove):
                    pipe.move_up_down()
                    pipe.blit(screen) 
                else:
                    pipe.blit(screen)
            elif(score.score < lvUp *3):
                #Thử di chuyển theo đường zic zac,   ((done))
                if(spacing == 3 or spacing == 0):
                    pipe.blit(screen)
                    if(spacing == 3):
                        spacing = 0
                    else:
                        spacing += 1
                else:
                    pipe.move_up_down()
                    pipe.blit(screen)
                    spacing +=1
                    
            elif(score.score < lvUp * 4):
                #Thử di chuyển cách khoảng,   ((done))
                if(spacing >= 2):
                    pipe.blit(screen)
                    if(spacing == 3):
                        spacing = 0
                    else:
                        spacing += 1
                else:
                    if(i < len(self.pipe_list)):
                        self.draw_synchronized(i,screen)
                    pipe.blit(screen)
                    spacing +=1

            else:
                break
        #Thử di chuyển ống đồng bộ trên dưới     ((done))
        while i < len(self.pipe_list):
            if(PipeBot.__instancecheck__(self.pipe_list[i])):
                self.move_synchronized(i)
                self.pipe_list[i].blit(screen)
                self.pipe_list[i+1].blit(screen)
                i += 2
            else:
                i += 1
            


           
            
    #Thử di chuyển ống đồng bộ trên dưới     ((vẫn))
    # def draw_pipe(self,screen,score,sync):
    #     i = 0
    #     while i < len(self.pipe_list):
    #         self.move_synchronized(i)
    #         i += 2

    #Code cũ
        # else:
        #     for pipe in self.move_pipex():
        #         if (pipe.rect.bottom >= 614 - 134):
        #             if(pipe.flagUp):
        #                 if(pipe.rect.bottom >= 500):
        #                     pipe.flagUp = False
        #                     print("Cong    ",pipe.rect.bottom)
        #                 pipe.rect.centery += 1
        #             else:
        #                 if(pipe.flagUp == False):
        #                     if(pipe.rect.bottom <= 480):
        #                         pipe.flagUp = True
        #                     pipe.rect.centery -= 1
        #                     print("Tru    ",pipe.rect.bottom)
        #             screen.blit(self.pipe_surface,pipe.rect)
                       
                # else:
                #     pipe.rect.centery -= 1
                    # flip_pipe = pygame.transform.flip(self.pipe_surface, False, True)
                #     screen.blit(flip_pipe, pipe)
        
        

        