
num_terms = int(input("Enter the number of terms: "))
a, b = 0, 1
count = 0
if num_terms <= 0:
    print("Please enter a positive integer.")
elif num_terms == 1:
    print("Fibonacci sequence up to", num_terms, ":")
    print(a)
else:
    print("Fibonacci sequence:")
    while count < num_terms:
        print(a, end=" ")
        nth = a + b
        a = b
        b = nth
        count += 1
        #
        # num = int(input("Enter the number of terms: "))
        # a, b = 0, 1
        # count = 0
        #                                                           #to print the nth term

        # if num <= 0:
        #     print("Please enter a positive integer.")
        # elif num == 1:
        #     print("Fibonacci sequence up to", num, "term is:", a)
        # else:
        #     while count < num - 1:
        #         nth = a + b
        #         a = b
        #         b = nth
        #         count += 1
        #     print(a)
