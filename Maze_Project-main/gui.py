# hello_psg.py

import PySimpleGUI as sg

names = []
lst = sg.Listbox(names, size=(20, 4), expand_y=True, enable_events=True, key='-LIST-')
layout = [[sg.Input(size=(20, 1), expand_x=True, key='-INPUT-'),
   sg.Button('Select'),
   sg.Button('Add')],
   [lst],
   [sg.Text("Please select grid size", key='-MSG-', font=('Arial Bold', 14), justification='center')]
]

#layout = [sg.Text('Select Desired Grid Size'),
 #         sg.Listbox(values=['10x10', '9x9', '8x8', '7x7', '6x6', '5x5', '4x4'], select_mode='extended', key='gridsize', size=(30, 6))],

window = sg.Window('Please Select Grid Size', layout, size=(600, 200))
while True:
   event, values = window.read()
   print(lst.get())
   if event in (sg.WIN_CLOSED, 'Exit'):
      break
   if event == 'Add':
      names.append(values['-INPUT-'])
      window['-LIST-'].update(names)
      msg = "A new item added : {}".format(values['-INPUT-'])
      window['-MSG-'].update(msg)
   if event == 'Select':
      names.append(values['-INPUT-'])
      window.close()
window.close()