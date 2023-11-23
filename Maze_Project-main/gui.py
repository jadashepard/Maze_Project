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

lst2 = sg.Text('Please select BFS or Djikstra for maze traversal', size=(10, 10), expand_y=True, enable_events=True, key='-LIST-')
layout2 = [[sg.Input(size=(1, 1), expand_x=True, key='-INPUT-'),
    sg.Button('DFS'),
    sg.Button('Kruskal'),
    [lst2],
    sg.Button('BFS'),
    sg.Button('Djikstra'),
    sg.Button('Next')],
[sg.Text("Please select DFS or Kruskal for maze generation", key='-MSG-', font=('Arial Bold', 14), justification='center')]
]


window = sg.Window('Please Enter row height and width of maze as 1 number', layout, size=(500, 200))
names2 = ["10"]
while True:
   event, values = window.read()
   print(lst.get())
   if event in (sg.WIN_CLOSED, 'Exit'):
      break
   if event == 'Add':
      names.append(values['-INPUT-'])
      window['-LIST-'].update(names)
      msg = "A new grid size added for selection : {}".format(values['-INPUT-'])
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
        window = sg.Window('Please select method of maze creation', layout2, size=(500, 200))
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