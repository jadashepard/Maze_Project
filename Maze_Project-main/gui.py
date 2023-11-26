# hello_psg.py

import PySimpleGUI as sg

names = []
names2 = []
names3 = []
names4 = []
lst = sg.Listbox(names, size=(20, 4), expand_y=True, enable_events=True, key='-LIST-')
layout = [[sg.Input(size=(5, 1), expand_x=True, key='-INPUT-'),
   sg.Button('Select'),
   sg.Button('Add')],
   [lst],
   [sg.Text("Please add a grid size", key='-MSG-', font=('Arial Bold', 14), justification='center')]
]

layout2 = [[sg.Menu([['File', ['Exit']]])],
           [sg.T("Please select method of maze creation")], [sg.T("        "), sg.Button('DFS', size=(10, 1)),  sg.Button('Kruskal', size=(10, 1))], [sg.T("")],
           [sg.T("Please select method of maze traversal")], [sg.T("        "), sg.Button('BFS', size=(10, 1)),  sg.Button('Djikstra', size=(10, 1))], [sg.T("")],
           [sg.T("Please select next to execute")], [sg.T("        "), sg.Button('Next', size=(10, 1)),  sg.T('')], [sg.T("")],
          ]



window = sg.Window('Please Enter row height and width of maze as 1 number', layout, size=(500, 200))
names2 = ["10"]
while True:
   event, values = window.read()
   if event in (sg.WIN_CLOSED, 'Exit'):
      break
   if event == 'Add':

      if values['-INPUT-'] == '9' or values['-INPUT-'] == '8' or values['-INPUT-'] == '7' or values['-INPUT-'] == '6' or values['-INPUT-'] == '5' or values['-INPUT-'] == '4' or values['-INPUT-'] == '3' or values['-INPUT-'] == '2':
           names.append(values['-INPUT-'])
           window['-LIST-'].update(names)
           msg = "A new grid size added for selection : {}".format(values['-INPUT-'])
      else: msg = "invalid"

      window['-MSG-'].update(msg)
   if event == 'Select':
      names2 = ['10']
      if values['-INPUT-'] == '9' or values['-INPUT-'] == '8' or values['-INPUT-'] == '7' or values['-INPUT-'] == '6' or values['-INPUT-'] == '5' or values['-INPUT-'] == '4' or values['-INPUT-'] == '3' or values['-INPUT-'] == '2':
        names2 = []
        names2.append(values['-INPUT-'])
   #     window.close()
#next ask the user with which alg to create the maze + with which alg to search it
        #create: DFS or Kruskal’s
        #search: BFS or Dijkstra’s
        #2nd gui window opens here
        window.close()
        window = sg.Window('Please select methods of maze creation + maze traversal', layout2, size = (500,300))
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Exit'):
                break
            if event == 'DFS':
                names3 = []
                names3.append('DFS')
            if event == 'Kruskal':
                names3 = []
                names3.append('Kruskal')
            if event == 'BFS':
                names4 = []
                names4.append('BFS')
            if event == 'Djikstra':
                names4 = []
                names4.append('Djikstra')

            if event == 'Next':

                    window.close()


      else: window['-MSG-'].update('Invalid Input, will default to 10')

window.close()