def is_even(number):
    if number % 2 == 0:
        print(number,"is even")
        return True
    else:
        print(number,"is odd")
        return False

is_even(5)
is_even(20)
is_even(2000000000000001)