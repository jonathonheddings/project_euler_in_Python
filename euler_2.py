# Problem Number Two
#
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
#   By starting with 1 and 2, the first 10 terms will be:
#   1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
#    find the sum of the even-valued terms.

fib_minor = 1
fib_major = 2
buffer = 0
evens = 0

while(fib_major <= 4000000):
    
    # Check Evens
    if fib_major % 2 == 0:
        evens += fib_major
    
    # Move Fibonacci Forward
    buffer = fib_major + fib_minor
    fib_minor = fib_major
    fib_major = buffer

print("Sum of Even Fibonacci Numbers Up Until 4 Million: ", evens)