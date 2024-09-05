MOD = 10**9 + 7

def pow_mod(a, b, mod):
    result = 1
    a = a % mod
    while b > 0:
        if b % 2:
            result = (result * a) % mod
        b //= 2
        a = (a * a) % mod
    return result

def calc_chinh_hop_lap_chap_k(n, k):
    return pow_mod(n, k, MOD)

# Người dùng tự nhập giá trị
n = int(input("Nhập giá trị n: "))
k = int(input("Nhập giá trị k: "))
print("Số cấu hình chỉnh hợp lặp chập k của n:", calc_chinh_hop_lap_chap_k(n, k))
