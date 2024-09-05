MOD = 10**9 + 7

def calc_nghiem_phuong_trinh(n, m, Y):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(Y[i-1], m + 1):
            dp[i][j] = (dp[i-1][j] + dp[i][j-Y[i-1]]) % MOD
    return dp[n][m]

# Người dùng tự nhập giá trị
n = int(input("Nhập giá trị n: "))
m = int(input("Nhập giá trị m: "))
Y = list(map(int, input("Nhập dãy Y (cách nhau bởi dấu cách): ").split()))
print("Số nghiệm của phương trình:", calc_nghiem_phuong_trinh(n, m, Y)