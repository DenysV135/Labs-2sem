import math

def calculate_max_wire_length(w, heights):
    n = len(heights)
    if n < 2:
        return 0.0

    dp = [[0.0, 0.0] for _ in range(n)]

    for i in range(1, n):
        dist_1_1 = math.sqrt(w**2 + (1 - 1)**2)
        dist_prev_max_1 = math.sqrt(w**2 + (heights[i-1] - 1)**2)
        dp[i][0] = max(dp[i-1][0] + dist_1_1, dp[i-1][1] + dist_prev_max_1)

        dist_1_curr_max = math.sqrt(w**2 + (1 - heights[i])**2)
        dist_prev_max_curr_max = math.sqrt(w**2 + (heights[i-1] - heights[i])**2)
        dp[i][1] = max(dp[i-1][0] + dist_1_curr_max, dp[i-1][1] + dist_prev_max_curr_max)

    return max(dp[n-1][0], dp[n-1][1])

def solve():
    try:
        w_line = input().strip()
        if not w_line:
            return
        w = int(w_line)
        
        h_line = input().strip()
        if not h_line:
            return
        heights = list(map(int, h_line.split()))
        
        print(f"{calculate_max_wire_length(w, heights):.2f}")
    except (EOFError, ValueError):
        pass

if __name__ == "__main__":
    solve()
