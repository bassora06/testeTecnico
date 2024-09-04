primeiroValor = 0
segundoValor = 1

fibonacci = []

numero = 5


for i in range(10):
    fibonacci.append(primeiroValor)
    terceiroValor = primeiroValor + segundoValor
    primeiroValor = segundoValor
    segundoValor = terceiroValor


if numero in fibonacci:
    print(f'O numero {numero} está presente na sequencia')
else: 
    print(f'O numero {numero} não esta presente na sequencia')
