# Function for nth Fibonacci number
# Credit to: https://www.freecodecamp.org/news/the-fibonacci-sequence-in-5-different-programming-languages-1c6514c749e5/

def F(n):  if n == 0:
   return 0  if n == 1:
   return 1  else:
   return F(n-1) + F(n-2)

print(Fibonacci(9))
