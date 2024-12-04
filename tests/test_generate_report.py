import pytest
from finances.nes_finances import Transaction, Account, Investment, Client
from finances.generate_report import generate_report

client_01 = Client([Account("Conta 1", 10.0, [Transaction(10.0, 1, "Asdasd")])], [Investment("Investimento 1", 1, 10.0, 1.5, 'Client_example')])

def test_generate_report():
    report = generate_report(client_01)
    assert report['client_estimate_money'] == client_01.get_net_worth()
    assert report['Accounts'] == ['Conta 1']
    assert report['Investments'] == ['Investimento 1']
    assert report['accounts_current_money'] == sum([account.balance for account in client_01.accounts])