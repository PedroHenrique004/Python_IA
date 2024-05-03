

class Bicicleta:
    def __init__(self,cor,modelo,ano,valor): # o self ´w tipo o this do java mas não precisa se chamar self
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("plim plim")

    def parar(self):
        print("Parando bicicleta")
        print("bicicleta parada")

    def correr(self):
        print("Vruuum")

    # def __str__(self):
    #     return f"Bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}"
    
    # Essa faz a mesma coisa mas caso seja adicionado uma caracteristica nova na classe exibira sem precisar atualizar: 
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"
                # Isso exibe o nome da classe          Isso transforma o objeto em um dicionario e exibe ele no modelo chave, valor
    


bike_1 = Bicicleta("Preta", "caloi", 2022, 600)

bike_1.buzinar()
bike_1.correr()
bike_1.parar()

print(bike_1.cor, bike_1.modelo, bike_1.ano, bike_1.valor)
print(bike_1) # Funciona pelo __str__

bike_2 = Bicicleta("Azul", "monark", 2021, 400)

print(bike_2.cor, bike_2.modelo, bike_2.ano, bike_2.valor)