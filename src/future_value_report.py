from .nes_finances import Client
from datetime import datetime, date

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