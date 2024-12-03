import pytest
from datetime import datetime
from finances.nes_finances import Client, Investment  # Ajuste o caminho conforme necessário

def test_client_initialization():
    client = Client(name="John Doe", investments=[], accounts=[])
    assert client.name == "John Doe"
    assert client.accounts == []
    assert client.investments == []

def test_client_add_account():
    client = Client(name="John Doe", investments=[], accounts=[])
    account = client.add_account(account_name="Savings")
    assert account.name == "Savings"
    assert len(client.accounts) == 1
    assert client.accounts[0] == account

def test_client_add_investment():
    client = Client(name="John Doe")
    inv = Investment(investment_type=1, amount=1000.0, rate_of_return=0.05, date_purchased=datetime(2024, 1, 1))
    client.add_investment(investment=inv)
    assert len(client.investments) == 1
    assert client.investments[0] == inv

def test_client_net_worth():
    client = Client(name="John Doe")
    account = client.add_account(account_name="Savings")
    account.add_transaction(amount=1000.0, investment_type=1, description="Salary")
    inv = Investment(investment_type=1, amount=500.0, rate_of_return=0.05, date_purchased=datetime(2024, 1, 1))
    client.add_investment(investment=inv)
    net_worth = client.get_net_worth()
    assert net_worth > 1500.0  # Saldo da conta mais valor do investimento