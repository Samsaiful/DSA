students= {
    "name":"Suman",
    "surname":"sarkar",
    "age" : 23,
    "subjects":["c++","python","oops"],
    "is indian":True


}
# print(students)
# print(students["subjects"])
# students["is male"] = True
# print(students)
# print(students.keys)
# print(students.items())
print(students.get("age"))
students.update({"city":"cooch behar","village":"bag bhander"})
print(students.items())
