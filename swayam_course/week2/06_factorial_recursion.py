def factorial(n):
    if n <= 0:
        return 1
    else:
        val = n * factorial(n - 1)
        return val
    
if __name__ == "__main__":
    n = 5
    val = factorial(n)
    print(f"Factorial of {n} is {val}")
