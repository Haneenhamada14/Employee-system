class Employee:
    def _init_(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

class EmployeesManager:
    def _init_(self):
        self.employees_list = []

    def add_employee(self, employee):
        self.employees_list.append(employee)

    def print_employees(self):
        for employee in self.employees_list:
            print(employee.name, employee.age, employee.salary)

    def delete_by_age(self, min_age, max_age):
        self.employees_list = [emp for emp in self.employees_list if emp.age < min_age or emp.age > max_age]

    def update_salary_by_name(self, name, new_salary):
        for emp in self.employees_list:
            if emp.name == name:
                emp.salary = new_salary
                break

class FrontEndManager:
    def _init_(self):
        self.employees_manager = EmployeesManager()

    def display_menu(self):
        print("Welcome to the Front End Manager menu!")
        print("1) Add new employee")
        print("2) Print all employees")
        print("3) Delete by age")
        print("4) Update Salary by name")
        print("5) End the program")
        choice = int(input("Enter your choice (1-5): "))
        return choice
        
    def run_program(self):
        while True:
            choice = self.display_menu()
            if choice == 1:
                name = input("Enter employee name: ")
                age = int(input("Enter employee age: "))
                salary = float(input("Enter employee salary: "))
                new_employee = Employee(name, age, salary)
                self.employees_manager.add_employee(new_employee)
            elif choice == 2:
                self.employees_manager.print_employees()
            elif choice == 3:
                min_age = int(input("Enter minimum age: "))
                max_age = int(input("Enter maximum age: "))
                self.employees_manager.delete_by_age(min_age, max_age)
            elif choice == 4:
                name = input("Enter employee name: ")
                new_salary = float(input("Enter new salary: "))
                self.employees_manager.update_salary_by_name(name, new_salary)
            elif choice == 5:
                break
            else:
                print("Invalid choice. Please enter a valid option.")
                
if __name__ == "__main__":
    frontend_manager = FrontEndManager()
    frontend_manager.run_program()