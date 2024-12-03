import pytest
from datetime import datetime
from finances.nes_finances import Transaction

"""
Testes da classe Transaction 
"""
def test_transaction_initialization():
    t = Transaction(amount=100.0, date=datetime(2024, 11, 28), category=1, description="Grocery shopping")
    assert t.amount == 100.0
    assert t.date == datetime(2024, 11, 28)
    assert t.category == "Food"
    assert t.description == "Grocery shopping"

def test_transaction_str():
    t = Transaction(amount=100.0, date=datetime(2024, 11, 28), category=1, description="Grocery shopping")
    assert str(t) == "Transação: Grocery shopping R$ 100.0 (Food)"

def test_transaction_update():
    t = Transaction(amount=100.0, date=datetime(2024, 11, 28), category=1, description="Grocery shopping")
    t.update(amount=120.0, category="Health")
    assert t.amount == 120.0
    assert t.category == "Health"

def test_transaction_date_update():
    t = Transaction(amount=100.0, date=datetime(2024, 11, 28), category=1, description="Grocery shopping")
    new_date = datetime(2024, 12, 1)
    t.update(date=new_date)
    assert t.date == new_date