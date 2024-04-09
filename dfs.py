graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['F'],
    'F':[]
    }
visited=[]
queue=[]
def dfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:
        s=queue.pop(0)
        print(s,end=" ")
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
dfs(visited,graph,'A')