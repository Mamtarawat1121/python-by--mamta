students = {}

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))

    students[roll] = {
        "Name": name,
        "Marks": marks
    }

    print("Student Added Successfully!")

def show_students():
    for roll, details in students.items():
        print("Roll:", roll)
        print("Name:", details["Name"])
        print("Marks:", details["Marks"])
        print("----------------")

def search_student():
    roll = input("Enter Roll Number: ")

    if roll in students:
        print(students[roll])
    else:
        print("Student Not Found")

while True:
    print("\n1. Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        show_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        break
    else:
        print("Invalid Choice")