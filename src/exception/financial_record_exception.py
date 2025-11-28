class FinancialRecordException(Exception):
    def __init__ (self,message="Error with financial record"):
        super().__init__(message)