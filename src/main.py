from generateHtml import genTable
from graph import genGraph
from grammar import gramatica
from automaton import automata
from readFile import readFile
import os
import time

messages = [
    "1. Cargar archivo",
    "2. Mostrar información general de gramática",
    "3. Generar automata de pila equivalente",
    "4. Reporte de tabla",
    "5. Salir"
]

grammars = []

clear = lambda : os.system("clear")
confirm = lambda : input("> Presione cualquier tecla para continuar...")
file = open("./log.txt","w")
file.write("")
file.close()
clear()
print("- Lenguajes formales y de programacion -")
print("> Gramaticas libres de contexto")
print("Saul Esteban Castellanos Ubeda, 201801178\n")
for i in range(5,0,-1):
    print(i,"",end="")
    time.sleep(1)

print("\n\n¡Bienvenido!")
time.sleep(2)
while True:
    clear()
    print()
    for m in messages:
        print(m)
    option = input("> Escoge una opción: ")
    print()
    if option == "5":
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
        clear()
        for i in range(len(grammars)):
            print(f"{i}.",grammars[i].name)
        opt = input("> Escoge el numero: ")
        try:
            clear()
            gram:gramatica = grammars[int(opt)]
            auto = automata(gram)
            gram.auto = auto
            genGraph(auto)
        except:
            print("[Error en la seleccion]")
        confirm()
    elif option == "4":
        clear()
        for i in range(len(grammars)):
            print(f"{i}.",grammars[i].name)
        opt = input("> Escoge el numero: ")
        try:
            clear()
            auto = grammars[int(opt)].auto
            string = input("> Ingresa una cadena: ")
            path = auto.validate(string)
            genTable(path,string)
        except ValueError or IndexError:
            print("[Error en la seleccion]")
        confirm()
clear()