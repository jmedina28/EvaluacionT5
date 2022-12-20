
import sys
import os



def lanzar():
    
    print("Bienvenido a la ejecución de ejercicios")
    print("=======================================")
    print("1. Calculadora")
    print("2. Contador")
    print("3. Gestor de personajes")
    print("4. Reloj")
    print("5. Salir")
    print("=======================================")
    opcion = input("Introduce una opción: ")
        
    if opcion == "1":
        from ejercicios import calculos
        
    elif opcion == "2":
        from ejercicios import contador
        
    elif opcion == "3":
        from ejercicios import gestor
        
    elif opcion == "4":
        from ejercicios import reloj
        
    elif opcion == "5":
        print("Hasta pronto!")

if __name__ == "__main__":
    lanzar()