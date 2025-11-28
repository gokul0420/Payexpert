class TaxCalculationException(Exception):
    def __init__(self,message="Error in Tax Calculation"):
        super().__init__()