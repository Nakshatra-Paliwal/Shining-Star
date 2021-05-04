# Calculate the Sum of every 4th number in the Range given by the User.
start = int(input("Enter the Start Value: "))
end = int(input("Enter the End Value:"))

for num in range(start,end,4):
    sum = num + num
    print(sum)
    
    
