import re
# def pal():
class palindrome:
    def reverse(self, a):
        b=''.join(reversed(a))
        if (a==b):
            return True
        else:
            return False
def remove(c):
    return re.sub(r'/d','', c)
print(remove("AB10BA"))


class paln(palindrome):
    def define(self):
        C = input(" enter the string to check if it is a palindrome =")
        # d = palindrome.remove(self, C)
        # print(d)
        

obj1=paln()
obj1.define()
# print(obj1.method1())

# if((obj1.method1(obj1.a)==True)):
#         print ("its a palindrome ")
# else:
#         print(" not a palindrome")
    

         
#this below program is for refefrence only how to reverse a string without direct inbuilt function

# def reverse(s):
#     str = ""
#     for i in s:
#         str = i + str
#     return str
 
# s = "steve"
 
# print("The original string is : ", end="")
# print(s)
 
# print("The reversed string(using loops) is : ", end="")
# print(reverse(s))

# def exp(a):
#     b="" 
#     for i in a:
       
#         print(i)
#         b=b+i
#         print(" value of b-"+ b)
#     return b

# a=input("input=")

# print(exp(a))
