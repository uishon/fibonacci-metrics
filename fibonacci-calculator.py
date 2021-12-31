def fib(n):
    if n < 0:
        raise ValueError(f"{n} < 0")

    if n < 2:
        return n

    return fib(n-1) + fib(n-2)


def main():
    n = 0
    while 1:
        n += 1
        print(f"{fib(n)}")


if __name__ == "__main__":
    main()
