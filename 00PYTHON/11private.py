class bank:
    def __init__(self,acc_no,__acc_pass,name):
        self.acc_no=acc_no
        self.__acc_pass=__acc_pass
        self.name=name

    def showpass(self):
        print(self.__acc_pass)
b1=bank(1223,"asdf","suman")
b1.showpass()
# print(b1.__acc_pass)    #as __acc_pass is pprivate