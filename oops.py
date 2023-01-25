class ClassName_Person:
    def __init__(self, parameterName,parameterAge ):
        self.attributeName = parameterName
        self.attributeAge = parameterAge
    # def FunctionName(sendData, parameterName, parameterAge): #self == sendData
    #     sendData.attributeName = parameterName
    #     sendData.attributeAge = parameterAge
    def printing(self):
        print(self.attributeName)
        print(self.attributeAge)

# class ClassName_Persons():
#     attributeName:str
#     attributeAge:int
# obj2 = ClassName_Persons()
# obj2.attributeName = "Jonathan"
# obj2.attributeAge = 20
# print(obj2.attributeAge)

obj1=ClassName_Person("Steve",'tyson','will','comeout','out ',)
# obj1.FunctionName("Steve",35)
obj1.printing()