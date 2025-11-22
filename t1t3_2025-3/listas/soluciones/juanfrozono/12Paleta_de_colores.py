#Crea una funcion que tome una lista de colores y:
#Agregue blanco al inicio y negro al final 
#Cree una version invertida de esta paleta
#Retorne ambas versiones (Original modificada e invertida)
Colores = ["rojo","verde","azul","amarillo"]

def colores():
    Colores_mod = Colores.copy()
    Colores_mod.insert(0,"blanco")
    Colores_mod.append("negro")
    Colores_inv = Colores_mod.copy()
    Colores_inv.reverse()
    print(f'La lista original es: {Colores}')
    print(f'La lista modificada es: {Colores_mod}')
    print(f'La lista invertida es: {Colores_inv}')
    
colores()

   



 
    

    








