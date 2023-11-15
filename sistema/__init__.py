# from defs.interface import menu, titulo
# from defs.arquivo import arquivo_existe, ler_arquivo, criar_arquivo, novo_cadastro, criar_cadastro
#
# arq = 'cadastro_veiculos.txt'
# if not arquivo_existe(arq):
#     criar_arquivo(arq)
#
# menu_principal = ('Cadastrar novo veículo',
#                   'Visualizar veículos cadastrados',
#                   'Sair')
# while True:
#     resp = menu(menu_principal)
#     if resp == 1:
#         titulo('CADASTRO DE VEICULO')
#         marca = str(input('Marca: ')).strip()
#         modelo = str(input('Modelo: ')).strip()
#         ano = int(input('Ano: '))
#         placa = input('Placa: ').upper()
#         f_placa = placa[-1]
#         ve = criar_cadastro(marca, modelo, ano, placa, f_placa)
#         novo_cadastro(arq, ve)
#     if resp == 2:
#         ler_arquivo(arq)
#     if resp == 3:
#         break
from defs.dados import carregar_dados, menu_principal

def main():
    # Carregar dados existentes
    veiculos = carregar_dados()

    # Chamar o menu principal
    menu_principal(veiculos)

if __name__ == "__main__":
    main()
