import json

faturamento = []
soma = 0
diasValidos = 0



with open('dados.json', 'r', encoding='utf-8')as arquivo:
    fonte = json.load(arquivo)

    for i in fonte:
        faturamento.append(i)

    
for dia in faturamento:
    if dia["valor"] != 0:
        soma += dia["valor"]
        diasValidos += 1
    else:
        soma += dia["valor"]

maiorValor = 0
menorValor = faturamento[0]["valor"]
superiorMediaMensal = 0


for dia in faturamento:
    if dia['valor'] > maiorValor:
        maiorValor = dia['valor']

for dia in faturamento:
    if dia['valor'] != 0:
        if dia['valor'] < menorValor:
            menorValor = dia['valor']

media = soma / diasValidos

for dia in faturamento:
    if dia['valor'] > media:
        superiorMediaMensal = dia

print(menorValor)
print(maiorValor)
print(superiorMediaMensal)



        
    