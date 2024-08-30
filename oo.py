class PrimeiraClasse:
    pass

primeiro_objeto = PrimeiraClasse()
segundo_objeto = PrimeiraClasse()
nome = 'Fatec Araras'
lista = []
print(type(lista))
print(type(nome))
lista.append(nome)
lista.append(primeiro_objeto)

def funcao1(valor):
    return valor

class SegundaClasse:
    def metodo1(self, valor):
        self.valor = valor
        return valor
    
    def metodo2(self, valor):
        return type(valor)
    
    def __str__(self):
        return 'SegundaClasse'

terceiro_objeto = SegundaClasse()
quarto_objeto = SegundaClasse()
print(terceiro_objeto.metodo1(1))
print(terceiro_objeto.metodo1('oi mundo'))
print(terceiro_objeto.metodo1(lista))
quarto_objeto.metodo1 = 12

# Inclimos um novo atributo ao objeto terceiro_objeto
terceiro_objeto.nome = 'Fatec'

# isinstance me ajuda a descobrir de que tipo é o objeto
print(isinstance(quarto_objeto, PrimeiraClasse)) # False
print(isinstance(quarto_objeto, SegundaClasse)) # True

print(issubclass(str,object))

# Demonstramos o conceito de Herança
class Transporte:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0 

class Carro(Transporte):
    def __init__(self, marca, modelo, ano):
        Transporte.__init__(self, marca, modelo, ano) 
 
class Moto(Transporte):
    def __init__(self, marca, modelo, ano):
        Transporte.__init__(self, marca, modelo, ano)    

fusca = Carro('VW', 'Fusca', 1970)
twister = Moto('Honda', 'Twister', 2020)

# Demonstramos o conceito de Herança Múltipla

class Pessoa:
    def __init__(self, nome, profissao):
        self.nome = nome
        self.profissao = profissao

    def mostrar(self):
        print('Pessoa')

class Voar:
    def __init__(self):
        self.voar = True

    def mostrar(self):
        print(' consegue voar')

class SuperForca:
    def __init__(self):
        self.superfoca = True
    
    def mostrar(self):
        print(' tem super força')
        
class Superman( Voar, Pessoa, SuperForca):
    def __init__(self, nome, profissao):
        Pessoa.__init__(self, nome, profissao)
        SuperForca.__init__(self)
        Voar.__init__(self)

    def mostrar(self):
        SuperForca.mostrar(self)

clark = Superman('Clark', 'Reporter')

