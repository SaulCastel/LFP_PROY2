import webbrowser
from automaton import automata
from validate import *
from graphviz import Digraph

def genGraph(auto:automata):
    dot = Digraph()
    dot.attr(rankdir="LR")
    dot.attr("node",shape="circle",fixedsize="true",width="1.5")
    dot.attr("node",fontsize="25")
    dot.attr("edge",fontsize="15")
    dot.node("i")
    dot.node("p")
    dot.node("q",width="1.9")
    dot.node("f",shape="doublecircle",width="1.4")
    prods = auto.Pr
    label = "<"
    for prod in prods:
        tail = prod.start
        head = prod.end
        if head != tail:
            dot.edge(tail,head,prod.getProd())
        else:
            label += "<FONT>"
            label += f'{prod.getProd()}'
            label += "</FONT>"
            label += "<BR/>"
    label += ">"
    dot.edge("q","q",label)
    dot.render("./graphs/solo/AP",cleanup=True,format="png")
    webbrowser.open_new_tab("./html/solo.html")

def genPath(auto:automata,path:path):
    for index in range(len(path.history)):
        shot = path.history[index]
        genSnap(auto,shot,index)

def genSnap(auto:automata,shot:snap,index:int):
    dot = Digraph()
    dot.attr(rankdir="LR")
    dot.attr("node",shape="circle",fixedsize="true",width="1.5")
    dot.attr("node",fontsize="25")
    dot.attr("edge",fontsize="15")
    dot.node("i")
    dot.node("p")
    dot.node("q",width="1.9")
    dot.node("f",shape="doublecircle",width="1.4")
    prods = auto.Pr
    label = "<"
    for prod in prods:
        tail = prod.start
        head = prod.end
        string = prod.getProd()
        if head != tail:
            if string == shot.prod:
                selected = '<<FONT COLOR="red">'
                selected += f"<B>{string}</B>"
                selected += "</FONT>>"
                dot.edge(tail,head,selected)
            else:
                dot.edge(tail,head,string)
        elif string == shot.prod:
            label += '<FONT COLOR="red">'
            label += f"<B>{string}</B>"
            label += "</FONT>"
            label += "<BR/>"
        else:
            label += '<FONT>'
            label += f'{string}'
            label += "</FONT>"
            label += "<BR/>"
    label += ">"
    dot.edge("q","q",label)
    dot.render(f"./graphs/path/{index}",cleanup=True,format="png")