#Tienes una lista de eventos en orden cronológico. Muestra los eventos del más reciente al más antiguo
# Luego cree una copia de esa lista para una línea temporal alternativa.

eventos = ["Nacimiento", "Escuela", "Universidad", "Trabajo", "Jubilación"]

##Creando linea alternativa
alterniativa = eventos.copy()
alterniativa.reverse()

##Liena original
print(eventos)

##linea alternativa
print(alterniativa)




