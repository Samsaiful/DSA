#First pattern

def ster (n) :
    for i in range (n):
        for j in range (n):
            print("*  ",end="")
        print("\n")

n=int(input("Enter the number of sters: "))

ster(n)


  