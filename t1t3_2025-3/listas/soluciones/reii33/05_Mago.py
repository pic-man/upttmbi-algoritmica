#Tienes una lista de números del 1 al 10. "Haz desaparecer" el último número y guárdalo, 
#luego haz lo mismo con el primero. Muestra cuántos números quedan y cuáles desaparecieron.

numeros_magicos = list(range(1, 11))


primer_numero = numeros_magicos.pop(0)


ultimo_numero = numeros_magicos.pop()

print(f'numeros que desaparecieron fueron {primer_numero} y {ultimo_numero} ')
print(f'los numeros restantes son {numeros_magicos}')