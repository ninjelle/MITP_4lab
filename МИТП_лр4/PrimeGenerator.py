def prime_generator(limit):

    for num in range(2, limit + 1):
        is_prime = True
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            yield num

limit = int(input("Enter limit: "))

print(f"Prime numbers up to {limit}:")
for prime in prime_generator(limit):
    print(prime, end=" ")
