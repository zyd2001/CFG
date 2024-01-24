import networkx as nx

def IDF(start : set, frontier):
    result = set()
    visited = set()
    change = True
    while change:
        change = False
        for i in start:
            if i not in visited:
                visited.add(i)
                result.update(frontier[i])
                change = True
        start = result.copy()
    
    return result