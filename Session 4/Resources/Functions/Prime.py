def is_prime(number):
    for i in range(2,number):
        if number % i == 0:
            print(number,"not prime")
            return False
    print(number,"is prime")
    return True

is_prime(7)
is_prime(21)
is_prime(567878)