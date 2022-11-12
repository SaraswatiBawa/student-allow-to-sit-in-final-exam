studentname=str(input("Enter the student name: ")) 
classheld=int(input("Enter the classheld: "))
classattend=int(input("Enter the classattend: "))

per=classattend*(classheld/100)
print("Total percentage of this student:",per)
   
if(per<75):
    print("You cannot be sit in final exam")
else:
    (print("You can be sit in final exam"))