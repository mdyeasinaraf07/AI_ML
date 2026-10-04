t = int(input())

for i in range(t):
    num = int(input())
    if num == 0:
        print(0)
        continue
    while num > 0:
        last_digit = num % 10
        num //= 10
        print(last_digit, end = " ")

    print()
