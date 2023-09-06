def gcd(m,n):
    # assume m >= n
    if m < n:
        (m,n) = (n,m)

    if (m % n) == 0:
        return n
    
    else:
        diff = m - n
        # diff > n? possible!
        return (gcd(max(n, diff), min(n, diff)))
    

if __name__ == "__main__":
    GCD = gcd(45,9)
    print(GCD)