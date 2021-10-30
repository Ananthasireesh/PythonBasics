""" In python we have Numbers of 3 types
    -> Intergers -> float Numbers and -> Complex numbers"""

"""Integers : They are positive or negitive whole numbers with no decimal point
    Integrs in py3 have unlimedted range where as py2 had two versions ints and longs,
    py3 doesnt support longs anymore """
a = 3
b = -6

""" Floating point numbers: Real Numbers with fractional decimal points"""
c = 1.06
d = 3.8909970907

""" complex numbers: are of form a + bj, Where a and b can be floats and j represents 
    Square root of -1 (imaginary number). real part is a and img part is b"""
e = (3 + 6j)
#Real Part of complex number
print('Complex Number: Real Part is = ', e.real)
#Imaginary Part of complex number
print('Complex Number: Imaginary Part is = ', e.imag)
#Conjugate of complex number
print('Complex Number: conjugate Part = ', e.conjugate())
f = 6 + 15j

#mathemetical calculations on complex numbers 
#Addition
print("Addition of two complex number =", e + f)
#Subtraction
print("Subtraction of two complex number =", e - f)
#Multiplication
print("Multiplication of two complex number =", e * f)
#Division
print("Division of two complex number =", e / f)

""" Python also supports represeting numbers in either hexadecimal or octal"""
hexa_number = 0xA0F
octal_number = 0o37

""" Number Type conversions, 
    some time you need to convert diffrent formats of numbers to other forms """

#lets type convert floating point to integer and display it
print("Integer value of c is:", int(c))
#lets type convert integer value to float and display it
print("Integer value of a is:", float(a))
#lets convert a integer and floating point to complex number 
print("Complaex value of a and c is:", complex(a,c))
#if complex function is given one number then img number would be taken as zero 
print("Complex value of b is:", complex(b))

""" Few built in functions that can be applied on numbers"""
# abs(var): The absolute value of var: the (positive) distance between var and zero.
print("Absolute value of b is:", abs(b))
# celi(var): The ceiling of var: the smallest integer not less than var.
import math #celi function should be imported from math library
print("Absolute value of c is:", math.ceil(c))
#floor(var): The floor of var: the largest integer not greater than var.
print("Absolute value of c is:", math.floor(c))
# exp(var): The exponential of var
print("exponential value of a is:", math.exp(a))
# log(var): The natural logarithm of x, for x > 0.
print("log value of a is:", math.log(a))
# log10(var): The 10th base logarithm of x, for x > 0.
print("log of 10th base value of a is:", math.log10(a))

""" max(x1, x2, x3, ....x5) returns max among the numbers input"""
print("max of a,b,c,d is:", max(a,b,c,d))
""" min(x1, x2, x3, ....x5) returns max among the numbers input"""
print("min of a,b,c,d is:", min(a,b,c,d))

#pow(x,y): returns x ** y
print("power of b to a is:", pow(a,b))

"""round(x[,n]): x rounded to n digits from the decimal point. 
 Python rounds away from zero as a tie-breaker: round(0.5) is 1.0 and round(-0.5) is -1.0."""
print("rounded value of c is:",round(c))
print("rounded value of d for 2 digits is:",round(d,2))

#sqrt(var):The square root of x for x > 0.
print("Sqrt of 25 is:",math.sqrt(25))

"""Random Number Functions
    Random numbers are used for games, simulations, testing, security, 
    and privacy applications."""
import random
#choice(seq): A random item from a list, tuple, or string.
list_a =[1,2,3,4]
print("A random number out of list_a is:", random.choice(list_a))

#randrange([start,]stop[,step]):A randomly selected element from range(start, stop, step).
"""start − Start point of the range. This would be included in the range. Default is 0

stop − Stop point of the range. This would be included in the range. Default is 1

step − Step point of the range. This would be excluded from the range.

Return Value
This method returns a random item from the given range."""

# randomly select an odd number between 1-100 
print ("randomly select an odd number between 1-100  : ", random.randrange(1, 100, 2))

# randomly select a number between 0-99 
print ("randomly select a number between 0-99  : ", random.randrange(100))

# random(): The random() method returns a random floating point number in the range [0.0, 1.0].
# First random number
print ("first random number : ", random.random())

# Second random number
print ("second random number : ", random.random())

""" seed(x): The seed() method initializes the basic random number generator.
 Call this function before calling any other random module function.
 syntax: seed ([x], [y])
 Parameters
x − This is the seed for the next random number. If omitted, then it takes system time to generate the next random number. If x is an int, it is used directly.

y − This is version number (default is 2). str, byte or byte array object gets converted in int. Version 1 used hash() of x.

"""
random.seed()
print ("random number with default seed", random.random())

random.seed(10)
print ("random number with int seed", random.random())

random.seed("hello",2)
print ("random number with string seed", random.random())

#shuffle(lst): Randomizes the items of a list in place. Returns None.
random.shuffle(list_a)
print("shuffled list of list_a:", list_a)

"""The uniform() method returns a random float r, 
such that x is less than or equal to r and r is less than y."""

print ("Random Float uniform(5, 10) : ",  random.uniform(5, 10))
print ("Random Float uniform(7, 14) : ",  random.uniform(7, 14))

#mathemaetical constants
#	pi: The mathematical constant pi.
print("value of pi is:", math.pi)

# e: The mathematical constant e.
print("value of e is:", math.e)
