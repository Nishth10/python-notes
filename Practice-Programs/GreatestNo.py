n1=int(input("Enter the 1st no:"))
n2=int(input("Enter the 2nd no:"))
n3=int(input("Enter the 3rd no"))
if(n1>n2 and n1>n3):
    print(n1,"is the greatest no")
elif(n2>n1 and n2>n3):
    print(n2,"is the greatest no")
elif(n3>n1 and n3>n1):
    print(n3,"is the greatest no")
else:
    print( n1, n2,n3,"are equal")