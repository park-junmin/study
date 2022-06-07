n = int(input())
rgb_graph = []

for i in range(n):
    rgb_graph.append(list(map(int, input().split())))

for i in range(1, n):
    rgb_graph[i][0] = rgb_graph[i][0] + min(rgb_graph[i-1][1], rgb_graph[i-1][2])
    rgb_graph[i][1] = rgb_graph[i][1] + min(rgb_graph[i-1][0], rgb_graph[i-1][2])
    rgb_graph[i][2] = rgb_graph[i][2] + min(rgb_graph[i-1][0], rgb_graph[i-1][1])

print(min(rgb_graph[n-1]))