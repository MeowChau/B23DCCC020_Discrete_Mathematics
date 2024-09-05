MOD = 10**9 + 7

def calc_mat_thu_tu(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    d = [0] * (n + 1)
    d[1], d[2] = 0, 1
    for i in range(3, n + 1):
        d[i] = (i - 1) * (d[i - 1] + d[i - 2]) % MOD
    return d[n]

# Người dùng tự nhập giá trị
n = int(input("Nhập giá trị n: "))
print("Số mất thứ tự D(n):", calc_mat_thu_tu(n))