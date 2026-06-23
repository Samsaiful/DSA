# count=int(input("enter a number:"))
# i=1
# while i<=count:
#     print(i)
#     i+=1

number=(1,4,9,16,25,36,49,64,81,100)
num=int(input("enter the number to search:"))
i=0
count=True
while(i<len(number)):
    if num==number[i]:
        print(num,"found in index ",i)
        count=False
        break
    else:
        count=True
        i+=1
if count :
    print(num ,"not found")
