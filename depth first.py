# def depthfirstPrint(graph,source):
#     stack = [source]
#     while(len(stack) > 0):
#         current = stack.pop()
#         print(current)
#         for i in graph[current]:
#             stack.append(i)
#             print(stack)


def depthfirstPrint(graph,source):
    print(source)
    for i in graph[source]:
        depthfirstPrint(graph,i)

graph = {
    'a' : ['b','c'],
    'b' : ['d'],
    'c' : ['e'],
    'd' : ['f'],
    'e' : [],
    'f' : []
}

depthfirstPrint(graph,'a')