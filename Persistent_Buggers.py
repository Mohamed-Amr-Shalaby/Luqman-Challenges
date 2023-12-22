import math
def persistence(n, iterations = 0):
    product = 1
    if n < 10:
        return iterations
    while n > 0:
        product = product * (n % 10)
        n = math.floor(n/10)
    return (persistence(product, iterations + 1))

print(persistence(39))