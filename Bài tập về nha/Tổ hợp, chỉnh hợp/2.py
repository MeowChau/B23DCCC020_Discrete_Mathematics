MOD = 10**9 + 7

def factorial_mod(n, mod):
    fact = [1] * (n + 1)
    for i in range(2, n + 1):
        fact[i] = (fact[i-1] * i) % mod
    return fact

def inverse_factorial_mod(fact, mod):
    inv_fact = [1] * len(fact)
    inv_fact[-1] = pow_mod(fact[-1], mod - 2, mod)
    for i in range(len(fact) - 2, 0, -1):
        inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % mod
    return inv_fact

def calc_to_hop_chap_k(n, k):
    fact = factorial_mod(n, MOD)
    inv_fact = inverse_factorial_mod(fact, MOD)
    return (fact[n] * inv_fact[k] % MOD) * inv_fact[n - k] % MOD

# Người dùng tự nhập giá trị
n = int(input("Nhập giá trị n: "))
k = int(input("Nhập giá trị k: "))
print("Số cấu hình tổ hợp chập k của n:", calc_to_hop_chap_k(n, k))