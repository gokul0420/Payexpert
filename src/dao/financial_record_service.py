import mysql.connector
from entity.financial_record import FinancialRecord
from exception.employee_not_found_exception import EmployeeNotFoundException
from exception.financial_record_exception import FinancialRecordException


class FinancialRecordService:
    def __init__ (self,conn):
        self.conn=conn
    
    def add_financial_record(self,employee_id,record_date,description,amount,record_type):
        try:
            cur=self.conn.cursor()
            cur.execute("select employee_id from employees where employee_id=%s",(employee_id,))
            if not cur.fetchone():
                raise EmployeeNotFoundException (f"Employee with ID{employee_id} not found")
            cur.execute("""
            Insert into financial_records (employee_id,record_date,description,amount,record_type) values (%s,%s,%s,%s,%s)
            """,
            (employee_id,record_date,description,amount,record_type),)
            self.conn.commit()
            cur.close()
            print(f"Financial record added for employee with ID {employee_id}")

        except mysql.connector.Error as e:
            raise FinancialRecordException (f"Error Adding financial record : {e}")

    def get_financial_record_by_id(self,record_id:int)->FinancialRecord:
        try:
            cur=self.conn.cursor()
            cur.execute("Select * from financial_records where record_id=%s",(record_id,))
            row=cur.fetchone()
            cur.close()
            if row:
                return FinancialRecord(*row)
            raise FinancialRecordException (f"Record with Id {record_id} not found")
        except mysql.connector.Error as e:
            raise Exception (f"Database Error: {e}")

    def get_financial_record_for_employee(self,employee_id:int):
        try:
            cur=self.conn.cursor()
            cur.execute("Select * from financial_records where employee_id=%s",(employee_id,))
            rows=cur.fetchall()
            cur.close()
            return [FinancialRecord(*row) for row in rows]
        except mysql.connector.Error as e:
            raise Exception (f"Database Error:{e}")

    def get_financial_records_for_date(self,record_date):
        try:
            cur=self.conn.cursor()
            cur.execute("select* from financial_records where record_date=%s",(record_date,))
            rows=cur.fetchall()
            cur.close()
            return [FinancialRecord(*row) for row in rows]
        except mysql.connector.Error as e:
            raise Exception (f"Database Error:{e}")
