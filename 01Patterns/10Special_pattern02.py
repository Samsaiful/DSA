num=int(input("Enter a number:"))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end="")
    for k in range(2*(num-i)):
        print(" ",end="")
    for l in range(i,0,-1):
        print(l,end="")
    print("")

#     Enter a number:4
# 1      1
# 12    21
# 123  321
# 12344321
    