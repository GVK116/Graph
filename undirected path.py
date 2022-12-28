def undirected_path(graph,src,dst,visit):
    if src == dst :
        return True
    if src in visit: return False
    visit.append(src)
    for i in graph[src]:
        if undirected_path(graph,i,dst,visit) == True: return True

    return False

def buildGraph(edge):
    d = {}
    for elem in edges:
        d[elem[0]] = []
        d[elem[1]] = []

    for elem in edges:
        d[elem[0]].append(elem[1])
        d[elem[1]].append(elem[0])
    return d


graph = {
    'i': ['j', 'k'],
    'j': ['i'],
    'k': ['i', 'm', 'l','j'],
    'm': ['k'],
    'l': ['k'],
    'o': ['n'],
    'n': ['o']
}

print(undirected_path(graph,'i','l',[]))

edges = [
    ['i','j'],
    ['k','i'],
    ['m','k'],
    ['k','l'],
    ['o','n']
]
