# Functinal_Solution

# Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.

def flatten_and_sort(array):

  newArray = []

  for subArray in array:

    for x in subArray:

      newArray.append(x)

  return sorted(newArray)

'''
Answer the following questions.

How does this solution ensure data immutability?

#This solution ensures data immutability: The input array is not modified. It creates a new array to keep the elements flattened and sorted. 

Is this solution a pure function? Why or why not?

#This solution is a pure function: does not produce or rely on side effects and its output purely depends on its input (will always return the #same output for the same input).

Is this solution a higher order function? Why or why not?

#This solution is not a higher-order function: it does not take a function as an argument or return a function as output

Would it have been easier to solve this problem using a different programming style?

#It may have been easier to solve this problem using a different programming style, such as a more imperative approach.


Why in particular is functional programming a helpful paradigm when solving this problem?

# Functional programming can be a helpful paradigm  in solving this problem: it highlights immutability, with that code can be predictable and bugs avoided. Also, the use of built-in functions is motivated byfunctional programming to have an efficient and easy to read function.

'''
# OOP_Solution

#Watto needs a new system for organizing his inventory of podracers. 
# Help him do this by implementing an Object Oriented solution according to the following criteria.

# First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes
class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

# Define a repair() method that will update the condition of the podracer to "repaired".
    def repair(self):
        self.condition = "repaired"

# Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.
class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__( max_speed, condition, price)
    
    def boost(self):
        self.max_speed *= 2

# Define another class that inherits Podracer and call this one SebulbasPod. This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".

class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(self,max_speed, condition, price)

        def flame_jet(self, other):
            other.condition = "trashed"

# Answer the following questions:

#How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
#The attributes of the podracer (max_speed, #condition, price) were defined within the Podracer class and made private with the self. notation. This solution demonstrates encapsulation.Another encapsulation was demonstrated with the repair() method. It modified the private condition attribute.

# There are two new classes AnakinsPod and SebulbasPod created that inherit the attributes and methods of the Podracer class. The solution demonstrates Inheritance.

#It does not demonstrate Abstraction and Polymorphism.

#Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?

#It could have been easier to implement a solution using a different coding style: The functional programming is the one . 
# OOP allows the organization of complex data structures and methods into classes and objects. With that the code can be more readable, maintainable and reusable. This is the main advantage of OOP.
#  In particular, the inheritance feature of OOP allows the creation of new classes that share properties and methods with other classes.

