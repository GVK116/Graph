def breadthfirstprint(graph,source):
    queue = [source]
    while (len(queue) > 0):
        current = queue.pop(0)
        print(current)
        for i in graph[current]:
            queue.append(i)





graph = {
    'a' : ['b','c'],
    'b' : ['d'],
    'c' : ['e'],
    'd' : ['f'],
    'e' : [],
    'f' : []
}

breadthfirstprint(graph,'a')



# a
# b
# c
# d
# e
# f