def fibonacci_iterative(n):
    """Return the nth Fibonacci number using an iterative approach."""
    if n < 0:
        raise ValueError("n must be non-negative")
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a