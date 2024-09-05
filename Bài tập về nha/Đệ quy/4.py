def gcd(M, N):
    if N == 0:
        return M
    return gcd(N, M % N)

M = int(input("Nhập số M: "))
N = int(input("Nhập số N: "))
if M < 10**6 and N < 10**6:
    print(f"Ước chung lớn nhất của {M} và {N} là: {gcd(M, N)}")
else:
    print("M và N phải nhỏ hơn 10^6.")