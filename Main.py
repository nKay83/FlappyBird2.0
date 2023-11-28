from src.Game import FlappyBird
class Main:
    def __init__(self) -> None:
        pass
    
    def run():
        game = FlappyBird()
        game.runGame()

Main.run()

'''self.bird_mid = pygame.image.load(r"flappy-bird-assets-master\sprites\bluebird-midflap.png").convert_alpha()
        self.bird_up = pygame.image.load(r"flappy-bird-assets-master\sprites\bluebird-upflap.png").convert_alpha()
        self.bird_down = pygame.image.load(r"flappy-bird-assets-master\sprites\bluebird-downflap.png").convert_alpha()
        
        self.bird_mid = pygame.transform.scale_by(self.bird_mid, 1.2)
        self.bird_up = pygame.transform.scale_by(self.bird_up, 1.2)
        self.bird_down = pygame.transform.scale_by(self.bird_down, 1.2)

        self.bird_list = [self.bird_down, self.bird_mid, self.bird_down]
        self.bird_index = 0
        self.bird = self.bird_list[self.bird_index]
        self.bird_rect = self.bird.get_rect(center = (50, (614 - 134)/2))'''