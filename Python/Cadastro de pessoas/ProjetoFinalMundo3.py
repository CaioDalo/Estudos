from ex115.lib.menu import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cadastro.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        cabecalho('PESSOAS CADASTRADAS')
        lerArquivo(arq)
        sleep(1)
    elif resposta == 2:
        cabecalho('CADASTRAR PESSOA')
        nome = str(input('Nome: ')).strip().capitalize()
        idade = validacao('Idade: ')
        cadastrar(arq, nome, idade)
        sleep(1)
    elif resposta == 3:
        print('Saindo do sistema...')
        sleep(0.5)
        break
    else:
        print('\33[31m[ERRO] Digite somente um dos número indicados\33[m')
        sleep(1)
