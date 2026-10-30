idade = int(input("Digite a idade: "))
esporte = input("Digite o esporte: ")
match idade:
    case 1:
        if idade <10:
            print("Categoria mirim")
        elif idade <=14:
            print("Categoria infantil")
        else:
            print(" Juvenil") 

    case 2:
        if idade <16:
            print("Categoria junior")
        else >=16:
            print("Categoria Adulto")
                
