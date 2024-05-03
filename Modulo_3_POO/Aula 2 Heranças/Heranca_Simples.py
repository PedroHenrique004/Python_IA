class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa 
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor")

class Motocicleta(Veiculo):
    pass

class Caminhao(Veiculo):

    def __init__(self, carregado, cor, placa, numero_rodas): # Preciso passar os argumentos da classe pai aqui se não nao roda
        super().__init__(cor,placa,numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")

class Carro(Veiculo):
    pass

# moto = Motocicleta() -> Assim não funciona pq ela tem as mesmas obrigações da classe pai

moto = Motocicleta("Preta", "abc-1234", 2)
moto.ligar_motor()

carro = Carro("Vermelho", "abc-45678", 4)
carro.ligar_motor()

caminhao = Caminhao("Roxo", "abc-12368", 4, True)
caminhao.ligar_motor()
caminhao.esta_carregado()