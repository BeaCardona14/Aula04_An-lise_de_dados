print("Escola Senac\n")
nome = input("nome: ").title()
prova01 = float(input("prova01: ").replace(",","."))
prova02 = float(input("prova02: ").replace(",","."))
prova03 = float(input("prova03: ").replace(",","."))
media = (prova01 + prova02 + prova03)/3
if media >= 7:
    resultado = "aprovado"
elif media >= 5:
    resultado ="recuperação"
else:
    resultado = "reprovado" 
print("resultado\n")           
print(f"nome: {nome}")           
print(f"prova01 {prova01:.1f}".replace(".",","))           
print(f"prova01 {prova02:.1f}".replace(".",","))           
print(f"prova01 {prova03:.1f}".replace(".",","))           
print(f"media {media:.1f}".replace(".",","))           
print(f"resultado {resultado.upper()}")        
