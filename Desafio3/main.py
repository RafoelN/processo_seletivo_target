import json

with open('dados.json') as new_json:
    dados = json.load(new_json)

maior_valor = 0

#Processamento para verificar o maior valor
for i in dados:
    if i['valor'] > maior_valor:
        maior_valor = i['valor']

menor_valor = maior_valor
valor_mensal = 0
qtd_dias = 0

#Processamento para verificar o menor valor e também calcular a média mensal
for i in dados:
    if i['valor'] < menor_valor and i['valor'] != 0:
        menor_valor = i['valor']

    valor_mensal = valor_mensal + i['valor']
    qtd_dias = qtd_dias + 1

qtd_valores_acima = 0
#Verificando número de didas em que o valor de faturamento diário foi superior à média mensal
for i in dados:
    if i['valor'] > valor_mensal / qtd_dias:
        qtd_valores_acima = qtd_valores_acima + 1

print(f'O menor valor é:{menor_valor}')
print(f'O maior valor é:{maior_valor}')
print(f'Dado que a média de faturamento diário foi:{valor_mensal/qtd_dias:,.2f} tiveram: {qtd_valores_acima} dias que ultrapassaram')