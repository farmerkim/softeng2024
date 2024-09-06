def is_prime(n: int) -> bool:
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def main():
    n = int(input("숫자를 입력하세요=>"))

    if is_prime(n):
        print(f"{n}은 소수입니다.")

    else:
        print(f"{n}은 소수가 아닙니다.")


if __name__ == "__main__":
    main()