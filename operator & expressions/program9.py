age=int(input("Enter your age: "))
m=int(input("Enter your marks: "))
if(age>=18 and m>=40):
    print("You are Eligible for the Exam")
elif(age>=18 or m>=40):
    print("You Meet one of the criteria for the Exam")
else:
    print("You are Not Eligible for the Exam")  