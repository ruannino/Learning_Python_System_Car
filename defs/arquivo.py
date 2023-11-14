from defs.interface import titulo

def arquivo_existe(nome):
    """
    -> Verifica se um arquivo existe ou não.
    :param nome: Nome do arquivo.
    :return: Verdadeiro se o arquivo foi encontrado ou Falso se o arquivo não foi encontrado.
    Criado por Ruannino.
    """
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome):
    """
    -> Cria um arquivo de texto.
    :param nome: Recebe o nome do arquivo a ser criado.
    :return: Criação de um arquivo txt.
    Criado por Ruannino.
    """
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um \033[31mERRO\033[m na criação do arquivo!')
    else:
        print(f'\033[32mArquivo {nome} criado com Sucesso!\033[m')


def ler_arquivo(nome):
    """
    -> Faz a leitura de uma arquivo e o ordena em um layout.
    :param nome: Recebe o nome do arquivo a ser lido.
    :return: Imprime os dados do arquivo em um layout ordenado.
    Criado por Ruannino.
    """
    try:
        with open(nome, 'r') as a:
            titulo('VEÍCULOS CADASTRADOS')
            print(f'{"ID":<2} | {"Descrição":<36}')
            cont = 1
            for linha in a:
                linha = linha.strip()

                if linha:
                    dado_str = linha[1:-1]

                    pares = [item.strip() for item in dado_str.split(",")]

                    dado = {}
                    for par in pares:
                        chave, valor = par.split(":")
                        dado[chave.strip()] = valor.strip()

                    modelo = dado.get("'Modelo'", "N/A")
                    placa = dado.get("'Placa'", "N/A")

                    modelo = modelo.replace("'", "")
                    print(f'{cont:<2} | {modelo:<36}'.strip())

    finally:
        a.close()


def novo_cadastro(arquivo, dic):
    try:
        a = open(arquivo, 'at')
    except Exception as e:
        print(f'\033[31mErro!\033[m não consigo abrir o arquivo {arquivo}!')
    else:
        try:
            dic_com_indice = {f'ID': obter_indice(arquivo), **dic}
            a.write(f'{dic_com_indice}/\n')
        except:
            print(f'\033[31mErro!\033[m não consigo escrever no arquivo {arquivo}!')
        else:
            print(f'\033[32mRegistro de veículo adicionado com sucesso!\033[m')
            a.close()


def criar_cadastro(marca='<desconhecida>', modelo='<desconhecido>', ano=0, placa=0, f_placa='N/A'):

    veiculo = {
        'Marca':marca,
        'Modelo':modelo,
        'Ano':ano,
        'Placa':placa,
        'Final da Placa':f_placa
    }
    return veiculo


def obter_indice(arquivo):
    try:
        with open(arquivo, 'rt') as a:
            numero_linhas =sum(1 for linha in a)
    except FileNotFoundError:
        print('Erro!')
        return 1
    except Exception as e:
        return 1
    return numero_linhas + 1

