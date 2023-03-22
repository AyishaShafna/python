mrks = [100,200,800,400,500]
length = len(mrks)
for i in range(length):
    for j in range(length):
        if mrks[i]<= mrks[j]:
            mrks[i] = mrks[j]
print("the largest number is :",mrks[i])
print("smallest")

for x in mrks:
    for y in mrks:
        if x>=y:
            x = y

print("smallest number is : ",x)

cost = [22.5,33.3,33.05,33.005]
frst = cost[0]
for k in cost:
    if frst <= k:
        frst = k
print("lrgst",frst)

element1 = cost[0]
for n in cost:
    if element1 >= n:
        element1 = n
print("smallest",element1)
