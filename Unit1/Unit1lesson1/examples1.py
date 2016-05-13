#!/usr/bin/python
# Data Science

# My Fibonacci
n = [0,1]

for a in range (3,10):
    n.append(n[a-2]+n[a-3])

print n

# Thinkful Fibonacci
def F(n):
    if n < 2:
        return n
    else:
        return F(n-2) + F(n-1)

for a in range(0,10):
    print F(a)

# Tom's Fibonacci

def tomsFib():
    a, b = 0, 1
    while a<40:
        print a + b
        a, b = b, a + b

tomsFib()

# My FizzBuzz

for n in range(1,100):
    # if n is divisible by both 5 and 3...
    if n%5==0 and n%3==0:
        print "FizzBuzz"
    # else, if n is divisible by 3...
    elif n%3==0:
        print "Fizz"
    # else, if n is divisible by 5...
    elif n%5==0:
        print "Buzz"
    # else...
    else:
        print n

# Tom's Fizzbuzz

for n in range(1,100):
    st = ""
    if n%3==0:
        st += "Fizz"
    if n%5==0:
        st += "Buzz"
    print st or n
