#function which calls itself is called recursion``

def factorial(n):
     if n == 0 or n == 1:  # Base case
        return 1
     else:
        return n*factorial(n-1) 

n=5
print(factorial(n))