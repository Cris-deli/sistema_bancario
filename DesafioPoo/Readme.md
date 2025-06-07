# Sistema Bancário em Python 🏦

![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![Status](https://img.shields.io/badge/status-conclu%C3%ADdo-green.svg)
![Licença](https://img.shields.io/badge/licen%C3%A7a-MIT-lightgrey.svg)

> Um sistema bancário simples, construído em Python, que evoluiu de uma abordagem procedural para uma arquitetura robusta e elegante com Programação Orientada a Objetos (POO).

Este projeto simula as operações básicas de um banco, como depósitos, saques e extratos, servindo como um excelente estudo de caso sobre os princípios da POO e a importância da refatoração de código.

---

### ✨ A Jornada da Refatoração: Do Caos à Clareza

Este projeto não nasceu pronto. Ele representa uma jornada de evolução de código:

* **Versão 1 (Procedural):** A primeira versão era funcional, mas utilizava dicionários para armazenar dados de clientes e contas, com funções globais manipulando essas estruturas. Isso tornava o código difícil de manter e escalar.

* **Versão 2 (Orientada a Objetos):** A versão atual! Refatoramos todo o sistema para usar classes, encapsulando dados e comportamentos. O resultado é um código mais limpo, intuitivo e modular.

### ✅ Funcionalidades Principais

O Sistema Bancário permite que você gerencie clientes e suas contas com as seguintes operações:

* **🧑 Novo Cliente:** Cadastre novos clientes (Pessoas Físicas) no sistema.
* **💳 Nova Conta:** Crie contas correntes vinculadas a clientes existentes.
* **💰 Depositar:** Realize depósitos em uma conta.
* **💸 Sacar:** Efetue saques, respeitando o saldo e os limites da conta.
* **🧾 Extrato:** Visualize o histórico de transações de uma conta.
* **📊 Listar Contas:** Exiba todas as contas cadastradas no banco.



### 🏛️ Arquitetura Orientada a Objetos

A mágica acontece aqui! A estrutura do sistema é modelada com as seguintes classes:

* `Cliente`: Classe base que define um cliente com endereço e uma lista de contas.
* `PessoaFisica`: Herda de `Cliente` e adiciona atributos como `nome`, `cpf` e `data_nascimento`.
* `Conta`: Modela os atributos e métodos essenciais de uma conta bancária, como `saldo`, `agencia`, e os métodos `sacar()` e `depositar()`.
* `ContaCorrente`: Herda de `Conta` e implementa regras de negócio específicas, como limite de saques e valor máximo por saque.
* `Operacao`: Classe abstrata que serve de modelo para as transações.
    * `Saque`: Representa uma operação de saque.
    * `Deposito`: Representa uma operação de depósito.
* `Historico`: Uma classe dedicada a registrar e gerenciar todas as transações de uma conta.


### 🛠️ Tecnologias Utilizadas

Este projeto foi construído puramente com:

* **Python 3**

Não são necessárias bibliotecas externas. Apenas o poder da biblioteca padrão!



### 🚀 Como Executar o Projeto

É muito simples colocar o ByteBank para funcionar. Siga os passos abaixo:

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
    ```

2.  **Navegue até o diretório do projeto:**
    ```bash
    cd seu-repositorio
    ```

3.  **Execute o script principal:**
    ```bash
    python main.py
    ```

Pronto! O menu interativo aparecerá no seu terminal.


### 🔭 Para Onde Vamos? (Próximos Passos)

Este projeto tem um grande potencial de expansão. Algumas ideias para o futuro:

* [ ] **Persistência de Dados:** Salvar os dados em um arquivo (`JSON`, `CSV`) ou em um banco de dados (`SQLite`) para que não se percam ao fechar o programa.
* [ ] **Múltiplas Contas:** Permitir que um mesmo cliente tenha mais de uma conta (corrente, poupança).
* [ ] **Transferências:** Implementar a funcionalidade de transferência de valores entre contas.
* [ ] **Testes Unitários:** Adicionar testes para garantir a robustez das classes e métodos.
* [ ] **Interface Gráfica:** Criar uma interface mais amigável usando `Tkinter` ou uma interface web com `Flask`/`Django`.


### 📜 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.



<p align="center">
  Feito com ❤️ por <strong>Carla Andrade]</strong>
</p>
<p align="center">
  <a href="https://www.linkedin.com/in/carlacristinasandrade/]">
    <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" />
  </a>
</p>
