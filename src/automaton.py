from tda import sList
from validate import *
import copy

debug = False
class produccion:
    def __init__(self,start,read,pop,end,push) -> None:
        self.start = start
        self.read = read
        self.pop = pop
        self.end = end
        self.push = push
        self.next = None

    def getProd(self):
        end = self.end.replace(" ","")
        push = self.push.replace(" ","")
        str = f"{self.start}, {self.read}, {self.pop};"
        str += f" {end}, {push}"
        return str

class automata:
    def __init__(self, grammar) -> None:
        self.name = "AP_"+grammar.name
        self.Sn = grammar.Sn
        self.Vt = grammar.Vt
        self.Pr = sList()
        self.genProd(grammar.Pr,self.Vt)
        self.state = None

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
        self.state = "i"
        input = self.strToArr(string,True)
        PrCopy = copy.deepcopy(self.Pr)
        first = path(input,[],PrCopy,[])
        paths = [first]
        pNum = 0
        curr:path = first
        while len(paths) > 0 and len(curr.input) > 0:
            if debug:
                print("\n------------\n")
                print("Nuevo camino...")
            curr = paths.pop(0)
            pNum += 1
            fail = False
            while not fail:
                while self.state == "f" or curr.prod.size > 0:
                    if self.state != "f":
                        prod = curr.prod.pop(0)
                    if self.state == "i" or self.state == "p":
                        self.apply(prod,curr)
                    elif self.state == "q":
                        if prod.start == "q":
                            sTop = curr.stack[-1]
                            if len(curr.input) > 0:
                                iTop = curr.input[-1]
                            if not self.isVt(sTop):
                                actual = prod.pop
                                next = None
                                if prod.next != None:
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
                                curr.prod = copy.deepcopy(self.Pr)
                                curr.used = []
                                self.apply(prod,curr)
                                break
                    elif self.state == "f":
                        if len(curr.input) == 0:
                            print("\n------------------------\n")
                            print(">> ??CADENA VALIDA!")
                            print(">> Cadena:",string)
                            print(">> Caminos analizados:",pNum)
                            print("\n------------------------\n")
                            curr.valid = True
                        else:
                            print("\n------------------------\n")
                            print(">> ??CADENA INVALIDA!")
                            print(">> Cadena:",string)
                            print(">> Caminos analizados:",pNum)
                            print("\n------------------------\n")
                        return curr
                else:
                    if debug:
                        print("\n------------\n")
                        print("Camino agotado...")
                    break
                if not len(curr.input) > 0:
                    if curr.stack[-1] != "#":
                        fail = True
            else:
                if debug:
                    print("\n------------\n")
                    print("Camino agotado...")
        else:
            print("\n------------------------\n")
            print(">> ??CADENA INVALIDA!")
            print(">> Cadena:",string)
            print(">> Caminos analizados:",pNum)
            print("\n------------------------\n")
            return curr
    
    def apply(self,prod:produccion,curr:path):
        if prod.read != "$" and len(curr.input) > 0:
            curr.input.pop()
        else:
            curr.used.append(prod)
        if prod.pop != "$" and len(curr.stack) > 0:
            curr.stack.pop()
        if prod.push != "$":
            curr.stack.extend(self.strToArr(prod.push))
        selection = prod.getProd()
        shot = snap(curr.input,curr.stack,selection)
        curr.history.append(shot)
        if debug:
            self.showStep(selection,curr.stack,curr.input)
        self.state = prod.end

    def strToArr(self, string:str,input=False) -> list:
        arr = string.split()
        if input:
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