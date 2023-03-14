import pyperclip as pc
import keyboard as kb

class MapCopier:
    def __init__(self):
        with open('t1_map_list.txt', 'r') as maplistfile:
            self.maplist = maplistfile.readlines()
        self.cur_map = 0

    def next_map(self):
        pc.copy('/map {}'.format(self.maplist[self.cur_map]))
        self.cur_map += 1

    def restart(self):
        self.cur_map = 0

    def previous_map(self):
        self.cur_map -= 1
        pc.copy('/map {}'.format(self.maplist[self.cur_map]))

if __name__=='__main__':
    copier = MapCopier()
    kb.add_hotkey('ctrl+1', copier.next_map)
    kb.add_hotkey('ctrl+2', copier.previous_map)
    kb.add_hotkey('ctrl+backspace', copier.restart)
    kb.wait()
