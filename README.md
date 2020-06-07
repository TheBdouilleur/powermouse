# What ?
Powermouse is a cross-platform python program empowering you to move your cursor with your
keyboards, using Vim-inspired keybindings.

# Usage
Download `powermouse.py`, and add a keybinding for it in your DE/WM settings.  
Say i3: add `bindsym $mod+p exec /path/to/powermouse.py` to your config file.

# Requirements
- easy-notify (for notifications): `pip install easy-notify`
- pynput (for reading global keyboard input): `pip install pynput`
- pyautogui (for moving and clicking the cursor): `pip install pyautogui`

# It keeps lagging, what can I do ?
Download [pypy3](https://pypy.org). PyPy is actually a Just-In-Time compiler for
python, making the app really faster.
- Install PyPy3: `sudo pacman -S pypy3`
- Enable pip support in PyPy3: `pypy3 -m ensurepip`
- Install modules: use commands in [requirements](#requirements), adding `pypy3
  -m ` in front of them

