def so_chu_so(n):
    if n < 10:
        return 1
    return 1 + so_chu_so(n // 10)

def tong_chu_so(n):
    if n == 0:
        return 0
    return n % 10 + tong_chu_so(n // 10)

N = int(input("Nhập số N: "))
if 1 < N < 10**6:
    print(f"Số chữ số của N: {so_chu_so(N)}")
    print(f"Tổng các chữ số của N: {tong_chu_so(N)}")
else:
    print("N phải lớn hơn 1 và nhỏ hơn 10^6.")