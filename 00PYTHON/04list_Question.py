values=[1,"abc",2,"abc",1]
# values1=values.copy()
# values1.reverse()
# if(values==values1):
#     print("it is palindrome")
# else:
#     print("not palindrome")

count=len(values)
pal=True
for i in range (count):
    if(values[i]!=values[count-1-i]):
        pal=False
        break
    else:
        pal=True


if(pal):
# if(values==values[::-1]):
    print("palindrome")
else:
    print("not palindrome")