num=int(input("Enter a number:"))
for i in range(num):
    for j in range(i+1):
        print("*",end="")
    print("")
for i in range(1,num):
    for j in range(num-i):
        print("*",end="")
    print("")

#     Enter a number:6
# *
# **
# ***
# ****
# *****
# ******
# *****
# ****
# ***
# **
# *
