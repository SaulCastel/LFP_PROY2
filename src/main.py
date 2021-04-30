from grammar import automata
from readFile import readFile
import os

messages = [
    "1. Cargar archivo",
    "2. Mostrar información general de gramática",
    "3. Generar automata de pila equivalente",
    "4. Reporte de recorrido",
    "5. Reporte de tabla",
    "6. Salir"
]

grammars = []

clear = lambda : os.system("clear")
confirm = lambda : input("> Presione cualquier tecla para continuar...")

while True:
    clear()
    print()
    for m in messages:
        print(m)
    option = input("> Escoge una opción: ")
    print()
    if option == "6":
        break
    if option == "1":
        route = input("> Ruta del archivo: ")
        try:
            grammars = readFile(route)
        except:
            print("[Ruta desconocida]")
            confirm()
    elif option == "2":
        clear()
        for i in range(len(grammars)):
            print(f"{i}.",grammars[i].name)
        opt = input("> Escoge el numero: ")
        try:
            clear()
            grammars[int(opt)].showGrammar()
        except:
            print("[Error en la seleccion]")
        confirm()
    elif option == "3":
        pass
    elif option == "4":
        clear()
        for i in range(len(grammars)):
            print(f"{i}.",grammars[i].name)
        opt = input("> Escoge el numero: ")
        clear()
        auto = automata(grammars[int(opt)])
        string = input("> Ingresa una cadena: ")
        auto.validate(string)
        confirm()
    elif option == "5":
        pass
clear()