# class calculator:
#     def __init__(self,a,b):
#         self.num1 = a
#         self.num2 = b
        
#     def add(self):
#         return self.num1+self.num2

#     def sub(self):
#         return self.num1-self.num2     
    
#     def mul(self):
#         return self.num1*self.num2

#     def div(self):
#         try:
#             val = self.num1/self.num2
#         except:
#             val = "Division by Zero Not Allowed."
#         finally:
#             return val 

# def QuestionPrint():
#     print('\n')
#     print("1: add")
#     print('2:sub')
#     print('3:mul')
#     print('4:div')
#     print('5:exit')
#     print('\n')

# def FinalCalc(OP, CAL):
#     print('\n')
#     if(OP==1):
#         print('the sum is :', CAL.add())
#     elif(OP==2):
#         print('the sub is : ', CAL.sub()) 
#     elif(OP==3):
#         print('the mult value is :',CAL.mul()) 
#     elif(OP==4):
#         print('the div value is :',CAL.div())

# def Main():
#     while True:
#         QuestionPrint()
#         try:
#             op=int(input('select operation:' ))
#             if op in (1,2,3,4,5):
#                 if(op==5):
#                     break
#                 a=int(input('first no.'))
#                 b=int(input('second no.'))
#                 cal=calculator(a,b)
#             else:
#                 print('invalid input')
#         except:
#             print('invalid choice')
#             continue
#         FinalCalc(op, cal)

# class main:
#     Main()