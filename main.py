from classes import Banco, Cliente

def menu():
    print("\n=== Menu ===")
    print("1. Criar Conta")
    print("2. Listar Contas")
    print("3. Consultar Saldo")
    print("4. Depositar")
    print("5. Sacar")
    print("6. Sair")


def main():
    print("Bem vindo ao UVA-BANK")
    banco = Banco()
    banco.criar_banco()

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do cliente: ")
            cliente = Cliente(nome)
            banco.inserir_conta(cliente.identificador, cliente.nome, cliente.saldo)
            print(f"Conta criada com sucesso! ID: {cliente.identificador}")

        elif opcao == "2":
            contas = banco.listar_contas()
            print("\n=== Contas Registradas ===")
            for conta in contas:
                print(f"ID: {conta[0]}, Nome: {conta[1]}, Saldo: {conta[2]}")

        elif opcao == "3":
            conta_id = input("Digite o ID da conta: ")
            conta = banco.buscar_conta(conta_id)
            if conta:
                print(f"Saldo da conta {conta_id}: {conta[2]}")
            else:
                print("Conta não encontrada.")

        elif opcao == "4":
            conta_id = input("Digite o ID da conta: ")
            valor = float(input("Digite o valor a depositar: "))
            conta = banco.buscar_conta(conta_id)
            if conta:
                novo_saldo = conta[2] + valor
                banco.atualizar_saldo(conta_id, novo_saldo)
                print(f"Depósito realizado com sucesso! Novo saldo: {novo_saldo}")
            else:
                print("Conta não encontrada.")

        elif opcao == "5":
            conta_id = input("Digite o ID da conta: ")
            valor = float(input("Digite o valor a sacar: "))
            conta = banco.buscar_conta(conta_id)
            if conta:
                if valor > conta[2]:
                    print("Saldo insuficiente.")
                else:
                    novo_saldo = conta[2] - valor
                    banco.atualizar_saldo(conta_id, novo_saldo)
                    print(f"Saque realizado com sucesso! Novo saldo: {novo_saldo}")
            else:
                print("Conta não encontrada.")

        elif opcao == "6":
            print("Saindo...")
            banco.fechar_banco()
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()