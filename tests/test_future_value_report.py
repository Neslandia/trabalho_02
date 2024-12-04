import pytest
from datetime import datetime
from finances.nes_finances import Transaction, Account, Investment, Client
from finances.future_value_report import future_value_report

client_01 = Client([Account("Conta 1", 10.0, [Transaction(10.0, 1, "Asdasd")])], [Investment("Investimento 1", 1, 10.0, 1.5, 'Client_example')])

def test_generate_report():
    dt_now = datetime.now()
    report = future_value_report(client_01, dt_now)
    assert report['client_estimate_money'] == client_01.get_net_worth(dt_now)
    assert report['Accounts'] == ['Conta 1']
    assert report['Investments'] == ['Investimento 1']
    assert report['accounts_current_money'] == sum([account.balance for account in client_01.accounts])