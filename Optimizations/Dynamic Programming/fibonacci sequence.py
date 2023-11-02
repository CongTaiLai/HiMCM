def fibonacci(n):
    # Create a list to store Fibonacci numbers
    fib = [0] * (n + 1)

    # Base cases
    fib[0] = 0
    fib[1] = 1

    # Compute the Fibonacci numbers from the bottom up
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]


# Test the Fibonacci function
n = 10  # Change this to the desired Fibonacci number
result = fibonacci(n)
print(f"The {n}-th Fibonacci number is: {result}")
