def multiplication_table(number):
    print(f"-----Table of {number}-----")
    for i in range(1,number+1):
        for j in range(1, number+1):
            mult = i * j
            print(i,"*",j,"=",mult)
    print("---------------------")

multiplication_table(1)
multiplication_table(5)
multiplication_table(12)