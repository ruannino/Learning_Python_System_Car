def leia_int(msg):
    while True:
        try:
            n = int(input(msg))
        except (TypeError, ValueError):
            print('ERRO! Digite um valor válido!')
            continue
        except (KeyboardInterrupt):
            print('ERRO! Usuário interrompeu a entrada de dados!')
            return 0
        else:
            return n

