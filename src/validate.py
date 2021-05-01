from tda import sList
class snap:
    def __init__(self,input,stack,prod) -> None:
        self.input = self.arrToStr(input)
        self.stack = self.arrToStr(stack)
        self.prod = prod

    def arrToStr(self,arr):
        str = ""
        for char in arr:
            str += char
        return str

class path:
    def __init__(self,input,stack,prod,used) -> None:
        self.input:list = input
        self.stack:list = stack
        self.prod:sList = prod
        self.used:list = used
        self.history = []
        self.pid = ""

    def take(self,shot:snap):
        self.history.append(shot)