from random import randint

def randbool(r, mxr):
    t = randint(0, mxr)
    return (t <= r)

def randcells(w, h):
    tw = randint(0, w - 1)
    th = randint(0, h - 1)
    return tw, th

#0 - up, 1 - right, 2 - left, 3 - down
def randcells2(x, y):
    moves = [(-1, 0), (0, 1), (0, -1), (1, 0)]
    t = randint(0, 3)
    dx, dy = moves[t][0], moves[t][1]
    return x + dx, y + dy
