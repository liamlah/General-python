import PySimpleGUI as sg
import webbrowser
sg.theme('BluePurple')

layout = [[sg.Text('Quick Med Search', font='bold')],
         [sg.Text('Search Query:'), sg.Text(size=(1,1))],
         [sg.Input(key='-IN-', size=(25,1))],
         [sg.Button('AMH', size=(21,1))],
         [sg.Button('Amboss', size=(21,1))],
         [sg.Button('BMJ', size=(21,1))],
         [sg.Button('StatPearls', size=(21,1))],
         [sg.Button('RACGP', size=(21,1))],
         [sg.Button('UpToDate', size=(21,1))],
         [sg.Button('Exit', size=(21,1))]]
          




window = sg.Window('QMS', layout, keep_on_top=True)

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'StatPearls' and (values['-IN-']) != "":
        webbrowser.open('https://www.ncbi.nlm.nih.gov/books/NBK430685/?term='+ (values['-IN-']),new=0, autoraise=False)
    if event == 'BMJ' and (values['-IN-']) != "":
        webbrowser.open('https://bestpractice-bmj-com.eu1.proxy.openathens.net/search?q='+ (values['-IN-']),new=0, autoraise=True)
    if event == 'AMH' and (values['-IN-']) != "":
        webbrowser.open('https://amhonline-amh-net-au.eu1.proxy.openathens.net/search?q='+ (values['-IN-']),new=0, autoraise=True)
    if event == 'Amboss' and (values['-IN-']) != "":
        webbrowser.open('https://next.amboss.com/us/search/'+ (values['-IN-']))
    if event == 'NPS' and (values['-IN-']) != "":
        webbrowser.open('https://www.nps.org.au/search?q='+ (values['-IN-']))
    if event == 'UpToDate' and (values['-IN-']) != "":
        webbrowser.open('https://www-uptodate-com.ipacez.nd.edu.au/contents/search?search='+ (values['-IN-']),new=0, autoraise=True)
    if event == 'RACGP' and (values['-IN-']) != "":
        webbrowser.open('https://www.racgp.org.au/search?q='+ (values['-IN-']),new=0, autoraise=True)
        
window.close()
