# def has_path(graph,src,dst):
#     if (src == dst):
#         return True
#     for i in graph[src]:
#         if (has_path(graph,i,dst) == True):
#             return True
#
#     return False

def has_path(graph,src,dst):
    queue = [src]
    while (len(queue) > 0):
        curr = queue.pop(0)
        if (curr == dst):
            return True
        for i in graph[curr]:
            queue.append(i)
    return False




graph = {
    'f' : ['g', 'i'],
    'g' : ['h'],
    'h' : [],
    'i' : ['g','k'],
    'j' : ['i'],
    'k' : []
}

print(has_path(graph,'g','i'))