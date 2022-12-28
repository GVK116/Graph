def shortest(graph,sta,dst):
    queue = [[sta,0]]
    visired = [sta]
    while (len(queue)>0):
        [node , distance] = queue.pop()
        if (node == dst):
            return distance
        for i in graph[node]:
            if i not in visired:

                visired.append(i)
                queue.append([i,distance+1])
    return -1




graph = {
    'w': ['x', 'v'],
    'x': ['w', 'y'],
    'y': ['x', 'z'],
    'z': ['y', 'v'],
    'v': ['z', 'w']
}






print(shortest(graph,'w','z'))
