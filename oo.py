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

class Transporte:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0 

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0 
 
class Moto:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0     
fusca = Carro('VW', 'Fusca', 1970)
