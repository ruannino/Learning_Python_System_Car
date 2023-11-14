from defs.interface import menu, titulo
from defs.arquivo import arquivo_existe, ler_arquivo, criar_arquivo, novo_cadastro

arq = 'cadastro_veiculos.txt'
if not arquivo_existe(arq):
    criar_arquivo(arq)

menu_principal = ('Cadastrar novo veículo',
                  'Visualizar veículos cadastrados',
                  'Sair')
while True:
    resp = menu(menu_principal)
    if resp == 1:
        titulo('CADASTRO DE VEICULO')
        marca = str(input('Marca: ')).strip()
        modelo = str(input('Modelo: ')).strip()
        ano = int(input('Ano: '))
        placa = input('Placa: ').upper()
        f_placa = placa[-1]
        novo_cadastro(arq, marca, modelo, ano, placa, f_placa)
    if resp == 2:
        ler_arquivo(arq)
