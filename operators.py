#ARTHMATIC operators
#mathmatical calculation
print(10+2)#this addition 
print(10-2)#this is substarction
print(10*2)#this is multiplication
print (10/2)#this division
print(10%2)#this returns reminder
print(10**2)# this 10 to the power 2(expotential)
print(15//2)#this is floor division(cnverts to the nearest integer) AKA print(int(15/2))

#assignment operators
#assigning values to variables
x=5#we r assignin value 5 to variable x
x+=3# we r incrementing the value of x with 3 AKA x = x+3
x-=4# v r decrementing the value of x with 4 AKA x = x-4
x*=5# v r multiplying the current value of x with 5 AKA x= x*5
x/=20# v r dividing the current value of x with 20 AKA x= x/20
print(x)

# comparison operators
# use to compare
y = 20
if(x==y):
    print(x,"==",y)
elif(x>y):
    print(x,">",y)
elif(x<y):
    print(x,"<",y)
    if(x>=y):
        print(x,">=",y)
    elif(x<=y):
        print(x,"<=",y)
if(x!=y):
    print(x,"!=",y)

# logical operators

z=10
if(x<z and y<z):
    print("and")
else:
    print("and not met")
if(x<z or y<z):
    print("or")
else:
    print("or not met")
if(not(x<z and y>z)):
    print("met")
else:
    print("not")

#identity operators 
x=['apple','banana']
y=['apple','banana']
z=x
if(x is z):
    print('returns true because z is the same object as x')
elif(x is not z):
    print('returns false because z is the same object as x')
if(x is y):
    print('this returns false because x is not the same object as y eventhough they have the same content')
elif(x is not y):
    print('returns true because x is not the same object as y even though they have the same content ')
if(x==y):
    print('x has the same content as y')
elif(x!=y):
    print('this would print if x didnot have the same content as y')   

#membership operators

a=['apple','banana']
b = 'banana'
c='grapes'
print(b in a)
print(c in a)
print(b not in a)
print(c not in a)

