def is_prime(n: int) -> bool:
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def main():
    primes = []
    for i in range(2, 51):
        if is_prime(i):
            primes.append(i)
    print(primes)


if __name__ == "__main__":
    main()