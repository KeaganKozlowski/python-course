def my_function():
    local_var = 20
    print("Inside function:",local_var)
#Call the function
my_function()
#Attempt to acccess local variable
#Outside the function
#Will result in NameError
print("Outside:",local_var)