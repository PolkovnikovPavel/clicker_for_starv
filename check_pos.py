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

image = cv2.imread("images/all_map.png")

boxes = pyautogui.locateAll(f'images/screen.png', 'images/all_map.png', confidence=0.7)
img = cv2.imread(f"images/screen.png")
if boxes != None:
    for box in boxes:
        x, y = int(box[0]), int(box[1])
        height, width = img.shape[:2]

        square = cv2.rectangle(image, (x, y), (x + width, y + height), RED)


print('show')
final_wide = 2000
k = float(final_wide) / image.shape[1]
new_size = (final_wide, int(image.shape[0] * k))

# уменьшаем изображение до подготовленных размеров
resized = cv2.resize(image, new_size, interpolation=cv2.INTER_AREA)
cv2.imshow("Resize image", resized)
cv2.waitKey(0)

