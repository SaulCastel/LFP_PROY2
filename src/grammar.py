from tda import sList


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
    
class automata:
    def __init__(self, grammar:gramatica) -> None:
        self.name = "AP_"+grammar.name
        self.stack = []
        self.Sn = grammar.Sn
        self.Pr = []
        self.genProd(grammar)

    def genProd(self, grammar:gramatica):
        groups = []
        for prod in grammar.Pr:
            prod[0] = prod[0].replace(" ","")
            prod[1] = prod[1].replace(" ","")
            for g in groups:
                if g[1].get() == prod[0]:
                    g.append(prod[1])
                    break
            else:
                group = sList()
                group.append(None)
                group.append(prod[0])
                group.append(prod[1])
                groups.append(group)
        self.Pr.extend(groups)
        for t in grammar.Vt:
            prod = sList()
            prod.append(t)
            self.Pr.append(prod)
    
    def validate(self,string):
        avlb = self.strToArr(string)
        self.stack.append("#")
        self.stack.append(self.Sn)
        char = avlb.pop(0)
        state = 0
        while len(avlb) > 0:
            if state == 0:
                for prod in self.Pr:
                    if prod[0].get() == None:
                        if prod[1].get() == self.stack[len(self.stack)-1]:
                            curr = prod[2]
                            if prod.size > 3 and curr.get()[0] != char:
                                curr = curr.next
                            self.stack.pop()
                            self.stack.extend(self.strToArr(curr.get(),True))
                            self.showStep(char)
                    elif prod[0].get() == char:
                        char = avlb.pop(0) 
                        self.stack.pop()
                        self.showStep(char)
                        break
                    if self.stack[len(self.stack)-1] == "#":
                        state = 1
            if state == 1:
                print("\n------------\n")
                print("Cadena valida\n")
                break
        else:
            print("\n------------\n")
            print("Cadena invalida\n")
    
    def strToArr(self, string:str,stack=False) -> list:
        arr = []
        for char in string:
            arr.append(char)
        if stack:
            arr.reverse()
        return arr

    def showStep(self,char):
        print("\n------------\n")
        print(f"Stack: {self.stack}")
        print(f"entrada: {char}")

class produccion:
    def __init__(self, read, pop, push) -> None:
        self.read = read
        self.pop = pop
        self.push = push

    def getProd(self):
        return f"({self.read},{self.pop},{self.push})"