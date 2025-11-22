#Hacer una lista de ingredientes para una pizza
#Agrega 3 ingredientes mas
#Elimina las anchoas

ig = ["queso","tomate","anchoas","jamon"]
a = 0

while True:
    ig.append(str(input("Ingrese ingrediente: ")))
    a += 1
    
    if a == 3:
        ig.remove("anchoas")
        print(ig)
        break