'''Solicitar una edad y clasificarla
en menores de edad (0-17), adultos (18-64) y 
adultos mayores (65+)
para este ejercicio usar if elif else
y tambien usar match/case
'''

menor_de_edad=range(0,18)
adultos=range(18,64)
adultos_mayores=range(65,100)

edad=int (input("Ingrese la edad"))
if edad in menor_de_edad:
    print("Es menor de edad")
elif edad in adultos:
    print("Es adulto")
else:
    