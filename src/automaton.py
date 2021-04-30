from tda import sList
from validate import *
import copy

class produccion:
    def __init__(self,start,read,pop,end,push) -> None:
        self.start = start
        self.read = read
        self.pop = pop
        self.end = end
        self.push = push
        self.next = None

    def getProd(self):
        str = f"({self.start},{self.read},{self.pop};"
        str += f"{self.end},{self.push})"
        return str

class automata:
    def __init__(self, grammar) -> None:
        self.name = "AP_"+grammar.name
        self.Sn = grammar.Sn
        self.Vt = grammar.Vt
        self.Pr = sList()
        self.genProd(grammar.Pr,self.Vt)
        self.state = "i"

    def isVt(self, target) -> bool:
        for t in self.Vt:
            if target == t:
                return True
        return False
        
    def genProd(self, Pr, Vt):
        self.Pr.append(produccion("i","$","$","p","#"))
        self.Pr.append(produccion("p","$","$","q",self.Sn))
        for prod in Pr:
            prod[0] = prod[0].replace(" ","")
            self.Pr.append(produccion("q","$",prod[0],"q",prod[1]))
        for t in Vt:
            self.Pr.append(produccion("q",t,t,"q","$"))
        self.Pr.append(produccion("q","$","#","f","$"))
    
    def validate(self,string) -> path:
        input = self.strToArr(string)
        first = path(input,[],self.Pr,[])
        paths = [first]
        while len(paths) > 0:
            print("\n------------\n")
            print("Nuevo camino...")
            curr:path = paths.pop(0)
            while True:
                for prod in curr.prod:
                    if self.state == "i" or self.state == "p":
                        self.apply(prod,curr)
                    elif self.state == "q":
                        if prod.start == "q":
                            sTop = curr.stack[-1]
                            iTop = curr.input[-1]
                            if not self.isVt(sTop):
                                actual = prod.pop
                                next = prod.next.pop
                                if sTop == actual:
                                    oldStack = copy.deepcopy(curr.stack)
                                    self.apply(prod,curr)
                                    if next == actual:
                                        new = copy.deepcopy(curr)
                                        new.stack = oldStack
                                        new.history.pop()
                                        paths.append(new)
                            elif iTop == prod.read and sTop == iTop:
                                curr.used.extend(curr.prod)
                                curr.prod = curr.used
                                curr.used = []
                                self.apply(prod,curr)
                                break
                    elif self.state == "f":
                        print("\n------------\n")
                        print(">> ¡Cadena valida!")
                        return curr
                else:
                    print("\n------------\n")
                    print("Camino agotado...")
                    #paths.remove(curr)
                    break
        else:
            print("\n------------\n")
            print(">> ¡Cadena invalida!")
    
    def apply(self,prod:produccion,curr:path):
        if prod.read != "$":
            curr.input.pop()
        else:
            curr.used.append(prod)
        if prod.pop != "$":
            curr.stack.pop()
        if prod.push != "$":
            curr.stack.extend(self.strToArr(prod.push))
        selection = prod.getProd()
        shot = snap(curr.input,curr.stack,selection)
        curr.history.append(shot)
        self.showStep(selection,curr.stack,curr.input)
        self.state = prod.end

    def strToArr(self, string:str) -> list:
        arr = string.split()
        if arr[0] == string:
            arr = []
            for char in string:
                arr.append(char)
        arr.reverse()
        return arr

    def showStep(self,prod,stack,input):
        print("\n------------\n")
        print(f"Prod: {prod}")
        print(f"Stack: {stack}")
        print(f"entrada: {input}")