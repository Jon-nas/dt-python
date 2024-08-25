from models.cliente import PessoaFisica
from models.conta import ContaCorrente
from models.transacao import Saque, Deposito
from utils.contas_iterador import ContasIterador

def main():
    endereco = "Rua Exemplo, 123"
    cliente = PessoaFisica("João Silva", "1990-01-01", "123.456.789-00", endereco)
    conta = ContaCorrente.nova_conta(cliente, "12345-6")

    cliente.adicionar_conta(conta)
    deposito = Deposito(1000)
    saque = Saque(200)

    cliente.realizar_transacao(conta, deposito)
    cliente.realizar_transacao(conta, saque)

    contas_iterador = ContasIterador(cliente.contas)
    for conta_info in contas_iterador:
        print(conta_info)

if __name__ == "__main__":
    main()