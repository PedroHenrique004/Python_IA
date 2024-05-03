from abc import ABC, abstractmethod, abstractproperty

# Metodo abstrato -> Todas as classes filhas tem que implementa-lo, ele nao precisa de um corpo nescessariamente

class ControleRemoto(ABC):

    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass


    @property  
    @abstractproperty
    def marca(self):
        pass

class ControleArCondicionado(ControleRemoto):

    def ligar (self):
        print("Ligando o ar")

    def desligar(self):
        print("Desligando o ar...")
        print("Desligado!")

    def marca(self):
        print("LG")

class ControleTV(ControleRemoto):

    def ligar (self):
        print("Ligando a TV")

    def desligar(self):
        print("Desligando a tv...")
        print("Desligada!")

    def marca(self):
        print("LG")

## Isso rodava antes: depois de add o abstractmethods, o ControleTV precisa implementar essas classes

# controle = ControleTV()
# controle.ligar()
# controle.desligar()

controle = ControleTV()
controle.ligar()
controle.desligar()
