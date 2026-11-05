#Teste 5 entradas novas, prova01,prova02,prova03.
#Faça a média ente as provas e mostre a situação onde:
#média>=7 aprovado; média>=5 recuperação; média<5 reprovado.

for aluno in range(1,6):
    print(f" --- Aluno {aluno} ---")
    nome = input("Digite o nome do aluno: ")
    prova1 = float(input(f"Digite a primeira nota: "))
    prova2 = float(input(f"Digite a segunda nota: "))
    prova3 = float(input(f"Digite a terceira nota: "))

#Calcular média
    media = (prova1 + prova2 + prova3) / 3

#Verificar situação

    if media >= 7:    
       situacao ="Aprovado"

    elif media >= 5:
        situacao ="Recuperação"
    
    else:
        situacao ="Reprovado"

#mostrar resultado
    print("--- Resultado ---")
    print(f"aluno: {nome}")
    print(f"prova1: {prova1}")
    print(f"prova2: {prova2}")
    print(f"prova3: {prova3}") 
    print(f"media: {media:.2f}")
    print(f"situação: {situacao}")   




