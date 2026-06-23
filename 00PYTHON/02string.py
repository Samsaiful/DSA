str1="suman"
str2="sarkar"
str3=str1+" "+str2
print(str1,str2)
print(str3)
print(len(str3))
# str3[6]='S'   not possible
print(str3[6])
print(str3[1:5])
print(str3[-5:-1])
# for i in range (len(str3)):
#     print(i+1,str3[i])

print(str3.capitalize())
print(str3.endswith("kar"))
print(str3.replace('s','A'))