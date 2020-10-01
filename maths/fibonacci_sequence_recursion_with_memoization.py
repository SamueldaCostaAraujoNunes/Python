# Fibonacci Sequence Using Recursion and Memoization

# Memoization Concept: https://en.wikipedia.org/wiki/Memoization
# Fibonacci Concept : https://pt.wikipedia.org/wiki/Sequ%C3%AAncia_de_Fibonacci

cache = dict()


def fibonacci(n):
    """
    Return number of index n in sequence fibonacci
    >>> fibonacci(12)
    89
    >>> [fibonacci(i) for i in range(12)]
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    """
    aux = n

    if aux in cache:
        return cache[aux]

    if (n == 0) or (n == 1):
        ans = n
    else:
        ans = fibonacci(n - 1) + fibonacci(n - 2)
    cache[aux] = ans

    return ans


def main() -> None:
    number = 12
    print(f"The first {number} Fibbonaci sequence terms are:")
    print([fibonacci(n) for n in range(number)])


if __name__ == "__main__":
    main()