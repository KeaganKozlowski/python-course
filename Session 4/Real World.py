def calculate_gross_salary(hourly_wage, hours_worked):
    if hours_worked <= 40:
        gross_salary = hourly_wage * hours_worked
    else:
        basic_pay = hourly_wage * 40
        overtime_pay = (hours_worked - 40) * 1.5 * hourly_wage
        gross_salary = basic_pay + overtime_pay
    return gross_salary

# Calling the function
my_gross_salary = calculate_gross_salary(15, 45)
print("Gross Salary:", my_gross_salary)
