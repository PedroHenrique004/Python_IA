menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[nc] Criar novo cliente
[cc] Criar conta corrente
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0

agencia = "0001"
numero_da_conta = 0

clientes = {}
conta_corrente = {}

def depositar(valor, saldo, extrato):
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Deposito realizado com sucesso")
        
        else:
            print("Operação falhou! O valor informado é inválido.")

        return saldo, extrato

def sacar(*, saldo, valor, extrato, numero_saques):
    
    if numero_saques >= 3:
        print("O limite é de 3 saques diários")
    
    else:

        if valor > saldo:
            print("Saldo insuficiente")

        elif valor > 500 or valor <= 0:
            print("Esse valor está fora dos valores permitido")

        else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

            return saldo, extrato, numero_saques
        
def exibir_extrato(saldo, /, *, extrato):

    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario():
    cliente = {}
    cliente["nome"] = input("Digite o nome: ")
    cliente["Data de nascimento"] = input("Digite a data de nascimento: ")
    cliente["cpf"] = input("Digite o CPF: ")

    if cliente["cpf"] in clientes:
        print("Esse cliente já existe")
    else:
        cliente["endereco"] = input("Digite o endereço: ")
        print("Usuário criado com sucesso!")
        clientes[cliente["cpf"]] = cliente

    return cliente

def criar_conta_corrente(clientes, agencia, numero_da_conta):
    numero_da_conta += 1
    cpf_conta = input("Digite o cpf do dono da nova conta: ")

    if cpf_conta in clientes:
        print(f"Conta criada : {agencia}-{numero_da_conta}")
    else:
        print("Não existe usuario com esse cpf")

    return numero_da_conta



while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        saldo, extrato = depositar(valor, saldo, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        saldo, extrato, numero_saques = sacar(saldo=saldo, valor=valor, extrato=extrato, numero_saques=numero_saques)


    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "nc":
      criar_usuario()

    elif opcao == "cc":
      criar_conta_corrente(clientes=clientes, agencia=agencia, numero_da_conta=numero_da_conta)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")