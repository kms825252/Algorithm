T = int(input())
for tc in range(1, T+1):
    cost = list(map(int, input().split()))
    plan = list(map(int, input().split()))

    dp = [0] * 12
    dp[0] = min(cost[0])