class gramatica:
    def __init__(self, parts:list) -> None:
        self.name = parts.pop(0)
        tmp = parts.pop(0).split(";")
        self.Vn = tmp[0].split(",")
        self.Vt = tmp[1].split(",")
        self.Sn = tmp[2]
        self.Pr = []
        while len(parts) > 0:
            prod = parts.pop(0).split("->")
            prod[0] = prod[0].strip()
            prod[1] = prod[1].strip()
            self.Pr.append(prod)

    def showGrammar(self):
        print("\n------------------------------------------\n")
        print("Nombre de gramatica =",self.name)
        str = "{"
        for nt in self.Vn:
            str += nt+","
        str = str.removesuffix(",")
        str += "}"
        print("No Terminales =",str)
        str = "{"
        for t in self.Vt:
            str += t+","
        str = str.removesuffix(",")
        str += "}"
        print("Terminales =",str)
        print("No terminal inicial =",self.Sn)
        print("Producciones =\n")
        groups = []
        for prod in self.Pr:
            for g in groups:
                if g[0] == prod[0]:
                    g.append(prod[1])
                    break
            else:
                group = [prod[0],prod[1]]
                groups.append(group)
        for g in groups:
            if len(g) > 2:
                str = g.pop(0) + " -> "
                str += g.pop(0)
                for rule in g:
                    str += f" | {rule}"
                print(str)
            else:
                print(g[0],"->",g[1])
        print("\n------------------------------------------")