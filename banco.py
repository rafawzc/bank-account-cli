import json
import os


class ContaBancaria:
    def __init__(self, numero, titular, saldo, limite_saque):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite_saque = limite_saque

    def depositar(self, valor):
        if valor <= 0:
            print("Ninguém deposita valor negativo ou 0.00 imenso.")
            return False

        self.saldo += valor
        return True

    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido.")
            return False

        if valor > self.saldo:
            print("Saldo insuficiente pobre.")
            return False

        if valor > self.limite_saque:
            print("Valor excede o limite de saque seu filho da puta.")
            return False

        self.saldo -= valor
        return True

    def transferir(self, destino, valor):
        if self.sacar(valor):
            destino.depositar(valor)
            return True
        return False

    def exibir_saldo(self):
        print(f"Saldo atual: R$ {self.saldo:.2f}")

    def to_dict(self):
        return {
            "numero": self.numero,
            "titular": self.titular,
            "saldo": self.saldo,
            "limite_saque": self.limite_saque
        }

    @staticmethod
    def from_dict(dados):
        return ContaBancaria(
            dados["numero"],
            dados["titular"],
            dados["saldo"],
            dados["limite_saque"]
        )


def salvar_contas(contas):
    with open("contas.json", "w") as arquivo:
        json.dump([conta.to_dict() for conta in contas], arquivo, indent=4)


def carregar_contas():
    if not os.path.exists("contas.json"):
        return []

    with open("contas.json", "r") as arquivo:
        dados = json.load(arquivo)
        return [ContaBancaria.from_dict(conta) for conta in dados]


def encontrar_conta(contas, numero):
    for conta in contas:
        if conta.numero == numero:
            return conta
    return None


def menu():
    contas = carregar_contas()

    while True:
        print("\n1 - Criar conta")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Transferir")
        print("5 - Exibir saldo")
        print("6 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            numero = input("Número da conta: ")
            titular = input("Nome do titular: ")
            saldo = float(input("Saldo inicial: "))
            limite = float(input("Limite de saque: "))

            if encontrar_conta(contas, numero):
                print("Conta já existe.")
                continue

            conta = ContaBancaria(numero, titular, saldo, limite)
            contas.append(conta)
            salvar_contas(contas)
            print("Conta criada com sucesso.")

        elif opcao == "2":
            numero = input("Número da conta: ")
            conta = encontrar_conta(contas, numero)

            if conta:
                valor = float(input("Valor para depósito: "))
                if conta.depositar(valor):
                    salvar_contas(contas)
                    print("Depósito realizado.")
            else:
                print("Conta não encontrada.")

        elif opcao == "3":
            numero = input("Número da conta: ")
            conta = encontrar_conta(contas, numero)

            if conta:
                valor = float(input("Valor para saque: "))
                if conta.sacar(valor):
                    salvar_contas(contas)
                    print("Saque realizado.")
            else:
                print("Conta não encontrada.")

        elif opcao == "4":
            origem_num = input("Conta origem: ")
            destino_num = input("Conta destino: ")

            origem = encontrar_conta(contas, origem_num)
            destino = encontrar_conta(contas, destino_num)

            if origem and destino:
                valor = float(input("Valor para transferir: "))
                if origem.transferir(destino, valor):
                    salvar_contas(contas)
                    print("Transferência realizada.")
            else:
                print("Conta inválida.")

        elif opcao == "5":
            numero = input("Número da conta: ")
            conta = encontrar_conta(contas, numero)

            if conta:
                conta.exibir_saldo()
            else:
                print("Conta não encontrada.")

        elif opcao == "6":
            print("Encerrando sistema.")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()