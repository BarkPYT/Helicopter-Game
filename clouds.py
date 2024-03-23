from utils import randbool
#0 ничего
#1 обычные облака
#2 грозовые облака
class Clouds:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for _ in range(w)] for _ in range(h)]

    def update(self, r = 1, rw = 20, g = 1, gw = 10):
        for i in range(self.h):
            for j in range(self.w):
                if randbool(r, rw):
                    self.cells[i][j] = 1
                    if randbool(g, gw):
                        self.cells[i][j] = 2
                else:
                    self.cells[i][j] = 0
                
    def export_data(self):
        return {'cells': self.cells}
    
    def import_data(self,data):
        self.cells = data['cells'] or [[0 for _ in range(self.w)] for _ in range(self.h)]