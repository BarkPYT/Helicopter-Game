#("🌲 🌊 🚁🟩 🔥 🏥 💛 💵 🧳 🏆 ⚡️⛅️🔲⬛️💧")
from utils import *

CELL_TYPES = '🟩🌲🌊🏥💵🔥'
TREE_BOONUS = 100
UPDATE_COST = 500
LIFE_COST = 1000

class Map:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for _ in range(w)] for _ in range(h)]

    def print_map(self, helico, clouds):
        print('⬛️' * (self.w + 2))
        for i in range(self.h):
            print('⬛️', end = '')
            for j in range(self.w):
                if clouds.cells[i][j] == 1:
                    print('⛅️', end='')
                elif clouds.cells[i][j] == 2:
                    print('⚡️', end='')
                elif helico.x == i and helico.y == j:
                    print('🚁', end = '')
                elif self.cells[i][j] >= 0 and self.cells[i][j] < len(CELL_TYPES):
                    print(CELL_TYPES[self.cells[i][j]], end = '')
            print('⬛️')
        print('⬛️' * (self.w + 2))

    def generate_forest(self, r, mxr):
        for i in range(self.h):
            for j in range(self.w):
                if randbool(r, mxr):
                    self.cells[i][j] = 1

    def generate_tree(self):
        c = randcells(self.w, self.h)
        cx, cy = c[0], c[1]
        if self.check_bounds(cx, cy) and self.cells[cx][cy] == 0:
            self.cells[cx][cy] = 1

    def generate_river(self, l):
        rc = randcells(self.w, self.h)
        rx, ry = rc[0], rc[1]
        self.cells[rx][ry] = 2
        while l > 0:
            rc2 = randcells2(rx, ry)
            rx2, ry2 = rc2[0], rc2[1]
            if self.check_bounds(rx2, ry2) and self.check_bounds(rx, ry):
                self.cells[rx2][ry2] = 2
                rx, ry = rx2, ry2
                l -= 1

    def add_fire(self):
        c = randcells(self.w, self.h)
        cx, cy = c[0], c[1]
        if self.check_bounds(cx, cy) and self.cells[cx][cy] == 1:
            self.cells[cx][cy] = 5

    def update_fire(self):
        for i in range(self.h):
            for j in range(self.w):
                if self.cells[i][j] == 5:
                    self.cells[i][j] = 0
        for _ in range(5):
            self.add_fire()

    def process_helicopter(self, helico, clouds):
        if self.cells[helico.x][helico.y] == 2:
            helico.tank = helico.mxtank
        elif self.cells[helico.x][helico.y] == 5 and helico.tank > 0:
            helico.score += TREE_BOONUS
            helico.tank -= 1
            self.cells[helico.x][helico.y] = 1
        elif self.cells[helico.x][helico.y] == 4 and helico.score >= UPDATE_COST:
            helico.mxtank += 1
            helico.score -= UPDATE_COST
        elif self.cells[helico.x][helico.y] == 3 and helico.score >= LIFE_COST:
            helico.lives += 10
            helico.score -= LIFE_COST
        elif clouds.cells[helico.x][helico.y] == 2:
            helico.lives -= 1
            if helico.lives == 0:
                helico.game_over()

    def generate_update_shop(self):
        c = randcells(self.w, self.h)
        cx, cy = c[0], c[1]
        self.cells[cx][cy] = 4

    def generate_hospital(self):
        c = randcells(self.w, self.h)
        cx, cy = c[0], c[1]
        if self.cells[cx][cy] != 4:
            self.cells[cx][cy] = 3
        else:
            self.generate_hospital()

    def check_bounds(self, x, y):
        if x < 0 or y < 0 or x >= self.h or y >= self.w:
            return False
        return True

    def export_data(self):
        return {'cells': self.cells}
    
    def import_data(self,data):
        self.cells = data['cells'] or [[0 for _ in range(self.w)] for _ in range(self.h)]