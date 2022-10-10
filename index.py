menu = '''
    =======================================

    Escolha a operação que deseja realizar:

    [D] Depositar
    [S] Sacar
    [E] Extrato
    [Q] Sair

    =======================================
    
-> '''

saldo = 0
limite = 500
extrato = ''
numero_de_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'D':
        valor = float(input('Informe o valor do depósito: '))

        if valor > 0:
            saldo += valor
            extrato += f'\tDepósito: R$ {valor:.2f}\n'
            print(f'Deposito no valor de R$ {valor:.2f} realizado com sucesso!')
        else:
            print('A operação falhou! O valor informado é invalido.')

    elif opcao == 'S':
        valor = float(input('Informe o valor do saque: '))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_de_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print('A operação falhou! Você não tem saldo suficiente.')

        elif excedeu_limite:
            print('A operação falhou! O valor do saque excede o limite.')

        elif excedeu_saques:
            print('A operação falhou! Número máximo de saques excedido.')

        elif valor > 0:
            saldo -= valor
            extrato += f'\tSaque: R$ {valor:.2f}\n'
            numero_de_saques += 1
            print(f'Saque no valor de R$ {valor:.2f} realizado com sucesso!')
        
        else:
            print('A operação falhou! O valor informado é inválido.')
    
    elif opcao == 'E':
        print(f'''
    =============== EXTRATO ===============

    {'Não foram realizadas movimentações.' if not extrato else extrato}

    Saldo: R$ {saldo:.2f}

    =======================================
    ''')

    elif opcao == 'Q':
        print('Obrigado por utilizar nossos serviços, até logo!')
        break

    else: 
        print('Operação inválida, por favor selecione novamente a operação desejada.')



