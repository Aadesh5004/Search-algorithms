from queue import Empty, Queue
graph_list = {
    "A": ["B","D"],
    "B": ["A","C"],
    "C": ["B"],
    "D": ["A", "E","F"],
    "E": ["D", "F","G"],
    "F": ["D", "E", "H"],
    "G": ["E", "H"],
    "H": ["F","G"]
}

visited = {}
parent = {}
bfs_transverse_path = []
queue = Queue()
level = {}

for node in graph_list.keys():
    parent[node] = None
    visited[node] = False
    level[node] = 0

source = "A"
queue.put(source)
level[source] = 0
visited[source] = True

while not queue.empty():
    a = queue.get()
    bfs_transverse_path.append(a)
    for b in graph_list[a]:
        if not visited[b]:
            visited[b] = True
            parent[b] = a
            level[b] = level[a]+1
            queue.put(b)

#print(parent)
destination = "G"
path = []
while destination is not None:
    path.append(destination)
    destination = parent[destination]
path.reverse()
print(path)
        


