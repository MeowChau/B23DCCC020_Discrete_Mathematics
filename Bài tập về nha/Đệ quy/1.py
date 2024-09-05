def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Nhập số nguyên dương n chia hết cho 6 (n < 1000): "))
if n % 6 != 0 or n >= 1000:
    print("n phải chia hết cho 6 và nhỏ hơn 1000.")
else:
    print(f"Số Fibonacci thứ 1: {fibonacci(1)}")
    print(f"Số Fibonacci thứ {n//3}: {fibonacci(n//3)}")
    print(f"Số Fibonacci thứ {n//2}: {fibonacci(n//2)}")
    print(f"Số Fibonacci thứ {n}: {fibonacci(n)}")
