x=520

y=60


'''condicional if elif else
if then else

if <condición>
    operación 1
    operación 2
    .
    .
    .
    operación n

'''


# caso 1 
if x > y: #condición
    print("x es mayor a y") #operación 


#caso 2
if x < y:
    print("x es menor que y")
else:
    print("x es mayor que y")


#caso 3 ---> uso de if elif else
if x < y:
    print("x es menor que y")
elif x ==y:
    print("x es igual que y")
elif x/y==8:
    print("x divido y es igual a 8")
else: 
    print("x esa mayor que y")

#variante
if x%2==0 and x>500: #múltiples condiciones a evaluar
    print("x es par y mayor que 500")


#caso de uso el login a una aplicacion
usuario=input("por favor ingrese su usuario")


# if usuario=="andres" and password=="1234":
#     print("usuario puede ingresar")
# else:
#     print("usuario o contraseña incorrectos")


if usuario=="andres":
    password=input("por favor ingrese su password")
    if password=="1234":
        print("usuario puede ingresar")
    else:
        print("contraseña incorrecta")
else:
    print("usuario o contraseña incorrectos")
print("ejecucion terminada")
