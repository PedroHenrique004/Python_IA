class Passaro:
    def voar(self): 
        print("Voando...")

class Pardal(Passaro):
    def voar(self):
        print("Pardal pode voar")

class Aveztruz(Passaro):
    def voar(self):
        print("Aveztruz não pode voar")

## Exemplo aleatorio
class Aviao(Passaro):
    def voar(self):
        print("Avião está decolando")

## Não interessa se voa ou nao, isso é metodo passado que sabe
def plano_de_voo(obj):
    obj.voar()

p1 = Pardal()
p2 = Aveztruz()

plano_de_voo(p1)
plano_de_voo(p2)