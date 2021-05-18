import json as js
import os.path as osp
import PySimpleGUI as sg
import path as pt

sg.theme("Dark Purple 4")

ELEMENT_PATH = pt.Path("json/element.json")
RETURN_KEY = 'Return:36'

layout = [
    [sg.Text("entrez le nom d'un atome, son symbole ou son numéro atomique")],
    [sg.Input(key='-INPUT-')],
    [sg.Text(size=(40, 1), key='-NAME-')],
    [sg.Text(size=(40, 1), key='-ATOM_NUM-')],
    [sg.Text(size=(40, 1), key='-SYM-')],
    [sg.Text(size=(60, 1), key="-ELEC-")],
    [sg.Button("Search"), sg.Button("Quit")]
]

window = sg.Window("Tableau mandeleiev", layout, return_keyboard_events=True, finalize=True)

while True:
    try:
        event, values = window.read()

        if event in ("Search", RETURN_KEY):
            if osp.exists(ELEMENT_PATH):
                with open(ELEMENT_PATH) as f:
                    data = js.loads(f.read())
                    if values["-INPUT-"] in data:
                        get_name = data[values['-INPUT-']]["NAME"]
                        get_atom = data[values['-INPUT-']]["ATOM_NUM"]
                        get_sym = data[values['-INPUT-']]["SYM"]
                        get_elec = data[values['-INPUT-']]["ELEC"]
                        window['-NAME-'].update("Nom: " + get_name, text_color="white")
                        window['-ATOM_NUM-'].update("Numéro atomique: " + get_atom, text_color="white", visible=True)
                        window['-SYM-'].update("Symbole: " + get_sym, text_color="white", visible=True)
                        window['-ELEC-'].update("Suite Electronique: " + get_elec, text_color="white", visible=True)
                    else:
                        window['-NAME-'].update("aucune référence de cet atome", text_color="red")
                        window['-ATOM_NUM-'](visible=False)
                        window["-SYM-"](visible=False)
                        window["-ELEC-"](visible=False)
        
        elif event in (sg.WINDOW_CLOSED, "Quit"):
            window.close()
            break
    except: print("erreur détecté")
    else: print("le programme c'est lancé sans problème")

