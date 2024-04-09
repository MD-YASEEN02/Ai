graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['F'],
    'F':[]
    }
visited=set()
def bfs(visited,graph,node):
    if node not in visited:
        print(node)
        for neighbour in graph[node]:
            bfs(visited,graph,neighbour)
bfs(visited,graph,'A')
