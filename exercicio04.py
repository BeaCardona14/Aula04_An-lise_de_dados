nota = input("Escolha uma letra entre A- B- C- D - F: ").upper()
match nota:
    case "A":
        print("Excelente")
    case "B":
        print("Bom")
    case "C":
        print("Regular")
    case "D":
        print("Ruim")
    case "F":
        print("Reprovado")
    case _:
        print("Letra não correspondente.")    
