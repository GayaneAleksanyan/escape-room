def sum_digits(n: int) -> int:
    return sum(int(digit) for digit in str(abs(n)))

def sum_digits_cycled(n: int) -> int:
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

print(sum_digits(1234))
print(sum_digits_cycled(1234))