import mysql.connector

from entity.employee import Employee

from exception.employee_not_found_exception import EmployeeNotFoundException
from exception.invalid_input_exception import InvalidInputException


class EmployeeService:
    def __init__(self,conn):
        self.conn=conn
    
    def get_employee_by_id(self,employee_id: int) -> Employee:
        try:
            cur=self.conn.cursor()
            cur.execute("Select * from employees where employee_id=%s",(employee_id,))
            row=cur.fetchone()
            if row:
                return Employee(*row)
            raise EmployeeNotFoundException (f"Employee with id {employee_id} not found")

        except mysql.connector.Error as e:
            raise Exception(f"Database error:{e}")

    def get_all_employees(self):
        try:
            cur=self.conn.cursor()
            cur.execute("Select * from employees")
            rows=cur.fetchall()
            cur.close()
            return [Employee(*row) for row in rows]
        except mysql.connector.Error as e:
            raise Exception (f"Database error:{e}")

    def add_employee(self,employee: Employee):
        if not employee.first_name or employee.email:
            raise InvalidInputException("First name and email are required")
        try:
            cur=self.conn.cursor()
            cur.execute("""Insert into employees (employee_id,first_name,last_name,date_of_birth,gender,email,phone_number,address,position,joining_date,termination_date) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) """,
            (employee.employee_id,
            employee.first_name,
            employee.last_name,
            employee.date_of_birth,
            employee.gender,
            employee.email,
            employee.phone_number,
            employee.address,
            employee.position,
            employee.joining_date,
            employee.termination_date,
            ),
            )
            self.conn.commit()
            cur.close()
            print(f"Employee {employee.first_name} {employee.lastname} added successfully")

        except mysql.connector.Error as e:
            raise Exception(f"Database Error: {e}")

    def update_employee(self,employee: Employee):
        try:
            cur=self.conn.cursor()
            cur.execute(
                """Update employees set first_name=%s, last_name=%s, date_of_birth=%s,
                gender=%s,email=%s,phone_number=%s,address=%s,position=%s,joining_date=%s,termination_date=%s where employee_id=%s""",
                (
                    employee.first_name,
                    employee.last_name,
                    employee.date_of_birth,
                    employee.gender,
                    employee.email,
                    employee.phone_number,
                    employee.address,
                    employee.position,
                    employee.joining_date,
                    employee.termination_date,
                    employee.employee_id,
                ),
            )
            self.conn.commit()
            if cur.rowcount==0:
                raise EmployeeNotFoundException (f"Employee with ID {employee.employee_id} not found")
            cur.close()
            print(f"Employee {employee.employee_id} updated successfully")
        except mysql.connector.Error as e:
            raise Exception(f"Database error:{e}")
    def remove_employee(self,employee_id:int):
        try:
            cur=self.conn.cursor()
            cur.execute("Delete from employees where employee_id=%s",(employee_id,))
            self.conn.commit()
            if cur.rowcount==0:
                raise EmployeeNotFoundException (f"Employee with ID {employee_id} not found")
            cur.close()
            print(f"Employee {employee_id} removed successfully")
        except mysql.connector.Error as e:
            raise Exception (f"Database error : {e}")
            





