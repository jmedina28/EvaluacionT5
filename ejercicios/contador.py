from io import open
import sys

fichero = open("contador.txt", "a+") 
fichero.seek(0)
valor = fichero.readline()

if len(valor) == 0:
    valor = "0"
    fichero.write(valor)

fichero.close()

try:
    contador = int(valor)

    if len(sys.argv) == 2:
        if sys.argv[1] == "inc":
            contador += 1
        elif sys.argv[1] == "dec":
            contador -= 1

    print(contador)
    fichero = open("contador.txt", "w")
    fichero.write(str(contador))
    fichero.close()

except:
    print("Error: Fichero corrupto.")