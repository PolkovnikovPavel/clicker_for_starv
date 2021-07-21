import pyautogui, time
import ctypes

time.sleep(2)
running = True
user32 = ctypes.WinDLL('user32', use_last_error=True)

pyautogui.mouseDown()


while running:
    user32.SetCursorPos(960, 400)
    time.sleep(0.3)
    pyautogui.keyDown("w")
    time.sleep(1.24 * 14 / 3)
    pyautogui.keyUp("w")
    #time.sleep(0.5)
    #pyautogui.keyDown("w")
    #time.sleep(1 / 3)
    #pyautogui.keyUp("w")
    #time.sleep(0.5)
    #pyautogui.keyDown("w")
    #time.sleep(11 / 3)
    #pyautogui.keyUp("w")

    time.sleep(0.3)
    user32.SetCursorPos(1200, 540)
    time.sleep(0.3)
    pyautogui.keyDown("d")
    time.sleep(1.24 * 3 / 3)
    pyautogui.keyUp("d")


    time.sleep(0.3)
    user32.SetCursorPos(960, 700)
    time.sleep(0.3)
    pyautogui.keyDown("s")
    time.sleep(1.24 * 14 / 3)
    pyautogui.keyUp("s")
    #time.sleep(0.5)
    #pyautogui.keyDown("s")
    #time.sleep(1 / 3)
    #pyautogui.keyUp("s")
    #time.sleep(0.5)
    #pyautogui.keyDown("s")
    #time.sleep(4 / 3)
    #pyautogui.keyUp("s")

    time.sleep(0.3)
    user32.SetCursorPos(700, 540)
    time.sleep(0.3)
    pyautogui.keyDown("a")
    time.sleep(1.24 * 3 / 3)
    pyautogui.keyUp("a")

    time.sleep(0.5)