class Item:
    pay_rate = 0.8 #payrate after 20% discount
    all = []
    def __init__(self, name: str, price:float, quantity=0):
        #Run validations on recived arguments
        assert price >= 0, f"Price {price} is not greater than or equal to Zero"
        assert quantity >= 0, f"quantity {quantity} is not greater than or equal to Zero"
        #assign to slef object
        self.name = name
        self.price = price
        self.quantity = quantity 
        # actions to excecute 
        Item.all.append(self) # appends the instances will be appended to the 'all' list
    def cal_total_price(self):
        return self.price * self.quantity
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    #__repr__ method will help us to print whatever declared inside this method instead of object name
    def __repr__(self):
        return f"Item('{self.name}','{self.price}','{self.quantity}')"

#item1 = Item("Iphone", 100, 10) # instance of class 
#item2 = Item("laptop", 1000, 3 )




""" By above code we see that item now has a class of Item """

#print(item1.cal_total_price())
#print(item2.cal_total_price())

#print(Item.pay_rate) # we can access class attributes from class directly 
#print(item1.pay_rate) #we can also access class variables directly from class instances 

"""__dict__: magic attribute that will help us to access all the attributes 
related to an class or class instance. """
#print(Item.__dict__) # All attributes for class level 
#print(item1.__dict__) # all attributes for instance level 


"""#print discounted amount
item1.apply_discount()
print(item1.price)

Class attributes can be overwritten by instances, when we use the class attribute with the instance name and give it a new value, 
now instance will not search for class attribute on class level.

item2.pay_rate=0.7 
item2.apply_discount()
print(item2.price) """


item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)



print(Item.all)
