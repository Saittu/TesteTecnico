#Estou acrescentando mais um à variável porque, anteriormente, ela encerrava o loop antes de alcançar o valor do usuário.
userValue = int(input("Digite um número: ")) + 1
print('-' * 70)
x, y = 0, 1

# Faz a sequência de fibonacci até q o valor de y seja menor que o fornecido pelo usuário
while y < userValue:
    print(x, end=", ")
    x, y = y, x+y
    
#escreve o ultimo número da sequência
print(x)

#Aqui, crio duas condições para verificar se o valor passado pelo usuário é igual ao valor final da sequência ou não. Coloquei o -1 nas variáveis para que elas retornem ao valor original fornecido pelo usuário.
if(userValue - 1 == x):
    print('-' * 70)
    print(f"O valor {userValue - 1} está presente na sequência de Fibonacci")
else:
    print('-' * 70)
    print(f"O valor {userValue - 1} não está presente na sequência de Fibonacci")
    
    
    