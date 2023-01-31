# my_list = ["Jonathan"]
# my_list.append("Chacko")
# print(my_list)



# my_dict = {"Name":["saro"],"Address":[],"Age":[]}:
# my_dict["Name"].append("Guru")
# my_dict["Name"].append("Mumbai")
# my_dict["Age"].append(30)	
# print(my_dict)



# my_dict = {}
# key = input("Enter Key Value = ")
# Value = int(input("Enter the Value for the KEY ("+key+") :"))
# key1= "hai"
# value="hello"
# my_dict.update({key1:value})
# print(my_dict)

# f=3
# list = [f,f]
# list.append("k")
# print(list)


# def keymap(key):
#     mydict={

#     'steve': 'tyson',
#     'age'  : '34',
#      'sex': 'male'
#     }
#     if(key=='steve' or key=='age' or key=='sex'):
#       print(mydict[key])
#     else:
#         print('key not identified')
# print('keys are steve,age,sex')
# key1=input('enter the required key =')

# keymap(key1)

# def keymap(key):
#     mydict={

#     'name': 'steve tyson',
#     'age' : '34',
#      'sex': 'male',
#      'about him':[]
#     }
#     a=input('enter wat you want write about him')
#     mydict['about him'].append(a)
#     print(mydict)
#     if(key=='steve' or key=='age' or key=='sex' or key=='about him'):
#       print(mydict[key])
#     else:
#         print('key not identified')
# print('keys are steve,age,sex,about him')
# key1=input('enter the required key =')

# keymap(key1)

# def keymap(key):
#     mydict={

#     'name': 'steve tyson',
#     'age' : '34',
#      'sex': 'male',
#      'about him':'manager in import / export documentation and operations'

#     }
#     if(key=='steve' or key=='age' or key=='sex' or key=='about him'):
#       print(mydict[key])
#     else:
#         print('key not identified')
# print('keys are steve,age,sex,about him')
# key1=input('enter the required key =')

# keymap(key1)

# def cube(x):
#    r=x**3
#    return r


# # a = 330
# # b = 330

# # if a > b:
# #    print("A")
# # else:
# #  print("=")
# #  if a == b:
# #    pass 
# #  else:
# #   print("B")


# # txt = "The price is {} dollars"
# # print(txt.format('34'))


class Parent():
   def __init__(self,name,age ):
      self.attr1= name
      self.attr2 = age
      

   def display1(self,name,age):
      print("fname and age are ",name,age)

# chld=Parent('steve','34')  
# chld.display()       

class Child(Parent):
   def __init__(self, lname,name,age):
      self.attr3=lname
      super().__init__(name,age) # Parent.__init__(self, name,age)      
         
   def display(self): 
      super().display1(self.attr1,self.attr2) # Parent.display1(self, self.attr1,self.attr2)
      print("full name and age is :",self.attr1,self.attr3,"and",self.attr2)

     
s=input("enter name :")
b=input("enter age :")
c=input("enter last name :")       

obj=Child(c,s,b)
obj.display()
obj.display1("Jonathan",20)


# chld=Parent(s,b)
# chld.display()

# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   def __init__(self, fname, lname,year):
#     self.graduationyear = year
#     super().__init__(fname, lname)
#   def printname(self):
#      print(self.firstname, self.lastname,self.graduationyear)
    

# x = Student("Mike", "Olsen","2019")
# x.printname()

              
        



