import mysql.connector
from entity.payroll import Payroll
from exception.employee_not_found_exception import EmployeeNotFoundException
from exception.payroll_generation_exception import PayrollGenerationException


class PayrollService:
    def __init__(self,conn):
        self.conn=conn
    
    def generate_payroll(self,employee_id,pay_period_start_date,pay_period_end_date,basic_salary,overtime_pay,deductions):
        try:
            cur = self.conn.cursor()
            cur.execute("Select employee_id from employees where employee_id = %s",(employee_id,))
            if not cur.fetchone():
                raise EmployeeNotFoundException(f"Employee with ID {employee_id} not found")
            net_salary=basic_salary+overtime_pay-deductions
            cur.execute("""
            Insert into payrolls (employee_id,pay_period_start_date,pay_period_end_date,basic_salary,overtime_pay,deductions,net_salary)
            values (%s,%s,%s,%s,%s,%s,%s)
            """,
            (employee_id,pC,pay_period_end_date,basic_salary,overtime_pay,deductions,net_salary),
            )
            self.conn.commit
            cur.close()
            print(f"Payroll generated for employee with ID {employee_id}.Net Salary : Rs.{net_salary}")
        except mysql.connector.Error as e:
            raise PayrollGenerationException (f"Error generating payroll : {e}")

    def get_payroll_by_id(self,payroll_id:int)->Payroll:
        try:
            cur=self.conn.cursor()
            cur.execute("Select * from payrolls where payroll_id=%s",(payroll_id,))
            row=curr.fetchone()
            cur.close()
            if row:
                return Payroll(*row)
            raise PayrollGenerationException (f"Payroll with ID {payroll_id} not found")
        except mysql.connector.Error as e:
            raise Exception(f"Database Error : {e}")

    def get_payrolls_for_employee(self,employee_id):
        try:
            cur=self.conn.cursor()
            cur.execute("select * from payrolls where employee_id=%s",(employee_id,))
            rows=cur.fetchall
            cur.close()
            return [Payroll(*row) for row in rows]
        except mysql.connector.Error as e:
            raise Exception(f"Database Error : {e}")

    def get_payrolls_for_period(self,start_date,end_date):
        try:
            cur=self.conn.cursor()
            cur.execute("select * from payrolls where pay_period_start_date >=%s pay_period_end_date<=%s",(start_date,end_date), )
            rows=cur.fetchall()
            cur.close()
            return [Payroll(*row) for row in rows]
        except mysql.connector.Error as e:
            raise Exception(f"Database Error: {e}")
            
