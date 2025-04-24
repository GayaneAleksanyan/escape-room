def get_prime(numbers):
    primes = []
    for num in numbers:
        if num < 2:
            continue
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(get_prime(my_list))
