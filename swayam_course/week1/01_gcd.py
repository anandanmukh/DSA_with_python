'''
1. fm, fn are the list of factors of m & n repectively
2. cf is the list for common factors
3. the last element from the list is chosen to find the greatest number from the common factors
'''



def gcd(m,n):
    fm = []
    fn = []
    cf = []

    for i in range(1,m+1):
        if (m%i) == 0:
            fm.append(i)

    for j in range(1,n+1):
        if (n%j) == 0:
            fn.append(j)

    for f in fm:
        if f in fn:
            cf.append(f)

    return (cf[-1])


if __name__ == "__main__":
    GCD = gcd(45,9)
    print(GCD)