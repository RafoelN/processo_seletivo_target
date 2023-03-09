sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

total = sp + rj + mg + es + outros

print(f'Percentual de faturamento de São Paulo em relação ao faturamento total: {sp/total*100:,.2f}%')
print(f'Percentual de faturamento do Rio de Janeiro em relação ao faturamento total: {rj/total*100:,.2f}%')
print(f'Percentual de faturamento de Minas Gerais em relação ao faturamento total: {mg/total*100:,.2f}%')
print(f'Percentual de faturamento do Espirito Santo em relação ao faturamento total: {es/total*100:,.2f}%')
print(f'Percentual de faturamento dos outros estados em relação ao faturamento total: {outros/total*100:,.2f}%')