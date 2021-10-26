""" This code will introduce you basic logical operations in python 
    we will learn logical operations on diffrent conditional statements """

"""Basic logical operators are logical AND(&),logical OR(|), logical NOT(!)(unary operator), these operators are 
    always used in compound conditions"""

#This code should be learnt after learning conditional operators

a= 10
b=5 
c=3 

if (a>b) & (b>c):
    print("a is greater than b and b is greater than c")

#this condition will excecute even if one of the condition is true
if (a>b) | (b<c):
    print("a is greater than b or b is less than c")

#logical Not is basically used to test the boolean variables in condition 
d=False
if not d: #this condition will excecute true since d is false and we used not operator before it
    print("d is false")