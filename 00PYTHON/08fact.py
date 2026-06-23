def factorial(num):
    if num==1 or num==0:
        return 1
    else:
        return num*factorial(num-1)

num=int(input("Enter a number to find factorial:"))
print("factorial of ",num," is ",factorial(num))


# num=int(input("Enter a number to find factorial:"))
# fact=1
# for i in range(1,num+1):
#     fact*=i
# print("factorial of ",num," is ",fact)

# def average(a,b):
#     return (a+b)/2

# print(average(average(8,8),9))