# limit = int(input("Enter the limit : "))
# for i in range (limit):
#     for j in range (i):
#         print("*",end = " ")
#     print()

# limit = int(input("Enter the limit : "))
# for i in range (limit,0,-1):
#     for j in range (i):
#         print("*",end = " ")
#     print()


     

limit = int(input("Enter the limit : "))
k = limit

for i in range (limit):            #for row
    for space in range(k):         #for space
            print(end = " ")
    k= k-1  
    for j in range (i):            #for row
        print("*",end = " ")
    print()