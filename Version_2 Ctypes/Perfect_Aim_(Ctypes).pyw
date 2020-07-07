
from pynput.mouse import Listener, Button, Controller
import PySimpleGUI as sg
import time
import ctypes

# MouseMoveTo(x,y)
# PressKey(hexkey_code)
# ReleaseKey(hexkey_code)

mouse = Controller() # var to control the mouse
shoot = False # trigger to the function
break_program = True # break the main loop if True
scroll_button = False # True if scroll button be pressed 
start_by_scroll = False # start the main loop if True

# recoil_size = number of pixels of the recoil
# fire_rate = var inversely proportional to the speed of the loop

# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions
def MouseMoveTo(x, y):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.mi = MouseInput(x, y, 0, 0x0001, 0, ctypes.pointer(extra))

    command = Input(ctypes.c_ulong(0), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(command), ctypes.sizeof(command))

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def on_move(x, y): # function detects the move of the mouse
    pass

def on_scroll(x, y, dx, dy): # function detects the scroll of the mouse
   pass
    
def on_click(x, y, button, pressed): # function detects any click of the mouse
    global shoot, scroll_button
    shoot=False
    press=(x, y, button, pressed) # save all mouse status when detect a click 

    # set the trigger when the left button be pressed or released
    if (str(press[2]) == 'Button.left'):
        if (bool(press[3])==True):
            shoot=True          
        else:
            shoot=False

    elif (str(press[2]) == 'Button.middle'): # start and pause
        if (bool(press[3])==True):
            scroll_button=True

sg.theme('DarkAmber') # window theme

#create the window interface
layout = [
    [sg.Text('                                                                         Made by Gustavo Pimenta')],
    [sg.Text('Fire Mode:')],
    [sg.Radio('Single Shot','shot', key='single', default=True), sg.Radio('Multiple Shot', 'shot', key='multiple', default=False)],  
    [sg.Text('')],
    [sg.Text('Recoil Size:')],
    [sg.Slider(range=(0, 200), orientation='h', size=(50, 15), default_value=30, tick_interval=50, key='recoil_size')],     
    [sg.Text('')],
    [sg.Text('Fire Rate:')],
    [sg.Slider(range=(0, 100), orientation='h', size=(50, 15), default_value=80, tick_interval=25, key='fire_rate')],           
    [sg.Text('')],
    [sg.Button('Start (press scroll button)', size=(26,1)), sg.Button('Stop (press scroll button)', size=(26,1))]  
]

janela = sg.Window('Perfect Aim', layout) 
        
def Iniciar(self): # get window informations

    button, values = janela.Read(timeout=10) 
    
    single = values['single']
    multiple = values['multiple']
    recoil_size = values['recoil_size']
    fire_rate = values['fire_rate']
    start_stop = button 
        
    return single, multiple, recoil_size, fire_rate, start_stop
    

with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener: # start the mouse listener
    
    while True: # program main loop
        
        try:
            single, multiple, recoil_size, fire_rate, start_stop = Iniciar(janela) # get window informations
        except:
            break # Error if the window be closed
        
        if start_stop == sg.WIN_CLOSED: 
            break

        if scroll_button==True:
            start_by_scroll=True
            scroll_button=False

        if start_stop == 'Start (press scroll button)' or start_by_scroll==True:     
            break_program=False

            if (single==True):
                while (break_program == False):
                    
                    single, multiple, recoil_size, fire_rate, start_stop = Iniciar(janela) # get window informations
                    
                    if (shoot==True):
                        MouseMoveTo(0,int(recoil_size)) # ctypes move the mouse
                        shoot=False
                    if (start_stop == 'Stop (press scroll button)') or (scroll_button==True):
                        break_program = True
                        scroll_button = False
                        start_by_scroll = False
                        
            if (multiple==True):
                while (break_program == False):
                    single, multiple, recoil_size, fire_rate, start_stop = Iniciar(janela) # get window informations

                    if (shoot==True):
                        MouseMoveTo(0,int(recoil_size)) # ctypes move the mouse
                        time.sleep((0.5-((fire_rate-0.001)/200))) # set the fire rate interval (at least 0.001 to avoid a speed problem)
                    if (start_stop == 'Stop (press scroll button)') or (scroll_button==True):
                        break_program = True
                        scroll_button = False
                        start_by_scroll = False
              
    listener.join()












