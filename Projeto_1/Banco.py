deposito = 0
saldo = 0
depositos_total = 0
quantidade_deposito = 0

extrato = ""


saque= 0
saque_diario = 0
saques_total = 0
quantidade_saque = 0

while True:

    tela_extrato = f""" 

        =============================================================================================

        O seu saldo atual é de : R${saldo:.2f}

        Foram feitos {quantidade_deposito} depositos na sua conta no total de R${depositos_total:.2f}
        
        
        Foram feitos {quantidade_saque} depositos na sua conta no total de R${saques_total:.2f}

        {extrato}

        =============================================================================================


    """

    opcao = "dseq"


    menu = """

        --------------------------------------

        Bom dia, o que gostaria de fazer hoje?

        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair

        --------------------------------------

    => """

    acao = input(menu)

    if acao not in opcao:
        print("Digite outro numero")
        acao = input(menu)

    if acao == "d": 

        deposito = float(input("Digite o valor do deposito :"))

        if deposito > 0 and deposito <= 500:
            saldo += deposito
            depositos_total += deposito
            quantidade_deposito += 1
            extrato += f"Depósito: {deposito:.2f}\n"
            print("Valor depositado com sucesso")

        else:
            print("Só são aceitos saques acima de R$0 e abaixo de R$501")
        

    elif acao == "s":

        saque = float(input("Quanto deseja sacar?"))

        if saque_diario > 3:
            print("Não é possivel realizar mais que 3 saques diários!")

        else: 
            if saque > saldo:
                print("Voce não pode sacar mais do que tem de saldo!")
            
            else:
                saldo -= saque
                print("Saque realizado com sucesso!")
                saque_diario += 1
                saques_total += saque
                quantidade_saque += 1
                extrato += f"Saque: {saque:.2f}\n"

    elif acao == "e":
        if quantidade_deposito == 0 and quantidade_saque == 0:
            print("Não foram realizadas movimentações")
        else:
            print(tela_extrato)

    elif acao == "q":
            print("Obrigado pela visita!")
            break


