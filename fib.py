def tribonacci(n):
    a, b, c = 0, 1, 1
    for _ in range(n):
        a, b, c = b, c, a + b + c
    return a


def main():
    n = int(input("Enter n: "))
    result = tribonacci(n)
    print(f"Tribonacci({n}) = {result}")


if __name__ == "__main__":
    main()