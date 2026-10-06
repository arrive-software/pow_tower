def pow_tower(n):
    """
    Calculate the power tower of n, which is defined as n^(n^(n^...)) with n levels.
    
    Args:
        n (int): The base of the power tower and the number of levels.
        
    Returns:
        int: The result of the power tower calculation.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    
    result = n
    for _ in range(n - 1):
        result = n ** result
    return result
# print(pow_tower(3))


def Fibonacci(num):
    """Return the nth Fibonacci number."""
    if num < 0:
        raise ValueError("num must be non-negative.")
    if num in (0, 1):
        return num

    a, b = 0, 1
    for _ in range(2, num + 1):
        a, b = b, a + b
    return b
print(Fibonacci(10000))  # Example usage