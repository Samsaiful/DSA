num=int(input("Enter number:"))
for i in range(num):
    for j in range(i+1):
        print("*",end="")
    
    for j in range(2*num-3-i*2):
        print(" ",end="")
    
    for j in range(i+1):
        if(i+1==num and i==j):
            pass
        else:
            print("*",end="")
    print("")
for i in range(num-1):
    for j in range(num-1-i,0,-1):
        print("*",end="")
    
    for j in range(i*2+1):
        print(" ",end="")
    for j in range(num-1-i,0,-1):
        print("*",end="")
    
    
    print("")
    