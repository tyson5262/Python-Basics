class calculator:
    def input(self):
        self.num1=int(input('first no.'))
        self.num2=int(input('second no.'))
    def add(self):
        return self.num1+self.num2
    def sub(self):
        return self.num1-self.num2        
    def mul(self):
        return self.num1*self.num2
    def div(self):
        try:
            val = self.num1/self.num2
        except:
            val = "Division by Zero Not Allowed."
        finally:
            return val 
    def QuestionPrint(self):
        print('\n')
        print("1: add")
        print('2:sub')
        print('3:mul')
        print('4:div')
        print('5:exit')
        print('\n')
    def FinalCalc(self, OP):
        print('\n')
        if(OP==1):
            print('the sum is :', self.add())
        elif(OP==2):
            print('the sub is : ', self.sub()) 
        elif(OP==3):
            print('the mult value is :',self.mul()) 
        elif(OP==4):
            print('the div value is :',self.div())
    
class main(calculator):
    def define(self):
        while True:
            # cal = calculator()
            calculator.QuestionPrint(self)
            ## super().QuestionPrint()
            # cal.QuestionPrint()
            try:
                op=int(input('select operation:' ))
                if op in (1,2,3,4,5):
                    if(op==5):
                        break
                    calculator.input(self)
                    ## super().input()
                    # cal.input()
                else:
                    print('invalid input')
            except:
                print('invalid choice')
                continue
            calculator.FinalCalc(self, op)
            ## super().FinalCalc(op)
            # cal.FinalCalc(op)

M = main()
# c=calculator()
# M.QuestionPrint()
M.define()