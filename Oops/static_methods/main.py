import csv
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
    """Class methods: Class methods can be only accessed from class item, but not instance. 

        Decorators in python is just a quick way to change the behaviour of functions
        we write by basically calling them before the function that we create. 

        Class methods should be always passed with a parameter called “cls” like self which says class itself is attribute of this function."""

    @classmethod
    def intiate_from_csv(cls):
        with open('items.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
            for item in items:
                Item(
                    name = item.get('name'),
                    price = float(item.get('price')),
                    quantity = int(item.get('quantity'))
                )
    @staticmethod
    def is_integer(num):
        # we will count out floats that are point 0 
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False


    #__repr__ method will help us to print whatever declared inside this method instead of object name
    def __repr__(self):
        return f"Item('{self.name}','{self.price}','{self.quantity}')"

Item.intiate_from_csv()
print(Item.all)
