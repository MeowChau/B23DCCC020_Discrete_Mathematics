from itertools import combinations
from math import gcd
from functools import reduce

def lcm(a, b):
    return a * b // gcd(a, b)

def calc_so_nho_hon_n_khong_chia_het(n, primes):
    count = 0
    k = len(primes)
    for i in range(1, k+1):
        for comb in combinations(primes, i):
            l = reduce(lcm, comb)
            if i % 2:
                count += n // l
            else:
                count -= n // l
    return n - count

# Người dùng tự nhập giá trị
n = int(input("Nhập giá trị n: "))
primes = list(map(int, input("Nhập k số nguyên tố (cách nhau bởi dấu cách): ").split()))
print("Số các số tự nhiên nhỏ hơn hoặc bằng n và không chia hết cho bất cứ số nguyên tố nào trong k số:", calc_so_nho_hon_n_khong_chia_het(n, primes))