import pyperclip as pc
import keyboard as kb

with open('t1_map_list.txt', 'r') as maplistfile:
    maplist = maplistfile.readlines()

cur_map = 0
while True:
    kb.wait('1')
    pc.copy('/map {}'.format(maplist[cur_map]))
    cur_map += 1
    if cur_map >= len(maplist):
        break
print('goodbye')
