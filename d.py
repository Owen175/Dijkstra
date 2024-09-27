# Dijkstra's
graph = {"A": {"B": 2, "C": 3, "D": 7}, "B": {"A": 2, "D": 4}, "C": {"A": 3}, "D": {"A": 7, "B": 4}}
start_node = "A"
distances = {}
for x in graph.keys():
    if x == start_node:
        distances[x] = 0
    else:
        distances[x] = 2**16 - 1 


queue = ["A"]
explored = []

while len(queue) != 0:
    current_node = queue.pop(0)
    current_distance = distances[current_node]
    explored.append(current_node)
    
    for x in graph[current_node]:
        if x not in explored:
            if len(queue) == 0:
                queue.append(x)
            else:
                j = 0
                while j < len(queue) and distances[x] > distances[queue[j]]:
                    j += 1
                queue.insert(j, x)
            distances[x] = current_distance + graph[current_node][x]

print(distances)

