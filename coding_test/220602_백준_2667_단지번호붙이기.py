from collections import deque


def bfs(graph, x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque([(x, y)])
    # 아래로 대체 가능
    # queue = deque()
    # queue.append((x,y))

    graph[x][y] = 0
    house = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1:
                    queue.append([nx, ny])
                    graph[nx][ny] = 0
                    house +=1
    return house


n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
cnt = 0;
house_cnt = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house_cnt.append(bfs(graph, i, j))
            cnt +=1

house_cnt.sort()
print(cnt)
for hc in house_cnt:
    print(hc)