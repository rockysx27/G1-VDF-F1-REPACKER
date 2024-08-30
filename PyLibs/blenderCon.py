from pynput.keyboard import Controller as KeyboardController, Key
from pynput.mouse import Controller as MouseController, Button
import time

# Initialize the controllers
keyboard = KeyboardController()
mouse = MouseController()

def double_click():
    """Perform a double-click."""
    mouse.click(Button.left)
    time.sleep(0.1)  # Small delay between clicks
    mouse.click(Button.left)

def perform_actions():
    
    time.sleep(.2)
    mouse.position = (1700, 355)
    time.sleep(.2)
    mouse.click(Button.left)
    
    # Press Right Shift + I
    keyboard.press(Key.shift_r)
    keyboard.press('i')
    keyboard.release('i')
    keyboard.release(Key.shift_r)
    time.sleep(.2)
   
   # Delete Model
    mouse.position = (1150, 355)
    time.sleep(.2)
    mouse.click(Button.left)
    time.sleep(.2)
    keyboard.press(Key.delete)
    keyboard.release(Key.delete)
    time.sleep(.2)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(.2)
    
    # Select Model
    mouse.position = (1150, 355)
    time.sleep(.2)
    double_click()
    time.sleep(.2)
    
    # Select to Merge
    mouse.position = (1069, 500)
    time.sleep(.2)
    mouse.click(Button.left)
    time.sleep(.2)
    
    # Copy Name
    mouse.position = (1415, 380)
    time.sleep(.2)
    double_click()
    time.sleep(.2)
    keyboard.press(Key.ctrl_l)
    keyboard.press('c')
    keyboard.release('c')
    keyboard.release(Key.ctrl_l)
    time.sleep(.2)
    
    # Compile
    mouse.position = (1210, 605)
    time.sleep(.2)
    mouse.click(Button.left)
    time.sleep(.2)
    # Paste Name
    mouse.position = (1840, 445)
    time.sleep(.2)
    mouse.click(Button.left)
    time.sleep(.2)
    keyboard.press(Key.ctrl_l)
    keyboard.press('v')
    keyboard.release('v')
    keyboard.release(Key.ctrl_l)
    time.sleep(.1)
    
    #remove .ext
    keyboard.press(Key.backspace)
    keyboard.release(Key.backspace)
    time.sleep(.1)
    keyboard.press(Key.backspace)
    keyboard.release(Key.backspace)
    time.sleep(.1)
    keyboard.press(Key.backspace)
    keyboard.release(Key.backspace)
    time.sleep(.1)
    keyboard.press(Key.backspace)
    keyboard.release(Key.backspace)
    
# Execute the actions
perform_actions()
