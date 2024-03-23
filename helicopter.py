#💧
from utils import randcells
import os

class Helicopter:
    def __init__(self,w , h):
        c = randcells(w, h)
        cx, cy = c[0], c[1]
        self.x, self.y = cx, cy
        self.w, self.h = w, h
        self.tank, self.mxtank = 0, 1
        self.score = 0
        self.lives = 30

    def move(self, dx, dy):
        nx, ny = self.x + dx, self.y + dy
        if nx >= 0 and ny >= 0 and nx < self.h and ny < self.w:
            self.x,self.y = nx, ny
    def print_stats(self):
        print('💧', self.tank, '/',self.mxtank, end = ' | ')
        print('🏆', self.score, end = ' | ')
        print('💛', self.lives)

    def game_over(self):
        os.system('cls')
        print('----------------------------------------')
        print('')
        print('     GAME OVER. YOUR SCORE IS', self.score,)
        print('')
        print('----------------------------------------')
        exit(0)
    
    def export_data(self):
        return {'score:' : self.score,
        'lives' : self.lives,
        'x' : self.x,
        'y' : self.y,
        'tank': self.tank,
        'mxtank': self.mxtank}

    def import_data(self, data):
        self.x = data['x'] or 0
        self.y = data['y'] or 0
        self.lives = data['lives'] or 30
        self.score = data['score'] or 0
        self.tank = data['tank'] or 0
        self.mxtank = data['mxtank'] or 1

