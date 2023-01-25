# my_dict = {"Name":["saro"],"Address":[],"Age":[]}
# my_dict["Name"].append("Guru")
# my_dict["Name"].append("Mumbai")
# my_dict["Age"].append(30)	
# print(my_dict)
# mylist=["d",'f','g','h','t']
# mylist.append('jhgjhghg')
# print(mylist)


def get_mapped_value(key):
    my_dict = {
        "key1": 5,
        "key2": 4,
        "key3": "value3"
    }
    return my_dict.get(key) #my_dict[key]

kept1 = get_mapped_value("key1") # Output: "value1"
kept2 = get_mapped_value("key2")
sum = kept1 + kept2
print(sum)


#updating empty dictionary
thisdict = {}
a=input("enter the key")
b=input('enter the value for the key')
thisdict.update({a:b})
print(thisdict)

#updating empty dictionary infinite times
thisdict = {}
while True:
    a=input("enter the key")
    b=input('enter the value for the key')
    thisdict.update({a:b})
    print(thisdict)

#try     