def gcd(m,n):
    cf = []
    for i in range(1, min(m,n)+1):
        if (m%i) == 0 and (n%i) == 0:
            cf.append(i)
    
    return(cf[-1])

if __name__ == "__main__":
    GCD = gcd(45,9)
    print(GCD)