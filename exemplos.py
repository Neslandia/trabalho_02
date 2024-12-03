from finances import CATEGORIES
from finances import Transaction
from finances import Account
from finances import Investment
from finances import Client
from finances import generate_report
from finances import future_value_report
from datetime import datetime

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

# Criando um investimento para o cliente
investimento = Investment(name="Fundo de Ações", investment_type=1, amount=10000, rate_of_return=50, client=cliente)

# Associando o investimento ao cliente
cliente.add_investment(investimento)

# Calculando o valor do investimento após 6 meses
data_futura = datetime(2024, 6, 1).date()
valor_estimado = investimento.calculate_value(estimate_date=data_futura)
print(f"Valor estimado do investimento após 6 meses: R${valor_estimado:.2f}")

# Gerando um relatório de saldo atual do cliente

relatorio = generate_report(cliente)

print("\nRelatório de Saldo Atual:")
print(f"Contas: {relatorio['Accounts']}")
print(f"Investimentos: {relatorio['Investments']}")
print(f"Dinheiro nas contas: R${relatorio['accounts_current_money']:.2f}")
print(f"Dinheiro estimado nos investimentos: R${relatorio['investments_current_money']:.2f}")
print(f"Dinheiro total estimado do cliente: R${relatorio['client_estimate_money']:.2f}")

# Gerando um relatório de valor futuro após 12 meses

data_futura = datetime(2025, 6, 1).date()

relatorio_futuro = future_value_report(cliente, data_futura)

print("\nRelatório de Valor Futuro:")
print(f"Contas: {relatorio_futuro['Accounts']}")
print(f"Investimentos: {relatorio_futuro['Investments']}")
print(f"Dinheiro nas contas após 12 meses: R${relatorio_futuro['accounts_current_money']:.2f}")
print(f"Dinheiro estimado nos investimentos após 12 meses: R${relatorio_futuro['investments_current_money']:.2f}")
print(f"Dinheiro total estimado do cliente após 12 meses: R${relatorio_futuro['client_estimate_money']:.2f}")

# Supondo que o cliente tenha uma conta corrente com saldo suficiente para vender o investimento
# Venda do investimento para a conta corrente do cliente

investimento.sell(conta_corrente)

# Verificando o saldo atualizado da conta após a venda do investimento
print(f"Saldo da Conta Corrente após venda do investimento: R${conta_corrente.balance:.2f}")
