principal = 1000
annual_interest_rate = 0.05
years = 5
#Current year
year = 1
while year <= years:
    future_value = principal * (1 + annual_interest_rate) ** year
    print("Year",year,":",future_value)
    year += 1