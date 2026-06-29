# Employee Management System using OOP

class Employee:
    def __init__(self, emp_id, name, department, designation, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.designation = designation
        self.salary = salary

    def display_details(self):
        print(f"ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Designation: {self.designation}")
        print(f"Salary: ${float(self.salary):,.2f}")


class EmployeeManagementSystem:
    def __init__(self):
        # Using a dictionary for faster O(1) lookups via Employee ID
        self.employees = {}

    def display_menu(self):
        print("\n" + "="*35)
        print("    EMPLOYEE MANAGEMENT SYSTEM    ")
        print("="*35)
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee by ID")
        print("4. Update Employee Details")
        print("5. Remove Employee")
        print("6. Exit")
        print("="*35)

    def add_employee(self):
        print("\n--- Add New Employee ---")
        emp_id = input("Enter Employee ID: ").strip()
        
        if emp_id in self.employees:
            print("❌ Error: Employee ID already exists!")
            return

        name = input("Enter Name: ").strip()
        department = input("Enter Department: ").strip()
        designation = input("Enter Designation: ").strip()
        
        while True:
            try:
                salary = float(input("Enter Salary: "))
                break
            except ValueError:
                print("❌ Invalid input! Please enter a valid number for salary.")

        # Create object and store in dictionary
        new_emp = Employee(emp_id, name, department, designation, salary)
        self.employees[emp_id] = new_emp
        print(f"✅ Employee '{name}' added successfully!")

    def view_all_employees(self):
        print("\n--- All Employee Records ---")
        if not self.employees:
            print("No records found.")
            return

        # Table formatting
        print(f"{'ID':<10} {'Name':<20} {'Department':<15} {'Designation':<15} {'Salary':<12}")
        print("-" * 75)
        for emp in self.employees.values():
            print(f"{emp.emp_id:<10} {emp.name:<20} {emp.department:<15} {emp.designation:<15} ${float(emp.salary):<11,.2f}")

    def search_employee(self):
        print("\n--- Search Employee ---")
        emp_id = input("Enter Employee ID to search: ").strip()
        
        if emp_id in self.employees:
            print("\n--- Record Found ---")
            self.employees[emp_id].display_details()
        else:
            print("❌ Employee not found.")

    def update_employee(self):
        print("\n--- Update Employee Details ---")
        emp_id = input("Enter Employee ID to update: ").strip()
        
        if emp_id not in self.employees:
            print("❌ Employee not found.")
            return
            
        emp = self.employees[emp_id]
        print(f"Updating details for {emp.name}. (Leave blank to keep existing value)")

        name = input(f"New Name ({emp.name}): ").strip()
        dept = input(f"New Department ({emp.department}): ").strip()
        desig = input(f"New Designation ({emp.designation}): ").strip()
        salary_input = input(f"New Salary (${emp.salary}): ").strip()

        # Update values if user typed something
        if name: emp.name = name
        if dept: emp.department = dept
        if desig: emp.designation = desig
        if salary_input:
            try:
                emp.salary = float(salary_input)
            except ValueError:
                print("⚠️ Invalid salary format. Keeping original salary value.")

        print("✅ Employee details updated successfully!")

    def remove_employee(self):
        print("\n--- Remove Employee ---")
        emp_id = input("Enter Employee ID to remove: ").strip()
        
        if emp_id in self.employees:
            removed_emp = self.employees.pop(emp_id)
            print(f"✅ Employee '{removed_emp.name}' removed successfully.")
        else:
            print("❌ Employee not found.")


def main():
    ems = EmployeeManagementSystem()
    
    while True:
        ems.display_menu()
        choice = input("Select an option (1-6): ").strip()
        
        if choice == '1':
            ems.add_employee()
        elif choice == '2':
            ems.view_all_employees()
        elif choice == '3':
            ems.search_employee()
        elif choice == '4':
            ems.update_employee()
        elif choice == '5':
            ems.remove_employee()
        elif choice == '6':
            print("\nExiting system. Goodbye!")
            break
        else:
            print("❌ Invalid selection. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()