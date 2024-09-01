import json

faturamento = []
soma = 0
diasValidos = 0



with open('dados.json', 'r', encoding='utf-8')as arquivo:
    fonte = json.load(arquivo)

    for i in fonte:
        faturamento.append(i)

    
for dia in faturamento:
    if dia[1] != 0:
        soma += dia[1]
        diasValidos += 1
    else:
        soma += dia[1]

maiorValor = 0
menorValor = faturamento[0][1]
superiorMediaMensal = 0


for dia in faturamento:
    if dia[1] > maiorValor:
        maiorValor = dia[1]

for dia in faturamento:
    if dia[1] != 0:
        if dia[1] < menorValor:
            menorValor = dia[1]

media = soma / diasValidos

for dia in faturamento:
    if dia[1] > media:
        superiorMediaMensal = dia

print(menorValor)
print(maiorValor)
print(superiorMediaMensal)



        
    