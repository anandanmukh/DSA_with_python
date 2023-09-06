def gcd(m, n):
    if m < n: # assume m >= n
        (m, n) = (n, m)

    if (m % n) == 0:
        return n
    
    else:
        return (gcd(n, m%n)) # m%n < n, always !
    
if __name__ == "__main__":
    GCD = gcd(45,9)
    print(GCD)