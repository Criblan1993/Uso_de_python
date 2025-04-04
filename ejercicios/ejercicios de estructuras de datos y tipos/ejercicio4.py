'''
Problema: Escribe un programa que determine si un número ingresado por el 
usuario es par o impar utilizando el operador módulo %.
'''

numero=float (input ("Por favor digitar el numero"))

resultado=numero%2

respuesta=resultado==0

print(respuesta)