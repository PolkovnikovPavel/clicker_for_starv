import pygame
import os
from System import *
from images.images import *


def exit(*args):
    global running
    running = False


def save(*args):
    description_map = open('description_map.txt', 'w')
    text = ''
    objs = []
    for tree in all_trees:
        if not tree.is_deleted:
            x, y, w, h = tree.x, tree.y, tree.width, tree.height
            w, h = w // 2, h // 2
            x, y = int(x + w), int(y + h)
            w, h = abs(w), abs(h)
            objs.append(f'{x} {y} {w} {h}')
    text += ';'.join(objs) + '\n'

    objs = []
    for stone in all_stones:
        if not stone.is_deleted:
            x, y, w, h = stone.x, stone.y, stone.width, stone.height
            w, h = w // 2, h // 2
            x, y = int(x + w), int(y + h)
            w, h = abs(w), abs(h)
            objs.append(f'{x} {y} {w} {h}')
    text += ';'.join(objs)

    description_map.write(text)
    description_map.close()


def start(*args):
    global type_window
    for button in buttons_main:
        button.visibility = False
    for object in objects_main:
        object.visibility = False
    main_map.visibility = True
    type_window = 'editor'


def create_all_game_objects():
    with open('description_map.txt', encoding='utf8') as f:
        texts = f.read()
    trees, stones = texts.split('\n')
    trees = trees.split(';')
    stones = stones.split(';')
    for tree in trees:
        x, y, w, h = map(int, tree.split(' '))
        x, y, w, h = x - w, y - h, w * 2, h * 2
        obj = GameObject(screen, x, y, w, h, 1)
        all_trees.append(obj)
    for stone in stones:
        x, y, w, h = map(int, stone.split(' '))
        x, y, w, h = x - w, y - h, w * 2, h * 2
        obj = GameObject(screen, x, y, w, h, 2)
        all_stones.append(obj)

def create_all_objects():
    global main_map, parametrs
    image = get_bg_main_window(size)
    bg_main_window = Object(screen, image, 0, 0, *size)

    image = get_btn_start_main((200, 50))
    image_2 = get_btn_start_main_click((200, 50))
    btn_start_main = Button(screen, image, width / 2 - 100, height / 2 + 200,
                           200, 50, start, image_2)

    image = get_btn_save_map((200, 50))
    image_2 = get_btn_save_map_click((200, 50))
    btn_save_map = Button(screen, image, width - 220, height - 72, 200, 50, save, image_2)

    image = get_pygame_image(image_map)
    main_map = Object(screen, image, map_x, map_y, width_map * zoom, height_map * zoom)
    main_map.visibility = False

    objects_main.append(bg_main_window)
    buttons_main.append(btn_start_main)
    buttons_map.append(btn_save_map)



FPS = 100

ratio = 3 / 5
zoom_plus = 0.2
zoom = 1
old_x, old_y = 0, 0
map_x, map_y = 0, 0
x_on_map, y_on_map = 0, 0
width_map, height_map = 9565, 3628
main_map = None

main_image_map = get_free_image('images/all_map.png', (width_map, height_map), 1)
image_map = main_image_map

objects_main = []
buttons_main = []
buttons_map = []

all_game_objects = []
all_trees = []
all_stones = []

type_window = 'main'


pygame.init()

display = pygame.display.Info()
width, height = display.current_w - 75, display.current_h - 75
if width * ratio <= height:
    height = int(width * ratio)
else:
    width = int(height / ratio)
size = width, height
print(size)
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (30, 30)
screen = pygame.display.set_mode(size)

create_all_objects()
create_all_game_objects()

all_game_objects.extend(all_trees)
all_game_objects.extend(all_stones)

running = True
moving_map = False
highlighting_obj = None
last_choce_obj = None
clock = pygame.time.Clock()
x, y = 0, 0
start_x = 0
start_y = 0
is_key_pressed = False
is_right_mous = False

while running:
    clock.tick(FPS)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for button in buttons_main:
                if button.check_tip(x, y):
                    button.status = True
            for button in buttons_map:
                if button.check_tip(x, y):
                    button.status = True
            if type_window == 'editor':
                if event.button == 1:
                    moving_map = True
                    old_x, old_y = x, y

                elif event.button == 3:
                    start_x = x
                    start_y = y
                    is_right_mous = True
                    for obj in all_game_objects:
                        if obj.check_tip(x // zoom - map_x, y // zoom - map_y):
                            if last_choce_obj:
                                last_choce_obj.is_choce = False
                                last_choce_obj = None
                            highlighting_obj = obj
                            obj.is_choce = True


            if event.button == 5:  # скрол вниз
                zoom -= zoom_plus
                if zoom < 0.1:
                    zoom += zoom_plus
                else:
                    image = resize_image(image_map, (int(width_map * zoom), int(height_map * zoom)))
                    image = get_pygame_image(image)
                    main_map.change_image(image)
                    map_x = map_x - int((width_map * zoom) - (width_map * (zoom * zoom_plus))) // 2
                    map_y = map_y - int((height_map * zoom) - (height_map * (zoom * zoom_plus))) // 2
                    main_map.move_to(map_x, map_y)

            if event.button == 4:   # скрол вверх
                zoom += zoom_plus
                if zoom > 4:
                    zoom -= zoom_plus
                else:
                    image = resize_image(image_map, (int(width_map * zoom), int(height_map * zoom)))
                    image = get_pygame_image(image)
                    main_map.change_image(image)
                    map_x = map_x - int((width_map * zoom) - (width_map * (zoom / zoom_plus))) // 2
                    map_y = map_y - int((height_map * zoom) - (height_map * (zoom / zoom_plus))) // 2
                    main_map.move_to(map_x, map_y)


        if event.type == pygame.MOUSEBUTTONUP:
            x, y = event.pos
            for button in buttons_main:
                if button.status and button.check_tip(x, y):
                    button.click()
                button.status = False
            for button in buttons_map:
                if button.status and button.check_tip(x, y):
                    button.click()
                button.status = False

            moving_map = False
            is_right_mous = False

            if highlighting_obj:
                last_choce_obj = highlighting_obj
                highlighting_obj = None
            if event.button == 3:
                if is_key_pressed == pygame.K_1:
                    x, y, w, h = start_x // zoom - map_x, start_y // zoom - map_y, (x - start_x) // zoom, (y - start_y) // zoom
                    obj = GameObject(screen, x, y, w, h, 1)
                    all_trees.append(obj)
                    all_game_objects.append(obj)
                if is_key_pressed == pygame.K_2:
                    x, y, w, h = start_x // zoom - map_x, start_y // zoom - map_y, (x - start_x) // zoom, (y - start_y) // zoom
                    obj = GameObject(screen, x, y, w, h, 2)
                    all_stones.append(obj)
                    all_game_objects.append(obj)



        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            if moving_map:
                shift_x = old_x - x
                shift_y = old_y - y
                old_x, old_y = x, y
                map_x = map_x - shift_x
                map_y = map_y - shift_y
                main_map.move_to(map_x, map_y)
            if highlighting_obj:
                shift_x = (start_x - x) // zoom
                shift_y = (start_y - y) // zoom
                start_x = x
                start_y = y
                highlighting_obj.move_to(highlighting_obj.x - shift_x, highlighting_obj.y - shift_y)

        if event.type == pygame.KEYDOWN:
            is_key_pressed = event.key

        if event.type == pygame.KEYUP:
            is_key_pressed = 0
            if event.key == pygame.K_DELETE:
                if last_choce_obj:
                    last_choce_obj.is_deleted = True
                last_choce_obj = None



    if type_window == 'main':
        for object in objects_main:
            object.show()
        for button in buttons_main:
            button.show()
    main_map.show()


    if type_window == 'editor':
        for button in buttons_map:
            button.show()
        for obj in all_game_objects:
            obj.show(map_x, map_y, zoom)
        if is_key_pressed and is_right_mous:
            pygame.draw.rect(screen, RED, (start_x, start_y, x - start_x, y - start_y), 3)

        for i in range(100):
            x = map_x + i * 102
            pygame.draw.line(screen, BLACK, (x, 0), (x, 1365), 2)
        for i in range(70):
            y = map_y + i * 102
            pygame.draw.line(screen, BLACK, (0, y), (2275, y), 2)

    pygame.display.flip()

pygame.quit()