'''Navigate and move your cursor with vim kebindings'''
from pynput.keyboard import Listener, Key, KeyCode
import pyautogui
from easy_notify import notify

pyautogui.FAILSAFE = False
SMALL_MOVEMENT = 40
QUICK_MOVEMENT = 40

LEFT_LEYS = [KeyCode.from_char('h'), Key.left]
DOWN_KEYS = [KeyCode.from_char('j'), Key.down]
UP_KEYS = [KeyCode.from_char('k'), Key.up]
RIGHT_KEYS = [KeyCode.from_char('l'), Key.right]

QUIT_KEYS = [KeyCode.from_char('x'), Key.esc]

CLICK_KEYS = [KeyCode.from_char('c'), Key.enter]


def on_press(key):
    """Get the key pressed and run some code depending on it"""

    if key in LEFT_LEYS:
        pyautogui.move(-SMALL_MOVEMENT, 0)

    if key in DOWN_KEYS:
        pyautogui.move(0, SMALL_MOVEMENT)

    if key in UP_KEYS:
        pyautogui.move(0, -SMALL_MOVEMENT)

    if key in RIGHT_KEYS:
        pyautogui.move(SMALL_MOVEMENT, 0)

    if key == Key.enter:
        pyautogui.click()

    if key in QUIT_KEYS:
        exit()


if __name__ == "__main__":
    notify("Powermouse", "Powermouse running")

    with Listener(on_press=on_press) as listener:
        listener.join()

