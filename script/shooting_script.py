from pynput.mouse import Listener, Button, Controller
import time

mouse = Controller() # var to control the mouse
shoot = False # trigger to the function
break_program = False # break the main loop

recoil_size = 10 # number of pixels of the recoil
fire_rate = 0.9 # var inversely proportional to the speed of the loop


def on_move(x, y): # function detects the move of the mouse
    pass

def on_scroll(x, y, dx, dy): # function detects the scroll of the mouse
    pass

def on_click(x, y, button, pressed): # function detects any click of the mouse
    global mouse, shoot
    shoot=False
    
    press=(x, y, button, pressed) # save all mouse status when detect a click 

    # loop to set the trigger when the left button be pressed or released
    if (str(press[2]) == 'Button.left'):
        if (bool(press[3])==True):
            shoot=True
        else:
            shoot=False

# activate the mouse listener
with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    
    # program main loop
    while (break_program == False):

            if (shoot==True):
                mouse.move(0, recoil_size)
                time.sleep((1-fire_rate))

    listener.join()
    


