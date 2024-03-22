list1=[1,2,3,4,5,6]
list2=[5,6,7,8,9]
for item in list1:
    if item in list2:
        print(item,"common element")
for item in list1:
    if item not in list2:
        print(item,"are non common element")
        print(list2[item],"non common")
        
