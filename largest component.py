def long_component(graph):
    count = 0
    valid = []
    for node in graph:
        size = exploresize(graph,node,valid)
        if size > count:
            count = size
    return count

def exploresize(graph,node,valid):
    if node in valid:
        return 0
    valid.append(node)
    size = 1
    for i in graph[node]:
        size+=exploresize(graph,i,valid)

    return size



graph = {
    0:[8,1,5],
    1:[0],
    5:[0,8],
    8:[0,5],
    2:[3,4],
    3:[2,4],
    4:[3,2]
}

print(long_component(graph))