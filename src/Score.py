class Score:
    score = 0   #Điểm
    high_score = 0   #Điểm cao nhất
    def __init__(self):        
        pass
    #Hàm hiện điểm
    def score_view(self,screen, game_font,game_state):
        if game_state:
            score_surface = game_font.render(f'Score: {int(self.score)}', True, (255, 255, 255))
            score_rect = score_surface.get_rect(center = ((screen.get_rect().centerx), 100))
            screen.blit(score_surface, score_rect)
        else:
            score_surface = game_font.render(f'Score: {int(self.score)}', True, (255, 255, 255))
            score_rect = score_surface.get_rect(center = ((screen.get_rect().centerx), 100))
            screen.blit(score_surface, score_rect)
            #Điểm cao nhất
            high_score_surface = game_font.render(f'High score: {int(self.high_score)}', True, (255, 255, 255))
            high_score_rect = high_score_surface.get_rect(center = ((screen.get_rect().centerx), 200 ))
            screen.blit(high_score_surface, high_score_rect)
    
    def update_hightScore(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score('high_score.txt')
    #Đọc điểm cao nhất từ file text
    def read_high_score(self,file_name):
        f = open(file_name, 'r')
        self.high_score = float(f.read())
        f.close()
    #Ghi điểm từ file text 
    def write_high_score(self,file_name):
        f = open(file_name, 'w')
        f.write(str(self.high_score))
        f.close()