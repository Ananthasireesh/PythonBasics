""" This code will introduce you Identity operators in python 
    we will learn Identity operators on diffrent datatypes """

"""There are only two identity operators IS and IS NOT which are basically 
    used to check whether a item is present sequence of data in dicts, tuple or list 
    both these operators when used with a condition will give a boolean result"""

"""IS- if two variables refer to same object then this returns True, otherwise false"""

a=5
b=5

if a is b:
    print("a is b")

"""IS Not- if two variables doesn't refer to same object then this returns True, otherwise false"""
if a is not b:
    print("a is not b")
else:
    print("a is b")
