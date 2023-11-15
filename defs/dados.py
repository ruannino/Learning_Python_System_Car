import json
from prettytable import PrettyTable
from termcolor import colored  # Certifique-se de instalar o pacote usando: pip install termcolor
veiculos = []

def linha(tam=42):
    return '-' * tam


def titulo(msg):
    print(linha())
    print(f'{msg}'.center(42))
    print(linha())


def cadastrar_veiculo(veiculos):
    titulo('CADASTRO DE VEÍCULO')
    # Implementar a lógica para cadastrar um novo veículo
    marca = input("Marca do veículo: ")
    modelo = input("Modelo do veículo: ")
    ano = input("Ano do veículo: ")
    placa = str(input("Placa do veículo: "))
    final_placa = placa[-1]

    titulo('VALORES RELACIONADOS')
    valor_compra = float(input("Valor de compra do veículo: ").replace(',', '.'))
    valor1 = float(input("Digite o primeiro valor para a média de valores do veículo: ").replace(',', '.'))
    valor2 = float(input("Digite o segundo valor para a média de valores do veículo: ").replace(',', '.'))
    valor3 = float(input("Digite o terceiro valor para a média de valores do veículo: ").replace(',', '.'))
    media_valores = (valor1 + valor2 + valor3) / 3

    # Coleta do percentual de desconto para o valor mínimo de venda
    percentual_desconto = float(input("Digite o percentual de desconto para o valor mínimo de venda: "))
    valor_minimo_venda = media_valores - (media_valores * percentual_desconto / 100)

    # Criar veículo com as informações coletadas
    novo_veiculo = {
        'marca': marca,
        'modelo': modelo,
        'ano': ano,
        'placa': placa,
        'final_placa': final_placa,
        'valor_compra': valor_compra,
        'media_valores': media_valores,
        'percentual_desconto': percentual_desconto,
        'valor_minimo_venda': valor_minimo_venda,
        'pecas': {'compradas': [], 'nao_compradas': []}
    }

    # Adicionar veículo à lista
    veiculos.append(novo_veiculo)

    print("Veículo cadastrado com sucesso!")


def visualizar_veiculos(veiculos):
    print("Veículos Cadastrados:")
    for indice, veiculo in enumerate(veiculos):
        print(f"\nVeículo {indice + 1}:")
        print(f"Marca: {veiculo['marca']}")
        print(f"Modelo: {veiculo['modelo']}")
        print(f"Ano: {veiculo['ano']}")
        print(f"Placa: {veiculo['placa']} - Final: {veiculo['final_placa']}")
        print(f"Valor de Compra: R${veiculo['valor_compra']:.2f}")

    if not veiculos:
        print("Nenhum veículo cadastrado.")

    if veiculos:
        opcao = input("\nDigite o número do veículo para ver detalhes ou pressione Enter para voltar: ")
        if opcao.isdigit() and 1 <= int(opcao) <= len(veiculos):
            veiculo_selecionado = veiculos[int(opcao) - 1]
            visualizar_veiculo(veiculo_selecionado)
        else:
            print("Opção inválida. Voltando ao menu principal.")


def visualizar_veiculo(veiculo):
    # Exibir informações básicas do veículo
    print(f"\nVeículo:")
    print(f"Marca: {veiculo['marca']}")
    print(f"Modelo: {veiculo['modelo']}")
    print(f"Ano: {veiculo['ano']}")
    print(f"Placa: {veiculo['placa']} - Final: {veiculo['final_placa']}")
    print(f"Valor de Compra: R${veiculo['valor_compra']:.2f}")
    print(f"Média de Valores: R${veiculo['media_valores']:.2f}")
    print(f"Percentual de Desconto: {veiculo['percentual_desconto']}%")
    print(f"Valor Mínimo de Venda: R${veiculo['valor_minimo_venda']:.2f}")

    # Criar tabela para resumo do veículo
    tabela_resumo = PrettyTable(["Atributo", "Valor"])
    tabela_resumo.add_row(["Marca", veiculo['marca']])
    tabela_resumo.add_row(["Modelo", veiculo['modelo']])
    tabela_resumo.add_row(["Ano", veiculo['ano']])
    tabela_resumo.add_row(["Placa", f"{veiculo['placa']} - Final: {veiculo['final_placa']}"])
    tabela_resumo.add_row(["Valor de Compra", f"R${veiculo['valor_compra']:.2f}"])
    tabela_resumo.add_row(["Média de Valores", f"R${veiculo['media_valores']:.2f}"])
    tabela_resumo.add_row(["Percentual de Desconto", f"{veiculo['percentual_desconto']}%"])
    tabela_resumo.add_row(["Valor Mínimo de Venda", f"R${veiculo['valor_minimo_venda']:.2f}"])

    print("\nResumo do Veículo:")
    print(tabela_resumo)

    # Calcular total de valor gasto nas peças compradas
    total_valor_pecas_compradas = sum(peca['valor'] for peca in veiculo['pecas']['compradas'])
    print(f"Total de Valor das Peças Compradas: R${total_valor_pecas_compradas:.2f}")

    # Calcular total de valor das peças não compradas
    total_valor_pecas_nao_compradas = sum(peca['valor'] for peca in veiculo['pecas']['nao_compradas'])
    print(f"Total de Valor das Peças Não Compradas: R${total_valor_pecas_nao_compradas:.2f}")

    # Calcular total de valor gasto (veículo + peças compradas)
    total_gasto = veiculo['valor_compra'] + total_valor_pecas_compradas
    print(f"Total Gasto: R${total_gasto:.2f}")

    # Calcular total possível de gastos (veículo + peças compradas + peças não compradas)
    total_possivel = veiculo['valor_minimo_venda'] + total_valor_pecas_compradas + total_valor_pecas_nao_compradas
    print(f"Total Possível de Gastos: R${total_possivel:.2f}")

    # Calcular o lucro (valor mínimo de venda - valor gasto)
    lucro = veiculo['valor_minimo_venda'] - total_gasto
    print(f"Lucro: R${lucro:.2f}")

    # Adicionar opção para acessar o sub-menu
    print("\nOpções:")
    print("1. Informações sobre Peças")
    print("2. Voltar")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        submenu_veiculo(veiculo)
    elif opcao == "2":
        print("Retornando ao menu principal.")
    else:
        print("Opção inválida. Tente novamente.")


def submenu_veiculo(veiculo):
    while True:
        print("\nSub-menu do Veículo:")
        print("1. Resumo do Veículo")
        print("2. Aquisição de Peças")
        print("3. Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            resumo_veiculo(veiculo)
        elif opcao == "2":
            aquisicao_pecas(veiculo)
        elif opcao == "3":
            print("Retornando ao menu de veículo.")
            break
        else:
            print("Opção inválida. Tente novamente.")


def resumo_veiculo(veiculo):
    tabela_resumo = PrettyTable(["Atributo", "Valor"])
    tabela_resumo.add_row(["Marca", veiculo['marca']])
    tabela_resumo.add_row(["Modelo", veiculo['modelo']])
    tabela_resumo.add_row(["Ano", veiculo['ano']])
    tabela_resumo.add_row(["Placa", f"{veiculo['placa']} - Final: {veiculo['final_placa']}"])
    tabela_resumo.add_row(["Valor de Compra", f"R${veiculo['valor_compra']:.2f}"])
    tabela_resumo.add_row(["Média de Valores", f"R${veiculo['media_valores']:.2f}"])
    tabela_resumo.add_row(["Percentual de Desconto", f"{veiculo['percentual_desconto']}%"])
    tabela_resumo.add_row(["Valor Mínimo de Venda", f"R${veiculo['valor_minimo_venda']:.2f}"])

    print("\nResumo do Veículo:")
    print(tabela_resumo)

    print("\nOpções:")
    print("1. Informações sobre Peças")
    print("2. Voltar")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        submenu_veiculo(veiculo)
    elif opcao == "2":
        print("Retornando ao menu principal.")
    else:
        print("Opção inválida. Tente novamente.")


def aquisicao_pecas(veiculo):
    print("\nAquisição de Peças:")
    print("1. Listar Peças")
    print("2. Excluir Peça")
    print("3. Adicionar Peça")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        listar_pecas(veiculo)
    elif opcao == "2":
        excluir_peca(veiculo)
    elif opcao == "3":
        adicionar_peca(veiculo)
    elif opcao == "4":
        print("Retornando ao menu do veículo.")
    else:
        print("Opção inválida. Tente novamente.")


def listar_pecas(veiculo):
    print("\nListar Peças:")

    # Tabela de Peças Compradas (em verde)
    print(colored("Peças Compradas:", 'green'))
    tabela_compradas = PrettyTable(["Índice", "Quantidade", "Descrição", "Valor"])
    for indice, peca_comprada in enumerate(veiculo['pecas']['compradas']):
        tabela_compradas.add_row([indice + 1, peca_comprada['quantidade'], peca_comprada['descricao'], f"R${peca_comprada['valor']:.2f}"])
    print(tabela_compradas)

    # Tabela de Peças Não Compradas (em vermelho)
    print(colored("\nPeças Não Compradas:", 'red'))
    tabela_nao_compradas = PrettyTable(["Índice", "Quantidade", "Descrição", "Valor"])
    for indice, peca_nao_comprada in enumerate(veiculo['pecas']['nao_compradas']):
        tabela_nao_compradas.add_row([indice + 1, peca_nao_comprada['quantidade'], peca_nao_comprada['descricao'], f"R${peca_nao_comprada['valor']:.2f}"])
    print(tabela_nao_compradas)

    # Adicionando informações de valores médios, valor total, etc.
    total_valor_pecas_compradas = sum(peca['valor'] for peca in veiculo['pecas']['compradas'])
    total_valor_pecas_nao_compradas = sum(peca['valor'] for peca in veiculo['pecas']['nao_compradas'])
    total_gasto = veiculo['valor_compra'] + total_valor_pecas_compradas
    total_possivel = veiculo['valor_minimo_venda'] + total_valor_pecas_compradas + total_valor_pecas_nao_compradas

    print(colored(f"\nTotal de Valor das Peças Compradas: R${total_valor_pecas_compradas:.2f}", 'green'))
    print(colored(f"Total de Valor das Peças Não Compradas: R${total_valor_pecas_nao_compradas:.2f}", 'red'))
    print(colored(f"Total Gasto: R${total_gasto:.2f}", 'cyan'))  # Cyan para diferenciar do verde
    print(colored(f"Total Possível de Gastos: R${total_possivel:.2f}", 'yellow'))  # Yellow para diferenciar do verde

    # Calcular o lucro (valor mínimo de venda - valor gasto)
    lucro = veiculo['valor_minimo_venda'] - total_gasto
    print(colored(f"Lucro: R${lucro:.2f}", 'magenta'))  # Magenta para diferenciar do verde


def excluir_peca(veiculo):
    listar_pecas(veiculo)
    indice_peca = int(input("Digite o índice da peça que deseja excluir: "))

    if 1 <= indice_peca <= len(veiculo['pecas']['compradas']):
        veiculo['pecas']['compradas'].pop(indice_peca - 1)
        print("Peça comprada excluída com sucesso.")
    elif 1 <= indice_peca <= len(veiculo['pecas']['nao_compradas']):
        veiculo['pecas']['nao_compradas'].pop(indice_peca - 1)
        print("Peça não comprada excluída com sucesso.")
    else:
        print("Índice inválido. Nenhuma peça excluída.")


def adicionar_peca(veiculo):
    print("\nAdicionar Peça:")
    print("1. Peça Comprada")
    print("2. Peça Não Comprada")

    opcao_peca = input("Escolha uma opção: ")

    if opcao_peca == "1":
        adicionar_peca_comprada(veiculo)
    elif opcao_peca == "2":
        adicionar_peca_nao_comprada(veiculo)
    else:
        print("Opção inválida. Tente novamente.")


def adicionar_peca_comprada(veiculo):
    quantidade = int(input("Digite a quantidade da peça: "))
    descricao = input("Digite a descrição da peça: ")
    valor = float(input("Digite o valor da peça: "))

    nova_peca = {'quantidade': quantidade, 'descricao': descricao, 'valor': valor}
    veiculo['pecas']['compradas'].append(nova_peca)

    print("Peça comprada adicionada com sucesso.")


def adicionar_peca_nao_comprada(veiculo):
    quantidade = int(input("Digite a quantidade da peça: "))
    descricao = input("Digite a descrição da peça: ")
    valor = float(input("Digite o valor estimado da peça: "))

    nova_peca = {'quantidade': quantidade, 'descricao': descricao, 'valor': valor}
    veiculo['pecas']['nao_compradas'].append(nova_peca)

    print("Peça não comprada adicionada com sucesso.")


def media_valores_veiculo(veiculo):
    print("\nMédia de Valores do Veículo:")
    print("1. Adicionar Valores")
    print("2. Editar Valores")
    print("3. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_valores(veiculo)
    elif opcao == "2":
        editar_valores(veiculo)
    elif opcao == "3":
        print("Retornando ao menu do veículo.")
    else:
        print("Opção inválida. Tente novamente.")


def adicionar_valores(veiculo):
    valor1 = float(input("Digite o primeiro valor para a média de valores do veículo: "))
    valor2 = float(input("Digite o segundo valor para a média de valores do veículo: "))
    valor3 = float(input("Digite o terceiro valor para a média de valores do veículo: "))

    veiculo['media_valores'] = (valor1 + valor2 + valor3) / 3

    percentual_desconto = float(input("Digite o percentual de desconto para o valor mínimo de venda: "))
    veiculo['valor_minimo_venda'] = veiculo['media_valores'] - (veiculo['media_valores'] * percentual_desconto / 100)

    print("Valores adicionados com sucesso.")


def editar_valores(veiculo):
    veiculo['media_valores'] = 0
    veiculo['valor_minimo_venda'] = 0

    adicionar_valores(veiculo)

    print("Valores editados com sucesso.")


def salvar_dados(veiculos):
    nome_arquivo = "dados_veiculos.json"

    try:
        with open(nome_arquivo, "w") as arquivo:
            json.dump(veiculos, arquivo, indent=4)
        print(f"Dados salvos com sucesso no arquivo {nome_arquivo}.\n")
    except Exception as erro:
        print(f"Erro ao salvar os dados: {erro}\n")


def carregar_dados():
    veiculos = []

    nome_arquivo = "dados_veiculos.json"

    try:
        with open(nome_arquivo, "r") as arquivo:
            veiculos = json.load(arquivo)
        print(f"Dados carregados com sucesso do arquivo {nome_arquivo}.\n")
    except FileNotFoundError:
        print("Arquivo não encontrado. Criando um novo arquivo.\n")
        salvar_dados(veiculos)
    except Exception as erro:
        print(f"Erro ao carregar os dados: {erro}\n")

    return veiculos


def menu_principal(veiculos):
    while True:
        print()
        titulo('MENU PRINCIPAL')
        print("1 - Cadastrar veículos")
        print("2 - Visualizar veículos cadastrados")
        print("3 - Sair")

        opcao = input("Sua opção: ")

        if opcao == "1":
            cadastrar_veiculo(veiculos)
        elif opcao == "2":
            visualizar_veiculos(veiculos)
        elif opcao == "3":
            salvar_dados(veiculos)  # Salva os dados antes de sair
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    veiculos = carregar_dados()
    menu_principal(veiculos)
