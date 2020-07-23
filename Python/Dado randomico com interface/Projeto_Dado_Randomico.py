import PySimpleGUI as sg
from random import choice
from time import sleep

sg.theme('Dark')

layout = [
        [sg.Text('Você deseja jogar o dado?', size=(25, 0))],
        [sg.Button('Sim', size=(5, 0)), sg.Button('Não', size=(5, 0))],
        ]

janela = sg.Window('Jogar dado', layout)

while True:
    event, values = janela.read()
    print(event, values)
    dado = ['1', '2', '3', '4', '5', '6']
    escolha = choice(dado)
    if event == 'Sim':
        sleep(0.5)
        sg.popup('O número sorteado é: ', escolha, font=15)
    elif event == sg.WIN_CLOSED or event == 'Não':
        break

janela.close()

'''# variáveis
dado = [1, 2, 3, 4, 5, 6]
# Prog
while True:
    escolha = str(input('Você deseja jogar o dado ? (S/N): ')).strip().lower()
    while True:
        if escolha not in ('sn'):
            escolha = str(input('Digite somente "S" ou "N". Você deseja jogar o dado ?: '))
        else:
            break
    if escolha == 's':
        print('Rolando dado...')
        sleep(1.5)
        print(f'Valor sorteado: {choice(dado)}')
        sleep(0.5)
    else:
        break
sleep(0.15)
print('\nObrigado por utilizar nosso programa !')'''
