import PySimpleGUI as sg
import shutil
import patoolib
import os

def RARextractor(rar):
    import rarfile
    extract_to = rar.replace(".rar", "")
    if os.path.exists(extract_to):
        shutil.rmtree(extract_to)
    os.makedirs(extract_to)
    patoolib.extract_archive(rar, outdir=extract_to)

# GUI Menu
sg.theme('Dark Amber')
layout = [  [sg.Text("Select RAR File to be Extracted:"), sg.Input(), sg.FileBrowse(file_types=(("RAR Files", "*.rar"),), key="-IN-")],
            [sg.Button("Submit")]
            ]
window = sg.Window('WinRAR PETRONAS version', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event=="Exit":
        break
    elif event == "Submit":
        sourceFile = values["-IN-"]
        break
window.close()

RARextractor(sourceFile)

# shutil.rmtree('__pycache__')