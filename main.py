'''
Alex Martinez
Lab Project test
11/29/2022
'''

# Code to find if a number is prime or not.


num = eval(input("Enter the prime number: "))

if num > 1:

    for i in range(2, int(num / 2) + 1):

        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")

else:
    print(num, "is not a prime number")