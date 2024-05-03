# Exemplo mais usado:

class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento

    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        _ano_atual = 2024
        return _ano_atual - self._ano_nascimento
    
    def get_nome(self):
        return self.nome
    
    def get_idade(self):
        return 2024 - self._ano_nascimento

pessoa = Pessoa("Pedro", 2004)

print(f"Nome: {pessoa.nome} \t Idade: {pessoa.idade}")
print("")
print(f"Nome: {pessoa.get_nome()} \t Idade: {pessoa.get_idade()}")


### Exemplo base


print("")
print("------------ Exemplo base ------------")
print("")

class Foo:
    def __init__(self, x=None):
        self._x = x

    @property
    def x(self):
        return self._x or 0

    @x.setter
    def x(self, value):
        _x = self._x or 0
        _value = value or 0
        self._x = _x + _value

    @x.deleter
    def x(self):
        self._x = -1

    
foo = Foo(10)

print(foo.x)

foo.x = 100 # não funciona sem o setter

print(foo.x)

del foo.x # Não funcina sem o deleter

print(foo.x)