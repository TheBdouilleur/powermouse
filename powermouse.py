#!/usr/bin.pypy3
'''Navigate and move your cursor with vim kebindings'''

from pynput.keyboard import Listener, Key, KeyCode
import pyautogui
from easy_notify import notify

screenWidth, screenHeight = pyautogui.size()
pyautogui.FAILSAFE = False

SMALL_MOVEMENT = 4
BIG_MOVEMENT = 40
HUGE_MOVEMENT = 200
DEFAULT_MOVEMENT = BIG_MOVEMENT

LEFT_LEYS = [KeyCode.from_char('h'), Key.left]
DOWN_KEYS = [KeyCode.from_char('j'), Key.down]
UP_KEYS = [KeyCode.from_char('k'), Key.up]
RIGHT_KEYS = [KeyCode.from_char('l'), Key.right]

LEFTMOST_KEYS = [KeyCode.from_char('0'), Key.home]
BOTTOM_KEYS = [KeyCode.from_char('G'), Key.page_down]
TOP_KEYS = [KeyCode.from_char('gg'), Key.page_down]
RIGHTMOST_KEYS = [KeyCode.from_char('$'), Key.end]

QUIT_KEYS = [KeyCode.from_char('x'), KeyCode.from_char('q'), Key.esc]

CLICK_KEYS = [KeyCode.from_char('c'), Key.enter]


def on_press(key):
    """Get the key pressed and run some code depending on it"""
    currentX, currentY = pyautogui.position()

    if key in LEFT_LEYS:
        pyautogui.move(-SMALL_MOVEMENT, 0)
    if key in DOWN_KEYS:
        pyautogui.move(0, SMALL_MOVEMENT)
    if key in UP_KEYS:
        pyautogui.move(0, -SMALL_MOVEMENT)
    if key in RIGHT_KEYS:
        pyautogui.move(SMALL_MOVEMENT, 0)

    if key in LEFTMOST_KEYS:
        pyautogui.moveTo(0, currentY)
        notify("Powermouse", "Moved to left of the screen")
    if key in BOTTOM_KEYS:
        pyautogui.moveTo(currentX, screenHeight)
        notify("Powermouse", "Moved to bottom of screen")
    if key in TOP_KEYS:
        pyautogui.moveTo(screenWidth, currentY)
        notify("Powermouse", "Moved to top of screen")
    if key in RIGHTMOST_KEYS:
        pyautogui.moveTo(0, currentY)
        notify("Powermouse", "Moved to right of screen")

    if key in CLICK_KEYS:
        pyautogui.click()
        notify("Powermouse", f"Clicked at position {pyautogui.position()}")

    if key in QUIT_KEYS:
        notify("Powermouse", "Quitting")
        exit()


if __name__ == "__main__":
    notify("Powermouse", "Powermouse running")

    with Listener(on_press=on_press) as listener:
        listener.join()
