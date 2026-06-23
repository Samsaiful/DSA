class cars:
    country="India"   #class attribite
    def __init__(self,name,Type,owner,fuel):
        self.name=name   #obj/instance attriibutes
        self.Type=Type
        self.owner=owner
        self.fuel=fuel
    def __init__(self,name,Type,owner="Suman",fuel="petrol"):
        self.name=name
        self.Type=Type
        self.owner=owner
        self.fuel=fuel
    def print_car(self):
        print("Car Name:",self.name )
        print("Car Type",self.Type)
        print("Car Owner",self.owner)
        print("Car Fuel",self.fuel)
        print("Country",self.country)
        

bmw=cars("BMW","4-chaka","suman","ethanol")
# print(bmw.fuel,bmw.owner)
bmw.print_car()
print()
toto=cars("toto","3-chaka")
# toto.print_car()

        