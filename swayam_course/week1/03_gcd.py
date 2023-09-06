def gcd(m, n):
    for i in range(1, min(m,n)+1):
        if (m%i) == 0 and (n%i) == 0:
            mrcf = i
    # mrcf = most recent common factor
    return (mrcf)

if __name__ == "__main__":
    GCD = gcd(45,9)
    print(GCD)