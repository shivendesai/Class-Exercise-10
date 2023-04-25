#Written by Shiven Desai
class Employee:
    def __init__(self, emp_num):
        self.emp_num = emp_num
    
    def set_emp_num(self, emp_num):
        self.emp_num = emp_num
    
    def get_emp_num(self):
        return self.emp_num
    

class ProductionWorker(Employee):
    def __init__(self, emp_num, shift_num, hourly_pay_rate):
        Employee.__init__(self, emp_num)
        self.shift_num = shift_num
        self.hourly_pay_rate = hourly_pay_rate
    
    def set_shift_num(self, shift_num):
        self.shift_num = shift_num
    
    def set_hourly_pay_rate(self, hourly_pay_rate):
        self.hourly_pay_rate = hourly_pay_rate
    
    def get_shift_num(self):
        return self.shift_num
    
    def get_hourly_pay_rate(self):
        return self.hourly_pay_rate


# create a ProductionWorker object and prompt the user for input
emp_num = input("Enter employee number: ")
shift_num = int(input("Enter shift number (1 for day, 2 for night): "))
hourly_pay_rate = float(input("Enter hourly pay rate: "))
pw = ProductionWorker(emp_num, shift_num, hourly_pay_rate)

# display the data using the accessor methods
print("Employee number:", pw.get_emp_num())
print("Shift number:", pw.get_shift_num())
print("Hourly pay rate:", pw.get_hourly_pay_rate())
