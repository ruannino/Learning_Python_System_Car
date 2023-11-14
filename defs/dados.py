from defs.interface import titulo
veiculos = list()

def cadastrar_veiculo(marca='<desconhecida>', modelo='<desconhecido>', ano=0, placa=0, f_placa='N\A'):
    titulo('CADASTRO DE VEÍCULO')
    marca = str(input('Marca: ')).strip()
    modelo = str(input('Modelo: ')).strip()
    ano = int(input('Ano: '))
    placa = input('Placa: ').upper()
    f_placa = placa[-1]

    veiculo = {
        'Marca':marca,
        'Modelo':modelo,
        'Ano':ano,
        'Placa':placa,
        'Final da Placa':f_placa
    }
    veiculos = veiculo.copy()
    print('Novo veiculo adicionado com sucesso!')
    print(veiculos)


def exibir_veiculos(list):
     list = veiculos

