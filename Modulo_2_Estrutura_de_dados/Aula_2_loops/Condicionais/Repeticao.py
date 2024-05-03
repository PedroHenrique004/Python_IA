texto = input("Digite um texto: ")
VOGAIS = "aeiou"

for letra in texto:
    if letra.lower() in VOGAIS:
        print(letra, end="")

print()


for numero in range (0, 51, 5): # o 3 parametro faz ele pular de 5 em 5
    print(numero, end=" ")

opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")