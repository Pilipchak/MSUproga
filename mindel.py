a = int(input())
def if_prime(x):
    if x%2==0:
        return 2
    i=3
    while i**2<x:
        if (x%i==0):
            return i
        i+=2
    else:
        return x
print(if_prime(a))
  