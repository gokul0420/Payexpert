class FinancialRecord:
    def __init__(self, record_id,employee_id,record_date,description,amount,record_type):
        self.record_id = record_id
        self.employee_id = employee_id
        self.record_date = record_date
        self.description =  description
        self.amount = amount
        self.record_type = record_type

    def __str__ (self):
        return (
            f"RecordID:{self.record_id} | EmployeeID:{self.employee_id} | "
            f"{self.record_type}: Rs.{self.amount} | Date:{self.record_date} | {self.description}"
        )