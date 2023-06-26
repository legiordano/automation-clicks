import pyautogui
import time

time_between_clicks = 30

while True:
    x, y = pyautogui.position()

    pyautogui.click(x, y, clicks=1, interval=0, button='left')

    time.sleep(time_between_clicks)