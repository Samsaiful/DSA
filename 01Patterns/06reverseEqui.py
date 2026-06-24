num=int(input("Enter a number:"))
for i in range (num):
    for j in range(i):
        print(" ",end="")
    for k in range(1,num*2-2*i):
        print("*",end="")
    print("")