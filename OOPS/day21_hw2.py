class Product:

    def __init__(self, name, price):
        self.name = name
        self.__price = price   

    def price(self):
        return self.__price

    def selling(self, selling_price):

        print(f"product name: {self.name}")
        print(f"cost price: ₹{self.__price}")
        print(f"selling price: ₹{selling_price}")

        if selling_price > self.__price:
            profit = selling_price - self.__price
            print(f"profit: ₹{profit}")

        elif selling_price < self.__price:
            loss = self.__price - selling_price
            print(f"loss: ₹{loss}")

        else:
            print("no profit no loss")


p1 = Product("laptop", 50000)
p1.selling(60000)
p1.selling(45000)