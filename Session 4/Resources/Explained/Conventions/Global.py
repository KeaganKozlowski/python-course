global_var = 10

def my_function():
    #Access global variable
    print("Inside function:",global_var)

#Call the function
my_function()

#Access global outside the function
print("Outside function:",global_var)