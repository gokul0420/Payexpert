class PayrollGenerationException(Exception):
    def __init__(self,message="Error generating payroll"):
        super().__init__(message)
        