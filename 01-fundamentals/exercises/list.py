
transaction1 = {
    'currency': 'CAD',
    'sum': 10.5,
    'date': '10-12-2020'}
transaction2 = {
    'currency': 'USD',
    'sum': 25.5,
    'date': '8-11-2021'}
transaction3 = {
    'currency': 'USD',
    'sum': 11,
    'date': '14-12-2020'}
transaction4 = {
    'currency': 'Bpd',
    'sum': 13.5,
    'date': '10-09-2021'}

transactions = [transaction1, transaction2]
transactions.append(transaction3)
transactions.append(transaction4)

i = 1
sum = 0
for transaction in transactions:
    print(f"Transaction{i} = {transaction['currency']} {transaction['sum']} on {transaction['date']}")
    sum = sum + transaction['sum']
    i += 1

print(f"Total: {sum}")
