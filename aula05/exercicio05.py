#Faça uma tabuada de multiplicar 
#Com número escolhido pelo usuário

n = int(input("Digite um número: "))
for i in range (1,11):
    print(f"{n} x {i} = {n * i}")