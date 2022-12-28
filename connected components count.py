def connected(graph):
    count = 0
    visit = []
    for i in graph:
        if (explore(graph,i,visit)==True):
            count += 1

    return count


def explore(graph,current,visited):
    if current in visited : return False
    visited.append(current)

    for j in graph[current]:
        explore(graph,j,visited)

    return True



graph = {
    3:[],
    4:[6],
    6:[4,5,7,8],
    7:[6],
    8:[6],
    5:[6],
    1:[2],
    2:[1]
}


a = [1,2,3,4]
print(connected(graph))