#Crea una funcion que reciba una lista de numeros y realice el truco del malabarista:
#toma el ultimo elemento y lo pone al inicio
#Repite este proceso 3 veces y retorna la lista transformada

numeros = [1,2,3,4,5]

def malabares(numeros):
    numeros.insert(0,numeros[-1])
    numeros.pop(-1)

malabares(numeros)    
malabares(numeros)    
malabares(numeros) 

print(numeros)
