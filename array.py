array1 = [10,20,60,70,80,100]      #to swap first and last element of the array1

length = len(array1)
temp = array1[0]
array1[0] = array1[length-1]
array1[length-1] = temp
for i in array1:
    print(i)

b = 10
c = 50
a,b = 5,65
print(a,b)    #to swap simply in python

marks = array1.copy() #to copy an array
print(marks)

array1.append(60)
print(array1)

b = [200,800,5000]
array1.extend(b)
print(array1)

array1.insert(0,1000)
print(array1)

indx = array1.index(100)
print(indx)

array1.reverse()
print(array1)

array1.sort()
print(array1)

txt = 'welcome to baabtra'
x = txt.replace('baabtra','world')
print(txt)
print(x)

y = txt.split()
print(y)