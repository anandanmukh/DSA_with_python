def divides(m, n):
    '''function to check wether two numbers are divisible or not'''
    if n%m == 0:
        return True
    else:
        return False
    
def even(n):
    '''using the divides finction to check wether the numbers are even or not'''
    return divides(2, n)

def odd(n):
    '''taking the opposite of the divides function to check wether a number is odd or not'''
    return (not divides (2, n))