from abc import abstractmethod
from datetime import datetime, date

# Cria o dicionário CATEGORIES como constante para armazenar os tipos de transação
CATEGORIES = {
    1: "Pagamento",
    2: "Depósito",
    3: "Transferência"
}

# Classes
class Transaction:

    def __init__(self, amount: float, category: int, description: str = "") -> None:
        """
        Instancia um objeto da classe Transaction

        args:
          amount(float): A quantidade de dinheiro que será utilizada na transação.
          category(int): A categoria da transação.
          description(str): A descrição da transação.
        """
        self.date = datetime.now()
        if amount < 0:
            raise ValueError("Amount não pode ser negativo")
        self.amount = amount
        # Se a categoria for inválida, mostra um erro
        if category not in CATEGORIES.keys():
            raise ValueError("Categoria inválida")
        self.category = category
        self.description = description
    
    def __str__(self) -> str:
        """
        Retorna as informações da transação

        returns:
          informations(str) -> As informações da transação
        """
        return f"Transação: {self.description} R${round(self.amount, 2)} ({CATEGORIES[self.category]})"

    def update(self, 
               amount: float | None = None,
               category: int | None = None,
               description: str | None = None,
               date: datetime | None = None
               ) -> None:
        """
        Atualiza a transação com novos atributos
        args:
          amount(float | None): Possível nova quantidade de dinheiro que será utilizada na transação.
          category(int | None): Possível nova categoria da transação.
          description(str | None): Possível nova descrição da transação.
          date(datetime | None): Possível nova data de criação da transação.
        """
        # Checa se pode atualizar o atributo, e se puder, o atualiza
        if amount is not None:
            if amount < 0:
              raise ValueError("Amount não pode ser negativo")
            self.amount = amount
        if category is not None:
            if category not in CATEGORIES.keys():
                raise ValueError("Categoria inválida")
            self.category = category
        if description is not None:
            self.description = description
        if date is not None:
            self.date = date


class Account:

    def __init__(self, name: str, balance: float, transactions: list[Transaction]) -> None:
        """
        Instancia um objeto da classe Account

        args:
          name(str): Nome da conta.
          balance(float): Saldo da conta.
          transactions(list[Transaction]): Transações já feitas pela conta
        """
        self.name = name
        if balance < 0:
            raise ValueError("Amount não pode ser negativo")
        self.balance = balance
        self.transactions = transactions
    
    def add_transaction(self, amount: float, category: int, description: str = "") -> None:
        """
        Instancia um objeto da classe Transaction e adiciona ele na lista de transações da conta

        args:
          amount(float): A quantidade de dinheiro que será utilizada na transação.
          category(int): A categoria da transação.
          description(str): A descrição da transação.
        """
        # Instancia a transação e a armazena em self.transactions
        self.transactions.append(Transaction(amount, category, description))
        self.balance += amount
    
    def get_transactions(self, 
                         start_date: datetime | None = None, 
                         end_date: datetime | None = None, 
                         category: int | None = None) -> list[Transaction]:
        """
        Gera uma lista nova de acordo com o atributo transitions.

        args:
          start_date(datetime | None): Apenas transações com datas depois dessa podem ser retornadas.
          end_date(datetime | None): Apenas transações com datas antes dessa podem ser retornadas.
          category(int | None): Apenas transações com categorias iguais a essa podem ser retornadas.

        returns:
          lista_nova(list[Transaction]): O atributo transactions depois das filtragens. 
        """
        return [
          transaction for transaction in self.transactions
          if (start_date is None or transaction.date > start_date)
          and (end_date is None or transaction.date < end_date)
          and (category is None or transaction.category == category)
        ]


class Investment:

    def __init__(self, name: str, investment_type: int, amount: float, rate_of_return: float, client) -> None:
        """
        Instancia um objeto da classe Investment

        args:
          type(int): Tipo de investimento.
          amount(float): Quantidade investida.
          rate_of_return(float): Rate de retorno
        """
        self.name = name
        self.investment_type = investment_type
        if amount < 0:
            raise ValueError("Amount não pode ser negativo")
        self.amount = amount
        self.rate_of_return = rate_of_return
        self.date = datetime.now()
        self.client = client

    def calculate_value(self, estimate_date: date = None) -> float:
        """
        Retorna uma estimativa do retorno de um investimento linear

        args:
          estimate_date(date): A data para o cálculo do valor estimado
        returns:
          valor(float): Valor estimado.
        """
        if estimate_date is None:
            estimate_date = datetime.now()
        months_elapsed = (estimate_date.year - self.date.year) * 12 + (estimate_date.month - self.date.month)
        return self.amount + self.rate_of_return * months_elapsed
    
    def sell(self, account: Account) -> None:
        """
        Vende um investimento para uma conta.

        args:
          account(Account): A conta onde será realizada a venda
        """
        investment_value = self.calculate_value()
        account.balance -= investment_value
        self.client.accounts[0].balance += investment_value
        

class Client:
    

    def __init__(self, accounts: list[Account], investments: list[Investment], name: str = ""):
        """
        Instancia um objeto da classe Client

        args:
          accounts(list[Account]): As contas do Client.
          investments(list[Investment]): Os investimentos do Client.
          name(str): Nome do cliente.
        """
        self.accounts = accounts
        self.investments = investments
        self.name = name

    def add_account(self, acc_name: str) -> Account:
        """
        Instancia um objeto da classe Account que é desse Client

        args:
          acc_name(str): O nome da conta.
        returns:
          new_acc(Account): A conta criada.
        """
        new_acc = Account(acc_name, 0, [])
        self.accounts.append(new_acc)
        return new_acc
    
    def add_investment(self, investment: Investment) -> None:
        """
        Associa um investimento à um cliente

        args:
          investment(Investment): O investimento que será associado.
        """
        self.investments.append(investment)
    
    def get_net_worth(self, estimate_date: date = datetime.now()) -> float:
        """
        Retorna o valor estimado em dinheiro de um cliente de acordo com seus investimentos/contas.

        args:
          estimate_date(date): A data para a estimativa da net_work
        returns:
          new_worth(float): A net worth do Client.
        """
        net_worth = sum(account.balance for account in self.accounts) + sum(investment.calculate_value(estimate_date) for investment in self.investments)
        return net_worth


# Functions

def generate_report(client: Client) -> dict:
    """
    Gera um dicionário com um relatório do cliente atualmente
    
    returns:
      relatorio(dict): O relatório em dicionário que contém como chaves
      os nomes das contas (Accounts), os nomes dos investimentos 
      (Investments), o dinheiro armazenado nas contas (accounts_current_money),
      o dinheiro estimado nos investimentos (investments_current_money),
      e uma estimativa do dinheiro total do cliente (client_estimate_money).
    """
    current_time = datetime.now()
    relatorio = dict()
    relatorio["Accounts"] = [account.name for account in client.accounts]
    relatorio["Investments"] = [investment.name for investment in client.investments]
    accounts_current_money = sum([account.balance for account in client.accounts])
    investments_current_money = sum([investment.calculate_value(current_time) for investment in client.investments])
    relatorio["accounts_current_money"] = accounts_current_money
    relatorio["investments_current_money"] = investments_current_money
    relatorio["client_estimate_money"] = client.get_net_worth(current_time)
    return relatorio

def future_value_report(client: Client, time: date) -> dict:
    """
    Gera um dicionário com um relatório de estimativa do cliente de acordo com uma data.
    
    returns:
      relatorio(dict): O relatório em dicionário que contém como chaves
      os nomes das contas (Accounts), os nomes dos investimentos 
      (Investments), o dinheiro armazenado nas contas (accounts_current_money),
      o dinheiro estimado nos investimentos (investments_current_money),
      e uma estimativa do dinheiro total do cliente (client_estimate_money).
    """
    relatorio = dict()
    relatorio["Accounts"] = [account.name for account in client.accounts]
    relatorio["Investments"] = [investment.name for investment in client.investments]
    accounts_current_money = sum([account.balance for account in client.accounts])
    investments_current_money = sum([investment.calculate_value(time) for investment in client.investments])
    relatorio["accounts_current_money"] = accounts_current_money
    relatorio["investments_current_money"] = investments_current_money
    relatorio["client_estimate_money"] = client.get_net_worth(time)
    return relatorio