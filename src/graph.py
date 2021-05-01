import webbrowser
from automaton import automata
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
    label = ""
    for prod in prods:
        tail = prod.start
        head = prod.end
        if head != tail:
            dot.edge(tail,head,prod.getProd())
        else:
            label += prod.getProd() + "\n"
    dot.edge("q","q",label)
    dot.render(f"./graphs/solo/AP",cleanup=True,format="png")
    webbrowser.open_new_tab("./html/solo.html")