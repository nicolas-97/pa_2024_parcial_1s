# Parcial de Programación Avanzada - Búsqueda de Ruta Más Corta en Grafo Ponderado

En este parcial, se evaluará su capacidad para analizar y mejorar un algoritmo de búsqueda de ruta más corta en un grafo ponderado.

## Descripción del Problema

Se proporcionará un algoritmo implementado en Python que busca la ruta más corta entre dos nodos en un grafo ponderado. Su tarea consistirá en analizar este algoritmo, identificar sus limitaciones y mejorar su eficiencia para garantizar que siempre encuentre la ruta más corta.

## Objetivos

- Implementar un algoritmo que encuentre la ruta más corta desde un nodo de inicio dado hasta un nodo objetivo en el grafo ponderado.
- Utilizar técnicas de algoritmos de ordenamiento y búsqueda para manipular y procesar la lista de aristas del grafo.
- Demostrar habilidades de análisis y solución de problemas en situaciones del mundo real.

## Restricciones

- Los estudiantes deben implementar su propio algoritmo para encontrar la ruta más corta en el grafo ponderado.
- No se permite copiar directamente algoritmos existentes. Se espera que los estudiantes desarrollen su propia solución utilizando los conocimientos adquiridos en la asignatura.
- Se debe proporcionar una explicación clara de la solución implementada, así como también una justificación de cualquier decisión de diseño o implementación.

## Archivos Proporcionados

1. **graph.py**: Contiene el algoritmo de búsqueda de ruta más corta en el grafo ponderado. Deben analizar este algoritmo y proponer mejoras.
2. **README.md**: Este archivo proporciona una descripción del parcial y las instrucciones para completarlo.

## Consideraciones
 Los grafos seran representados en una lista de tuplas por ejemplo:
```python
 aristas = [(0, 1, 2), (0, 2, 4), (1, 2, 1), (1, 3, 7), (2, 3, 3)]
````
Donde cada tupla tiene 3 posiciones
- la primera posicion indica el nodo de origen
- La segunda posicion indica el nodo de destino o relacionado
- La tercera poscion indica el peso de ese camino

A continuacion una representacion grafica de este grafo ponderado

![Grafo Ponderado](/images/grafo.jpg)


## Tareas a Realizar

1. Analizar el algoritmo proporcionado en graph.py y describir su funcionamiento, complejidad temporal y en que casos el algoritmo se demoraria mas, en que casos sufre mas.
3. Implementar las mejoras correspondientes en un script llamado (`resolve.py`) que nos aseguren que siempre va a encontrar la ruta mas corta de la manera mas eficiente posible y explicar cómo estas mejoras mejoran la eficiencia del algoritmo.
4. Crear un archivo de texto (`.txt`) o Markdown (`.md`) que incluya el análisis del algoritmo, las mejoras propuestas y la implementación de las mejoras.

## Entrega

Se habilitara una entrega en avata, por favor comprimir la carpeta y subirla, gracias!

¡Buena suerte!
