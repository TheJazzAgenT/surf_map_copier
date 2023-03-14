import pyperclip as pc
import keyboard as kb


# Edit these to be the hotkeys you want
#-------------------------------------
NEXT_MAP_HOTKEY = 'ctrl+1'
PREVIOUS_MAP_HOTKEY = 'ctrl+2'
RESTART_HOTKEY = 'ctrl+backspace'
#-------------------------------------

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
    kb.add_hotkey(NEXT_MAP_HOTKEY, copier.next_map)
    kb.add_hotkey(PREVIOUS_MAP_HOTKEY, copier.previous_map)
    kb.add_hotkey(RESTART_HOTKEY, copier.restart)
    kb.wait()
