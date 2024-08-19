num = int(input("Enter a number : "))

a = 0
b = 1

i = 0

if num <= 0:
    print("Please enter a positive integer ")

elif num == 1:
    print("Fibonacci sequence of 1 : ", a)

else:
    print("Fibonacci sequence : ")
    while i < num:
        print(a)
        sum = a + b
        a = b
        b = sum
        i += 1