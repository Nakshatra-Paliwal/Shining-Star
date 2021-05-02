"""
Write a code to calculate Area of two triangles. 
And compare these areas, and
print which triangle has the greater area
Note : Take input from the user as Base
and Height values for two triangles

"""
Base1 = float(input("Please enter the value of Base of the 1st Triangle : "))
Height1 = float(input("Please enter the value of Height of the 1st Triangle : "))
Base2 = float(input("Please enter the value of Base of the 2nd Triangle : "))
Height2 = float(input("Please enter the value of Height of the 2nd Triangle : "))
Area1 = (1/2 * Base1 * Height1)
Area2 = (1/2 * Base2 * Height2)
print("Area of the 1st Triangle is " + str(Area1))
print("Area of the 2nd Triangle is " + str(Area2))


if Area1<Area2:
    print("Area of the 1st Triangle is smaller. ") 
else:
    print("Area of the 2nd Triangle is smaller. ")    


