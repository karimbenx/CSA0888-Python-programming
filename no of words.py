a = "Geeksforgeeks is best Computer Science Portal, and it is used for making many things "

print("The original string is : " + a)
 
x= (a.split(", "))
print (x)
res=list(x.split())
 
# printing result
print("The number of words in string are : " + str(res))
