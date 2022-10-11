import textwrap


def menu():
    menu = '''\n
    ================ MENU =================

    Escolha a operação que deseja realizar:

    [D]\tDepositar
    [S]\tSacar
    [E]\tExtrato
    [NU]\tNovo Usuário
    [LU]\tListar Usuários
    [NC]\tNova Conta
    [LC]\tListar Contas
    [Q]\tSair

    =======================================
    
    -> '''
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito:\tR$ {valor:.2f}\n'
        print(f'\nDeposito no valor de R$ {valor:.2f} realizado com sucesso!')
    else:
        print('\nA operação falhou! O valor informado é invalido.')
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_de_saques, LIMITE_SAQUES):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_de_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print('\nA operação falhou! Você não tem saldo suficiente.')

    elif excedeu_limite:
        print('\nA operação falhou! O valor do saque excede o limite.')

    elif excedeu_saques:
       print('\nA operação falhou! Número máximo de saques excedido.')

    elif valor > 0:
        saldo -= valor
        extrato += f'Saque:\t\tR$ {valor:.2f}\n'
        numero_de_saques += 1
        print(f'\nSaque no valor de R$ {valor:.2f} realizado com sucesso!')
        
    else:
        print('\nA operação falhou! O valor informado é inválido.')
    
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print(f'''
=============== EXTRATO ===============

{'Não foram realizadas movimentações.' if not extrato else extrato}

Saldo:\t\tR$ {saldo:.2f}

=======================================
    ''')

def cadastrar_usuario(usuarios):
    cpf = input('Informe o CPF (somente números): ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\nJá existe um usuário com esse CPF!')
        return
    
    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe o endereço (logadouro, nº - bairro - cidade/UF): ')

    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})

    print('\nUsuário cadastrado com sucesso!')

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def listar_usuarios(usuarios):
    for usuario in usuarios:
        tabela = f'''
            Nome:\t\t{usuario['nome']}
            Data Nasc.:\t{usuario['data_nascimento']}
            CPF:\t\t{usuario['cpf']}
        '''
        print('=' * 40)
        print(textwrap.dedent(tabela))

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('informe o CPF do usuário: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\nConta criada com sucesso!')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
    
    print('Usuário não encontrado, é necessário cadastrar o usuário.')
    return None

def listar_contas(contas):
    for conta in contas:
        linha = f'''
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        '''
        print('=' * 40)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    saldo = 0
    limite = 500
    extrato = ''
    numero_de_saques = 0
    usuarios = []
    contas = []
    numero_conta = 1

    while True:
        opcao = menu()

        if opcao == 'D':
            valor = float(input('Informe o valor do depósito: '))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == 'S':
            valor = float(input('Informe o valor do saque: '))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_de_saques=numero_de_saques,
                LIMITE_SAQUES=LIMITE_SAQUES,
            )

        elif opcao == 'E':
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == 'NU':
            cadastrar_usuario(usuarios)
        
        elif opcao == 'LU':
            listar_usuarios(usuarios)

        elif opcao == 'NC':
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
                numero_conta += 1
         
        elif opcao == 'LC':
            listar_contas(contas)

        elif opcao == 'Q':
            print('\nObrigado por utilizar nossos serviços, tenha um bom dia!')
            break

        else: 
            print('\nOperação inválida, por favor selecione novamente a operação desejada.')

main()