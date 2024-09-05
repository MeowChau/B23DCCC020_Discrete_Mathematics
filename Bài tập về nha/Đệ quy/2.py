def to_hop(n, k):
    if k == 0 or k == n:
        return 1
    return to_hop(n-1, k-1) + to_hop(n-1, k)

n = int(input("Nhập giá trị n: "))
k = int(input("Nhập giá trị k: "))
if 2 <= k <= n <= 1000:
    print(f"Số tổ hợp chập {k} của {n} là: {to_hop(n, k)}")
else:
    print("Điều kiện 2 <= k <= n <= 10^3 không thỏa mãn.")