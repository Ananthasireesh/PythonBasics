"""#Empty class
class Item:
    pass
"""

class Item:
    def cal_total_price(self, x, y):
        return x*y

item1 = Item() # instance of class 
item2 = Item()
#assign attributes to class instance 
item1.name="IPhone"
item1.qunatity= 10 
item1.price= 100
print(item1.cal_total_price(item1.qunatity,item1.price))
#assign new attributes
item2.name="laptop"
item2.qunatity= 3 
item2.price= 1000
# see the item
print(type(item1))
print(item1.cal_total_price(item2.qunatity,item2.price))

""" By above code we see that item now has a class of Item """

#how to create methods.
