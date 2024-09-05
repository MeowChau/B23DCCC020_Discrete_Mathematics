MOD = 10**9 + 7

def calc_xuc_xac_sum_2n(n):
    dp = [0] * (2 * n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(6 * i, i - 1, -1):
            dp[j] = sum(dp[j - k] for k in range(1, 7) if j - k >= 0) % MOD
    return dp[2 * n]

# Người dùng tự nhập giá trị
n = int(input("Nhập giá trị n: "))
print("Số cách lắc xúc xắc để tổng bằng 2n:", calc_xuc_xac_sum_2n(n))