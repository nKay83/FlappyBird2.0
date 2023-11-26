import pygame, random
class Pipe:
    pipe_surface = pygame.image.load(r"flappy-bird-assets-master\sprites\pipe-green.png")
    pipe_surface = pygame.transform.scale_by(pipe_surface, 1.2)
    def __init__(self,pipe_pos) -> None:
        self.flagStop = True
        self.flagUp = True
        self.rect = self.pipe_surface.get_rect(midtop = (500, pipe_pos))
        self.anchor = self.rect.bottom

    def blit(self, screen):
        screen.blit(self.pipe_surface,self.rect)
    

class PipeTop(Pipe):
    def __init__(self,pipe_pos) -> None:
        Pipe.__init__(self,pipe_pos)
        self.pipe_surface = pygame.transform.flip(self.pipe_surface, False, True)

    
    def move_up_down(self):
        if(self.flagStop):
            if(self.rect.bottom <= 64 + self.anchor * 3/10):
                self.flagStop = False
            else:
                self.rect.centery -= 2
        else:
            if(self.rect.bottom > self.anchor):
                self.flagStop = True
            else:
                self.rect.centery += 2

class PipeBot(Pipe):
    def __init__(self,pipe_pos) -> None:
        Pipe.__init__(self,pipe_pos)

    def move_up_down(self):
        if(self.flagStop):
            if(self.rect.bottom >= 789):
                self.flagStop = False
            else:
                self.rect.centery += 2
        else:
            if(self.rect.bottom < self.anchor):
                self.flagStop = True
            else:
                self.rect.centery -= 2

    
class PipeList:
    pipe_surface = pygame.image.load(r"flappy-bird-assets-master\sprites\pipe-green.png")
    pipe_surface = pygame.transform.scale_by(pipe_surface, 1.2)
    def __init__(self) :
        #Tạo ống
        self.pipe_list = []
        self.pipe_height = [230,255,280,305,330,355,380,405]
        # ,255,280,305,330,355,380,

    #Hàm tạo ống
    def create_pipe(self):
        random_pipePos = random.choice(self.pipe_height)
        self.pipe_list.append( PipeBot(random_pipePos))
        self.pipe_list.append(PipeTop(random_pipePos - 550))

    def clear(self):
        self.pipe_list.clear()
    
    def printlist(self):
        for pipe in self.pipe_list:
            print("Top: "+ str(pipe.rect.top) + "Bot: " + str(pipe.rect.bottom))
        print("\n")

    #Hàm di chuyển ống
    def move_pipex(self):
        for pipe in self.pipe_list:
            pipe.rect.centerx -= 2
    
    def move_pipey_in(self):
        i = 0
        for pipe in self.pipe_list_top:
            if(pipe.flagStop):
                if(pipe.rect.bottom <= 34):
                    pipe.flagStop = False
                else:
                    pipe.rect.centery -= 2
            else:
                if(pipe.rect.bottom ):
                    pipe.flagStop = True
                else:
                    pipe.rect.centery += 2
        return self.pipe_list
    
    #Hàm vẽ ống
    def draw_pipe(self,screen,score):
        self.move_pipex()
        for pipe in self.pipe_list:
            if(score.score < 1):
                pipe.blit(screen)
            else:
                pipe.move_up_down()
                pipe.blit(screen)
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
        
        

        