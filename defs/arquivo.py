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
        a = open(nome, 'rt')
    except Exception:
        print(f'\033[31mErro!\033[m não consigo ler o arquivo {nome}!')
    else:
        print('VEÍCULOS CADASTRADOS')
        cont = 1
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{cont:<2} - {dado[0]:<8}{dado[1]:<15} {dado[3]:>3}')
            cont += 1
        print(a.read())
    finally:
        a.close()


def novo_cadastro(arquivo, marca='<desconhecida>', modelo='<desconhecido>', ano=0, placa=0, f_placa='N\A'):
    try:
        a = open(arquivo, 'at')
    except:
        print(f'\033[31mErro!\033[m não consigo abrir o arquivo {arquivo}!')
    else:
        try:
            a.write(f'{marca};{modelo};{ano};{placa};{f_placa}\n')
        except:
            print(f'\033[31mErro!\033[m não consigo escrever no arquivo {arquivo}!')
        else:
            print(f'\033[32mRegistro de {modelo} adicionado com sucesso!\033[m')
            a.close()
