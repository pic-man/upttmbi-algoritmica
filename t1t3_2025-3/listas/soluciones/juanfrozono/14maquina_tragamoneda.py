#Crea una funcion que genere 3 simbolos aleatorios
#Determina si ganaste:
#3 simbolos iguales = Jackpot
#2 simbolos iguales = Premio menor 
#Todos diferentes = Sin premio

import random

simbolos_posibles = ["🍒","🍋","🔔","💎","7️ "]
def funsion():
    simbolos1 = random.randint(0,4)
    simbolos2 = random.randint(0,4)
    simbolos3 = random.randint(0,4)
    print(f'{simbolos_posibles[simbolos1]}|{simbolos_posibles[simbolos2]}|{simbolos_posibles[simbolos3]}')
    if simbolos1 == simbolos2 == simbolos3 :
        print("jackpot")
    elif simbolos1 == simbolos2 != simbolos3 or simbolos1 != simbolos2 == simbolos3 or simbolos2 != simbolos1 == simbolos3:
        print("premio menor")
    else:
        print("Sin premio")
funsion()