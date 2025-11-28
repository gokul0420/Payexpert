from dao.employee_service import EmployeeService
from dao.financial_record_service import FinancialRecordService
from dao.payroll_service import PayrollService
from dao.tax_service import TaxService
from entity.employee import Employee
from exception.database_connection_exception import DatabaseConnectionException
from exception.employee_not_found_exception import EmployeeNotFoundException
from exception.financial_record_exception import FinancialRecordException
from exception.invalid_input_exception import InvalidInputException
from exception.payroll_generation_exception import PayrollGenerationException
from exception.tax_calculation_exception import TaxCalculationException
from utils.db_conn_util import DbConnUtil


def main():
    try:
        conn=DbConnUtil.get_connection()
        print("Connected to database successfully")

        employee_service=EmployeeService(conn)
        payroll_service=PayrollService(conn)
        tax_service=TaxService(conn)
        financial_record_service=FinancialRecordService(conn)

        while True:
            print("\n"+"="*60)
            print("PAYROLL SYSTEM")
            print("="*60)
            print("1.View All Employees")
            print("2.Get Employee By ID")
            print("3.Add New Employee")
            print("4.Update Employee")
            print("5.Remove Employee")
            print("6.Generate Payroll")
            print("7.View Payroll By ID")
            print("8.View Payrolls for Employee")
            print("9.View Payrolls for period")
            print("10.Calculate Tax")
            print("11.View Tax By ID")
            print("12.View Taxes For Employees")
            print("13.View Taxes For Year")
            print("14.Add Financial Record")
            print("15.View Financial Record By ID")
            print("16.View Financial Record For Employee")
            print("17.View Financial Record For Date")
            print("0.Exit")
            choice=input("\n Enter your Choice: ")

            try:
                if choice =="1":
                    employees=employee_service.get_all_employees()
                    if employees:
                        print("\n--ALL EMPLOYEES--")
                        for emp in employees:
                            print(emp)
                    else:
                        print("No employees Found")

                elif choice=="2":
                    emp_id=int(input("Enter Employee ID: "))
                    employee=employee_service.get_employee_by_id(emp_id)
                    print("\n",employee)

                elif choice=="3":
                    print("ADD NEW EMPLOYEE")
                    emp_id=int(input("Employee ID :"))
                    fname=input("Enter First Name:")
                    lname=input("Enter Last Name:")
                    dob=input("Date of Birth(YYYY-MM-DD):")
                    gender=input("Gender:")
                    email=input("Email: ")
                    phone=input("Phone Number: ")
                    address=input("Address: ")
                    position=input("Position: ")
                    joining=input("Joining Date(YYYY-MM-DD):")

                    employee=Employee(emp_id,fname,lname,dob,gender,email,phone,address,position,joining,)
                    employee_service.add_employee(employee)

                elif choice=="4":
                    print("UPDATE EMPLOYEE")
                    emp_id=int(input("Enter Employee ID to update: "))
                    employee=employee_service.get_employee_by_id(emp_id)
                    print(f"Current:{employee}")
                    fname=input(f"First Name [{employee.first_name}]:") or employee.first_name
                    lname=input(f"Last Name [{employee.last_name}]:") or employee.last_name
                    email=input(f"Email [{employee.email}]:") or employee.email
                    phone=input(f"Phone [{employee.phone_number}]: ")or employee.phone_number
                    position=input(f"Position [{employee.position}]: ") or employee.position

                    employee.first_name= fname
                    employee.last_name=lname
                    employee.email=email
                    employee.phone_number=phone
                    employee.position=position
                    employee_service.update_employee(employee)

                elif choice=="5":
                    emp_id=int(input("Enter emp_id to remove: "))
                    confirm=input("Are you confirm to do so? (Yes/No)")
                    if confirm.lower()=="yes":
                        employee_service.remove_employee(emp_id)
                        print("employee removed")

                elif choice=="6":
                    print("Generate Payroll")
                    emp_id=int(input("Employee ID: "))
                    start=input("Period Start(YYYY-MM-DD):")
                    end=input("Period End(YYYY-MM-DD):")
                    basic=float(input("Basic Salary:"))
                    overtime=float(input("Overtime Salary:"))
                    deduction=float(input("Deduction:"))
                    payroll_service.generate_payroll(emp_id,start,end,basic,overtime,deduction)

                elif choice =="7":
                    payroll_id=int(input("Enter Payroll ID:"))
                    payroll=payroll_service.get_payroll_by_id(payroll_id)
                    print("/n",payroll)
                
                elif choice=="8":
                    emp_id=int(input("Enter Employee ID: "))
                    payrolls=payroll_service.get_payrolls_fo_employee(emp_id)
                    if payrolls:
                        for p in payroll:
                            print(p)
                    else:
                        print("Payrolls not found")

                elif choice =="9":
                    start=input("Start Date(YYYY-MM-DD): ")
                    end=input("End Date(YYYY-MM-DD): ")
                    payrolls=payroll_service.get_payrolls_for_period(start,end)
                    if payrolls:
                        for p in payrolls:
                            print(p)
                    else:
                        print("No payrolls found")
                
                elif choice=="10":
                    print("Calculate Tax")
                    emp_id=int(input("Enter Employee ID:"))
                    year=int(input("Enter year:"))
                    income=float(input("Enter Income:"))
                    tax_service.calculate_tax(emp_id,year,income)

                elif choice=="11":
                    tax_id=int(input("Enter Tax Id : "))
                    tax=tax_service.get_tax_by_id(tax_id)
                    print("\n",tax)

                elif choice=="12":
                    emp_id=int(input("Employee ID:"))
                    taxes=tax_service.get_taxes_for_employees(emp_id)
                    if taxes:
                        for t in taxes:
                            print(t)
                    else:
                        print("taxes not found for this employee")

                elif choice=="13":
                    year=int(input("Enter Tax Year:"))
                    taxes=tax_service.get_taxes_for_year(year)
                    if taxes:
                        print(f"Taxes for year {year}")
                        for p in taxes:
                            print(p)
                    else:
                        print("No Tax records found")

                elif choice =="14":
                    print("ADD FINANCIAL RECORD")
                    emp_id=int(input("Employee ID:"))
                    date=input("Record Date(YYYY-MM-DD): ")
                    description=input("Description:")
                    amount=float(input("Enter Amount:"))
                    record_type=input("Record type (income/expense/tax payment):")
                    financial_record_service.add_financial_record(emp_id,date,description,amount,record_type)

                elif choice =="15":
                    rec_id=int(input("Enter Record ID:"))
                    rec=financial_record_service.get_financial_record_by_id(rec_id)
                    print("\n",rec)

                elif choice=="16":
                    print("VIEW RECORDS FOR EMPLOYEES")
                    emp_id=int(input("Employee ID:"))
                    recs=financial_record_service.get_financial_record_for_employee(emp_id)
                    if recs:
                        for i in recs:
                            print(i)
                    else:
                        print("No records found")
                    
                elif choice=="17":
                    date=input("Enter Date(YYYY-MM-YY):")
                    recs=financial_record_service.get_financial_records_for_date(date)
                    if recs:
                        print(f"financial records for the date {date}")
                        for i in recs:
                            print(i)
                    else:
                        print("no records found on that date")

                elif choice=="0":
                    print("Thanks for using pay expert!bye")
                    break
                else:
                    print("Invalid Choice")

            except EmployeeNotFoundException as e:
                print(f"\nERROR:{e}")
            except PayrollGenerationException as e:
                print(f"\nERROR:{e}")
            except FinancialRecordException as e:
                print(f"\nERROR:{e}")
            except InvalidInputException as e:
                print(f"\nERROR:{e}")
            except TaxCalculationException as e:
                print(f"\n ERROR : {e}")
            except ValueError as e:
                print(f"\nInvalid input format-{e}")
            except Exception as e:
                print(f"\nERROR:{e}")

        conn.close()
        print("Database Connection Closed")
    except DatabaseConnectionException as e:
        print(f"\n FATAL ERROR: {e}")
        print("pls check db configuration in db.properties")


if __name__=="__main__":
    main()










