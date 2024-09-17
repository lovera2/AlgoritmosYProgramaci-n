""" 
Escriba un programa en Python que pueda solicitar los ingredientes al usuario e indique la cantidad (masa) de arepas resultante. 
Use input("pregunta") para permitirle al usuario introducir el valor

Nota: El usuario sólo puede introducir strings. para hacer la conversión, deberá usar
int(string) #convierte a enteros/íntegros
float(string) #convierte a decimales / punto flotante
si necesita convertir de int a float, puede usar
float(int)
"""

print("Bienvenido al programa que permite conocer la cantidad de arepas resultante. \n Introduce la cantidad utilizada para cada uno de los ingredientes.")

harina = float(input("¿Cuántas tazas de harina utilizó?:"))

agua = float(input("¿Cuántas tazas de agua utilizó?:"))

sal = float(input("¿Cuántas cucharadas de sal utilizó?:"))

sal_taza=sal*1/16

aceite=float(input("¿Cuántas cucharaditas de aceite utilizó?:"))

aceite_taza=sal*1/16*1/13

arepa = harina+agua+sal_taza

budare=arepa+aceite_taza*0.75

print(f"La cantidad de arepas resultante es {budare}")
