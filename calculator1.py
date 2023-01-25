
# def add(a,b):
#     sum =a+b
#     print('the sum is =',sum)

# def sub(a,b):
#     sub =a-b
#     print('the substracted value is =',sub)

# def mul(a,b):
#     mul =a*b
#     print('the multiplied value is =',mul)

# def div(a,b):
#     if(b==0):
#         print('not dvisible by 0')
#     else:
#         div=a/b
#         print('the divided value is =',div)

# def expon(a,b):
#     exp =a**b
#     print('the exp is =',exp)

# def mod(a,b):
#     mod =a//b
#     print('the ,mod is =',mod)
    

# a1=float(input("1st Input Value = "))
# b1=float(input("2nd Input Value = "))
# operation=(input('enter operation (sum,sub,mul,div,exp,mod) = '))
# if(operation=='sum'):
#    add(a1,b1)
# elif(operation=='sub'):
#     sub(a1,b1)
# elif(operation=='mul'):
#     mul(a1,b1)

# elif(operation=='div'):
#     div(a1,b1)
# elif(operation=='exp'):
#     expon(a1,b1)
# elif(operation=='mod'):
#     mod(a1,b1)             
   
# else:
#     print('operation is invalid')

#=====================================================================================================================
while True:
  def cal(a,b):
    if(operation=='sum'):
      add=a+b
      print('the sum is',add)

    elif(operation=='sub'):
      sub=a-b
      print('the sub is',sub)

    elif(operation=='mul'):
      mul=a*b
      print('the mul is',mul)

    elif(operation=='div'):
      try:
        div=a/b
      except:
        div = 'not dvisible by 0'
      finally:
        print(div) 

    elif(operation=='exp'):
      exp=a*b
      print('the exp is',exp)

    elif(operation=='mod'):
      mod=a//b
      print('the mod is',mod)

    else:
      print('operation is invalid')

  a1=float(input("1st Input Value = "))
  b1=float(input("2nd Input Value = "))
  operation=(input('enter operation (sum,sub,mul,div,exp,mod) = '))    
  cal(a1,b1)
