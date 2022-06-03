from collections import deque


def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append([nx, ny])


m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
queue = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i, j))

bfs()


def get_answer():
    day = 0
    for i in graph:
        for j in i:
            if j == 0:
                return -1

        day = max(day, max(i))
    return day-1


print(get_answer())
