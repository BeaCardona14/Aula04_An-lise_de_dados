mês = int(input("Digite um numero de 1 a 12: "))
match mês:
    case 1:
        print("Janeiro")
    case 2:
        print("Fvereiro")
    case 3:
        print("Março")
    case 4:
        print("Abril")
    case 5:
        print("Maio")
    case 6:
        print("Junho")
    case 7:
        print("Julho")
    case 8:
        print("Agosto")
    case 9:
        print("Setembro")
    case 10:
        print("Outubro")
    case 11:
        print("Novembro")
    case 12:
        print("Dezembro")
    case _: 
        print(" Número inválido.Dgite um número válido entre 1 a 12")    
       