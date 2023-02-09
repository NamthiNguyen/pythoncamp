"""
Name: Namthi Nguyen
project: tax estimated calculator 

"""


def calculate_deductibles(income, expenses):
    return min(income * 0.2, expenses)

def calculate_tax(income, expenses):
    federal_tax_rate = 0.1 # 10%
    state_tax_rate = 0.0575 # 5.75%

    deductible = calculate_deductibles(income, expenses)
    taxable_income = income - deductible
    federal_tax = taxable_income * federal_tax_rate
    state_tax = taxable_income * state_tax_rate
    return federal_tax + state_tax

income = float(input("Enter your yearly income: "))
expenses = float(input("Enter your yearly expenses: "))
tax = calculate_tax(income, expenses)
print("Tax owed: $%.2f" % tax)