n = int(input())
money = list(map(int, input().split()))
m = int(input())

while sum(money) >= m:
    for i in range(n):
        if money[i] == max(money) & money[i] > (m // n):
            money[i] -= 1


print(max(money))

n = int(input())
money = list(map(int, input().split()))
m = int(input())

max_money = max(money)
# min_money = min(money) // 이렇게하면 틀림
min_money = 0

while max_money >= min_money:
    mid = (max_money + min_money) // 2
    res = 0

    for i in money:
        # 요청 예산이 상한액보다 클 경우 상한액 지급
        if i >= mid:
            res += mid
        # 요청 예산이 상한액보다 작을 경우 요청 예산 지급
        else:
            res += i

    # 지급예정인 금액이 m보다 작거나 같을경우 상한액을 높여주기위해
    # 최소 배정 금액을 상한액보다 +1 높여준다
    if res <= m:
        min_money = mid + 1
    # 지급 예정인 금액이 m보다 클 경우  상한액을 낮춰야 하므로
    # 최대 배정 금액을 상한액보다 -1 해준다
    else:
        max_money = mid - 1

print(max_money)




