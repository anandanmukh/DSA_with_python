def gcd(m, n):
    if m < n: # assume m >= n
        (m, n) = (n,m)

    while (m % n) != 0:
        diff = m - n
        # diff > n? possible!
        (m, n) = max(n, diff), min(n, diff)

    return n

if __name__ == "__main__":
    GCD = gcd(45,9)
    print(GCD)