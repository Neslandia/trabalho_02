# 🚀 Sistema de Gestão de Finanças Pessoais

Este projeto implementa um sistema de gestão de finanças pessoais, permitindo o controle de contas bancárias e investimentos, incluindo a adição de transações e o cálculo de valores futuros de investimentos.

## 🔍 Funcionalidades

- **Contas Bancárias**: O usuário pode adicionar diferentes tipos de contas (corrente, poupança, etc.) e realizar transações como depósitos e retiradas.
- **Investimentos**: Permite o registro de investimentos e a estimativa do valor futuro baseado em taxas de retorno.
- **Relatórios**: Geração de relatórios com o saldo atual das contas e o valor estimado de investimentos.

## 📁 Estrutura do Projeto

A estrutura do diretório do projeto é a seguinte:
```
trabalho_02/
├── src/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── future_value_report.py
│   ├── generate_report.py
│   ├── nes_finances.py
│   ├── relations.txt
│   ├── requirements.txt
├── .gitignore
├── exemplos.py
├── LICENSE
└── README.md
```

## Instalação

No terminal do diretório em que você deseja instalar, digite o código:
```
git clone https://github.com/Neslandia/trabalho_02.git
```

### 📝 Descrição dos Arquivos

- **`generate_report.py`**: Contém a função `generate_report(client)` para gerar um relatório financeiro com o saldo atual das contas e investimentos do cliente.
- **`future_value_report.py`**: Contém a função `future_value_report(client, time)` para gerar um relatório de valor estimado futuro, considerando uma data específica.
- **`nes_finances.py`**: Implementação das classes `Client`, `Account`, `Transaction`, e `Investment`. Também contém métodos como `add_account()`, `add_transaction()`, `get_net_worth()`, entre outros.
- **`exemplos.py`**: Demonstração de como utilizar as classes e funções implementadas.
- **`relations.txt`**: Descrição das relações entre as classes e tipos de relacionamento como herança, agregação, etc.
- **`requirements.txt`**: Arquivo de dependências para o projeto (ainda vazio).

## 💻 Como Rodar

### Requisitos

Para rodar este projeto, você precisará de Python 3.x e das dependências listadas no arquivo `requirements.txt` (atualmente vazio).

1. **Instale as dependências**:

   Se você ainda não tiver o `requirements.txt` configurado, instale as dependências manualmente com:

   ```bash
   pip install <pacote>
   ```

2. **Execute o Código de Exemplo**:

   O arquivo `exemplos.py` contém um exemplo de uso do sistema de finanças. Para executá-lo, rode o seguinte comando:

   ```bash
   python exemplos.py
   ```

## 🧩 Funções e Métodos

### **Funções no módulo `generate_report.py`**

- **`generate_report(client)`**:

  Gera um relatório financeiro com o saldo atual das contas e o valor estimado de investimentos. Retorna um dicionário com as seguintes chaves:
  - `Accounts`: Lista de nomes das contas bancárias do cliente.
  - `Investments`: Lista de nomes dos investimentos do cliente.
  - `accounts_current_money`: Valor total nas contas bancárias.
  - `investments_current_money`: Valor estimado nos investimentos.
  - `client_estimate_money`: Estimativa do valor total do cliente.

  **Exemplo de uso:**

  ```python
  from src import generate_report
  relatorio = generate_report(cliente)
  print(relatorio)
  ```

### 🧩 **Funções no módulo `future_value_report.py`**

- **`future_value_report(client, time)`**:

  Gera um relatório de valor estimado futuro com base em uma data específica. Retorna um dicionário semelhante ao de `generate_report`, mas utilizando a data fornecida para calcular o valor estimado futuro de investimentos e saldo de contas.

  **Exemplo de uso:**

  ```python
  from src import future_value_report
  data_futura = date(2025, 12, 31)
  relatorio_futuro = future_value_report(cliente, data_futura)
  print(relatorio_futuro)
  ```

### 🧩 **Classes no módulo `nes_finances.py`**

```Client```: Representa um cliente com várias contas e investimentos. Permite adicionar contas e realizar transações.

```Account```: Representa uma conta bancária. Permite adicionar transações (depósitos e retiradas).

```Transaction```: Representa uma transação de uma conta. Contém informações como o valor, a categoria (ex: pagamento, depósito) e a descrição da transação.

```Investment```: Representa um investimento do cliente. Permite calcular o valor futuro com base na taxa de retorno e na data de avaliação.

### ```Documentação das Classes e Métodos``:

Este repositório contém a implementação de classes para gerenciar transações, contas bancárias, investimentos e clientes, com o objetivo de simular operações financeiras. Abaixo estão descritos os métodos e suas funcionalidades para cada classe:

---

### Classe `Transaction`
Representa uma transação financeira.

#### Métodos:
- **`__init__(amount: float, category: int, description: str = "")`**
  Constrói uma nova transação com valores validados.
  **Parâmetros:**
  - `amount` (float): Valor da transação.
  - `category` (int): Categoria da transação (baseada no dicionário `CATEGORIES`).
  - `description` (str): Descrição opcional da transação.
  **Erros levantados:**
  - `ValueError` se `amount` for negativo ou `category` inválida.

- **`__str__()`**
  Retorna uma string representando os detalhes da transação.

- **`update(amount: float | None = None, category: int | None = None, description: str | None = None, date: datetime | None = None)`**
  Atualiza os atributos da transação.
  **Parâmetros opcionais:** Novos valores para `amount`, `category`, `description` ou `date`.
  **Erros levantados:**
  - `ValueError` para valores inválidos.

---

### Classe `Account`
Representa uma conta bancária.

#### Métodos:
- **`__init__(name: str, balance: float, transactions: list[Transaction])`**
  Inicializa uma conta com nome, saldo inicial e lista de transações.
  **Parâmetros:**
  - `name` (str): Nome da conta.
  - `balance` (float): Saldo inicial.
  - `transactions` (list[Transaction]): Lista de transações associadas.

- **`add_transaction(amount: float, category: int, description: str = "")`**
  Adiciona uma nova transação à conta e atualiza o saldo.
  **Parâmetros:** Mesmos que a classe `Transaction`.

- **`get_transactions(start_date: datetime | None = None, end_date: datetime | None = None, category: int | None = None)`**
  Filtra transações com base em data ou categoria.
  **Parâmetros opcionais:**
  - `start_date`: Data inicial.
  - `end_date`: Data final.
  - `category`: Categoria desejada.
  **Retorno:** Lista filtrada de `Transaction`.

---

### Classe `Investment`
Representa um investimento feito por um cliente.

#### Métodos:
- **`__init__(name: str, investment_type: int, amount: float, rate_of_return: float, client)`**
  Cria um investimento com valores validados.
  **Parâmetros:**
  - `name` (str): Nome do investimento
  - `investment_type` (int): Tipo de investimento.
  - `amount` (float): Valor investido.
  - `rate_of_return` (float): Taxa de retorno mensal.
  - `client`: Cliente associado.

- **`calculate_value(estimate_date: date = None)`**
  Calcula o valor estimado do investimento com base no tempo.
  **Parâmetros:**
  - `estimate_date` (date, opcional): Data de referência para o cálculo.
  **Retorno:** Valor estimado (float).

- **`sell(account: Account)`**
  Vende o investimento, transferindo o valor para uma conta do cliente.
  **Parâmetros:**
  - `account`: Conta de destino.


### Classe `Client`
Representa um cliente com contas e investimentos.

#### Métodos:
- **`__init__(accounts: list[Account], investments: list[Investment], name: str = "")`**
  Inicializa um cliente com contas e investimentos.
  **Parâmetros:**
  - `accounts`: Lista de contas do cliente.
  - `investments`: Lista de investimentos.
  - `name` (opcional): Nome do cliente.

- **`add_account(acc_name: str)`**
  Cria uma nova conta para o cliente.
  **Parâmetros:**
  - `acc_name`: Nome da conta.
  **Retorno:** Nova conta criada.

- **`add_investment(investment: Investment)`**
  Associa um investimento ao cliente.
  **Parâmetros:**
  - `investment`: Investimento a ser adicionado.

- **`get_net_worth(estimate_date: date = datetime.now())`**
  Calcula o patrimônio líquido estimado do cliente.
  **Parâmetros:**
  - `estimate_date` (opcional): Data de referência para o cálculo.
  **Retorno:** Valor total em contas e investimentos.


### Constante `CATEGORIES`
Um dicionário que mapeia inteiros para categorias de transação:
- `1`: Pagamento
- `2`: Depósito
- `3`: Transferência

## 📌 Exemplo de Uso

### 1. Criando um Cliente, Contas e Realizando Transações
```
from datetime import datetime
from nes_finances import Client, Account, Transaction, CATEGORIES

# Criando o cliente

cliente = Client(accounts=[], investments=[], name="João Silva")

# Criando duas contas para o cliente

conta_corrente = cliente.add_account("Conta Corrente")
conta_poupanca = cliente.add_account("Conta Poupança")

# Adicionando algumas transações às contas

conta_corrente.add_transaction(amount=500, category=1, description="Depósito inicial")
conta_corrente.add_transaction(amount=200, category=2, description="Pagamento de boleto")
conta_poupanca.add_transaction(amount=1500, category=2, description="Depósito inicial")

# Imprimindo as transações
print("Transações Conta Corrente:")
for transacao in conta_corrente.get_transactions():
    print(transacao)

print("\nTransações Conta Poupança:")
for transacao in conta_poupanca.get_transactions():
    print(transacao)
```

Saída esperada:
```
Transações Conta Corrente:
Transação: Depósito inicial R$500.0 (Pagamento)
Transação: Pagamento de boleto R$ 200.0 (Depósito)

Transações Conta Poupança:
Transação: Depósito inicial R$1500.0 (Depósito)
```

### 2. Criando Investimentos e Calculando o Valor Futuro

#### Criando um investimento para o cliente
```
investimento = Investment(name="Fundo de Ações", investment_type=1, amount=10000, rate_of_return=50, client=cliente)

# Associando o investimento ao cliente
cliente.add_investment(investimento)

# Calculando o valor do investimento após 6 meses
data_futura = datetime(2024, 6, 1).date()

valor_estimado = investimento.calculate_value(estimate_date=data_futura)

print(f"Valor estimado do investimento após 6 meses: R${valor_estimado:.2f}")
```

Saída esperada:
```
Valor estimado do investimento após 6 meses: R$ 9700.00

```

### 3. Gerando Relatório de Cliente (Dinheiro Atual nas Contas e Investimentos)

#### Gerando um relatório de saldo atual do cliente
```
from src import generate_report
relatorio = generate_report(cliente)

print("\nRelatório de Saldo Atual:")
print(f"Contas: {relatorio['Accounts']}")
print(f"Investimentos: {relatorio['Investments']}")
print(f"Dinheiro nas contas: R${relatorio['accounts_current_money']:.2f}")
print(f"Dinheiro estimado nos investimentos: R${relatorio['investments_current_money']:.2f}")
print(f"Dinheiro total estimado do cliente: R${relatorio['client_estimate_money']:.2f}")
```

Saída esperada:
```
Relatório de Saldo Atual:
Contas: ['Conta Corrente', 'Conta Poupança']
Investimentos: ['Fundo de Ações']
Dinheiro nas contas: R$2200.00
Dinheiro estimado nos investimentos: R$10000.00
Dinheiro total estimado do cliente: R$12200.00
```

### 4. Gerando Relatório de Valor Futuro de Contas e Investimentos

#### Gerando um relatório de valor futuro após 12 meses
```
data_futura = datetime(2025, 6, 1).date()
from future_value_report import future_value_report

relatorio_futuro = future_value_report(cliente, data_futura)

print("\nRelatório de Valor Futuro:")
print(f"Contas: {relatorio_futuro['Accounts']}")
print(f"Investimentos: {relatorio_futuro['Investments']}")
print(f"Dinheiro nas contas após 12 meses: R${relatorio_futuro['accounts_current_money']:.2f}")
print(f"Dinheiro estimado nos investimentos após 12 meses: R${relatorio_futuro['investments_current_money']:.2f}")
print(f"Dinheiro total estimado do cliente após 12 meses: R${relatorio_futuro['client_estimate_money']:.2f}")
```

Saída esperada:
```
Relatório de Valor Futuro:
Contas: ['Conta Corrente', 'Conta Poupança']
Investimentos: ['Fundo de Ações']
Dinheiro nas contas após 12 meses: R$2200.00
Dinheiro estimado nos investimentos após 12 meses: R$10300.00
Dinheiro total estimado do cliente após 12 meses: R$12500.00
```
### 5. Realizando a Venda de um Investimento
```# Supondo que o cliente tenha uma conta corrente com saldo suficiente para vender o investimento
# Venda do investimento para a conta corrente do cliente
investimento.sell(conta_corrente)

# Verificando o saldo atualizado da conta após a venda do investimento
print(f"Saldo da Conta Corrente após venda do investimento: R${conta_corrente.balance:.2f}")
```

Saída esperada:
```
Saldo da Conta Corrente após venda do investimento: R$700.00
```

## ✍️ Contribuição

Se você deseja contribuir para o projeto, siga as etapas abaixo:

1. Faça um fork deste repositório.
2. Crie uma branch com a sua feature (`git checkout -b feature/nova-feature`).
3. Faça commit das suas mudanças (`git commit -am 'Adicionando 7nova feature'`).
4. Envie para o repositório (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

## 📜 Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👥 Desenvolvedores:

### Almir Sérgio Ramos dos Santos Filho

![almir](imagens/foto_almir.png)

##### contato: almirsergio.a@gmail.com

### João Marcus Vieira de Sena Reis

![joão](imagens/foto_JM.png)

##### contato: joaosenareis@gmail.com