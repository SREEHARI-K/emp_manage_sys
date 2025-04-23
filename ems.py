employee_data = {
    101:{'name':'Satya','age':27,'department':'HR','salary':50000},
    102:{'name':'aJcob','age':30,'department':'Teaching','salary':60000},
    103:{'name':'Arun','age':25,'department':'IT','salary':30000},
    104:{'name':'Suresh','age':35,'department':'HOD','salary':100000},
    105:{'name':'Hari','age':27,'department':'Anlaytics','salary':5000000},
    106:{'name':'Veena','age':24,'department':'Developer','salary':50000}
   
}


def add_employee():
    emp_id = int(input("Enter Employee ID:"))
    while emp_id is not None:
        if emp_id in employee_data:
            emp_id = int(input("Employee ID already exists.Enter a new one:"))
        else:
            break
    name = input("Enter name:")
    age = int(input("Enter age:"))
    department = input("Enter department:")
    salary = float(input("Enter salary:"))
    employee_data[emp_id] = {'name':name,'age':age,'department':department,'salary':salary}
    print("Employee added successfully.")

def view_employees():
    if not employee_data:
        print("No employees available.")
    else:
        for emp_id,details in employee_data.items():
            print(f"ID: {emp_id}, Name: {details['name']}, Age: {details['age']}, Department: {details['department']}, Salary: {details['salary']}")


def search_employee():
    emp_id = int(input("Enter Employee ID to search:"))
    if emp_id in employee_data:
        details = employee_data[emp_id]
        print(f"ID:{emp_id},Name:{details['name']},Age:{details['age']},Department:{details['department']},Salary:{details['salary']}")
    else:
        print("Employee not found")


def main_menu():
    while True:
        print("\n==Employee Management System==")
        print("1.Add Employee")
        print("2.View All Employees")
        print("3.Search for Employee")
        print("4.Exit")

        choice = input("Enter your choice:")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            print("Thank-You")
            break
        else:
            print("invalid choice")

main_menu()
                
