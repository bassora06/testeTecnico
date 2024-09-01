estados = [['SP', 67836.43], ['RJ', 36678.66], ['MG', 29229.88], ['ES', 27165.48], ['Outros', 19849.53]]
soma = 0


for i in estados:
    soma += i[1]
    
sp = int((estados[0][1] * 100) / soma)
rj = int((estados[1][1] * 100) / soma)
mg = int((estados[2][1] * 100) / soma)
es = int((estados[3][1] * 100) / soma)
outros = int((estados[4][1] * 100) / soma)

print(f'São Paulo:{sp}%')   
print(f'Rio de Janeiro:{rj}%')   
print(f'Minas Gerais:{mg}%')   
print(f'Espirito Santo:{es}%')   
print(f'Outros:{outros}%')



