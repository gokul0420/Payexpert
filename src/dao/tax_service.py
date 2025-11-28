import mysql.connector
from entity.tax import tax
from exception.employee_not_found_exception import EmployeeNotFoundException
from exception.tax_calculation_exception import TaxCalculationException


class TaxService:
    def __init__(self,conn):
        conn=self.conn

    def calculate_tax(self,employee_id,tax_year,taxable_income):
        try:
            cur=self.conn.cursor()
            cur.execute("Select employee_id from employees where employee_id=%s",(employee_id,))
            if not cur.fetchone():
                raise EmployeeNotFoundException(f"Employee with ID {employee_id} not found")
            tax_amount=taxable_income*0.20

            cur.execute("""insert into taxes (employee_id,tax_year,taxable_income,tax_amount) values (%s,%s,%s,%s)""",(employee_id,tax_year,taxable_income,tax_amount),)
            self.conn.commit()
            cur.close()
            print(f"Tax calculated for employee {employee_id}:Rs.{tax_amount}")
            return tax_amount

        except mysql.connector.Error as e:
            raise TaxCalculationException (f"Error calculating tax:{e}")

    def get_tax_by_id(self,tax_id:int)->Tax:
        try:
            cur=self.conn.cursor()
            cur.execute("select * from taxes where tax_id=%s",(tax_id,))
            row=cur.fetchone()
            cur.close()
            if row:
                return Tax(*row)
            raise TaxCalculationException (f"Tax with ID {tax_id} is not found")
        except mysql.connector.Error as e:
            raise Exception (f"Database Error : {e}")

    def get_taxes_for_employees(self,employee_id: int):
        try:
            cur=self.conn.cursor()
            cur.execute("select * from taxes where employee_id=%s",(employee_id,))
            rows=cur.fetchall()
            cur.close()
            return [Tax(*row) for row in rows]
        except mysql.connector.Error as e:
            raise Exception (f"Database Error: {e}")
    
    def get_taxes_for_year(self,tax_year: int):
        try:
            cur=self.conn.cursor()
            cur.execute("select * from taxes where tax_year=%s",(tax_year,))
            rows=cur.fetchall()
            cur.close()
            return [Tax(*row) for row in rows]
        except mysql.connector.Error as e:
            raise Exception(f"Database Error: {e}")

