#Bienvenida al programa.

print("Bienvenido al mundo de Pokemon!")

#Petición del sexo al usuario.

genero=input("Eres un niño o una niña?: ")

if genero=="niño":
    print("Bienvenido, estimado entrenador!")
else:
    print("Bienvenida, estimada entrenadora!")

#Petición de la edad al usuario.

edad=input("Que edad tienes?: ")
if int(edad)<10:
    if genero=="niño":
        print("No tienes edad para ser entrenador.")
    else:
        print ("No tienes edad para ser entrenadora.")

print("Comienza tu aventura!")

#Petición de la región al usuario.

region = input("Necesitarás un compañero de viaje! En que región te encuentras?:")

if region == "Kanto" and genero == "niño":
    print("Tu compañera de viaje es Misty.")
else:
    print("Tu compañero de viaje es Brook.")

#Selección del Pokemón.

while True:
    tipo = input("Que tipo de pokemon quieres para empezar?: ")
    if tipo == "agua":
        print("Tu starter es Oshawott")
        break
    elif tipo == "fuego":
        print("Tu starter es Cyndaquil")
        break
    elif tipo == "planta":
        print("Tu starter es Rowlet")
        break
    else:
        print("No tengo ese tipo. Intenta de nuevo.")