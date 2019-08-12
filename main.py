import os
from PIL import Image

def graficar(f,c,x,y,k,tipo):
    f1 = f
    c1 = c
    x1 = x
    y1 = y
    k1 = k
    grafo = ""

    # Apertura
    grafo += "digraph Tarea2{\n"
    '''
    if tipo is 1:
        grafo += str("rankdir=TB;\n\n")
    elif tipo is 2:
        grafo += str("rankdir=LR;\n\n")
    '''
    #grafo += str("{ rank=same tbl arr }\n")
    # Matriz
    grafo += str("subgraph cluster_0{\n")
    grafo += str("tbl [shape=\"plaintext\", label=<\n")
    grafo += str("<table border='0' cellborder='1'>\n")
    for i in range(f):
        grafo += str("<tr>\n")
        for j in range(c):
            if i is x and j is y:
                grafo += str("<td bgcolor=\"lightblue\">")
            else:
                grafo += str("<td>")
            grafo += str("(" + str(i)  + "," + str(j) + ")")
            grafo += str("</td>\n")
        grafo += str("</tr>\n")
    grafo += str("</table>\n")
    grafo += str(">];\n")
    grafo += str("label=\"Matriz\"\n")
    grafo += str("}\n\n")

    # Arreglo
    grafo += str("subgraph cluster_1{\n")
    grafo += str("arr [shape=\"plaintext\", label=<\n")
    grafo += str("<table border='0' cellborder='1'>\n")
    grafo += str("<tr>\n")
    for l in range(f*c):
        if l is k:
            grafo += str("<td bgcolor=\"lightblue\">")
        else:
            grafo += str("<td>")
        grafo += str("(" + str(l) + ")")
        grafo += str("</td>\n")
    grafo += str("</tr>\n")
    grafo += str("</table>\n")
    grafo += str(">];\n")    
    grafo += str("label=\"Arreglo\"\n")
    grafo += str("}\n\n")

    # Cierre
    if tipo is 1:
        grafo += str("label=\"Mapeo por Filas\"\n")
    else:
        grafo += str("label=\"Mapeo por Columnas\"\n")
    grafo += str("}")

    f = open("Matriz_Arreglo.dot","w+")
    f.write(grafo)
    f.close()

    os.system("dot -Tjpg Matriz_Arreglo.dot -o Matriz_Arreglo.jpg")
    im = Image.open('Matriz_Arreglo.jpg')
    im.show()
    pass

def mFilas():
    f = -1
    c = -1
    x = -1
    y = -1
    print("")

    while True:
        try:
            print("Numero de filas: ")
            f = int(input())
            print("Numero de columnas: ")
            c = int(input())
        except:
            print("Error al ingresar datos\n")

        if f > 0 and c > 0:
            break
        else:
            print("No pueden haber filas o colmnas con size 0\n")
    print("Matriz de: (" + str(f) + "," + str(c) + ")\n")

    # Tanto las posiciones en la matriz
    # y en el arreglo empiezan desde cero
    while True:
        try:
            print("Posicion en x: ")
            x = int(input())
            print("Posicion en y: ")
            y = int(input())
        except:
            print("Error al ingresar datos\n")

        if (x >= 0 and x < f) and (y >= 0 and y < c):
            break
        else:
            print("Posiciones fuera de los indices\n")
    print("Pos en la matriz: " + str(x) + "," + str(y))
    map = x * c + y
    print("Pos en el arreglo: " + str(map))

    graficar(f,c,x,y,map,1)

    print("")

def mColumnas():
    f = -1
    c = -1
    x = -1
    y = -1
    print("")

    while True:
        try:
            print("Numero de filas: ")
            f = int(input())
            print("Numero de columnas: ")
            c = int(input())
        except:
            print("Error al ingresar datos\n")

        if f > 0 and c > 0:
            break
        else:
            print("No pueden haber filas o colmnas con size 0\n")
    print("Matriz de: (" + str(f) + "," + str(c) + ")\n")

    # Tanto las posiciones en la matriz
    # y en el arreglo empiezan desde cero
    while True:
        try:
            print("Posicion en x: ")
            x = int(input())
            print("Posicion en y: ")
            y = int(input())
        except:
            print("Error al ingresar datos\n")

        if (x >= 0 and x < f) and (y >= 0 and y < c):
            break
        else:
            print("Posiciones fuera de los indices\n")
    print("Pos en la matriz: " + str(x) + "," + str(y))
    map = y * f + x
    print("Pos en el arreglo: " + str(map))

    graficar(f,c,x,y,map,2)

    print("")

if __name__ == "__main__":
    op = -1
    
    print("Tarea 2 -- 201603168")
    print("Mapeo Lexicografico")
    print("")
    while True:
        print("1. Mapeo por Filas")
        print("2. Mapeo por Columnas")
        print("3. Salir")
        op = input()
        
        if op is "1":
            mFilas()
        elif op is "2":
            mColumnas()
        elif op is "3":
            break
        else:
            print("Opcion invalida")