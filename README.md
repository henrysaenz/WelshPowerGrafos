# WelshPowellGrafos
Algoritmo Welsh Powell para la coloración de los vértices de un grafo
El algoritmo de Welsh-Powell es un algoritmo heurístico para la coloración de vértices en grafos no dirigidos. Su objetivo es asignar un color a cada vértice del grafo de manera que dos vértices adyacentes no tengan el mismo color, utilizando la menor cantidad de colores posibles.

El algoritmo de Welsh-Powell sigue los siguientes pasos:

1. Ordena los vértices del grafo en orden decreciente según su grado (número de vecinos).
2. Toma el vértice de mayor grado y asígnale el color 1
3.  Recorre los vértices restantes en el orden determinado en el paso 1 y asígnales el color más bajo posible que no esté siendo utilizado por ninguno de sus vecinos.
4. Repite el paso 3 hasta que todos los vértices hayan sido coloreados.

El algoritmo de Welsh-Powell puede no encontrar siempre la solución óptima, pero en muchos casos proporciona una buena aproximación utilizando un número reducido de colores.
