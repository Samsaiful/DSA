num=int(input("Enter a number:"))
for i  in range (num):
    ch=ord('A')
    for j in range(1,num-i):
        print(" ",end="")

    for j in range(i+1):
        print(chr(ch),end="")
        ch+=1
    ch-=2
    for j in range(i,0,-1):
        print(chr(ch),end="")
        ch-=1
    print("")


