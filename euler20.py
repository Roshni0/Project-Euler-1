def factorial(n):
    if n == 0: return 1
    else: return n * factorial(n - 1)
 
def sum_digits(n):
    return sum([int(i) for i in str(n)])
 
sumOfFactorial = sum_digits(factorial(100))
 
print(sumOfFactorial)