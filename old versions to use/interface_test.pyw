import PySimpleGUI as sg
import time


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
            [sg.Slider(range=(0, 1000), orientation='h', size=(50, 15), default_value=25, tick_interval=250, key='recoil_size')],     
            [sg.Text('')],
            [sg.Text('Fire Rate:')],
            [sg.Slider(range=(0, 1000), orientation='h', size=(50, 15), default_value=25, tick_interval=250, key='fire_rate')],           
            [sg.Text('')],
            [sg.Text('Made by Pimen_Top                                 '), sg.Button('Stop', size=(10,1)), sg.Button('Start', size=(10,1))]   
        ]
        self.janela = sg.Window('Perfect Aim', layout) 
        

    def Iniciar(self):
        while True:

            self.button, self.values = self.janela.Read() # get the window info

            single = self.values['single']
            multiple = self.values['multiple']
            recoil_size = self.values['recoil_size']
            fire_rate = self.values['fire_rate']
            start_stop = self.button

            if self.button == sg.WIN_CLOSED: 
                break

            if self.button == 'Stop':
                print('parou')
                # break_program = True

            if self.button == 'Start':
                print('roda')
                # break_program = True

            # return single, multiple, recoil_size, fire_rate, start_stop
            print(single, multiple, recoil_size, fire_rate, start_stop)


TelaPython().Iniciar()
