def AddStudent():
    rollno = input("Enter Student Roll-no: ")
    name = input("Enter Student name: ")
    grade = input("Enter grade: ")

    with open("student.txt","a") as file:
        file.write(f"{rollno} | {name} | {grade}\n")
print("Student is successfully saved!")

def viewStudent():
    try:
        with open("student.txt","r") as file:
            students = file.readlines()

        if not students:
            print("There is no students to display!");
            return
    except FileNotFoundError:
        print("There is no file to display!")

    print("Roll number | Student Name | Grade")
    print("_" * 30)
    for student in students:
        print(student.strip())
#Search a Student
def searchStudent():
    try:
        rollno = input("Enter the roll no to search: ")
        found = False

        with open("student.txt","r") as file:
            for line in file:
                if line.startswith(rollno):
                    print("Student found: ", line.strip())
                    found = True
                    break

        if not found:
            print("There is no student with this rollno! try another one")
    except FileNotFoundError:
        print("This is no data in the file!")
#################deleteand updae record
def delete_or_update():
    rollno = input("Enter roll no to update or delete: ")
    find = False
    students = []
    with open("student.txt", "r") as file:
        students = file.readlines()
    with open("student.txt","w") as file:    
        for line in students:
            if line.startswith(rollno):
                found = True
                choice = input("Do you want to update (u) or delete (d): ").lower()
                if choice == 'u':
                    new_name = input("Enter new Name: ")
                    new_grade = input("Enter new grade: ")
                    file.write(f"{rollno} | {new_name} {new_grade} \n")
                    print("Student is update!")
                elif choice == 'd':
                    print("Student is deleted:")
            continue
        file.write(line)
   # if not find:
   #     print("Student with this rollno does not exist!")

def main():
    while True:
        print("\n--- Student Management System---")
        print("1. Add Student\n")
        print("2. View Student\n")
        print("3. Search a Student\n")
        print("4. Update or Delete Student\n")
        print("5. Exit")
        choice = input("Enter the choice from 1-5: ")
        if choice=='1':
            AddStudent()
        elif choice=='2':
            viewStudent();
        elif choice=='3':
            searchStudent()
        elif choice=='4':
           delete_or_update()
        elif choice=='5':
            print("Extiing Student Management System. goodbye")
            break
        else:
            print("Bad choice! try again!")

main()