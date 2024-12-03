import pytest
from datetime import datetime
from finances.nes_finances import Investment, Account  # Ajuste o caminho conforme necessário

def test_investment_initialization():
    inv = Investment(investment_type=1, amount=1000.0, rate_of_return=0.05, date_purchased=datetime(2024, 11, 1))
    assert inv.investment_type == 1
    assert inv.initial_amount == 1000.0
    assert inv.rate_of_return == 0.05
    assert inv.date_purchased == datetime(2024, 11, 1)

def test_investment_calculate_value():
    inv = Investment(investment_type=1, amount=1000.0, rate_of_return=0.05, date_purchased=datetime(2024, 1, 1))
    value = inv.calculate_value()
    assert value > 1000.0  # Valor deve ter crescido com o rendimento

def test_investment_sell():
    acc = Account(name="Savings", balance=0, transactions=[])
    inv = Investment(investment_type=1, amount=1000.0, rate_of_return=0.05, date_purchased=datetime(2024, 1, 1))
    inv.sell(account=acc)
    assert acc.balance > 0.0
    assert len(acc.transactions) == 1

def test_investment_partial_growth():
    inv = Investment(investment_type=1, amount=1000.0, rate_of_return=0.03, date_purchased=datetime(2024, 6, 1))
    value = inv.calculate_value()
    assert value > 1000.0  # Rendimento parcial é esperado