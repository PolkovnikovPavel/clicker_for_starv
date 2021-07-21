import pyautogui
import numpy as np
import time
import ctypes
import math
import cv2


user32 = ctypes.WinDLL('user32', use_last_error=True)
is_error = False
RED = (0, 0, 255)
yellow = (0, 255, 255)


def click(x=0, y=0, data=0, t=0.01):
    MOUSEEVENTF_LEFTDOWN = 0x0002
    MOUSEEVENTF_LEFTUP = 0x0004

    MOUSEEVENTF_RIGHTDOWN = 0x0008
    MOUSEEVENTF_RIGHTUP = 0x0010

    if data == 0:
        mose_down = MOUSEEVENTF_RIGHTDOWN
        mose_up = MOUSEEVENTF_RIGHTUP
    else:
        mose_down = MOUSEEVENTF_LEFTDOWN
        mose_up = MOUSEEVENTF_LEFTUP

    user32.SetCursorPos(x, y)
    user32.mouse_event(mose_down)
    time.sleep(t)
    user32.mouse_event(mose_up)

print('start...')
t = time.time()

#pyautogui.screenshot('images/screen2.png', (0, 115, 1000, 885))
image = cv2.imread("images/all_map.png")
confidence = 40
all_trees = []
all_stones = []

for i in range(1, 7+1):
    #boxes_tree_night = pyautogui.locateAllOnScreen(f'images/trees/d_{i}.png', confidence=0.95)
    boxes = pyautogui.locateAll(f'images/trees/d_{i}.png', 'images/all_map.png', confidence=0.93)
    img = cv2.imread(f"images/trees/d_{i}.png")
    boxes_x_y = []

    if boxes != None:
        for box in boxes:
            x, y = int(box[0]), int(box[1])
            height, width = img.shape[:2]
            temp = False
            for j in boxes_x_y:
                if abs(j[0] - x) < confidence and abs(j[1] - y) < confidence:
                    x = (j[0] + x) / 2
                    y = (j[1] + y) / 2
                    temp = True
                    j[0] = int(x)
                    j[1] = int(y)
                    break
            if not temp:
                boxes_x_y.append([x, y])


        for x, y in boxes_x_y:
            line = cv2.line(image, (x, y), (x + height, y), yellow, thickness=1, lineType=8, shift=0)
            line = cv2.line(image, (x + height, y), (x + height, y + width), yellow, thickness=1, lineType=8, shift=0)
            line = cv2.line(image, (x + height, y + width), (x, y + width), yellow, thickness=1, lineType=8, shift=0)
            line = cv2.line(image, (x, y + width), (x, y), yellow, thickness=1, lineType=8, shift=0)
            all_trees.append((x, y, width, height))


for i in range(1, 3+1):
    boxes = pyautogui.locateAll(f'images/stones/d_{i}.png', 'images/all_map.png', confidence=0.9)
    img = cv2.imread(f"images/stones/d_{i}.png")
    boxes_x_y = []

    if boxes != None:
        for box in boxes:
            x, y = int(box[0]), int(box[1])
            height, width = img.shape[:2]
            temp = False

            for j in boxes_x_y:
                if abs(j[0] - x) < confidence and abs(j[1] - y) < confidence:
                    x = (j[0] + x) / 2
                    y = (j[1] + y) / 2
                    temp = True
                    j[0] = int(x)
                    j[1] = int(y)
                    break
            if not temp:
                boxes_x_y.append([x, y])

        for x, y in boxes_x_y:
            line = cv2.line(image, (x, y), (x + height, y), RED, thickness=1, lineType=8, shift=0)
            line = cv2.line(image, (x + height, y), (x + height, y + width), RED, thickness=1, lineType=8, shift=0)
            line = cv2.line(image, (x + height, y + width), (x, y + width), RED, thickness=1, lineType=8, shift=0)
            line = cv2.line(image, (x, y + width), (x, y), RED, thickness=1, lineType=8, shift=0)
            all_stones.append((x, y, width, height))


print(time.time() - t)
print('saving...')
text = ''
objs = []
for tree in all_trees:
    x, y, w, h = tree
    w, h = w // 2, h // 2
    x, y = int(x + w), int(y + h)
    objs.append(f'{x} {y} {w} {h}')
text += ';'.join(objs) + '\n'

objs = []
for stone in all_stones:
    x, y, w, h = stone
    w, h = w // 2, h // 2
    x, y = int(x + w), int(y + h)
    objs.append(f'{x} {y} {w} {h}')
text += ';'.join(objs) + '\n'

with open('description_map.txt', 'w') as f:
    f.write(text)


print('show')
final_wide = 2000
k = float(final_wide) / image.shape[1]
new_size = (final_wide, int(image.shape[0] * k))

# уменьшаем изображение до подготовленных размеров
resized = cv2.resize(image, new_size, interpolation=cv2.INTER_AREA)
cv2.imshow("Resize image", resized)
cv2.waitKey(0)


