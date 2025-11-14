# divider.py

def divide_two(a, b):
    """Return a / b with zero-division protection."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def divide_chain(*nums):
    """Divide first number by each of the remaining numbers in order."""
    if len(nums) < 2:
        raise ValueError("Provide at least two numbers")
    result = nums[0]
    for i, n in enumerate(nums[1:], start=2):
        if n == 0:
            raise ZeroDivisionError(f"Zero at position {i}")
        result /= n
    return result

def divide_list(nums):
    """Same as divide_chain but takes an iterable of numbers."""
    nums = list(nums)
    return divide_chain(*nums)

if __name__ == "__main__":
    # Demo/CLI: python divider.py 100 2 5 -> prints 10.0
    import sys
    if len(sys.argv) < 3:
        print("Usage: python divider.py n1 n2 [n3 ...]")
        sys.exit(1)
    try:
        values = [float(x) for x in sys.argv[1:]]
        print(divide_list(values))
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
