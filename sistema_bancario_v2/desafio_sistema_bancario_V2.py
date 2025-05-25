import textwrap

def menu():
    """Exibe o menu de opções e retorna a escolha do usuário."""
    menu_texto = """
    ================ MENU ================
    [1]\t💰 Depositar
    [2]\t💸 Sacar
    [3]\t🧾 Extrato
    [4]\t🧑 Novo Usuário
    [5]\t💳 Nova Conta
    [6]\t📊 Listar Contas
    [0]\t🚪 Sair
    => """
    return input(textwrap.dedent(menu_texto))


def depositar(conta, valor):
    """Realiza um depósito na conta especificada."""
    if valor > 0:
        conta['saldo'] += valor
        conta['extrato'] += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
        return True
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
        return False

def sacar(*, conta, valor, limite, limite_saques):
    """Realiza um saque da conta especificada."""
    saldo = conta['saldo']
    numero_saques = conta['numero_saques']

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
    elif valor > 0:
        conta['saldo'] -= valor
        conta['extrato'] += f"Saque:\t\tR$ {valor:.2f}\n"
        conta['numero_saques'] += 1
        print("\n=== Saque realizado com sucesso! ===")
        return True
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
        
    return False

def exibir_extrato(conta):
    """Exibe o extrato da conta especificada."""
    saldo = conta['saldo']
    extrato = conta['extrato']
    
    print("\n================ EXTRATO ================")
    print(f"Conta: {conta['numero_conta']} | Titular: {conta['usuario']['nome']}")
    print("------------------------------------------")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    """Cria um novo usuário no sistema."""
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("\n=== Usuário criado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    """Busca um usuário pelo CPF."""
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios, contas):
    """Cria uma nova conta corrente, associando a um usuário."""
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        # Adiciona saldo, extrato e numero_saques à nova conta
        return {
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": usuario,
            "saldo": 0.0,
            "extrato": "",
            "numero_saques": 0
        }

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
    return None

def listar_contas(contas):
    """Lista todas as contas cadastradas."""
    if not contas:
        print("\n@@@ Nenhuma conta cadastrada. @@@")
        return

    print("\n================ LISTA DE CONTAS ================")
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
            Saldo:\t\tR$ {conta['saldo']:.2f}
        """
        print(textwrap.dedent(linha))
        print("-" * 50)
    print("===============================================")

# --- Função Auxiliar para Selecionar Conta ---

def selecionar_conta(contas):
    """Pede ao usuário o número da conta e a retorna se encontrada."""
    if not contas:
        print("\n@@@ Nenhuma conta cadastrada. Crie uma conta primeiro. @@@")
        return None

    try:
        num_conta = int(input("Informe o número da conta: "))
        for conta in contas:
            if conta['numero_conta'] == num_conta:
                return conta
        print("\n@@@ Conta não encontrada! @@@")
        return None
    except ValueError:
        print("\n@@@ Número da conta inválido. Use apenas números. @@@")
        return None


def main():
    """Função principal que executa o sistema bancário."""
    LIMITE_SAQUES = 3
    LIMITE_VALOR_SAQUE = 500
    AGENCIA = "0001"

    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1": # Depositar
            conta = selecionar_conta(contas)
            if conta:
                valor = float(input("Informe o valor do depósito: "))
                depositar(conta, valor)

        elif opcao == "2": # Sacar
            conta = selecionar_conta(contas)
            if conta:
                valor = float(input("Informe o valor do saque: "))
                sacar(
                    conta=conta,
                    valor=valor,
                    limite=LIMITE_VALOR_SAQUE,
                    limite_saques=LIMITE_SAQUES,
                )

        elif opcao == "3": # Extrato
            conta = selecionar_conta(contas)
            if conta:
                exibir_extrato(conta)

        elif opcao == "4": # Criar Usuário
            criar_usuario(usuarios)

        elif opcao == "5": # Criar Conta
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios, contas)
            if conta:
                contas.append(conta)

        elif opcao == "6": # Listar Contas
            listar_contas(contas)

        elif opcao == "0": # Sair
            print("\nObrigado por usar nosso sistema. Até logo! 👋")
            break

        else:
            print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")

# Executa a função principal
main()