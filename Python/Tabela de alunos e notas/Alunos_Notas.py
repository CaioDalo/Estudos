from time import sleep
#Variáveis
lalunos = []
cadastro = []
#Prog.
    #Cadastro das notas dos alunos
while True:
    aluno = str(input('Nome: ')).lower().strip()
    cadastro.append(aluno)
    n1 = float(input('Nota 1: '))
    cadastro.append(n1)
    n2 = float(input('Nota 2: '))
    cadastro.append(n2)
    lalunos.append(cadastro[:])
    cadastro.clear()
    r = str(input('Deseja continuar ? (S/N): ')).lower().strip()
    while True:
        if r == 's' or r == 'n':
            break
        elif r != 's' or r != 'n':
            r = str(input('Digite somente "S" ou "N". Deseja continuar ? (S/N): ')).lower().strip()
            if r == 's' or r == 'n':
                break
    if r == 'n':
        break
#Cálculo da média do aluno e formatação da tabela:
print('-=' * 20 + '-')
print(f'{"Nº":<5}{"NOME":<15}MÉDIA')
print('-' * 30)
for c in range(len(lalunos)):
    media = (lalunos[c][1] + lalunos[c][2]) / 2
    print(f'{c + 1:<5}{lalunos[c][0].capitalize():<15}{media}')
print('-' * 30)
#Mostrar nota individualmente:
while True:
    aluno = int(input('Mostrar notas de qual aluno ? ("999" para interromper): '))
    if aluno == 999:
        break
    escolha = aluno - 1
    print(f'As notas de {lalunos[escolha][0].capitalize()} são {lalunos[escolha][1]} e {lalunos[escolha][2]}')
    print()
print('Finalizando...')
sleep(1)