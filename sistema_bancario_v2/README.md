# 🏦 Sistema Bancário em Python

Este é um projeto de um sistema bancário básico desenvolvido em Python. O objetivo principal foi aplicar conceitos fundamentais de programação, como variáveis, condicionais, laços, funções e manipulação de estruturas de dados (listas e dicionários), para criar uma interface de linha de comando funcional.

Este projeto foi desenvolvido como parte de um desafio de curso DIO e evoluiu de um script simples para uma versão mais organizada e funcional, utilizando funções e suportando múltiplos usuários e contas.

## ✨ Funcionalidades

O sistema permite realizar as seguintes operações:

* **🧑 Criar Novo Usuário:** Cadastra um novo cliente com nome, data de nascimento, CPF e endereço. O sistema impede o cadastro de CPFs duplicados.
* **💳 Criar Nova Conta Corrente:** Cria uma nova conta corrente (agência fixa "0001", número sequencial) e a associa a um usuário existente através do CPF. Cada conta possui seu próprio saldo, extrato e limite de saques.
* **💰 Depositar:** Adiciona um valor ao saldo de uma conta específica, registrando a transação no extrato.
* **💸 Sacar:** Retira um valor do saldo de uma conta específica, sujeito a validações:
    * Saldo suficiente.
    * Valor do saque dentro do limite (R$ 500,00 por saque).
    * Número máximo de saques diários (3 saques).
* **🧾 Exibir Extrato:** Mostra todas as transações (depósitos e saques) realizadas em uma conta específica, além do saldo atual.
* **📊 Listar Contas:** Exibe todas as contas correntes cadastradas, mostrando agência, número da conta e nome do titular.
* **🚪 Sair:** Encerra a execução do sistema.

## 🛠️ Tecnologias Utilizadas

* **Python 3:** Linguagem de programação principal utilizada para toda a lógica do sistema.
* **Módulo `textwrap`:** Utilizado para formatar textos multi-linha (como o menu e a listagem de contas) de forma mais limpa no código.

## 🚀 Como Executar

1.  **Pré-requisitos:** Certifique-se de ter o [Python 3](https://www.python.org/downloads/) instalado em sua máquina.
2.  **Clone o Repositório (Opcional):**
    ```bash
    git clone [URL_DO_SEU_REPOSITORIO]
    cd [NOME_DA_PASTA_DO_REPOSITORIO]
    ```
    Ou simplesmente baixe/copie o arquivo `.py` principal.
3.  **Execute o Script:** Abra um terminal ou prompt de comando na pasta onde o arquivo `.py` está localizado e execute o comando:
    ```bash
    python nome_do_seu_arquivo.py
    ```
    *(Substitua `nome_do_seu_arquivo.py` pelo nome real do seu script)*.
4.  **Interaja:** Siga as instruções apresentadas no menu interativo para utilizar as funcionalidades do sistema.

## 📈 Estrutura e Evolução

O código foi estruturado utilizando funções para separar as responsabilidades e tornar o sistema mais modular e legível:

* `menu()`: Exibe as opções.
* `depositar()`, `sacar()`, `exibir_extrato()`: Gerenciam as operações bancárias.
* `criar_usuario()`, `criar_conta()`, `listar_contas()`: Gerenciam usuários e contas.
* `filtrar_usuario()`, `selecionar_conta()`: Funções auxiliares.
* `main()`: Orquestra a execução do programa.

## 👤 Autor

**Carla Andrade**
[LinkedIn](https://www.linkedin.com/in/carlacristinasandrade)
[GitHub] (https://github.com/Cris-deli?tab=repositories)

---
