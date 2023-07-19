s=str(input("Enter the strings: "))
i=s.split(",") or s.split(".")
t=[s.split(" ") for s in i]
l=max(t,key=len)
li=len(l)
print ("The longest sentence has",li,"words")
print ("The longest sentence is", " ".join(l))

