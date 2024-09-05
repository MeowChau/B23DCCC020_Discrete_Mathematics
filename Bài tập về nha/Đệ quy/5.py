def thap_ha_noi(n, from_rod, to_rod, aux_rod):
    if n == 1:
        print(f"Di chuyển đĩa 1 từ cọc {from_rod} sang cọc {to_rod}")
        return
    thap_ha_noi(n-1, from_rod, aux_rod, to_rod)
    print(f"Di chuyển đĩa {n} từ cọc {from_rod} sang cọc {to_rod}")
    thap_ha_noi(n-1, aux_rod, to_rod, from_rod)

N = int(input("Nhập số nguyên dương N: "))
print(f"Thứ tự các bước giải bài toán tháp Hà Nội với {N} đĩa:")
thap_ha_noi(N, 'A', 'C', 'B')