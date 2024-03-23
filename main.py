from map import Map
from helicopter import Helicopter
from clouds import Clouds
import time
import os
from pynput import keyboard
import json

TIME_SLEEP = 0.05
TREE_UPDATE = 50
FIRE_UPDATE = 100
MAP_W, MAP_H = 10, 10
CLOUDS_UPDATE = 150

clouds = Clouds(MAP_W, MAP_H)

helico = Helicopter(MAP_W, MAP_H)

game_map = Map(MAP_W, MAP_H)

game_map.generate_forest(3, 10)
game_map.generate_river(25)
game_map.generate_update_shop()
game_map.generate_hospital()

MOVES = {'w': (-1, 0), 'd': (0, 1), 's': (1, 0), 'a': (0, -1)}

def process_key(key):
    global game_map, clouds, helico, tick
    c = key.char.lower()
    if c in MOVES.keys():
        helico.move(MOVES[c][0], MOVES[c][1])
    if c == 'c':
        data = {'helicopter': helico.export_data(),
                'map' : game_map.export_data(),
                'clouds' : clouds.export_data(),
                'tick': tick}
        with open('level.json', 'w') as lvl:
            json.dump(data, lvl)
    if c == 'v':
        with open('level.json', 'r') as lvl:
            data = json.load(lvl)
            tick = data['tick']
            game_map.import_data(data['map'])
            clouds.import_data(data['clouds'])
            helico.import_data(data['helicopter'])
    else:
        None

listener = keyboard.Listener(on_release=process_key)
listener.start()


tick = 1

while 1:
    os.system('cls')
    print('TICK= ', tick)
    game_map.process_helicopter(helico, clouds)
    helico.print_stats()
    game_map.print_map(helico, clouds)
    tick += 1
    time.sleep(TIME_SLEEP)
    if tick % TREE_UPDATE == 0:
        game_map.generate_tree()
    if tick % FIRE_UPDATE == 0:
        game_map.update_fire()
    if tick % CLOUDS_UPDATE == 0:
        clouds.update()