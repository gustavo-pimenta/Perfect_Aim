from pynput.mouse import Listener, Button, Controller
import PySimpleGUI as sg
import time

mouse = Controller() # var to control the mouse
shoot = False # trigger to the function
break_program = True # break the main loop

# recoil_size = number of pixels of the recoil
# fire_rate = var inversely proportional to the speed of the loop


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
    [sg.Slider(range=(0, 10), orientation='h', size=(50, 15), default_value=8, tick_interval=2, key='fire_rate')],           
    [sg.Text('')],
    [sg.Text('Made by Pimen_Top                                 '), sg.Button('Stop', size=(10,1)), sg.Button('Start', size=(10,1))]   
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
        
        if start_stop == sg.WIN_CLOSED: 
            break

        if start_stop == 'Start':     
            break_program=False
    
            if (single==True):
                while (break_program == False):
                    
                    single, multiple, recoil_size, fire_rate, start_stop = Iniciar(janela) # get window informations
                    
                    if (shoot==True):
                        mouse.move(0, recoil_size) # move the mouse
                        shoot=False
                    if start_stop == 'Stop':
                        break_program = True

            if (multiple==True):
                while (break_program == False):
                    
                    single, multiple, recoil_size, fire_rate, start_stop = Iniciar(janela) # get window informations

                    if (shoot==True):
                        mouse.move(0, recoil_size) # move the mouse
                        time.sleep((1.01-(fire_rate/10))) # set the fire rate (at least 0.01 to avoid a speed problem)
                    if start_stop == 'Stop':
                        break_program = True

                
    listener.join()












