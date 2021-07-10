graph_list = {
    "A": ["B","C"],
    "B": ["D","E"],
    "C": ["B","F"],
    "D": [],
    "E": ["F"],
    "F": []
}

color = {}
parent ={}
trav_time = {}
dfs_trav_path = []

for node in graph_list:
    color[node]= "W"
    parent[node]= None
    trav_time[node]= [-1,-1]

time = 0

def DFS_algo(source):
    color[source] = "G"
    global time
    trav_time[source][0]= time
    dfs_trav_path.append(source)
    time += 1
    for child in graph_list[source]:
        if color[child] == "W":
            color[child] == "G"
            parent[child] = source
            DFS_algo(child)
    color[source] = "B"
    trav_time[source][1] = time
    time += 1

DFS_algo("A")
print(dfs_trav_path)
print(color)
print(trav_time)

