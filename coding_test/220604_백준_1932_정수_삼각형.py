n = int(input())
tree = []

for i in range(n):
    tree.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            tree[i][j] = tree[i-1][j] + tree[i][j]
        elif j == i:
            tree[i][j] = tree[i-1][j-1] + tree[i][j]
        else:
            tree[i][j] = max(tree[i-1][j] + tree[i][j], tree[i-1][j-1] + tree[i][j])

print(max(tree[n-1]))