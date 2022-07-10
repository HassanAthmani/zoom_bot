import subprocess

import pyautogui
import os
import time
import sys
from meeting_config import read_credentials


def locator_and_click(image_path):
    loc = pyautogui.locateCenterOnScreen(image_path)
    pyautogui.click(loc)
    time.sleep(5)
    return loc


def locator_and_double_click(image_path):
    loc = pyautogui.locateCenterOnScreen(image_path)
    pyautogui.doubleClick(loc)
    time.sleep(5)
    return loc


def locator(image_path):
    loc = pyautogui.locateCenterOnScreen(image_path)
    time.sleep(5)
    return loc


def join():
    c = read_credentials()
    zoom_path = str(c["zoom_path"])
    meeting_id = str(c["meeting_id"])
    passcode = str(c["passcode"])
    name = str(c["name"])
    email = str(c["email"])

    try:
        subprocess.Popen(zoom_path)

    except Exception:
        print("Zoom application has not been executed, check zoom path")
        return 0

    base_path = str(os.path.dirname(os.path.abspath(__file__))).replace("//", "/")
    locator_and_click(base_path + '/icons/join_meeting.png')
    loc = locator(base_path + '/icons/meeting_id_input.png')
    pyautogui.write(meeting_id, interval=0.15)
    x, y = loc
    pyautogui.click((x, y + 43))
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    pyautogui.write(name, interval=0.15)
    locator_and_double_click(base_path + '/icons/do_not_connect_to_audio.png')
    locator_and_click(base_path + '/icons/do_not_connect_to_audio.png')
    locator_and_double_click(base_path + '/icons/turn_off_my_video.png')
    locator_and_click(base_path + '/icons/turn_off_my_video.png')
    locator_and_click(base_path + '/icons/join.png')
    time.sleep(10)
    locator_and_click(base_path + '/icons/passcode.png')
    time.sleep(2)
    pyautogui.write(passcode, interval=0.15)
    locator_and_click(base_path + '/icons/join_m.png')
    locator_and_click(base_path + '/icons/your_email2.png')
    pyautogui.write(email, interval=0.15)
    locator_and_click(base_path + '/icons/join_m.png')


if __name__ == '__main__':
    print("Bot has started")
    print("Hold on a couple of seconds -- ")
    time.sleep(30)
    join()
