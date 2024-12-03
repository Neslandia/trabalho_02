import pytest
from finances.nes_finances import Account  # Ajuste o caminho conforme necessário

"""
Faz os testes da classe Account
"""
def test_account_initialization():
    acc = Account(name="Savings", balance=0.0, transactions=[])
    assert acc.name == "Savings"
    assert acc.balance == 0.0
    assert acc.transactions == []

def test_account_add_transaction():
    acc = Account(name="Savings", balance=0, transactions=[])
    t = acc.add_transaction(amount=200.0, category=1, description="Salary")
    assert acc.balance == 200.0
    assert len(acc.transactions) == 1
    assert acc.transactions[0] == t

def test_account_get_transactions():
    acc = Account(name="Savings", balance=0, transactions=[])
    acc.add_transaction(amount=200.0, category=1, description="Salary")
    acc.add_transaction(amount=-50.0, category=2, description="Groceries")
    transactions = acc.get_transactions(category=2)
    assert len(transactions) == 1
    assert transactions[0].category == 2

def test_account_negative_balance():
    acc = Account(name="Savings", balance=0, transactions=[])
    acc.add_transaction(amount=200.0, category=1, description="Salary")
    acc.add_transaction(amount=-250.0, category=3, description="Shopping")
    assert acc.balance == 450.0