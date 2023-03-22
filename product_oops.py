# class Product:
#     count = 0
#     def __init__(self,name,category,price):
#         self.name = name                    #instance variable
#         self.category = category
#         self.price = price
#         Product.count = Product.count + 1

#     def display_product(self):
#         print("name:",self.name)
#         print("category :",self.category)
#         print("price:",self.price)

#     def product_count(self):
#         print("Total number of products: %d",%Product.count)

class Books:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price

    def display_bkdetails(self):
        print("Book name is:",self.title)
        print("Written by:",self.author)
        print("Price is :",self.price)
        # print(self.title,"is written by ",self.author," priced ",self.price)     // to print in single line 


# Objects
book1 = Books("The Kite Runner","Khalid Hussain",399)
book1.display_bkdetails()

book2 = Books("Born A Crime", "Trevor Noah" , 499)
book2.display_bkdetails()