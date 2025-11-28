class Payroll:
    def __init__ (self, payroll_id,employee_id,pay_period_start_date,pay_period_end_date,basic_salary,overtime_pay,deductions,net_salary):
        self.payroll_id = payroll_id
        self.employee_id = employee_id
        self.pay_period_start_date = pay_period_start
        self.pay_period_end_date = pay_period_end_date
        self.basic_salary = basic_salary
        self.overtime_pay = overtime_pay
        self.deductions = deductions
        self.net_salary = net_salary
    
    def __str__(self):
        return (
            f"PayrollID:{self.payroll_id} | EmployeeID:{self.employee_id} | "
            f"Period:{self.pay_period_start_date} to {self.pay_period_end_date} | NetSalary: Rs. {self.net_salary}")
        
