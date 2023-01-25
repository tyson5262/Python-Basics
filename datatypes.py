#numerical data types
a=10 #this is an integer value
b=10.5#this is a float
c=float(a) #this is coversion of data type from int to float
# print(c)
d=int(b) #this converting float to int
i = 1j#this is complex data type 
print(d)

#text data type
e1="this is string"
e2='this also a string'
e3=str('this a also a string')
print(e3)

#sequential data types
f=(b,2,"3",5)# this a tuple
g={1,'2',3,a}#this is a set
h=[a,b,c,d,e1,6,"7"]# this is a list
j=range(a)#this is a range from 0 to a
k=range(5,15)# this is a range from 5 to 15
print(h[4])# here we r printing index value 4 from list h

#mapping data types
l={'key':h, 'map':b}#this a dictionary were we map a value to corresponding key
print(l['map'])#over here we aRE calling the key to return the value

#boolean data type
m=True#this boolean data type sets a variable to true
n=False#this seting the variable to false
print(type(m))#this will print the bool type 
print(10>9)#returns true 
print(10<9)#returns false