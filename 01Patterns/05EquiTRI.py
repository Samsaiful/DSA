# num=int(input("Enter a number:"))
# for i in range(1,num+1):
#     print("  "*(num-i)+"* "*(i*2-1))
num=int(input("Enter a number:"))
for i in range(1,num+1):
    for j in range(num,i,-1):
        print(" ",end="")
    for k in range(1,i*2):
        print("*",end="")
    print("")