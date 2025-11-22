#Tienes una lista de numeros del 1 al 10
#Haz desaparecer el ultimo numero y guardalo
#Luego haz lo mismo con el primero 
#Muestra cuantos numeros quedan y cuales desaparecieron
import time

numeros = list(range(1,11))
eliminados = []



print(numeros)
time.sleep(1)

eliminados.append(numeros[-1])
numeros.pop(-1)

print(numeros)
time.sleep(1)

eliminados.append(numeros[0])
numeros.pop(0)

print(numeros)
time.sleep(1)
contador_n = len(numeros)
print(f'En la lista de numeros quedaron {contador_n} numeros')
print(f'los numeros que desaparecieron fueron {eliminados}')
