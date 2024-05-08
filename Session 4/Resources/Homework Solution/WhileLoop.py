#The list of numbers
my_numbers = [12, 7, 3, 20, 16, 9, 24, 8, 15]
#Odd and Even counters
odd = 0
even = 0
#n is the first index of the list
n = 0
while n < len(my_numbers):
    #Even
    if my_numbers[n] % 2 == 0:
        even += 1
    else:
        odd += 1
    n += 1
print("The number of odd numbers is:",odd)
print("The number of even numbers is:",even)
    