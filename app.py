import PySimpleGUI as sg
import random
import string

# Função para gerar senha aleatória com base nas preferências do usuário
def gerar_senha(tamanho, maiusculas, minusculas, numeros, especiais):
    caracteres = ""
    if maiusculas:
        caracteres += string.ascii_uppercase
    if minusculas:
        caracteres += string.ascii_lowercase
    if numeros:
        caracteres += string.digits
    if especiais:
        caracteres += "!@#$%^&*()_+-=[]{}|;:,.<>?"

    if not caracteres:
        sg.popup_error("Selecione pelo menos um tipo de caractere.")
        return ""

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

sg.theme('DarkBlue3')

layout = [
    [sg.Text("Gerador de Senhas Personalizadas", font=("Helvetica", 16))],
    [sg.Text("Tamanho da Senha:"), sg.InputText(key="-TAMANHO-", size=(5, 1))],
    [sg.Checkbox("Maiúsculas", key="-MAIUSCULAS-"), sg.Checkbox("Minúsculas", key="-MINUSCULAS-")],
    [sg.Checkbox("Números", key="-NUMEROS-"), sg.Checkbox("Especiais", key="-ESPECIAIS-")],
    [sg.Text("Senha Gerada: "), sg.Text("", size=(15, 1), key="-SENHA-")],
    [sg.Button("Gerar Senha"), sg.Button("Sair")]
]

window = sg.Window("Gerador de Senhas", layout, finalize=True)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "Sair":
        break
    elif event == "Gerar Senha":
        tamanho = int(values["-TAMANHO-"])
        maiusculas = values["-MAIUSCULAS-"]
        minusculas = values["-MINUSCULAS-"]
        numeros = values["-NUMEROS-"]
        especiais = values["-ESPECIAIS-"]

        senha_gerada = gerar_senha(tamanho, maiusculas, minusculas, numeros, especiais)
        window["-SENHA-"].update(senha_gerada)

window.close()
