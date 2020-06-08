# What ?
Powermouse is a cross-platform python program empowering you to move your cursor with your
keyboards, using Vim-inspired keybindings.

# Usage
Download `powermouse.py`, and add a keybinding for it in your DE/WM settings.  
Say i3: add `bindsym $mod+p exec /path/to/powermouse.py` to your config file.

# Features
Currently implemented:
- Small movement navigation:
    - <kbd>h</kbd> for right,
    - <kbd>j</kbd> for down,
    - <kbd>k</kbd> for up,
    - <kbd>l</kbd> for down

- Border movement navigation:
    - <kbd>0</kbd> for rightmost,
    - <kbd>G</kbd> for bottom,
    - <kbd>gg</kbd> for top,
    - <kbd>$</kbd> for leftmost,

- Clicks and Drags:
    - <kbd>c</kbd> for single click,

- Quit:
    - <kbd>q</kbd> for quit,

# Requirements
- easy-notify (for notifications): `pip install easy-notify`
- pynput (for reading global keyboard input): `pip install pynput`
- pyautogui (for moving and clicking the cursor): `pip install pyautogui`
- Linux: python3-xlib (for pyautogui): `sudo pacman -S python3-xlib`
- macOS: rubicon-objc (for pyautogui): `brew install rubicon-objc`

# It keeps lagging, what can I do ?
Download [pypy3](https://pypy.org). PyPy is actually a Just-In-Time compiler for
python, making the app really faster.
- Install PyPy3: `sudo pacman -S pypy3`
- Enable pip support in PyPy3: `pypy3 -m ensurepip`
- Install modules: use commands in [requirements](#requirements), adding `pypy3
  -m ` in front of them

