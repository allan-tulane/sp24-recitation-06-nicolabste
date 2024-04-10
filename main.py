def fib_recursive(n, counts):
  """
  Return the nth Fibonacci number. 
  counts is a list of n+1 elements, where counts[i] is incremented
  each time fib_recursive(i, counts) is called.
  """
  if n <= 1:
      return n

  counts[n] += 1  # Increment the count for this value of n

  # Recursive calls for the two previous Fibonacci numbers
  return fib_recursive(n-1, counts) + fib_recursive(n-2, counts)

    

    
def fib_top_down(n, fibs):
  # Base case: if the Fibonacci number is already computed, return it
  if fibs[n] != -1:
      return fibs[n]

  # Base cases: F0 = 0 and F1 = 1
  if n <= 1:
      fibs[n] = n
      return n

  # Recursive computation with memoization
  fibs[n] = fib_top_down(n-1, fibs) + fib_top_down(n-2, fibs)
  return fibs[n]



def fib_bottom_up(n):
  if n <= 1:
    return n

  fibs = [0] * (n+1)  # Initialize the list of Fibonacci numbers with 0's
  fibs[1] = 1  # F1 = 1

  # Iteratively compute each Fibonacci number from 2 to n
  for i in range(2, n+1):
    fibs[i] = fibs[i-1] + fibs[i-2]

  return fibs[n]  # Return the nth Fibonacci number
