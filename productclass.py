class Products:
    count = 0

    def __init__(self,name,category,price):
        self.name = name
        self.category = category
        self.__price = price
        Products.count = Products.count + 1
    
    def display_accountdetails(self):
        print("Product Name : ",self.name)
        print("Product Category : ",self.category)
        print("Price of the product : ",self.price)
# ----------------to set and get the private variable--------------
    def set_price(self,price):
        self.__price=price

    def get_price(self):
        return self.__price
      
product1 = Products("mobile","electronics",10000)

# print(product1.name)
# print(product1.__price) /////results error because it is a private variable
# print(product1._Product__price)  ///// to get the private variable

   
# print(product1._Products__price)

# product1.__price=20
# print(product1.__price)


product1.set_price(50000)
print(product1.get_price())

print(product1._Products__price)