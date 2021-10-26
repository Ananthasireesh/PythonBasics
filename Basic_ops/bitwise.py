""" This code will introduce you bitwise operators in python 
    Bitwise operators are used to compare binary variables """

""" There are operators like OR, AND , XOR , complement, left shift and 
    right shift operators"""

""" Bitwise AND operator: Returns 1 if both the bits are 1 else 0.
Example: 
a = 10 = 1010 (Binary)
b = 4 =  0100 (Binary)

a & b = 1010
         &
        0100
      = 0000
      = 0 (Decimal)
Bitwise or operator: Returns 1 if either of the bit is 1 else 0.
Example:

a = 10 = 1010 (Binary)
b = 4 =  0100 (Binary)

a | b = 1010
         |
        0100
      = 1110
      = 14 (Decimal)
Bitwise not operator: Returns one’s complement of the number.
Example:

a = 10 = 1010 (Binary)

~a = ~1010
   = -(1010 + 1)
   = -(1011)
   = -11 (Decimal)
Bitwise xor operator: Returns 1 if one of the bits is 1 and the other is 0 else returns false.
Example:

a = 10 = 1010 (Binary)
b = 4 =  0100 (Binary)

a & b = 1010
         ^
        0100
      = 1110
      = 14 (Decimal)

"""

a = 10
b = 4
 
# Print bitwise AND operation   
print("a & b =", a & b)
 
# Print bitwise OR operation
print("a | b =", a | b)
 
# Print bitwise NOT operation
print("~a =", ~a)
 
# print bitwise XOR operation
print("a ^ b =", a ^ b)

"""Shift Operators
These operators are used to shift the bits of a number left or right thereby multiplying or dividing the number by two respectively. They can be used when we have to multiply or divide a number by two. 
Bitwise right shift: Shifts the bits of the number to the right and fills 0 on voids left( fills 1 in the case of a negative number) as a result. Similar effect as of dividing the number with some power of two.
Example: 

Example 1:
a = 10 = 0000 1010 (Binary)
a >> 1 = 0000 0101 = 5

Example 2:
a = -10 = 1111 0110 (Binary)
a >> 1 = 1111 1011 = -5 
Bitwise left shift: Shifts the bits of the number to the left and fills 0 on voids right as a result. Similar effect as of multiplying the number with some power of two.
Example: 

Example 1:
a = 5 = 0000 0101 (Binary)
a << 1 = 0000 1010 = 10
a << 2 = 0001 0100 = 20 

Example 2:
b = -10 = 1111 0110 (Binary)
b << 1 = 1110 1100 = -20
b << 2 = 1101 1000 = -40 """

