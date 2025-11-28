from datetime import datetime


class Employee:
    def __init__(self, employee_id,first_name,last_name,date_of_birth,gender,email,phone_number,address,position,joining_date,termination_date=None):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.position = position
        self.joining_date = joining_date
        self.termination_date = termination_date

    def calculate_age(self):
        today=datetime.today()
        if isinstance(self.date_of_birth,datetime):
            dob=self.date_of_birth
        else:
            dob=datetime.strptime(str(self.date_of_birth),"%Y-%m-%d")
        return today.year-dob.year - ((today.month,today.day)<(dob.month,dob.day))
    
    def __str__(self):
        return (f"ID:{self.employee_id} | {self.first_name} {self.last_name} | "
        f"Position: {self.position} | Age:{self.calculate_age()}")
