
a=float(input("1st Input Value = "))
b=float(input("2nd Input Value = "))
operation=(input('enter operation {+,-,*,/,**,%,//} = ')) 
if(operation=='+'):
    print('sum is=',a+b) 
elif(operation=='-'):
    print('substracted value is =', a-b)
elif(operation=='*'):
    print('multiplied value is =',a*b)
elif(operation=='/'):
    if(b==0):
        print('cannot be divided by zero')
    else:  
        print('divided value is =',a/b)
elif(operation=='%'):   
        print('modulus value=',a%b)
elif(operation=='**'):
    print('exponential value=',a**b)
elif(operation=='//'):
    print('floor divided value is =',a//b)                
else:
    print('invalid choice')        

