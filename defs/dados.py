# Lista global para armazenar os veículos
veiculos = []


def cadastrar_veiculo(veiculos):
    # Implementar a lógica para cadastrar um novo veículo
    marca = input("Digite a marca do veículo: ")
    modelo = input("Digite o modelo do veículo: ")
    ano = input("Digite o ano do veículo: ")
    placa = input("Digite a placa do veículo: ")
    final_placa = placa[-1]
    valor_compra = float(input("Digite o valor de compra do veículo: "))

    # Coleta da média de valores do veículo
    valor1 = float(input("Digite o primeiro valor para a média de valores do veículo: "))
    valor2 = float(input("Digite o segundo valor para a média de valores do veículo: "))
    valor3 = float(input("Digite o terceiro valor para a média de valores do veículo: "))
    media_valores = (valor1 + valor2 + valor3) / 3

    # Coleta do percentual de desconto para o valor mínimo de venda
    percentual_desconto = float(input("Digite o percentual de desconto para o valor mínimo de venda: "))
    valor_minimo_venda = media_valores - (media_valores * percentual_desconto / 100)

    # Criar o dicionário representando o veículo
    veiculo = {
        'marca': marca,
        'modelo': modelo,
        'ano': ano,
        'placa': placa,
        'final_placa': final_placa,
        'valor_compra': valor_compra,
        'media_valores': media_valores,
        'percentual_desconto': percentual_desconto,
        'valor_minimo_venda': valor_minimo_venda,
        'pecas': {
            'compradas': [],
            'nao_compradas': []
        }
    }

    # Adicionar o veículo à lista de veículos
    veiculos.append(veiculo)

    print("Veículo cadastrado com sucesso!\n")


def visualizar_veiculos(veiculos):
    print("Veículos Cadastrados:")
    for indice, veiculo in enumerate(veiculos):
        print(f"\nVeículo {indice + 1}:")
        print(f"Marca: {veiculo['marca']}")
        print(f"Modelo: {veiculo['modelo']}")
        print(f"Ano: {veiculo['ano']}")
        print(f"Placa: {veiculo['placa']} - Final: {veiculo['final_placa']}")
        print(f"Valor de Compra: R${veiculo['valor_compra']:.2f}")
        print(f"Média de Valores: R${veiculo['media_valores']:.2f}")
        print(f"Percentual de Desconto: {veiculo['percentual_desconto']}%")
        print(f"Valor Mínimo de Venda: R${veiculo['valor_minimo_venda']:.2f}")

    if not veiculos:
        print("Nenhum veículo cadastrado.")

    # Adicionar opção para selecionar um veículo para visualização detalhada
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

    # Adicionar opção para acessar o sub-menu
    print("\nOpções:")
    print("1. Resumo do Veículo")
    print("2. Informações sobre Peças")
    print("3. Voltar")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        resumo_veiculo(veiculo)
    elif opcao == "2":
        submenu_veiculo(veiculo)
    elif opcao == "3":
        print("Retornando ao menu principal.")
    else:
        print("Opção inválida. Tente novamente.")


def submenu_veiculo(veiculo):
    while True:
        print("\nSub-menu do Veículo:")
        print("1. Resumo do Veículo")
        print("2. Aquisição de Peças")
        print("3. Média de Valores do Veículo")
        print("4. Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            resumo_veiculo(veiculo)
        elif opcao == "2":
            aquisicao_pecas(veiculo)
        elif opcao == "3":
            media_valores_veiculo(veiculo)
        elif opcao == "4":
            print("Retornando ao menu de veículo.")
            break
        else:
            print("Opção inválida. Tente novamente.")


def resumo_veiculo(veiculo):
    # Exibir informações básicas do veículo
    print(f"\nResumo do Veículo:")
    print(f"Marca: {veiculo['marca']}")
    print(f"Modelo: {veiculo['modelo']}")
    print(f"Ano: {veiculo['ano']}")
    print(f"Placa: {veiculo['placa']} - Final: {veiculo['final_placa']}")
    print(f"Valor de Compra: R${veiculo['valor_compra']:.2f}")
    print(f"Média de Valores: R${veiculo['media_valores']:.2f}")
    print(f"Percentual de Desconto: {veiculo['percentual_desconto']}%")
    print(f"Valor Mínimo de Venda: R${veiculo['valor_minimo_venda']:.2f}")

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


def aquisicao_pecas(veiculo):
    # Implementar a lógica para aquisição de peças
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
    print("Peças Compradas:")
    for indice, peca_comprada in enumerate(veiculo['pecas']['compradas']):
        print(f"{indice + 1}. {peca_comprada['quantidade']}x {peca_comprada['descricao']} - R${peca_comprada['valor']:.2f}")

    print("\nPeças Não Compradas:")
    for indice, peca_nao_comprada in enumerate(veiculo['pecas']['nao_compradas']):
        print(f"{indice + 1}. {peca_nao_comprada['quantidade']}x {peca_nao_comprada['descricao']} - R${peca_nao_comprada['valor']:.2f}")

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
    # Implementar a lógica para média de valores do veículo
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
    veiculo['media_valores'] = 0  # Reinicia a média para recalcular
    veiculo['valor_minimo_venda'] = 0  # Reinicia o valor mínimo de venda para recalcular

    adicionar_valores(veiculo)  # Reutiliza a função de adição de valores

    print("Valores editados com sucesso.")


import os


def salvar_dados(veiculos):
    # Implementar a lógica para salvar os dados em um arquivo TXT
    nome_arquivo = "dados_veiculos.txt"

    try:
        # Verificar se o arquivo já existe
        arquivo_existe = os.path.isfile(nome_arquivo)

        with open(nome_arquivo, "a" if arquivo_existe else "w") as arquivo:
            if not arquivo_existe:
                # Escrever o cabeçalho se o arquivo não existir
                arquivo.write("Dados dos Veículos\n\n")

            for indice, veiculo in enumerate(veiculos, start=1):
                arquivo.write(f"Veículo {indice}:\n")
                arquivo.write(f"Marca: {veiculo['marca']}\n")
                arquivo.write(f"Modelo: {veiculo['modelo']}\n")
                arquivo.write(f"Ano: {veiculo['ano']}\n")
                arquivo.write(f"Placa: {veiculo['placa']}\n")
                arquivo.write(f"Final da Placa: {veiculo['final_placa']}\n")
                arquivo.write(f"Valor de Compra: {veiculo['valor_compra']}\n")
                arquivo.write(f"Média de Valores: {veiculo['media_valores']}\n")
                arquivo.write(f"Percentual de Desconto: {veiculo['percentual_desconto']}\n")
                arquivo.write(f"Valor Mínimo de Venda: {veiculo['valor_minimo_venda']}\n")
                arquivo.write("\n")

        print(f"Dados salvos com sucesso no arquivo {nome_arquivo}.\n")

    except Exception as erro:
        print(f"Erro ao salvar os dados: {erro}\n")


def carregar_dados():
    # Implementar a lógica para carregar os dados de um arquivo TXT
    veiculos = []

    nome_arquivo = "dados_veiculos.txt"

    try:
        with open(nome_arquivo, "r") as arquivo:
            linhas = arquivo.readlines()
            veiculo = None

            for linha in linhas:
                if linha.startswith("Veículo"):
                    # Iniciar um novo veículo
                    veiculo = {'pecas': {'compradas': [], 'nao_compradas': []}}
                elif linha.strip() == "":
                    # Finalizar veículo e adicioná-lo à lista
                    veiculos.append(veiculo)
                else:
                    # Processar linha e adicionar informações ao veículo
                    chave, valor = map(str.strip, linha.split(":", 1))

                    # Converter valores numéricos
                    if chave in ('Valor de Compra', 'Média de Valores', 'Percentual de Desconto', 'Valor Mínimo de Venda'):
                        valor = float(valor)

                    veiculo[chave] = valor

        print(f"Dados carregados com sucesso do arquivo {nome_arquivo}.\n")
        return veiculos

    except FileNotFoundError:
        # Se o arquivo não existir, cria o arquivo e chama a função novamente
        with open(nome_arquivo, "w"):
            pass
        salvar_dados(veiculos)

    except Exception as erro:
        print(f"Erro ao carregar os dados: {erro}\n")
        return []

def menu_principal(veiculos):
    while True:
        print("\nMenu Principal:")
        print("1 - Cadastrar veículos")
        print("2 - Visualizar veículos cadastrados")
        print("3 - Sair")

        opcao = input("Escolha uma opção (1, 2 ou 3): ")

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
