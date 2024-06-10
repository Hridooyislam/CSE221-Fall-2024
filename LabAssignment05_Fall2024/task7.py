from collections import defaultdict
input=open('input7.txt','r')
def dfs(graph, start, visited, distances):
    stack = [(start, 0)]
    visited[start] = True

    while stack:
        current, distance = stack.pop()
        distances[current] = distance

        for neighbor in graph[current]:
            if not visited[neighbor]:
                stack.append((neighbor, distance + 1))
                visited[neighbor] = True

def find_farthest_cities(graph, n):
    visited = [False] * (n + 1)
    distances = [0] * (n + 1)

    # First DFS to find city A
    dfs(graph, 1, visited, distances)
    city_a = distances.index(max(distances))
    print(distances)
    # Reset visited and distances arrays
    visited = [False] * (n + 1)
    distances = [0] * (n + 1)

    # Second DFS to find city B
    dfs(graph, city_a, visited, distances)
    city_b = distances.index(max(distances))
    print(distances)

    return city_a, city_b

# Read input
n= int(input.readline())
graph = defaultdict(list)

for _ in range(n - 1):
    u, v =list( map(int, input.readline.split()))
    graph[u].append(v)
    graph[v].append(u)

# Find and print the result
city_a, city_b = find_farthest_cities(graph, n)
print(city_a, city_b)
