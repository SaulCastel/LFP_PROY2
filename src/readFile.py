from grammar import gramatica


def readFile(route):
    grammars = []
    file = open(route)
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
        grammars.append(grammar)
    return grammars