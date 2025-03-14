def main():
    saldo = 0.0
    extrato = []
    limite_saque = 500.0
    saques_diarios = 0
    limite_saques = 3
    
    while True:
        print("\n===== MENU =====")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Extrato")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            valor = float(input("Qual valor deseja depositar?: "))
            if valor > 0:
                saldo += valor
                extrato.append(f"Depósito: R$ {valor:.2f}")
                print("Depósito realizado com sucesso!")
            else:
                print("Valor inválido para depósito!")
        
        elif opcao == "2":
            if saques_diarios >= limite_saques:
                print("Desculpe, você atingiu o limite de saque permitido!")
            else:
                valor = float(input("Por favor, Informe o valor que deseja sacar: "))
                if valor > saldo:
                    print("Saldo insuficiente!")
                elif valor > limite_saque:
                    print("O valor máximo para saque é de R$ 500.00!")
                elif valor > 0:
                    saldo -= valor
                    extrato.append(f"Saque: R$ {valor:.2f}")
                    saques_diarios += 1
                    print("O saque foi realizado com sucesso!")
                else:
                    print("Valor inválido para saque!")
        
        elif opcao == "3":
            print("\n===== EXTRATO =====")
            if extrato:
                for movimento in extrato:
                    print(movimento)
            else:
                print("Não foram realizadas movimentações.")
            print(f"Saldo em conta: R$ {saldo:.2f}")
            print("===================")
        
        elif opcao == "4":
            print("Saindo do sistema...")
            break
        
        else:
            print("Opção inválida! Escolha uma opção válida.")

if __name__ == "__main__":
    main()
