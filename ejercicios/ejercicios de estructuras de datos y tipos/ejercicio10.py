'''
Problema: Crear un diccionario con algunos productos 
y permitir que el usuario agregue un nuevo producto con su precio.
'''


# Productos={"Cebollas": float 2.500, "Tomates": 1.900, "Papas": 3.400, "Platanos": 2.800}
# print(Productos)
# usuario=input("Por favor ingresar un nuevo producto con su respectivo precio")
# print(Productos.get(usuario))



Productos={
    "pera" : 50,
    "manzana" : 200,
    "guayaba": 80}
Productos=input("por favor ingrese el nombre")
precio=float(input("por favor ingrese el precio"))

#productos[producto]=precio #forma1
Productos.update({Productos:precio, "limon":80})
print(Productos)