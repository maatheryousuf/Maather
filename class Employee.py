class Employee:
    overtimes = 0
    overtimes_amount = 0
    def __init__(self, emp_id, emp_name, emp_salary, emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department
        Employee.overtimes = 0
        Employee.overtimes_amount = 0
    def calculate_emp_salary(self, salary, hours_worked):
        overtimes = hours_worked - 50
        if hours_worked > 50:
            overtimes_amount = overtimes*(salary/50)
            self.emp_salary = salary + overtimes_amount
        else:
            self.salary = salary
            
       
    def set_department(self, new_deparment):
             self.emp_department = new_deparment 
        

    def print_employee_details(self):
           return "{} for {} and salary {} working in {} department ".format( self.emp_id,self.emp_name, self.emp_salary, self.emp_department)
        
        
p1 = Employee("DS0010", "Maather", 50000, "Technical support")
p2 = Employee("E7499", "JONES", 450000, "Research")
p3 = Employee("E7900", "MARTIN", 50000, "SALES")


p2.set_department("Technical")
print(p2.print_employee_details())
p3.calculate_emp_salary(50000, 55)
print(p3.print_employee_details())



        