from report import report
from grammar import gramatica


def readFile(route):
    grammars = []
    file = open(route)
    report("Archivo cargado: " + route)
    line = None
    lines = file.readlines()
    file.close()

    while len(lines) > 0:
        line = lines.pop(0)
        line = line.removesuffix("\n")
        parts = []
        while line != "*":
            if line != "\n" and line != "":
                parts.append(line)
            line = lines.pop(0)
            line = line.removesuffix("\n")
        grammar = gramatica(parts)    
        if grammar.glc:
            grammars.append(grammar)
        else:
            report(f"'{grammar.name}' No es GLC, así que no se cargó")
    return grammars