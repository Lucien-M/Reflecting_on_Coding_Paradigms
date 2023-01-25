# Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.

def flatten_and_sort(array):

  a = []

  for b in array:

    for c in b:

      a.append(c)

  return sorted(a)

'''
Answer the following questions.

How does this solution ensure data immutability?

#This solution ensures data immutability: The input array is not modified. It creates a newarray to keep the elements flattened and sorted. 

Is this solution a pure function? Why or why not?

#This solution is a pure function: does not produce or rely on side effects and its output purely depends on its input (will always return the #same output for the same input).

Is this solution a higher order function? Why or why not?

#This solution is not a higher-order function: it does not take a function as an argument or return a function as output

Would it have been easier to solve this problem using a different programming style?

#It may have been easier to solve this problem using a different programming style, such as a more imperative approach.


Why in particular is functional programming a helpful paradigm when solving this problem?

# Functional programming can be a helpful paradigm  in solving this problem: it highlights immutability, with that code can be predictable and bugs avoided. Also, the use of built-in functions is motivated byfunctional programming to have an efficient and easy to read function.

'''