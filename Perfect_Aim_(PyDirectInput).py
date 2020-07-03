import pyautogui
import pydirectinput
import time

# pydirectinput.moveTo(100, 150) # Move the mouse to the x, y coordinates 100, 150.
# pydirectinput.click() # Click the mouse at its current location.
# pydirectinput.click(200, 220) # Click the mouse at the x, y coordinates 200, 220.
# pydirectinput.move(None, 30) # Move mouse 10 pixels down, that is, move the mouse relative to its current position.
# pydirectinput.doubleClick() # Double click the mouse at the
# pydirectinput.press('esc') # Simulate pressing the Escape key.
# pydirectinput.keyDown('shift')
# pydirectinput.keyUp('shift')

from pynput.mouse import Listener, Button, Controller
import PySimpleGUI as sg
import time

mouse = Controller() # var to control the mouse
shoot = False # trigger to the function
break_program = True # break the main loop if True
scroll_up = False # break the main loop if True
scroll_down = False # start the main loop if True
start_by_scroll = False # start the main loop if True

# recoil_size = number of pixels of the recoil
# fire_rate = var inversely proportional to the speed of the loop


def on_move(x, y): # function detects the move of the mouse
    pass

def on_scroll(x, y, dx, dy): # function detects the scroll of the mouse
    global scroll_up, scroll_down
    if (dy == 1):
        scroll_up = True
        scroll_down = False
    if (dy == -1):
        scroll_up = False
        scroll_down = True
    

def on_click(x, y, button, pressed): # function detects any click of the mouse
    global shoot
    shoot=False
    press=(x, y, button, pressed) # save all mouse status when detect a click 

    # loop to set the trigger when the left button be pressed or released
    if (str(press[2]) == 'Button.left'):
        if (bool(press[3])==True):
            shoot=True
        else:
            shoot=False


sg.theme('DarkAmber') # window theme

#create the window interface
layout = [
    [sg.Text('Fire Mode:')],
    [sg.Radio('Single Shot','shot', key='single', default=True), sg.Radio('Multiple Shot', 'shot', key='multiple', default=False)],  
    [sg.Text('')],
    [sg.Text('Recoil Size:')],
    [sg.Slider(range=(0, 200), orientation='h', size=(50, 15), default_value=30, tick_interval=50, key='recoil_size')],     
    [sg.Text('')],
    [sg.Text('Fire Rate:')],
    [sg.Slider(range=(0, 100), orientation='h', size=(50, 15), default_value=80, tick_interval=25, key='fire_rate')],           
    [sg.Text('')],
    [sg.Text('Made by Pimen_Top    '), sg.Button('Stop (or scroll-up)', size=(18,1)), sg.Button('Start (or scroll-down)', size=(18,1))]   
]

janela = sg.Window('Perfect Aim', layout) 
        

def Iniciar(self): # get window informations

    button, values = janela.Read(timeout=10) 
    
    single = values['single']
    multiple = values['multiple']
    recoil_size = values['recoil_size']
    fire_rate = values['fire_rate']
    start_stop = button 
        
    # print(single, multiple, recoil_size, fire_rate, start_stop)
    return single, multiple, recoil_size, fire_rate, start_stop
    

with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener: # start the mouse listener
    
    while True: # program main loop
        
        single, multiple, recoil_size, fire_rate, start_stop = Iniciar(janela) # get window informations
        print(start_stop)
        
        if start_stop == sg.WIN_CLOSED: 
            break

        if scroll_down == True:
            start_by_scroll=True
            scroll_down=False

        if start_stop == 'Start (or scroll-down)' or start_by_scroll==True:     
            break_program=False
            start_by_scroll=False
    
            if (single==True):
                while (break_program == False):
                    single, multiple, recoil_size, fire_rate, start_stop = Iniciar(janela) # get window informations
                    
                    if (shoot==True):
                        pydirectinput.move(0, int(recoil_size)) # PyDirectInput move the mouse
                        shoot=False
                    if (start_stop == 'Stop (or scroll-up)') or (scroll_up == True):
                        break_program = True
                        scroll_up = False

            if (multiple==True):
                while (break_program == False):
                    single, multiple, recoil_size, fire_rate, start_stop = Iniciar(janela) # get window informations

                    if (shoot==True):
                        pydirectinput.move(0, int(recoil_size)) # PyDirectInput move the mouse
                        time.sleep((0.5-((fire_rate-0.001)/200))) # set the fire rate interval (at least 0.001 to avoid a speed problem)
                    if (start_stop == 'Stop (or scroll-up)') or (scroll_up == True):
                        break_program = True
                        scroll_up = False
                
    listener.join()


















