grade = 0
total = 0
i=0

grade = int(input("Enter the grades:"))
             
             
while (grade != -1):
            total = total + grade
            i += 1
            grade = int(input("If you want to continue enter the grade, otherwise click -1"))


if grade > 0:
   print("Ther average of the grades is:", total/i)
else:
   print("Ther average of the grades is:", 0.0)

    