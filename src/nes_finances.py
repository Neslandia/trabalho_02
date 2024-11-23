from abc import abstractmethod
from datetime import datetime

# Cria o dicionário CATEGORIES como constante para armazenar os tipos de transação
CATEGORIES = {
    1: "Pagamento",
    2: "Depósito",
    3: "Transferência"
}

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
        return f"Transação: {self.description} R${self.amount:.2f} {CATEGORIES[self.category]}"

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
        self.transactions.append(Transaction(amount, category, description))
    
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
        lista_nova = self.transactions
        # Checa se os filtros são ou não aplicados
        if start_date is not None:
            lista_nova = [x for x in lista_nova if x.date > start_date]
        if end_date is not None:
            lista_nova = [x for x in lista_nova if x.date < start_date]
        if category is not None:
            lista_nova = [x for x in lista_nova if x.category == category]
        
        return lista_nova


class Investment:

    def __init__(self, type: int, amount: float, rate_of_return: float, account: Account) -> None:
        """
        Instancia um objeto da classe Investment

        args:
          type(int): Tipo de investimento.
          amount(float): Quantidade investida.
          rate_of_return(float): Rate de retorno
        """
        self.type = type
        self.amount = amount
        self.rate_of_return = rate_of_return
        self.date = datetime.now()
        self.account = account

    def calculate_value(self) -> float:
        """
        Retorna uma estimativa do retorno de um investimento linear

        returns:
          valor(float): Valor estimado.
        """
        return self.amount + self.rate_of_return * (datetime.now() - self.date).month
    
    def sell(self, account: Account) -> None:
        """
        Vende um investimento para uma conta.

        args:
          account(Account): A conta onde será realizada a venda
        """
        if account.balance > self.calculate_value():
            account.balance -= self.calculate_value()
            self.account.balance += self.calculate_value()
        

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
    
    def get_net_worth(self) -> float:
        """
        Retorna o valor estimado em dinheiro de um cliente de acordo com seus investimentos/contas.

        returns:
          new_worth(float): A net worth do Client.
        """
        net_worth = 0
        for i in self.accounts:
            net_worth += i.balance
        for i in self.investments:
            net_worth += i.calculate_value()
        return net_worth
    