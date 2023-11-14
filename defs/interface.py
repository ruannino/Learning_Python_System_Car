from defs.operadores import leia_int

def linha(tam=42):
    return '-' * tam


def titulo(txt):
    print(linha())
    print(f'{txt}'.center(42))
    print(linha())


def menu(lista):
    titulo('SISTEMA DE VEÍCULOS')
    c = 1
    for i in lista:
        print(f'{c} - {i}')
        c += 1
    print(linha())
    op = leia_int('Sua opção: ')
    return op
