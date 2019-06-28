import math
print(math.sqrt(81))

## math is a modules, module contains methods

from math import sqrt as s
print(s(9))

## Copying into an object
a=math.factorial(5)
print(a)

##Factorial
n = 5
k = 3

a = math.factorial(5) / math.factorial(k) * math.factorial(n-k)
print(a)

#Above can also be written as 

from math import factorial
b = factorial(n) / factorial(k) * factorial(n-k)
print(b)


#It can simplified as

from math import factorial as f
c = f(n) / f(k) * f(n-k)
print(c)

