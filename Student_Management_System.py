Students = []
while True:
    print("======= Student Management System =======")
    print("1. Add Student")
    print("2. Show Student Details")
    print("3. Exit")
    Choice = int(input("Enter your Choice:"))
    if Choice == 1:
        Name = input("Enter Student Name: ")
        Students.append(Name)
        Roll_no = int(input("Enter your Roll_no:"))
        Students.append(Roll_no)
        English = int(input("Enter English Marks: "))
        Maths = int(input("Enter Maths Marks: "))
        Physics = int(input("Enter Physics Marks: "))
        Chemistry = int(input("Enter Chemistry Marks: "))
        Computer = int(input("Enter Computer Marks: "))
        Total_Marks = English + Maths + Physics + Chemistry + Computer
        Percentage = (Total_Marks / 500) * 100
        if Percentage >= 90:
            Grade = "A+"
        elif Percentage > 80:
            Grade = "A"    
        elif Percentage > 70:
            Grade = "B+"
        elif Percentage > 60:
            Grade = "B"
        elif Percentage > 50:
            Grade = "C" 
        else:
            Grade = "FAIL!!"
        print("Student Added Successfully!")
    elif Choice == 2:    
        print("========= Student Details =========")
        print("Name :", Name)
        print("Roll No :", Roll_no)
        print("Total Marks :", Total_Marks)
        print("Percentage :", Percentage, "%")
        print("Grade :", Grade)
    elif Choice == 3:
         print("🙏 Thank you for using the Student Management System!")
         print("👋 Have a Nice Day!")
         break
    else:
        print("Invalid Choice")     
   