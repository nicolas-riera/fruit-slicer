# Fruit Slicer - Python / pygame

![pythonversion](https://img.shields.io/badge/python-3.x-blue)
![pygame](https://img.shields.io/badge/pygame-required-green)

![logo_title](/assets/img/logo_title.png)

**Fruit Slicer** is a *Fruit Ninja–inspired* arcade game made with **Python and Pygame**.  
The twist? You slice fruits using your **keyboard**, not the mouse or touchscreen.

## Presentation

Fruit Slicer is a reflex-based arcade game where fruits, bombs, and special items appear on the screen.  
Each object is associated with **a unique letter displayed on it**, and the player must press the **correct key at the right moment** to interact with it.

Different objects have different effects:
- Fruits increase your score 
- Bombs make you lose
- Ice items freeze time for a short duration

The goal is to react quickly, press the correct keys, and survive as long as possible to have the highest score.

## Features

- Fruit Ninja–like arcade gameplay
- One keyboard key per object
- Fruits with unique letters
- Bombs to avoid
- Ice items that freeze time for **3 seconds**
- Score system

## Installation (Windows only)

Download the latest release of the l'executable here: https://github.com/nicolas-riera/fruit-slicer/releases/latest

After downloading it, simply run ```Fruit-Slicer_[version].exe``` to launch the game.

## Controls

- **Keyboard**:
    - Use your keyboard to slice items, all letter keys.
    - Go back/close the game with the Escape key.

- **Mouse:**
    - Use your mouse to select buttons on the menu and popups.

## Run and Build from source

### Requirements
- Python **3.x**
- pygame -> ```python -m pip install pygame```
- PyInstaller -> ```python -m pip install pyinstaller```

### Run

From the root folder, run :

```bash
python main.py
```

### Build

To build the game (in .exe for Windows, in .app on MacOs, and as a binary file on Linux), use pyinstaller :

```bash
pyinstaller main.py --onefile --noconsole --icon=assets/img/logo.ico --hidden-import=pygame --name "Fruit-Slicer" --add-data="assets;assets" --add-data="gamedata;gamedata"
```

On ```--add-data```, replace ";" by ":" if you are on MacOS or Linux.

# Authors

This project has been realised by [Nicolas](https://github.com/nicolas-riera), [André](https://github.com/andrebtw) and [Cheikh lo](https://github.com/mbaye-cheikh-lo).

