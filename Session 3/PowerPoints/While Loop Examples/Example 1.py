#Find all odd numbers between 1 and 100
max_num = 100
current_num = 1
while current_num <= max_num:
    if current_num % 2 == 1:
        print(current_num,"is an odd number")
    else:
        print(current_num,"is an even number")
    current_num += 1