def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def main():
    n = int(input("Enter n: "))
    result = fibonacci(n)
    print(f"Fibonacci({n}) = {result}")


if __name__ == "__main__":
    main()