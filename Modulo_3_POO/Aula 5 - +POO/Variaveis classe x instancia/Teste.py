class Estudante:
    escola = "DIO" ## Atributo de classe -> Geral para todos as instancias

    def __init__(self, nome, matricula): ## Nome e matricula sao atributos de instancia, diferentes a cada nova instancia
        self.nome =nome 
        self.matricula = matricula

    def __str__(self):
        return f"{self.nome} - {self.matricula} - {self.escola}"        
    
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

print("")
print("Mostrando valores iniciais:")

aluno_1 = Estudante("Guilherme", 1)   
aluno_2 = Estudante("Giovanna", 2) 

mostrar_valores(aluno_1, aluno_2)

print("")
print("Mostrando valores apos subst da variavel de instancia :")


aluno_1.matricula = 3

mostrar_valores(aluno_1, aluno_2)

print("")
print("Mostrando valores apos subst da variavel de classe:")


Estudante.escola = "Python"

mostrar_valores(aluno_1, aluno_2)