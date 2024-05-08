#The list of numbers
my_numbers = [12, 7, 3, 20, 16, 9, 24, 8, 15]
#Odd and Even counters
odd = 0
even = 0
for e in my_numbers:
    #Even
    if e % 2 == 0:
        even += 1
    else:
        odd += 1
print("The number of odd numbers is:",odd)
print("The number of even numbers is:",even)