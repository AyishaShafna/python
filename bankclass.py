class Bank:
    user_count = 0

    def __init__(self,name,address,mobile,email,acc_num):
        self.name = name
        self.address = address
        self.mobile = mobile
        self.email = email
        self.acc_num = acc_num
        Bank.user_count = Bank.user_count + 1
    
    def display_accountdetails(self):
        print("Account holder name : ",self.name)
        print("Account holder addres : ",self.address)
        print("Account holder Mobile Number : ",self.mobile)
        print("Account holder Email Id : ",self.email)
        print("Account Number : ",self.acc_num)

    def number_of_users(self):
        print("Total number of users : ",Bank.user_count)


user1 = Bank("Shafna","jduwehjshfghf",7896541230,"bcdefgh@gmail.com",334532342422)
user2 = Bank("shana","calicut",7777894525,"shan@gmail.com",101010102)
user3 = Bank("Irshad","Kannur",8888958741,"irshad@gmail.com",2020202020)

user1.display_accountdetails()
user2.display_accountdetails()
user3.number_of_users()
