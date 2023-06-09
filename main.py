#Ejemplo 1.

"""G = [[0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [0, 1, 0, 0]]
"""
#Ejemplo 2.

G = [[0, 1, 0, 0, 0, 0, 1], [1, 0, 1, 1, 0, 0, 1], [0, 1, 0, 1, 0, 1, 0],
     [0, 1, 1, 0, 1, 0, 0], [0, 0, 0, 1, 0, 1, 1], [0, 0, 1, 0, 1, 0, 1],
     [1, 1, 0, 0, 1, 1, 0]]


vertices = "abcdefghijklmnopqrstuvwxyz"  # nombre de los vértices del grafo
idxv = {}
for i in range(len(G)):
  idxv[vertices[i]] = i
#asigna a cada vértice su índice correspondiente en la matriz de adyacencia G.

grados = []  #guardar grados de los vértices
for i in range(len(G)):
  grados.append(sum(G[i]))
  
colores = {}  #almacena los posibles colores
for i in range(len(G)):
  colores[vertices[i]] = [
    "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10"
  ]

ordenVertices = []
indices = []

for i in range(len(grados)):
  max = 0
  for j in range(0, len(grados)):
    if j not in indices:  #Validación que no se ha agregado a ordenVertices
      if grados[j] > max:
        max = grados[j]
        idx = j

  indices.append(idx)
  ordenVertices.append(vertices[idx])
  
print(ordenVertices)
print(indices)

solucion = {}
for n in ordenVertices:
  print(n)
  colorear = colores[n]
  solucion[n] = colorear[0]
  vecino = G[idxv[n]]
  for j in range(len(vecino)):
    if vecino[j] == 1 and (colorear[0] in colores[vertices[j]]):
      colores[vertices[j]].remove(colorear[0])
    


for t, w in sorted(solucion.items()):
  print("Vértice", t, " = ", w)

#Implementación por Valentina Bustamante y Zharick Molina