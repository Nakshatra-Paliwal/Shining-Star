# Write a code to find the addition of all the odd numbers in a range 1-100.
for num in range(1,101):
    if num % 3 == 0:
        sum = num + num
        print((sum))