def sort_graph(aristas: list) -> list:

    if len(aristas) <= 1:
        return aristas
    
    middle = len(aristas) // 2

    left = [x for x in aristas if aristas[middle][2] > x[2]]
    right = [x for x in aristas if aristas[middle][2] < x[2]]

    return sort_graph(left) + [aristas[middle]] + sort_graph(right)

def search_objetive(aristas:list, target: int, start = 0, end = 0) -> int:

    if start == 0 and end == 0:
        end = len(aristas)
    
    if start >= end:
        return -1

    middle = (start + end) // 2
    if aristas[middle][1] == target:
        return middle
    elif aristas[middle][1] > target:
        return search_objetive(aristas, target, start, middle)
    elif aristas[middle][1] < target:
        return search_objetive(aristas, target, middle + 1, end)

def bad_graph_algorithm(aristas:list, start_node: int, objetive_node: int) -> list:
    objetive = search_objetive(aristas, objetive_node)

    if objetive == -1:
        return []

    if (aristas[objetive][0] == start_node):
        return [aristas[objetive]]
    
    return  bad_graph_algorithm(aristas, start_node, aristas[objetive][0]) + [aristas[objetive]] 




def main():

    aristas = [(0, 1, 2), (0, 2, 4), (1, 2, 1), (1, 3, 7), (2, 3, 3)]
    aristas_ordenadas_por_peso = sort_graph(aristas)

    path = bad_graph_algorithm(aristas, 0, 3)

    print(path)
    


if __name__ == "__main__":
    main()
