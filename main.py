import pyautogui, keyboard, ctypes, math, cv2, time
import numpy as np
from tkinter import Tk


user32 = ctypes.WinDLL('user32', use_last_error=True)
root = Tk()
root.withdraw()
shift_x = 7
shift_y = 151
max_cage_size = 80
screen_x = 1500
screen_y = 800


class Game:
    def __init__(self, starv_x=None, starv_y=None):
        self.bord = [[0 for _ in range(100)] for _ in range(300)]
        self.starv_x = starv_x
        self.starv_y = starv_y
        self.all_trees = []
        self.all_stones = []
        if starv_x is None or starv_y is None:
            self.check_pos()

    def check_pos(self):
        pyautogui.keyDown("o")
        time.sleep(0.03)
        pyautogui.keyUp("o")
        keyboard.write('pos')
        pyautogui.keyDown("enter")
        pyautogui.keyUp("enter")


        user32.SetCursorPos(1753, 1312)
        user32.mouse_event(0x0002)
        time.sleep(0.04)
        user32.SetCursorPos(1803, 1312)
        time.sleep(0.04)
        user32.mouse_event(0x0004)


        pyautogui.keyDown("ctrlleft")
        pyautogui.keyDown("c")
        pyautogui.keyUp("ctrlleft")
        pyautogui.keyUp("c")
        pos = root.clipboard_get()
        pyautogui.keyDown("esc")
        pyautogui.keyUp("esc")
        try:
            x, y = list(map(int, pos.split(':')))
        except Exception:
            x, y = 0, 0
        #self.bord[y][x] = 'p'
        self.starv_x = x
        self.starv_y = y

    def set_objects(self):
        with open('description_map.txt', encoding='utf8') as f:
            texts = f.read()
        trees, stones = texts.split('\n')
        trees = trees.split(';')
        stones = stones.split(';')
        for tree in trees:
            x, y, w, h = map(int, tree.split(' '))
            b_x = int((x - 51) / 102 + 0.5) + shift_x
            b_y = int((y - 51) / 102 + 0.5) + shift_y
            x, y = b_x * 102 + 51, b_y * 102 + 51
            if w > max_cage_size or h > max_cage_size:
                self.bord[b_y][b_x + 1] = 1
                self.bord[b_y - 1][b_x + 1] = 1
                self.bord[b_y - 1][b_x] = 1
                self.bord[b_y - 1][b_x - 1] = 1
                self.bord[b_y][b_x - 1] = 1
                self.bord[b_y + 1][b_x - 1] = 1
                self.bord[b_y + 1][b_x] = 1
                self.bord[b_y + 1][b_x + 1] = 1
            self.bord[b_y][b_x] = 1
            self.all_trees.append([x, y, w, h])

        for stone in stones:
            x, y, w, h = map(int, stone.split(' '))
            b_x = int((x - 51) / 102 + 0.5) + shift_x
            b_y = int((y - 51) / 102 + 0.5) + shift_y
            x, y = b_x * 102 + 51, b_y * 102 + 51
            if w > max_cage_size or h > max_cage_size:
                self.bord[b_y][b_x + 1] = 2
                self.bord[b_y - 1][b_x + 1] = 2
                self.bord[b_y - 1][b_x] = 2
                self.bord[b_y - 1][b_x - 1] = 2
                self.bord[b_y][b_x - 1] = 2
                self.bord[b_y + 1][b_x - 1] = 2
                self.bord[b_y + 1][b_x] = 2
                self.bord[b_y + 1][b_x + 1] = 2
            self.bord[b_y][b_x] = 2
            self.all_stones.append([x, y, w, h])

    def show_bord(self):
        for i in self.bord:
            for j in i:
                print(j, end='')
            print()

    def find_way(self, x1, y1, x2, y2, p_max=15, p=1, x=0, y=0, old_pos=[]):
        if p == 1:
            x, y = x1, y1

        if x < 0 or y < 0 or x > 99 or y > 299 or self.bord[y][x] != 0 or p == p_max:
            return 0

        if [x, y] in old_pos:
            return 0
        else:
            old_pos.append([x, y])

        if x == x2 and y == y2:
            return [[x, y]]

        if x2 > x:
            rez = self.find_way(x1, y1, x2, y2, p_max, p + 1, x + 1, y, old_pos)
            if rez == 0:
                if y2 > y:
                    rez = self.find_way(x1, y1, x2, y2, p_max, p + 1, x, y + 1, old_pos)
                    if rez == 0:
                        rez = self.find_way(x1, y1, x2, y2, p_max, p + 1, x, y - 1, old_pos)
                        if rez == 0:
                            rez = self.find_way(x1, y1, x2, y2, p_max, p + 1, x - 1, y, old_pos)
                else:
                    rez = self.find_way(x1, y1, x2, y2, p_max, p + 1, x, y - 1, old_pos)
                    if rez == 0:
                        rez = self.find_way(x1, y1, x2, y2, p_max, p + 1, x, y + 1, old_pos)
                        if rez == 0:
                            rez = self.find_way(x1, y1, x2, y2, p_max, p + 1, x - 1, y, old_pos)

        elif x2 == x:
            if y2 > y:
                rez = self.find_way(x1, y1, x2, y2, p_max, p + 1, x, y + 1, old_pos)
                if rez == 0:
                    rez = self.find_way(x1, y1, x2, y2, p_max, p + 1, x, y - 1, old_pos)
                    if rez == 0:
                        rez = self.find_way(x1, y1, x2, y2, p_max, p + 1, x - 1, y, old_pos)
                        if rez == 0:
                            rez = self.find_way(x1, y1, x2, y2, p_max, p + 1, x + 1, y, old_pos)
            else:
                rez = self.find_way(x1, y1, x2, y2, p_max, p + 1, x, y - 1, old_pos)
                if rez == 0:
                    rez = self.find_way(x1, y1, x2, y2, p_max, p + 1, x, y + 1, old_pos)
                    if rez == 0:
                        rez = self.find_way(x1, y1, x2, y2, p_max, p + 1, x - 1, y, old_pos)
                        if rez == 0:
                            rez = self.find_way(x1, y1, x2, y2, p_max, p + 1, x + 1, y, old_pos)

        else:
            rez = self.find_way(x1, y1, x2, y2, p_max, p + 1, x - 1, y, old_pos)
            if rez == 0:
                if y2 > y:
                    rez = self.find_way(x1, y1, x2, y2, p_max, p + 1, x, y + 1, old_pos)
                    if rez == 0:
                        rez = self.find_way(x1, y1, x2, y2, p_max, p + 1, x, y - 1, old_pos)
                        if rez == 0:
                            rez = self.find_way(x1, y1, x2, y2, p_max, p + 1, x + 1, y, old_pos)
                else:
                    rez = self.find_way(x1, y1, x2, y2, p_max, p + 1, x, y - 1, old_pos)
                    if rez == 0:
                        rez = self.find_way(x1, y1, x2, y2, p_max, p + 1, x, y + 1, old_pos)
                        if rez == 0:
                            rez = self.find_way(x1, y1, x2, y2, p_max, p + 1, x + 1, y, old_pos)
        if rez == 0:
            return 0
        else:
            rez.append([x, y])
            return rez

    def find_object(self, num_obj):
        if num_obj == 1:
            all_objects = self.all_trees
        if num_obj == 2:
            all_objects = self.all_stones
        else:
            all_objects = self.all_trees
        min_id = 0
        min_r = 99999
        for i in range(len(all_objects)):
            obj = all_objects[i]
            r = (abs(obj[0] - self.starv_x * 102) ** 2 + abs(obj[1] - self.starv_y * 102) ** 2) ** 0.5
            if r < min_r:
                min_r = r
                min_id = i
        obj = all_objects[min_id]
        x = int((obj[0] - 51) / 102 + 0.5)
        y = int((obj[1] - 51) / 102 + 0.5)
        if abs(x - self.starv_x) > abs(y - self.starv_y):
            if x > self.starv_x:
                if obj[2] > max_cage_size or obj[3] > max_cage_size:
                    x -= 2
                else:
                    x -= 1
            else:
                if obj[2] > max_cage_size or obj[3] > max_cage_size:
                    x += 2
                else:
                    x += 1
        else:
            if y > self.starv_y:
                if obj[2] > 75 or obj[3] > 75:
                    y -= 2
                else:
                    y -= 1
            else:
                if obj[2] > 75 or obj[3] > 75:
                    y += 2
                else:
                    y += 1

        return x, y

    def go_to(self, d_x=0, d_y=0):
        if d_x == 0 and d_y == 0:
            return
        if d_x != 0:
            b = 'd'
            if d_x < 0:
                b = 'a'
        elif d_y != 0:
            b = 's'
            if d_y < 0:
                b = 'w'
        d_t = (abs(d_x) + abs(d_y))
        for i in range(d_t // 3):
            pyautogui.keyDown(b)
            time.sleep(0.9789)
            pyautogui.keyUp(b)
            self.starv_x += d_x * 3
            self.starv_y += d_y * 3
        pyautogui.keyDown(b)
        time.sleep((d_t % 3) * 1 / 3)
        pyautogui.keyUp(b)
        self.starv_x += d_x
        self.starv_y += d_y

    def go_on(self, way):
        for pos in way:
            self.go_to(*pos)

    def translate_way(self, way):
        new_way = []
        way = way[::-1]
        d_x = 0
        d_y = 0
        last_x = way[0][0]
        last_y = way[0][1]
        for pos in way[1::]:
            d_x += pos[0] - last_x
            d_y += pos[1] - last_y
            if abs(d_y) == 1 and d_x != 0:
                new_way.append([d_x, 0])
                d_x = 0
            if abs(d_x) == 1 and d_y != 0:
                new_way.append([0, d_y])
                d_y = 0

            last_x = pos[0]
            last_y = pos[1]
        new_way.append([d_x, d_y])

        return new_way

    def get_object(self, id, count, additionally=1):
        x, y = self.find_object(id)
        way = self.find_way(self.starv_x, self.starv_y, x, y)
        way = self.translate_way(way)
        self.go_on(way)
        if self.bord[y][x + 1] == id:
            pyautogui.mouseDown(screen_x // 2 + 100, screen_y // 2)
        elif self.bord[y][x - 1] == id:
            pyautogui.mouseDown(screen_x // 2 - 100, screen_y // 2)
        elif self.bord[y + 1][x] == id:
            pyautogui.mouseDown(screen_x // 2, screen_y // 2 + 100)
        elif self.bord[y - 1][x] == id:
            pyautogui.mouseDown(screen_x // 2, screen_y // 2 - 100)
        time.sleep(count // 2 + additionally)
        pyautogui.mouseUp()


    def craft_sth(self, name, functions, is_cr_table=False, is_ready=False):
        if not is_ready:
            self.check_pos()
            for f, arg in functions:
                f(arg)




print('start...')
t = time.time()

game = Game(0, 0)
game.set_objects()
time.sleep(1)
#game.check_pos()
#game.show_bord()
#x, y = game.find_object(1)
#way = game.find_way(game.starv_x, game.starv_y, x, y)
#print(way)
#way = game.translate_way(way)
#print(way)
#for pos in way:
#    game.go_to(*pos)

game.go_to(-50, 0)

