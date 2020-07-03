from pynput.mouse import Listener, Button, Controller
import PySimpleGUI as sg
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


sg.theme('DarkAmber') # window theme

# create window
class TelaPython:
    def __init__(self):
        # window raws:
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
        self.janela = sg.Window('Perfect Aim', layout) 
        

    def Iniciar(self):
        global break_program, shoot
        while True:

            self.button, self.values = self.janela.Read() # get the window info

            single = self.values['single']
            multiple = self.values['multiple']
            recoil_size = self.values['recoil_size']
            fire_rate = self.values['fire_rate']
            start_stop = self.button

            if self.button == sg.WIN_CLOSED: 
                break

            if self.button == 'Start':
                
                break_program=False
                # activate the mouse listener
                with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
                    
                    while (break_program == False):
                
                        if (single==True):
                            if (shoot==True):
                                mouse.move(0, recoil_size)
                                shoot=False
                                if self.button == 'Stop':
                                    break_program = True

                        if (multiple==True):
                            if (shoot==True):
                                mouse.move(0, recoil_size)
                                time.sleep((1-(fire_rate/10)))
                            if self.button == 'Stop':
                                break_program = True

                
                    listener.join()
                    


            
            
                

            # return single, multiple, recoil_size, fire_rate, start_stop
            print(single, multiple, recoil_size, fire_rate, start_stop)
            print('CAIU FORA DO LOOP')


TelaPython().Iniciar()
















