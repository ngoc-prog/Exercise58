from Employee import Employee  # Import lớp Employee từ file Employee.py

def input_employee():
    last_name = input("Enter last name: ")
    first_name = input("Enter first name: ")
    while True:
        try:
            num_products = int(input("Enter number of products: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer for number of products.")
    return Employee(last_name, first_name, num_products)

def compare_employees(emp1, emp2):
    print("\n--- Comparison Results ---")
    print(f"{emp1.first_name} {emp1.last_name}'s Salary: ${emp1.getsalary():.2f}")
    print(f"{emp2.first_name} {emp2.last_name}'s Salary: ${emp2.getsalary():.2f}")

    if emp1.IsHigher(emp2):
        print(f"{emp1.first_name} {emp1.last_name} has more products and earns more.")
    elif emp2.IsHigher(emp1):
        print(f"{emp2.first_name} {emp2.last_name} has more products and earns more.")
    else:
        print("Both employees have the same number of products.")

    if emp1.num_products > emp2.num_products:
        print(f"Without IsHigher: {emp1.first_name} {emp1.last_name} has more products.")
    elif emp2.num_products > emp1.num_products:
        print(f"Without IsHigher: {emp2.first_name} {emp2.last_name} has more products.")
    else:
        print("Without IsHigher: Both employees have the same number of products.")

def menu():
    employees = []

    while True:
        print("\n--- Employee Management Menu ---")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Compare Two Employees")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            employee = input_employee()
            employees.append(employee)
            print("Employee added successfully.")

        elif choice == "2":
            if not employees:
                print("No employees available.")
            else:
                print("\n--- Employee List ---")
                for idx, emp in enumerate(employees, start=1):
                    print(f"{idx}. {emp.first_name} {emp.last_name}, Products: {emp.num_products}, Salary: ${emp.getsalary():.2f}")

        elif choice == "3":
            if len(employees) < 2:
                print("You need at least 2 employees to compare.")
            else:
                print("\n--- Select Employees to Compare ---")
                for idx, emp in enumerate(employees, start=1):
                    print(f"{idx}. {emp.first_name} {emp.last_name}")

                try:
                    choice1 = int(input("Select the first employee (number): ")) - 1
                    choice2 = int(input("Select the second employee (number): ")) - 1
                    if 0 <= choice1 < len(employees) and 0 <= choice2 < len(employees):
                        compare_employees(employees[choice1], employees[choice2])
                    else:
                        print("Invalid selection. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter valid numbers.")

        elif choice == "4":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
