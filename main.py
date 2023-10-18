#1.1 implement a recursive function to colculate tha factorial of a given number .
def factorial(n):
 
    if n == 0: 
        return 1

    return n * factorial(n-1)
  
# Driver code
num = 5;
print("Factorialof", num, "is", 
factorial(num))

# This code is contributed by smitha Dineash semwal 