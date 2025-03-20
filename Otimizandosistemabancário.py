# Constantes
AGENCIA = "0001"

# Função para cadastrar um usuário
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario_existente = next((user for user in usuarios if user["cpf"] == cpf), None)
    
    if usuario_existente:
        print("Usuário já cadastrado!")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário cadastrado com sucesso!")

# Função para criar uma conta bancária
def criar_conta(usuarios, contas):
    cpf = input("Informe o CPF do usuário: ")
    usuario = next((user for user in usuarios if user["cpf"] == cpf), None)
    
    if not usuario:
        print("Usuário não encontrado. Cadastre o usuário primeiro!")
        return
    
    numero_conta = len(contas) + 1
    contas.append({"agencia": AGENCIA, "numero_conta": numero_conta, "usuario": usuario})
    print(f"Conta {numero_conta} criada com sucesso para {usuario['nome']}!")

# Função de depósito (Positional Only)
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: +R$ {valor:.2f}")
    else:
        print("Valor inválido!")
    return saldo, extrato

# Função de saque (Keyword Only)
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("Saldo insuficiente!")
    elif valor > limite:
        print("Valor excede o limite de saque!")
    elif numero_saques >= limite_saques:
        print("Limite diário de saques atingido!")
    elif valor > 0:
        saldo -= valor
        extrato.append(f"Saque: -R$ {valor:.2f}")
        numero_saques += 1
    else:
        print("Valor inválido!")
    return saldo, extrato

# Função para exibir o extrato (Positional e Keyword Only)
def exibir_extrato(saldo, /, *, extrato):
    print("\nExtrato:")
    print("\n".join(extrato) if extrato else "Nenhuma movimentação registrada.")
    print(f"Saldo atual: R$ {saldo:.2f}")

# Função para listar contas
def listar_contas(contas):
    for conta in contas:
        print(f"Agência: {conta['agencia']}, Conta: {conta['numero_conta']}, Titular: {conta['usuario']['nome']}")

# Execução do sistema
usuarios = []
contas = []
saldo = 0.0
limite = 500.0
extrato = []
numero_saques = 0
limite_saques = 3

while True:
    opcao = input("\n[1] Criar usuário\n[2] Criar conta\n[3] Depositar\n[4] Sacar\n[5] Extrato\n[6] Listar contas\n[0] Sair\nEscolha uma opção: ")
    
    if opcao == "1":
        criar_usuario(usuarios)
    elif opcao == "2":
        criar_conta(usuarios, contas)
    elif opcao == "3":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(saldo, valor, extrato)
    elif opcao == "4":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=limite_saques)
    elif opcao == "5":
        exibir_extrato(saldo, extrato=extrato)
    elif opcao == "6":
        listar_contas(contas)
    elif opcao == "0":
        break
    else:
        print("Opção inválida!")
