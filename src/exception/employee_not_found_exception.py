class EmployeeNotFoundException(Exception):
    def __init__(self,message="Employee Not Found"):
        super().__init__(message)
