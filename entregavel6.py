#modelagem de classes
from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    @abstractmethod
    def calcular_rendimento(self):
        pass

class ContaCorrente(Conta):
    def __init__(self, titular, saldo):
        super().__init__(titular, saldo)

    def calcular_rendimento(self):
        return self.saldo * 0.01

class ContaPoupanca(Conta):
    def __init__(self, titular, saldo):
        super().__init__(titular, saldo)

    def calcular_rendimento(self):
        return self.saldo * 0.05

class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

#contrutor e representação 
class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def __str__(self):
        return f"Cliente: {self.nome} | E-mail: {self.email}"


class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def __str__(self):
        return f"Titular: {self.titular} | Saldo: R$ {self.saldo:.2f}"


cliente = Cliente("João", "joao@gmail.com")
conta = Conta("João", 1500)

print(cliente)
print(conta)

#Encapsulamento com @property
import re

class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        padrao = r"^[\w.+-]+@[\w.-]+\.[a-zA-Z]{2,}$"

        if not re.fullmatch(padrao, valor):
            raise ValueError("E-mail inválido!")

        self._email = valor


class Conta:
    def __init__(self, saldo):
        self.saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("O saldo não pode ser negativo!")

        self._saldo = valor


cliente = Cliente("João", "joao@gmail.com")
conta = Conta(1000)

print(cliente.email)
print(conta.saldo)

#Herança e super()
class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def mostrar_dados(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo: R$ {self.saldo:.2f}")


class ContaCorrente(Conta):
    def __init__(self, titular, saldo, limite):
        super().__init__(titular, saldo)
        self.limite = limite


class ContaPoupanca(Conta):
    def __init__(self, titular, saldo, taxa):
        super().__init__(titular, saldo)
        self.taxa = taxa


corrente = ContaCorrente("João", 1500, 500)
poupanca = ContaPoupanca("Maria", 2000, 0.05)

corrente.mostrar_dados()
poupanca.mostrar_dados()

#Polimorfismo
class Conta:
    def __init__(self, saldo):
        self.saldo = saldo

    def calcular_rendimento(self):
        return 0


class ContaCorrente(Conta):
    def calcular_rendimento(self):
        return self.saldo * 0.01


class ContaPoupanca(Conta):
    def calcular_rendimento(self):
        return self.saldo * 0.05


contas = [
    ContaCorrente(1000),
    ContaPoupanca(1000)
]

for conta in contas:
    print(f"Rendimento: R$ {conta.calcular_rendimento():.2f}")

#Métodos Especiais (Dunder)
class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def __str__(self):
        return f"{self.titular} - R$ {self.saldo:.2f}"

    def __repr__(self):
        return f"Conta({self.titular!r}, {self.saldo!r})"

    def __eq__(self, outra):
        if not isinstance(outra, Conta):
            return NotImplemented
        return self.titular == outra.titular

    def __lt__(self, outra):
        if not isinstance(outra, Conta):
            return NotImplemented
        return self.saldo < outra.saldo


conta1 = Conta("João", 1000)
conta2 = Conta("Maria", 2000)

print(conta1)
print(repr(conta1))
print(conta1 == conta2)
print(conta1 < conta2)

#Testes e Demonstração
class Conta:
    def __init__(self, titular, saldo):
        if saldo < 0:
            raise ValueError("Saldo inválido!")

        self.titular = titular
        self.saldo = saldo

    def calcular_rendimento(self):
        return 0

    def __str__(self):
        return f"{self.titular} - R$ {self.saldo:.2f}"


class ContaCorrente(Conta):
    def calcular_rendimento(self):
        return self.saldo * 0.01


class ContaPoupanca(Conta):
    def calcular_rendimento(self):
        return self.saldo * 0.05


contas = [
    ContaCorrente("João", 1000),
    ContaPoupanca("Maria", 2000),
    ContaCorrente("Pedro", 1500),
    ContaPoupanca("Ana", 3000),
    ContaCorrente("Carlos", 800),
    ContaPoupanca("Julia", 2500),
    ContaCorrente("Lucas", 1200),
    ContaPoupanca("Fernanda", 4000),
    ContaCorrente("Rafael", 900),
    ContaPoupanca("Beatriz", 3500)
]

print("=== RELATÓRIO DE CONTAS ===")

for conta in contas:
    print(f"\n{conta}")
    print(f"Rendimento: R$ {conta.calcular_rendimento():.2f}")

print(f"\nTotal de contas: {len(contas)}")

# Tratamento de exceções
try:
    conta_invalida = ContaCorrente("Teste", -500)

except ValueError as erro:
    print(f"\nErro encontrado: {erro}")