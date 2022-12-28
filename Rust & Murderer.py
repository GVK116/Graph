def Graph(edges,k):
    graph = dict()
    for i in edges:
        graph[i[0]],graph[i[1]] = list(map(int,range(1,k+1))),list(map(int,range(1,k+1)))
    for i in edges:
        graph[i[0]].remove(i[0])
        graph[i[0]].remove(i[1])
        graph[i[1]].remove(i[0])
    return graph

def direct(start,dest,graph,visited):
    visited.append(start)
    que = [[start,0]]
    while(len(que)>0):
        print(que)
        node,dist = que.pop(0)
        if node == dest:
            return dist
        for i in graph.get(node):
            if i not in visited:
                visited.append(i)
                que.append([i,dist+1])


def main():
    edges,distance,visited = [],[],[]
    N,M = map(int,input().split())
    for _ in range(M):
        edges.append(list(map(int,input().split())))
    distance.append(direct(int(input()),1,Graph(edges,N),visited))

    return distance



print(main())