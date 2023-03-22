try:
    f = open('sample.txt','a') #'r' read ony file, 'a' read and write file
    # b = f.read()
    # print (b)

    c = f.write('writing')
except FileNotFoundError:
    print('File Not Found')
except IOError :
    print('Read only file, writg not possible')
