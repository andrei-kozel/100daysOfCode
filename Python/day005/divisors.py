# Count the number of divisors of a positive integer n.


def divisors(n):
    count = 0
    for x in range(1, n+1):
        if n % x == 0:
            count += 1
    print(count)
    return count


divisors(4)   # 3 -> 1, 2, 4
divisors(5)   # 2 -> 1, 5
divisors(12)  # 6 -> 1, 2, 3, 4, 6, 12
divisors(30)  # 8 -> 1, 2, 3, 5, 6, 10, 15, 30
