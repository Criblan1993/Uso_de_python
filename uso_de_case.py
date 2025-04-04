dia=input("Ingrese el dia de la semana: ").lower()
match dia:
    case "sabado" | "domingo":
        print(f"{dia} es fin de semana")
    case "lunes":
            print(f"{dia} es el dia mas dificil")
    case "martes":
            print(f"{dia} es un dia normal")
    case "viernes":
            print(f"{dia} es un dia feliz")
    case _:
            print("El texto no es un día de las semana")