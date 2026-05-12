import math

def solve():
    try:
        w = int(input("Введіть відстань між стовпами: "))
        heights = list(map(int, input("Введіь висоти кожного з стовпів: ").split()))
    except EOFError:
        return

    n = len(heights)
    if n < 2:
        print("0.00")
        return

    dp = [[0.0, 0.0] for _ in range(n)]
    print(dp)
    for i in range(1, n):
        dist_1_1 = math.sqrt(w**2 + (1 - 1)**2)
        dist_prevMax_1 = math.sqrt(w**2 + (heights[i-1] - 1)**2)
        
        dp[i][0] = max(dp[i-1][0] + dist_1_1, dp[i-1][1] + dist_prevMax_1)

        dist_1_currMax = math.sqrt(w**2 + (1 - heights[i])**2)
        dist_prevMax_currMax = math.sqrt(w**2 + (heights[i-1] - heights[i])**2)
        
        dp[i][1] = max(dp[i-1][0] + dist_1_currMax, dp[i-1][1] + dist_prevMax_currMax)

    result = max(dp[n-1][0], dp[n-1][1])
    print(f"Максимальна потрібна кількість дроту - {result:.2f}")

if __name__ == "__main__":
    solve()