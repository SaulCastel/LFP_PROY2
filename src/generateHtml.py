from validate import path
import webbrowser
import xml.etree.ElementTree as ET

def genTable(pt:path,string):
    entries:list = pt.history
    file = open(f"./html/tabla.html","w")
    file.write("<!DOCTYPE html>\n")
    root = ET.Element("html")
    head = ET.Element("head")
    title = ET.Element("title")
    title.text = "Reporte"
    cssArgs = {
        "rel" :"stylesheet",
        "href" :"styles/tablas.css"
    }
    css = ET.Element("link",cssArgs)
    head.append(title)
    head.append(css)
    body = ET.Element("body")
    # Llenando el body
    input = ET.Element("h1")
    input.text = f"Cadena: {string}"
    body.append(input)
    table = ET.Element("table")
    header = ET.Element("tr")
    c0 = ET.Element("th")
    c0.text = "Iteración"
    header.append(c0)
    c1 = ET.Element("th")
    c1.text = "Pila"
    header.append(c1)
    c2 = ET.Element("th")
    c2.text = "Entrada"
    header.append(c2)
    c3 = ET.Element("th")
    c3.text = "Transición"
    header.append(c3)
    table.append(header)
    index = 0
    for entry in entries:
        index += 1
        row = ET.Element("tr")
        d0 = ET.Element("td")
        d0.text = str(index)
        row.append(d0)
        d1 = ET.Element("td")
        d1.text = str(entry.stack)
        row.append(d1)
        d2 = ET.Element("td")
        d2.text = str(entry.input)
        row.append(d2)
        d3 = ET.Element("td")
        d3.text = str(entry.prod)
        row.append(d3)
        table.append(row)  
    body.append(table)
    result = ET.Element("h1")
    if pt.valid:
        result.text = "Cadena aceptada"
    else:
        result.text = "Cadena invalida"
    body.append(result)
    root.append(head)
    root.append(body)
    tree = ET.ElementTree(root)
    ET.indent(tree, space="\t", level=0)
    tree.write(file_or_filename=file,encoding="unicode",short_empty_elements=True)
    file.close()
    webbrowser.open_new_tab(f"./html/tabla.html")