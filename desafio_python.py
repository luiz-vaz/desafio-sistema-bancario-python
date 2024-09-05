# Exibe o menu principal com as opções disponíveis para o usuário
menu = """
Bem vindo ao Vaz Bank! Digite a letra correspondente para acessar serviço desejado:

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

=> """

# Inicializa as variáveis de controle
saldo = 0  # Saldo inicial da conta
extrato = ""  # Registra as transações realizadas
LIMITE_DIARIO = 3  # Limite máximo de saques por dia
saques_feitos = 0  # Contador de saques realizados no dia

# Função para realizar depósitos
def func_deposito():
    data = "04/09/2024"  # Data da transação
    valor_deposito = 0  # Inicializa o valor do depósito
    global saldo  # Permite a modificação da variável global 'saldo'
    registro = ""  # Armazena o registro da transação para o extrato

    # Solicita o valor do depósito ao usuário
    valor_deposito = float(input("Deposito - Por favor insira o valor: R$"))

    # Verifica se o valor do depósito é negativo
    if valor_deposito < 0:
        print("Deposito inválido!!! Valor de deposito negativo\n")
        return ""  # Retorna uma string vazia, não registrando o depósito
    else:
        # Confirma o depósito e atualiza o saldo e o extrato
        print(f"Valor de R$ {valor_deposito:.2f} foi depositado com Sucesso!!\n")
        saldo += valor_deposito
        registro = f"Depósito(+) de R${valor_deposito:.2f} no dia {data}\n"  
        return registro  # Retorna o registro para ser adicionado ao extrato

# Função para realizar saques
def func_saque():
    global saldo  # Permite a modificação da variável global 'saldo'
    limite = 500  # Limite máximo para um saque individual
    registro = ""  # Armazena o registro da transação para o extrato
    data = "04/09/2024"  # Data da transação

    # Solicita o valor do saque ao usuário
    valor_saque = float(input("Saque - Por favor insira o valor: R$"))

    # Verifica se o valor do saque é maior que o saldo disponível
    if valor_saque > saldo:
        print("Não foi possivel realizar operação - SALDO INSUFICIENTE")        
        return None  # Retorna None para indicar que o saque não foi realizado
    # Verifica se o valor do saque excede o limite permitido
    elif valor_saque > limite:
        print(f"Valor de saque maior que limite->R${limite:.2f}")
        return None  # Retorna None para indicar que o saque não foi realizado
    # Verifica se o saque é válido e dentro dos limites
    elif valor_saque <= saldo and valor_saque < limite:
        saldo -= valor_saque  # Deduz o valor do saque do saldo
        print(f"Saque no valor de R${valor_saque:.2f} foi realizado com sucesso")
        registro = f"Saque(-) de R${valor_saque:.2f} no dia {data}\n"
        return registro  # Retorna o registro para ser adicionado ao extrato

# Loop principal que mantém o programa em execução até o usuário sair
while True:    
    # Exibe o menu e solicita uma opção do usuário
    opcao = input(menu).lower()  

    # Opção de depósito
    if opcao == "d":
        extrato += func_deposito()  # Executa a função de depósito e adiciona o registro ao extrato
    # Opção de saque
    elif opcao == "s":
        resultado_saque = func_saque()  # Executa a função de saque e armazena o resultado
        # Verifica se o limite diário de saques foi atingido
        if saques_feitos >= LIMITE_DIARIO:
            print("Atenção: Limite de Saque Diário Atingido")
        # Verifica se o saque foi realizado com sucesso
        elif resultado_saque is not None:
            extrato += resultado_saque  # Adiciona o registro do saque ao extrato
            saques_feitos += 1  # Incrementa o contador de saques realizados
    # Opção para exibir o extrato
    elif opcao == "e":
        # Verifica se há registro no extrato
        if extrato == "":
            print("*"*20, "EXTRATO", "*"*20, "\n", f"Não há transações registras\n Seu Saldo Atual: R$ {saldo:.2f}\n", "*"*48)
        else:
            print("*"*20, "EXTRATO", "*"*20, "\n", f"{extrato}\n Seu Saldo Atual: R$ {saldo:.2f}\n", "*"*48)
    # Opção para sair do programa
    elif opcao == "q":
        break  # Sai do loop e encerra o programa
    # Tratamento para opções inválidas
    else:
        print("Opção Inválida!!!!!!")
