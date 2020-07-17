def validacao(msg):
    while True:
        try:
            i = int(input(msg))
        except (TypeError, ValueError):
            print('\33[31m[ERRO] Digite somente um dos valores indicados\33[m')
        else:
            return i


def linha(tam=40):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(40))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    return validacao('Sua opção: ')


