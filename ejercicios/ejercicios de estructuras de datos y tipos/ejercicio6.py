'''
Problema: Solicitar al usuario 5 números enteros, almacenarlos en una lista y luego mostrar:

    La lista original.

    La lista en orden inverso.

    La suma de los números.
'''

mensaje_principal = print("A continuación digitar 5 números enteros")

numero1=int (input ("Por favor digitar el primer numero: "))
numero2=int (input ("Por favor digitar el segundo numero: "))
numero3=int (input ("Por favor digitar el tercer numero: "))
numero4=int (input ("Por favor digitar el cuarto numero: "))
numero5=int (input ("Por favor digitar el quinto numero: "))

mi_lista= [numero1,numero2,numero3,numero4,numero5] #su utiliza la funcion sum
print(type(mi_lista))
print("La lista original es: ", mi_lista)

mi_lista.reverse() #NO es ordenar descendente o ascendente
print("La lista en orden inverso es: ", mi_lista)

print("La suma de los dos numeros es:", numero1+numero2+numero3+numero4+numero5)

mi_lista.sort(reverse=True)#Cuando reverse=true descendente - Cuando reverse=false ascendente
print(mi_lista)
mi_lista.sort(reverse=False)
print(mi_lista)




# lista="123456789"
# print(len(lista))
# print(list(lista))