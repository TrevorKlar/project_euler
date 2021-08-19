# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13.

# What is the 10 001st prime number?

import math #This is where we get all the math functions like math.sqrt()

def is_prime(n):
  for i in [2]+range(3, int(math.sqrt(n))+1, 2):
  # Checking divisibility by everything from 2 up to sqrt(n). We don't have to
  # check all the way up to n, since if i > sqrt(n) then n/i < sqrt(n). We also
  # skip all the even numbers since we already check divisibility by 2.
    if n%i == 0:
      return False # If n has any divisors, then it isn't prime.
    # Otherwise, do nothing
  # If the code gets to this line, then we checked all possible divisors and
  # none divided evenly.
  return True

counter = 6 # Count how many primes we've found
prime = 13 # Keep track of the highest prime found so far

while counter < 101:
  n = prime+2
  if is_prime(n):
    counter += 1 # A python shortcut for counter = counter + 1
    print(n)
    prime = n # Keep track of this highest prime and keep going
