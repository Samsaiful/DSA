num=int(input("Enter number:"))
for i in range(1,num+1):
    for j in range(num,i,-1):
        print(" ",end="")
    for k in range(1,i*2):
        print("*",end="")
    print("")
for i in range (1,num):
    for j in range(i):
        print(" ",end="")
    for k in range(1,num*2-2*i):
        print("*",end="")
    print("")

#     Enter number:7
#       *
#      ***
#     *****
#    *******
#   *********
#  ***********
# *************
#  ***********
#   *********
#    *******
#     *****
#      ***
#       *