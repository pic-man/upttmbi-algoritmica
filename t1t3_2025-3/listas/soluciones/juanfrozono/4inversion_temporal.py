#Tienes una lista de eventos en orden cronologico
#Muestra los eventos del mas reciente al mas antiguo
#Luego crea una copia de esa lista para una linea temporal alternativa

Eventos = ["Nacimiento","Escuela","Universidad","Trabajo","Jubilacion"]
eventos_alt = Eventos.copy()
eventos_alt.reverse()
print(f'la lista original es esta: {Eventos}')
print(f'la lista alternativa es esta: {eventos_alt}')