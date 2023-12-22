
import csv

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
    
    @classmethod
    def iniate_instances_from_csv(cls):
        with open("item.csv","r") as f:
            reader=csv.DictReader(f)
            data=list(reader)
        for item in data :
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    def __repr__(self) -> str:
        return f"Item('{self.name}','{self.price}','{self.quantity}')"


if __name__ == "__main__":
    Item.iniate_instances_from_csv()
    print(Item.all_instances)