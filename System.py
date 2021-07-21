import pygame
import time, time, copy, random
import sqlite3
from images.images import *

pygame.init()

WHITE = (255, 255, 255)  # установка цветов
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 0, 255)
LIGHT_GREEN = (27, 65, 16)
BROWN = (74, 47, 4)
GRAY = (128, 128, 128)

width, height = 0, 0


def install_size(size):  # инициализация
    global width, height
    width, height = size


def open_file():  # открывает файл с сохранением игрока
    with open('data/SaveGame.txt', 'r') as f:
        read_data = f.read()
    return read_data


def change_parametrs(id):  # нужно для заполнения карты

    # id;(x,y);количество макс. поисков;радиация;множитель скорости
    # id:количество:износ; и повторять так же     это то что можно найти
    # ????????????    это то кто может напасть
    # id:количество:износ; и повторять так же     это то что лежит на локации
    if id[0] == 0:
        parametrs = '''0;(x,y);0;-1;1
            NONE
            NONE
            NONE'''
    elif id[0] == 1:
        parametrs = '''1;(x,y);1000;0;0.05
            1:10000:0
            NONE
            NONE'''
    elif id[0] == 2:
        parametrs = '''2;(x,y);15;0;0.90
                    2:75:0;3:15:0;70:10:0;1:2:0
                    NONE
                    NONE'''
    elif id[0] == 3:
        parametrs = '''3;(x,y);20;0;0.70
            2:80:0;3:20:0;70:40:0
            NONE
            NONE'''
    elif id[0] == 4:
        parametrs = '''4;(x,y);20;0;0.90
            70:15:0;3:20:0;71:140:0
            NONE
            NONE'''
    elif id[0] == 5:
        parametrs = '''5;(x,y);5;0;1
            70:5:0;3:1:0;71:5:0
            NONE
            NONE'''
    elif id[0] == 6:
        parametrs = '''6;(x,y);0;1;0.85
            2:75:0;3:15:0;70:10:0
            NONE
            NONE'''
    elif id[0] == 7:
        parametrs = '''7;(x,y);5;2;1
            70:5:0;3:1:0;71:5:0
            NONE
            NONE'''
    elif id[0] == 8:
        parametrs = '''8;(x,y);3;0;1.5
            71:15:0;3:1:0
            NONE
            NONE'''
    elif id[0] == 9:
        parametrs = '''9;(x,y);3;2;1.6
            71:15:0;3:1:0
            NONE
            NONE'''
    elif id[0] == 10:
        parametrs = '''10;(x,y);3;1;1.5
            71:15:0;3:1:0;65:1:0
            NONE
            NONE'''
    elif id[0] == 11:
        parametrs = '''11;(x,y);3;1;1.5
            71:15:0;3:1:0
            NONE
            NONE'''
    elif id[0] == 12:
        parametrs = '''12;(x,y);3;1;1.5
            71:15:0;3:1:0
            NONE
            NONE'''
    elif id[0] == 13:
        parametrs = '''13;(x,y);4;3;0.4
            13:1:0;21:8:0;43:2:0;9:16:0;10:16:0;1:2:0
            NONE
            NONE'''
    elif id[0] == 14:
        parametrs = '''14;(x,y);4;3;0.4
            43:12:0;44:20:0;26:1:0;1:2:0;4:40:0
            NONE
            NONE'''
    elif id[0] == 15:
        parametrs = '''15;(x,y);4;4;0.3
            1:20:0;33:8:720;28:1:39200;60:2:480;46:16:0;57:24:0
            NONE
            NONE'''
    elif id[0] == 16:
        parametrs = '''16;(x,y);3;4;0.6
            6:70002:0;33:3:720;1:6:0;67:1:0
            NONE
            NONE'''
    elif id[0] == 17:
        parametrs = '''17;(x,y);3;4;0.6
            6:70002:0;33:3:720;1:6:0;67:1:0
            NONE
            NONE'''
    elif id[0] == 18:
        parametrs = '''18;(x,y);4;4;0.3
            1:20:0;33:8:720;28:1:39200;60:2:480;46:16:0;57:24:0
            NONE
            NONE'''
    elif id[0] == 19:
        parametrs = '''19;(x,y);5;2;0.4
            1:50:0;25:1:100;57:15:0;21:1:0
            NONE
            NONE'''
    elif id[0] == 20:
        parametrs = '''20;(x,y);4;2;0.4
            1:40:0;25:1:100;57:12:0;21:20:0
            NONE
            NONE'''
    elif id[0] == 21:
        parametrs = '''21;(x,y);3;2;0.3
            2:15:0;70:3:0;43:1:0;3:3:0
            NONE
            NONE'''
    elif id[0] == 22:
        parametrs = '''22;(x,y);2;3;0.4
            57:10:0;43:1:0
            NONE
            NONE'''
    elif id[0] == 23:
        parametrs = '''23;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 24:
        parametrs = '''24;(x,y);3;4;0.5
            4:3:0;42:3:0;40:2:0;39:2:0;36:6:0;35:6:0
            NONE
            NONE'''
    elif id[0] == 25:
        parametrs = '''25;(x,y);3;4;0.5
            4:3:0;42:3:0;40:2:0;39:2:0;36:6:0;35:9:0
            NONE
            NONE'''
    elif id[0] == 26:
        parametrs = '''26;(x,y);1;3;1
            65:1:0
            NONE
            NONE'''
    elif id[0] == 27:
        parametrs = '''27;(x,y);3;4;0.7
            65:1:0;6:1500:0;10:546:0;26:2:0;45:333:0;9:543:0;3:3:0
            NONE
            NONE'''
    elif id[0] == 28:
        parametrs = '''28;(x,y);6;4;0.7
            65:1:0;6:3000:0;10:546:0;26:2:0;45:333:0;9:543:0;3:6:0
            NONE
            NONE'''
    elif id[0] == 29:
        parametrs = '''29;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 30:
        parametrs = '''30;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 31:
        parametrs = '''31;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 32:
        parametrs = '''32;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 33:
        parametrs = '''33;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 34:
        parametrs = '''34;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 35:
        parametrs = '''35;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 36:
        parametrs = '''36;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 37:
        parametrs = '''37;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 38:
        parametrs = '''38;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 39:
        parametrs = '''39;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 40:
        parametrs = '''40;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 41:
        parametrs = '''41;(x,y);3;2;1
            3:6:0;1:6:0
            NONE
            NONE'''
    elif id[0] == 42:
        parametrs = '''42;(x,y);2;0;0.8
            3:16:0;70:8:0
            NONE
            NONE'''
    elif id[0] == 43:
        parametrs = '''43;(x,y);2;2;0.8
            3:16:0;70:8:0
            NONE
            NONE'''
    elif id[0] == 44:
        parametrs = '''44;(x,y);5;0;0.25
            3:90:0;1:15:0
            NONE
            NONE'''
    elif id[0] == 45:
        parametrs = '''45;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    else:
        parametrs = '''0;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    return parametrs


def ps_height(percent):  # возрощает число процентов от высоты
    percent = percent / 100
    return int(height * percent)


def ps_width(percent):  # возрощает число процентов от ширены
    percent = percent / 100
    return int(width * percent)


class Sparks(pygame.sprite.Sprite):  # частицы
    def __init__(self, all_sparks, image, dx, dy):
        super().__init__(all_sparks)
        self.image = image
        self.rect = self.image.get_rect()
        self.dx = dx
        self.dy = dy

        self.velocity = [dx, dy]
        pos = (random.choice(range(0, ps_width(100))),
               random.choice(range(ps_height(80), ps_height(100))))
        self.rect.x, self.rect.y = pos
        self.gravity = 1

    def update(self):
        self.velocity[1] += self.gravity
        # перемещаем частицу
        self.rect.x += int(self.velocity[0])
        self.rect.y += int(self.velocity[1])
        # убиваем, если частица ушла за экран
        if not self.rect.colliderect((-1, -1, width + 1, height + 1)):
            pos = (random.choice(range(0, ps_width(100))),
                   random.choice(range(ps_height(80), ps_height(100))))
            self.rect.x, self.rect.y = pos
            self.velocity = [self.dx, self.dy]


class Object:  # любой граффический объект
    def __init__(self, canvas, image, x, y, width, height):
        self.canvas = canvas
        self.image = image
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.visibility = True

    def move_to(self, x, y):
        self.x = x
        self.y = y

    def change_image(self, image):
        self.image = image

    def check_tip(self, x, y):  # проверка на принодлежность х и у в объекте
        if self.visibility:
            return (x >= self.x and x <= self.x + self.width and y >= self.y and
                    y <= self.y + self.height)

    def show(self):  # отобразить
        if self.visibility:
            self.canvas.blit(self.image, (self.x, self.y))


class Text(Object):  # объект текст
    def __init__(self, canvas, x, y, text, font, color=WHITE):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.text = str(text)
        self.font = font
        self.visibility = True
        self.color = color
        self.height = len(str(self.text).split('\n')) * ps_height(2)

    def change_text(self, new_text):
        self.text = str(new_text)

    def show(self):  # отобразить построчно
        if not self.visibility:
            return
        texts = str(self.text).split('\n')
        for i in range(len(texts)):
            text = self.font.render(texts[i], 1, self.color)
            self.canvas.blit(text, (self.x, int(self.y + i * ps_height(2))))


class Button(Object):  # кнопка
    def __init__(self, canvas, image, x, y, width, height, function=None, image_animation=None):
        self.canvas = canvas
        self.image = image
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.function = [function]
        self.image_animation = image_animation
        self.visibility = True
        self.status = False

    def add_function(self, function):  # добовляет функцию
        if self.function == [None]:
            self.function = [function]
        else:
            self.function.append(function)

    def get_function(self, function):  # устонавливает одну функцию
        self.function = [function]

    def del_function(self):  # удоляет все функции
        self.function = [None]

    def get_image_animation(self, image):  # установка анимации при нажатии
        self.image_animation = image

    def show_animation(self):  # отобразить анимацию
        if self.image_animation is not None:
            self.canvas.blit(self.image_animation, (self.x, self.y))
        else:
            self.canvas.blit(self.image, (self.x, self.y))

    def click(self, *args):  # запустить все функции
        if self.function == [None] or not self.visibility:
            return False
        for function in self.function:
            try:
                return function(args)
            except:
                print('не удалось запустить функцию')
                return False

    def show(self):  # отобразить
        if self.visibility:
            if self.status:
                self.show_animation()
                return
            self.canvas.blit(self.image, (self.x, self.y))


class Call:  # клетка
    def __init__(self, canvas, x, y, size, color=BLACK, parametrs=None):
        self.canvas = canvas
        self.size = size
        self.x = x
        self.y = y
        self.color = color
        self.visibility = True

        if parametrs is None:  # установка параметров по умолчанию
            self.id = '0'
            self.cor = (x, y)
            self.count = 0
            self.rad = '-1'
            self.speed = 1
            self.can_find = 'NONE'
            self.can_attack = 'NONE'
            self.lies = 'NONE'
        else:
            parametrs = parametrs.split()
            self.id = parametrs[0].split(';')[0]
            self.cor = (x, y)
            self.count = int(parametrs[0].split(';')[2])
            self.rad = parametrs[0].split(';')[3]
            self.speed = parametrs[0].split(';')[4]
            self.can_find = parametrs[1]
            self.can_attack = parametrs[2]
            self.lies = parametrs[3]

    def find_things(self):  # произвести поиск на клетке
        if self.count == 0:
            return
        can_find = []
        lies = []
        all_things_ling = {}
        all_things_can_find = {}
        if 'NONE' in self.lies:
            all_things_ling = {}
        else:
            for thing in self.lies.split(';'):
                id, count, strength = thing.split(':')
                count = int(count)
                strength = int(strength)
                all_things_ling[id] = [count, strength]

        if 'NONE' in self.can_find:
            all_things_can_find = {}
        else:
            for thing in self.can_find.split(';'):
                id, count, strength = thing.split(':')
                count = int(count)
                strength = int(strength)
                all_things_can_find[id] = [count, strength]

        for i in all_things_can_find.keys():
            id, count, strength = i, *all_things_can_find[i]
            if id in all_things_ling:
                all_things_ling[id][0] += count // self.count
                all_things_can_find[i][0] -= count // self.count
            else:
                all_things_ling[id] = [count // self.count, strength]
                all_things_can_find[i][0] -= count // self.count

        for i in all_things_ling.keys():
            lies.append(f'{i}:{all_things_ling[i][0]}:{all_things_ling[i][1]}')
        for i in all_things_can_find.keys():
            can_find.append(f'{i}:{all_things_can_find[i][0]}:{all_things_can_find[i][1]}')

        self.count -= 1
        self.lies = ';'.join(lies)
        self.can_find = ';'.join(can_find)

    def change_parametrs(self, parametrs):
        parametrs = parametrs.split()
        self.id = parametrs[0].split(';')[0]
        self.count = parametrs[0].split(';')[2]
        self.rad = parametrs[0].split(';')[3]
        self.speed = parametrs[0].split(';')[4]
        self.can_find = parametrs[1]
        self.can_attack = parametrs[2]
        self.lies = parametrs[3]

    def get_text_for_save(self):
        text = f'''{self.id};({self.cor[0]},{self.cor[1]});{self.count};{self.rad};{self.speed}
{self.can_find}
{self.can_attack}
{self.lies}</>
'''
        return text

    def show_mark(self, image, x, y):
        if image is None:
            return
        self.canvas.blit(image, (x, y))

    def draw(self, x, y, font):
        if not self.visibility or x < 0 or y < 0 or x > 1700 or y > 1000:
            return
        pygame.draw.rect(self.canvas, self.color, (x, y, self.size, self.size), 1)
        if self.id != '0':
            text = font.render(self.id, 1, WHITE)
            self.canvas.blit(text, (x + 2, y + 4))


class Board:  # поле
    def __init__(self, canvas, width, height, font, cell_size=10, visibility=True, parametrs=None):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.font = font
        self.visibility = visibility
        if parametrs is not None:
            parametrs = parametrs.split('</>')

        self.board_with_marks = []
        self.board = []
        for j in range(height):
            self.board.append([])
            for i in range(width):
                param = None
                if parametrs is not None:
                    index = j * width + i
                    param = parametrs[index]
                self.board[j].append(Call(canvas, i, j, cell_size, parametrs=param))
                if self.board[j][i].lies != 'NONE':
                    self.board_with_marks.append(self.board[j][i])
        self.left = 0
        self.top = 0
        self.cell_size = cell_size
        self.image_mark = None

    def set_move(self, left, top):
        self.left = left
        self.top = top

    def change_size_call(self, new_size):
        self.cell_size = new_size
        for i in range(self.height):
            for j in range(self.width):
                self.board[i][j].size = new_size

    def show_all_marks(self, size_call, left, top):
        for call in self.board_with_marks:
            x = call.x * size_call + left
            y = call.y * size_call + top
            call.show_mark(self.image_mark, x, y)

    def render(self):
        if not self.visibility:
            return
        for i in range(self.height):
            for j in range(self.width):
                x = j * self.cell_size + self.left
                y = i * self.cell_size + self.top
                self.board[i][j].draw(x, y, self.font)

    def made_unvisibility_call(self, x, y, width, height):
        # скрывает все клетки которые не видно, для оптимизации
        for i in range(self.height):
            for j in range(self.width):
                if (i >= y and i <= y + height and j >= x and j <= x + width):
                    self.board[i][j].visibility = True
                else:
                    self.board[i][j].visibility = False

    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        height = self.height * self.cell_size + self.top
        width = self.width * self.cell_size + self.left
        if (x >= width or y >= height or x < self.left or y < self.top):
            return
        x = int((x - self.left) / self.cell_size)
        y = int((y - self.top) / self.cell_size)
        return x, y

    def get_call_in_bord(self, mouse_pos):
        x, y = mouse_pos
        height = self.height * self.cell_size + self.top
        width = self.width * self.cell_size + self.left
        if (x >= width or y >= height or x < self.left or y < self.top):
            return
        x = int((x - self.left) / self.cell_size)
        y = int((y - self.top) / self.cell_size)
        return self.board[y][x]


class Window(Object):  # пролистывающиеся окно
    def __init__(self, canvas, image, x, y, width, height, column_count):
        self.canvas = canvas
        self.image = image
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.column_count = column_count
        self.visibility = True
        self.paging = False
        self.mod = True
        self.objects = []
        self.shift_y = y
        self.width_object = 70
        self.last_x, self.last_y = 0, 0

    def show_all(self):
        for object in self.objects:
            object.visibility = True

    def hide_all(self):
        for object in self.objects:
            object.visibility = False

    def delete_all_objects(self):
        self.objects = []

    def add_object(self, object):  # добавляет объект и меняет его позицию
        object.visibility = self.visibility

        x = (len(self.objects) - ((len(self.objects) // self.column_count) * self.column_count)) * (
                self.width // self.column_count) + self.x
        if self.column_count != 1:
            y = (len(self.objects) // self.column_count) * object.height + self.shift_y
        else:
            y = sum(map(lambda x: x.height, self.objects)) + self.shift_y + (ps_height(2) * len(self.objects))
        object.move_to(x, y)
        self.objects.append(object)

    def check(self, event):  # проверка событий
        if not self.visibility:
            return
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            self.last_x, self.last_y = x, y
            for object in self.objects:
                if isinstance(object, Button):
                    if object.check_tip(x, y):
                        object.status = True

                if isinstance(object, Function):
                    object.group_buttons.check(event)

                if isinstance(object, Window):
                    if event.button == 5:  # скрол вниз
                        if object.check_tip(x, y) and object.visibility:
                            object.pag(object.shift_y - 50)
                    if event.button == 4:  # скрол вверх
                        if object.check_tip(x, y) and object.visibility:
                            object.pag(object.shift_y + 50)
                    if event.button == 1:  # левое нажатие мыши
                        if object.check_tip(x, y) and object.visibility:
                            object.paging = True

        if event.type == pygame.MOUSEBUTTONUP:
            x, y = event.pos
            for object in self.objects:
                if isinstance(object, Button):
                    if object.status and object.check_tip(x, y):
                        object.click()
                    object.status = False

                if isinstance(object, Window):
                    object.paging = False

                if isinstance(object, Function):
                    object.group_buttons.check(event)

        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            shift_x = self.last_x - x
            shift_y = self.last_y - y
            self.last_x, self.last_y = x, y
            for object in self.objects:
                if isinstance(object, Window):
                    if object.paging:
                        object.pag(object.shift_y - shift_y)

    def pag(self, y):
        self.shift_y = y
        if self.mod:  # следующие действия делают так,
            # чтоб объекты не выходили за границы экрана
            if self.shift_y > self.y:
                self.shift_y = self.y
            if ((len(self.objects) // self.column_count) + 1) >= (
                    self.height // self.width_object):

                if self.shift_y < -((((len(self.objects) // self.column_count)) - (
                        self.height // self.width_object))) * self.width_object:
                    self.shift_y = -((((len(self.objects) // self.column_count)) - (
                            self.height // self.width_object))) * self.width_object
            else:
                self.shift_y = self.y

        for i in range(len(self.objects)):
            object = self.objects[i]
            if self.column_count != 1:
                y = (i // self.column_count) * self.objects[i].height + self.shift_y
            else:
                y = sum(map(lambda x: x.height, self.objects[:i])) + self.shift_y + (ps_height(2) * i)
            object.move_to(object.x, y)

    def render(self):
        if not self.visibility:
            return
        if self.image is not None:
            self.show()
        for object in self.objects:
            object.show()


class Group:  # группа
    def __init__(self):
        self.all_objects = []
        self.last_x, self.last_y = 0, 0
        self.visibility = True

    def add_objects(self, *objects):
        for object in objects:
            self.all_objects.append(object)

    def delete(self, *objects):
        if len(objects) == 0:
            self.all_objects = []
        for object in objects:
            del self.all_objects[self.all_objects.index(object)]

    def off_all(self):
        for object in self.all_objects:
            object.visibility = False

    def on_all(self):
        for object in self.all_objects:
            object.visibility = True

    def check(self, event):  # проверка событий
        if not self.visibility:
            return
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            self.last_x, self.last_y = x, y
            for object in self.all_objects:
                if isinstance(object, Button):
                    if object.check_tip(x, y):
                        object.status = True

                if isinstance(object, Window):
                    if event.button == 5:  # скрол вниз
                        if object.check_tip(x, y) and object.visibility:
                            object.pag(object.shift_y - 50)
                    if event.button == 4:  # скрол вверх
                        if object.check_tip(x, y) and object.visibility:
                            object.pag(object.shift_y + 50)
                    if event.button == 1:  # левое нажатие мыши
                        if object.check_tip(x, y) and object.visibility:
                            object.paging = True

        if event.type == pygame.MOUSEBUTTONUP:
            x, y = event.pos
            for object in self.all_objects:
                if isinstance(object, Button):
                    if object.status and object.check_tip(x, y):
                        object.click()
                    object.status = False

                if isinstance(object, Window):
                    object.paging = False

        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            shift_x = self.last_x - x
            shift_y = self.last_y - y
            self.last_x, self.last_y = x, y
            for object in self.all_objects:
                if isinstance(object, Window):
                    if object.paging:
                        object.pag(object.shift_y - shift_y)

    def show(self):  # отображение
        for object in self.all_objects:
            object.show()


class GameObject:
    def __init__(self, canvas, x, y, width, height, type=1):
        self.type = type

        self.canvas = canvas
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.visibility = True
        self.is_choce = False
        self.is_deleted = False

    def move_to(self, x, y):
        self.x = x
        self.y = y

    def check_tip(self, x, y):  # проверка на принодлежность х и у в объекте
        if self.visibility:
            return (x >= self.x and x <= self.x + self.width and y >= self.y and
                    y <= self.y + self.height)

    def show(self, map_x, map_y, zoom):  # отобразить
        if self.visibility and not self.is_deleted:
            if self.type == 1:
                color = BROWN
            else:
                color = WHITE
            pygame.draw.rect(self.canvas, color,
                             (int(self.x * zoom) + map_x, int(self.y * zoom) + map_y, int(self.width * zoom), int(self.height * zoom)), 4)
            if self.is_choce:
                pygame.draw.rect(self.canvas, RED,
                                 (int(self.x * zoom) + map_x - 3, int(self.y * zoom) + map_y - 3, int(self.width * zoom) + 6, int(self.height * zoom) + 6), 3)

