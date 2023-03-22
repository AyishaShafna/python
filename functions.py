# def odd_even(x):
#     if x % 2 == 0:
#         print("number is even")
#     else:
#         print("number is odd")
# odd_even(1)

a = 10
def number():
    global a
    a += 10
    global b
    b = 10
    print(a)
    print(b)
number()    
print("call  outside the function",a)
print("call  outside the function",b)
