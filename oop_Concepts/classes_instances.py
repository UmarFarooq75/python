class Item:
    discount_item=0.8 #20% discount of instance
    all_instances=[]
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        #Actions to excute
        Item.all_instances.append(self)
    

    def calculate_total_price(self):
        return self.price * self.quantity
    def calculate_total_discount(self):
        self.price=self.price*self.discount_item
    def __repr__(self) -> str:
        return f"Item('{self.name}','{self.price}','{self.quantity}')"


item1 = Item("Phone", 10002, 1)
item2 = Item("Laptop", 1000, 1)
item3 = Item("Tablet", 4000, 1)
item4 = Item("PC", 6000, 1)
item5 = Item("Graphic Card", 5500, 1)
item6 = Item("Ram", 7700, 1)

# print(item1.calculate_total_price())
# print(item2.calculate_total_price())

#setting 50% discount
item2.discount_item=0.5

item2.calculate_total_discount()
# print(item2.calculate_total_price())

#showing instances data as string
templist=Item.all_instances #lets change the view how we need to recieved using __repr__
item7=Item("IPhone", 50002, 1)
templist.append(item7)
# print(templist)

print(Item.all_instances)

#showing how many instances created

for instance in Item.all_instances:
    print(instance.name)