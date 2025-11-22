#Simula 20 Lanzamientos de dados (numeros del 1-6)
#Muestra cuantas veces salió cada numero del 1 al 6
import random
Lanzamientos = [random.randint(1, 6)for _ in range(20)]
print(Lanzamientos)

cantidad1 = Lanzamientos.count(1)
cantidad2 = Lanzamientos.count(2)
cantidad3 = Lanzamientos.count(3)
cantidad4 = Lanzamientos.count(4)
cantidad5 = Lanzamientos.count(5)
cantidad6 = Lanzamientos.count(6)

porcentaje1 = (cantidad1 / 20) * 100
porcentaje2 = (cantidad2 / 20) * 100
porcentaje3 = (cantidad3 / 20) * 100
porcentaje4 = (cantidad4 / 20) * 100
porcentaje5 = (cantidad5 / 20) * 100
porcentaje6 = (cantidad6 / 20) * 100

print(f'1: ({cantidad1} veces - {porcentaje1}%) {"0"*cantidad1}')
print(f'2: ({cantidad2} veces - {porcentaje2}%) {"0"*cantidad2}')
print(f'3: ({cantidad3} veces - {porcentaje3}%) {"0"*cantidad3}')
print(f'4: ({cantidad4} veces - {porcentaje4}%) {"0"*cantidad4}')
print(f'5: ({cantidad5} veces - {porcentaje5}%) {"0"*cantidad5}')
print(f'6: ({cantidad6} veces - {porcentaje6}%) {"0"*cantidad6}')