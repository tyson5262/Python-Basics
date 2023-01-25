'''
try:
    x="Try tus Block of code"
except:
    y="if there is an error in the above code this executes"
else:
    a="this Runs if execpt doesnt run"
finally:
    b="this code block will execute in all cases in the end after the previous codes"
'''
# x = 5
# try:
#     print(x)
# except:
#     print(10)

#make a calculator with two variable dividing

a=10
b=6



try:
    div=a/b
except:
    div = 'cant be divded by 0'
finally:
    print(div)   


# specific error catching
try:
    if True:
        print(10/0)
except NameError:
    print("Variable x is not defined" + NameError)
except ZeroDivisionError:
    print("Something else went wrong", ZeroDivisionError)
except:
    print("Other")    