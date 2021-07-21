import time

import cv2, ctypes, pyautogui, keyboard

cod = 'test0'
num_of_screen = 0
confidence = 40

while True:
    keyboard.wait('Ctrl')
    num_of_screen += 1
    name = f'images/map/{cod}_{num_of_screen}.png'
    pyautogui.screenshot(name, (155, 180, 2235, 1575))

    boxes = pyautogui.locateAll(f'images/map/last_screen.png', name, confidence=0.9)
    boxes_x_y = []
    if boxes:
        for box in boxes:
            x, y = int(box[0]), int(box[1])
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

    if len(boxes_x_y) > 0:
        x, y = boxes_x_y[0]
        img = cv2.imread(name)
        x, y = x, y - 100
        if y < 0:
            y = 0
        w, h = 2235 - x, 1575 - y
        img = img[y:y + h, x:x + w]
        cv2.imwrite(name, img)

    try:
        last_screen = cv2.imread(name)
        height, width = last_screen.shape[:2]
        x, y = width - 235, 100
        w, h = 235, height - 200
        last_screen = last_screen[y:y + h, x:x + w]
        cv2.imwrite('images/map/last_screen.png', last_screen)
    except Exception:
        print('was error')
    print('new screen')

