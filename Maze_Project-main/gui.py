# hello_psg.py

import PySimpleGUI as sg



layout = [sg.Text('Select Desired Grid Size'),
          sg.Listbox(values=['10x10', '9x9', '8x8', '7x7', '6x6', '5x5', '4x4'], select_mode='extended', key='gridsize', size=(30, 6))],

# Create the window
window = sg.Window("Welcome!", layout, size = (290, 300))
#window.size(val = "")

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break




window.close()