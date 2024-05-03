class Pessoa:
    


    def __init__(self, nome=None, idade=None):
        self.nome = nome 
        self.idade = idade

    ## Instancia de classe:

    @classmethod
    def achar_data_nascimento(cls,ano,mes,dia,nome):
        idade = 2024 - ano
        return Pessoa(nome, idade)
    
    ## Instancia estatica:

    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18

# p = Pessoa("Pedro", 19)
# print(p.nome, p.idade)

# Esse codigo não fica legal: (cria uma instancia atoa: Pessoa())
# p2 = Pessoa().achar_data_nascimento(2004,13,12, "Pedro")
# print(p2.nome, p2.idade)

# Com o classmethod posso codar assim:
p3 = Pessoa.achar_data_nascimento(2004,13,12, "Pedro")
print(p3.nome, p3.idade)

print(Pessoa.e_maior_idade(28))
print(Pessoa.e_maior_idade(11))