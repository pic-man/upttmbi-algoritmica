#Tienes una lista con elementos duplicados y valores None
#Crea una version limpia sin duplicados ni valores nulos

Lista_sucia = [1,2,None,3,2,4,None,1,5,3]
Lista_limpia = []
eliminados = []
for valor in Lista_sucia:
    if valor == None:
        
        eliminados.append(valor) 
          
    if valor not in Lista_limpia:
        Lista_limpia.append(valor) 

Lista_limpia.remove(None)   
print(Lista_limpia)


