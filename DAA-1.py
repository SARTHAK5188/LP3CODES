iteration_counter = 0
recursion_counter = 0

def fibonacci(n):
    global iteration_counter
    fib_series = []
    a = 0
    b = 1

    for i in range(n):
        fib_series.append(a)
        a, b = b, a + b
        iteration_counter += 1

    return fib_series

def fibonacci_recursive(n):
    global recursion_counter
    recursion_counter += 1
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = fibonacci_recursive(n - 1)
        fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series

n = int(input("Enter total numbers to print in fibonacci series: "))
print("Fibonacci Series (non-recusive):\t", fibonacci(n))
print("Iteration counter:\t", iteration_counter)

print("Fibonacci Series (recusive):\t\t", fibonacci_recursive(n))
print("Recursion counter:\t", recursion_counter)