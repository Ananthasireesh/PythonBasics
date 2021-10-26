""" This code will introduce you mermbership operators in python 
    we will learn membership operators on diffrent datatypes """

"""There are only two membership operators IN and NOT IN which are basically 
    used to check whether a item is present sequence of data in dicts, tuple or list 
    both these operators when used with a condition will give a boolean result"""

a="hi"
b=["hi","how","are","you"]

if a in b:
    print("Hi is present b")

c="Hey"
if c not in b:
    print("Hey is not present in b")