 
from collections import Counter

#Advanced Area Calculator
#Likhitha Koppula
#ICS3U Assignment
import math

#power function
def power(base, exponent):
    return base **exponent

#square root function
def mathsqrt(x):
    return math.sqrt(x)

#addition function
def addition(x, y):
    return x + y

#subtraction function
def subtraction(x1, y2):
    return x1 - y2

#multipulcation function
def multiplication(x3, y3):
    return x3 * y3

#division function
def division(x4, y4):
    return x4 / y4

#calculates the slope
def slope(y1,y2,x1,x2):
    return (y1-y2) / (x1-x2)

#calculates the y-int
def y_int(y,m,x):
    b = y-m*x
    return b

#calculates the x-int
def x_int(b,m):
    x = (-b)/m
    return x

#calculates the reciprocal
def reciprocal_slope(x,y):
    return x / y

#area of square
def square_area(x):
    return x**2

#area of rectangle
def rectangle_area(x,y):
    return x * y

#area of triangle
def triangle_area(b,h):
    return (b*h) / 2

#area of circle
def circle_area (r):
    return (r**2)*(3.1415)

#perimeter of square
def square_perimeter(x):
    return x * 4

#perimeter of rectangle
def rectangle_perimeter(x,y):
    return (x*2) + (y*2)

#perimeter of triangle
def triangle_perimeter(x,y,z):
    return x+y+z

#circumference/perimeter of circle
def circle_perimeter(r):
    return 2*(3.1415)*(r)

def my_mean(sample):
    return sum(sample)/len(sample)


def mine_mode(sample):
    max_counter = 0
    mode_1 = 0
    for i in range(len(sample)):
        count = 0
        for j in range(len(sample)):
            if sample[i] == sample[j]:
                count =+ count +1
        if count>max_counter:
            max_counter = count
            mode_1 = sample[i]
        if max_counter == 1:
            mode_1 = -1
    return mode_1

def median(sample):
    quotient, remainder = divmod(len(sample), 2)
    if remainder:
        return sorted(sample)[quotient]
    return sum(sorted(sample)[quotient - 1:quotient + 1]) / 2



#Function for sqared used in respected section

#The instructions/intro for the user
print ("Hello, welcome to the Advanced Calculator")
print (" ")
print ("You may Calculate Basic Numbers or choose between our Advanced functions")
print (" ")
print ("Basic Numbers : You can choose simple functions(addition, subratction, multipulcation, division), square roots or powers of numbers.")
print (" ")
print ("Our Advanced functions : Geometry Components, Algebra Linear Equations, Averages")
       
print ("Geometry Components : includes the area of shapes, perimeter of shapes")
print ("Algebra Linear Equations : includes the slope, y-intercept given a point on the line and the slope, x-intercept and the slope of the reciprocal")
print ("Averages : includes the average of numbers through mean, median, mode ")
print(" ")

while True:
    data_valid3 = False
    #this loop makes sure userd only choose between the two options of basic numbers and advanced functions
    while not data_valid3:
        
        calc_needs = str(input("Would you like to calculate Basic Numbers or Advanced Functions:"))
        #calc_needs is a variable to store what the user would like to calculate

        if calc_needs == 'Basic Numbers' or calc_needs == 'basic numbers' or calc_needs == 'Basic numbers': 
            data_valid3 = True  
            
            data_valid = False  
            while not data_valid:
                #this loop make sures the user only chooses the basic number functions given
                basic_needs = str(input("Would you like to calculate Powers, Squares or Simple Functions: "))
                #basic_needs stores the basic calculation need for the user
                if basic_needs == 'Powers':
                    print ("You are calculating the Power")
                    data_valid = True
                    
                    if basic_needs == 'Powers'or basic_needs == 'powers':
                        base_chosen = float(input("Enter your base number here:"))
                        #The base number of the power
                        exponent_chosen = float(input("Enter your exponent here: "))
                        #The exponent number of the power
                        power_number_result =  power(base_chosen, exponent_chosen)
                        #Function at the top
                        print (" ")
                        print("Your result : " + str(power_number_result))
                        #prints the result of the power
                    
                if basic_needs == 'Squares':
                    print ("You are calculating the Square")
                    data_valid = True
                    
                    if basic_needs == 'squares' or basic_needs == 'Squares' or calc_needs ==  'Square roots': 
                        square_number_chosen = float(input("Enter your number here:"))
                        # square_number_chosen stores the number chosen by the user to square
                        # MAKE IT SO THAT YOU CANNOT ENTER NEGATIVE VALUES
                        square_number_result = mathsqrt(square_number_chosen)
                        print (" ")
                        print ("Your result : " + str(square_number_result))
                        #prints the result of the square
                    
                if basic_needs == 'Simple Functions':
                    print ("You are calculating Simple Functions")
                    data_valid = True
                    
                    if basic_needs == 'Simple Functions':
                        data_valid4 = False
                        while not data_valid4:
                            #this loop makes sure the user only chooses the simple functions options given
                            sf_needs = str(input("Addition, Subtraction, Division or Multipulcation:"))
                            #users simple functions options
                        
                            if sf_needs == 'Addition':
                                data_valid4 = True
                                #sf_needs represents the  useres needs for simple functions(sf)
                                add_x = float(input("Enter First Number Here:"))
                                add_y = float(input("Enter Second Number Here:"))
                                addition_result = addition(add_x, add_y)
                                #Function at the top
                                print (" ")
                                print("Your result : " + str(addition_result))
                                #prints results
                                
                            if sf_needs == 'Subtraction':
                                data_valid4 = True
                                subtraction_x = float(input("Enter First Number Here:"))
                                subtraction_y = float(input("Enter Second Number Here:"))
                                subtraction_result = subtraction(subtraction_x, subtraction_y )
                                #Function at the top
                                print (" ")
                                print("Your result : " + str(subtraction_result))
                                #prints results
                                
                            if sf_needs == 'Multipulcation':
                                data_valid4 = True
                                multiplication_x = float(input("Enter First Number Here:"))
                                multiplication_y = float(input("Enter Second Number Here:"))
                                multiplication_result = multiplication(multiplication_x, multiplication_y)
                                #Function at the top
                                print (" ")
                                print("Your result : " + str(multiplication_result))
                                #prints results
                                
                            if sf_needs == 'Division':
                                data_valid4 = True
                                division_x = float(input("Enter First Number Here:"))
                                division_y = float(input("Enter Second Number Here:"))
                                division_result = division(division_x, division_y)
                                #Function at the top
                                print (" ")
                                print("Your result : " + str(division_result))
                                #prints results
                

                        
                    
    #calculator is now calculating advanced functions
        if calc_needs == 'Advanced Functions' or calc_needs == 'advanced functions' or calc_needs == 'Advanced functions': 
            data_valid3 = True 
            print ("You are calculating Advanced Functions")
            print (" ")
            data_valid2 = False 
            while not data_valid2:
                #this loop checks to make sure user enteres Geometry Components or Linear Equations or Mean and Mode
                advanf_needs = str(input("Would you like to calculate Geometry Components, Linear Equations, or Averages:"))
                #advanf_needs represnets the users needs for advanced functions(advanf)
                #function to store what advanced funtion the user wants to calculate
            #add data validation for the bonus points as well make sure to use correct data validation number 
                if advanf_needs == 'Linear Equations' or advanf_needs == 'linear equations' or advanf_needs == 'Linear equations':
                    print ("You are now calculating linear equations")
                    data_valid2 = True
                    
                    data_valid5 = False  
                    #loop to make sure user chooses the linear options given
                    while not data_valid5:
                        linear_needs =  input("Would you like to calculate the slope, y-intercept, x-intercept or slope of the reciprocal:")
                        
                        if linear_needs == 'slope':
                            data_valid5 = True
                            frac1_x = float(input("Enter x of first fraction:"))
                            frac1_y = float(input("Enter y of first fraction:"))
                            frac2_x = float(input("Enter x of second fraction:"))
                            frac2_y = float(input("Enter y of second fraction:"))
                            slope_result = slope(frac1_y,frac2_y,frac1_x,frac2_x)
                            print ("Your slope:" + str(slope_result))
                            
                        if linear_needs == 'y-intercept':
                            data_valid5 = True
                            #asks for the x-value of a point and y-value of a point then asks for the slope.
                            print ("You are now calculating the y-intercept with slope and one point given")
                            y_int_x_point = float(input("Enter the x-value of point:"))
                            y_int_y_point = float(input("Enter the y-value of point:"))
                            y_int_slope = float(input("Enter the slope in decimal form:"))
                            y_intercept_result = y_int(y_int_y_point, y_int_slope, y_int_x_point, )
                            print ("Your y-intercept:" + str(y_intercept_result))
                        
                        if linear_needs == 'x-intercept':
                            data_valid5 = True
                            #to calculate the x-intercept the following code will ask for the clope as well as the 'b' value or y-intercept
                            #x-int will be solved by a def function written above
                            x_int_b_point = float(input("Enter y-intercept:"))
                            x_int_slope = float(input("Enter slope:"))
                            x_intercept_result = x_int(x_int_b_point, x_int_slope)
                            print("Your x-intercept:" + str(x_intercept_result))
                        
                        
                        if linear_needs == 'slope of the reciprocal':
                            #asks for the y-value(rise) and then the x-value(run)
                            #then plugged into the def function written above at the top of code
                            data_valid5 = True
                            reciprocal_y1 = float(input("Enter rise:"))
                            reciprocal_x1 = float(input("Enter run:"))
                            reciprocal_result = reciprocal_slope(reciprocal_x1,reciprocal_y1)
                            print ("Slope of Reciprocal:" + str(reciprocal_result))
                        
                if advanf_needs == 'Geometry Components'or advanf_needs == 'geometry components' or advanf_needs == 'Geometry components':
                    print ("You are now calculating geometrey components")
                    data_valid2 = True
                    
                    data_valid6 = False  
                    while not data_valid6:
                        #this loop makes sure user enters area or perimeter
                        
                        geometry_needs = input("Would you like to calculate Area or Perimeter:")
                        if geometry_needs == 'Area' or geometry_needs == 'area':
                            data_valid6 = True
                            
                            data_valid7 = False  
                            while not data_valid7:
                                #this loop checks to make sure users entered a valid dhape to calculate area
                                area_shape = input("Would you like to calculate the area of a square, rectangle, triangle, and circle:")

                                if area_shape == 'square' or area_shape == 'Square':
                                    data_valid7 = True
                                    square_area_side_length = float(input("Enter side length here:"))
                                    square_area_result = square_area(square_area_side_length)
                                    print ("Square Area:" + str(square_area_result))
                                    #area of square
                                
                                if area_shape == 'rectangle' or area_shape == 'Rectangle':
                                    data_valid7 = True
                                    rectangle_side_length1 = float(input("Enter first side length:"))
                                    rectangle_side_length2 = float(input("Enter second side length:"))
                                    rectangle_area_result = rectangle_area(rectangle_side_length1,rectangle_side_length2)
                                    print ("Rectangle Area:" + str(rectangle_area_result))
                                    #area of rectangle
                                    
                                if area_shape == 'triangle' or area_shape == 'Triangle':
                                    data_valid7 = True
                                    triangle_base = float(input("Enter triangle base:"))
                                    trianle_height = float(input("Enter triangle height:"))
                                    triangle_area_result = triangle_area(triangle_base,trianle_height)
                                    print ("Triangle Area:" + str(triangle_area_result))
                                    #area of triangle
                                    
                                if area_shape == 'circle' or area_shape == "Circle":
                                    data_valid7 = True
                                    circle_radius = float(input("Enter radius:"))
                                    circle_area_result = circle_area(circle_radius)
                                    print ("Circle Area:" + str(circle_area_result))
                                    #area of circle
                                    
                        if geometry_needs == 'Perimeter' or geometry_needs == 'perimeter':
                            data_valid6 = True
                            
                            data_valid8 = False
                            while not data_valid8:
                            #this loop makes sure the user only chooses from the following shapes 
                                perimeter_shape = input("Would you like to calculate the perimeter of a square, rectangle, triangle or circle:")
                                
                                if perimeter_shape == 'square' or perimeter_shape == 'Square':
                                    data_valid8 = True
                                    square_perimeter_side_length = float(input("Enter side length:"))
                                    square_perimeter_result = square_perimeter(square_perimeter_side_length)
                                    print ("Square Perimeter:" + str(square_perimeter_result))
                                    #perimeter of square
                                
                                if perimeter_shape == 'rectangle' or perimeter_shape == 'Recatngle':
                                    data_valid8 = True
                                    rectangle_side_length1_perimeter = float(input("Enter first side length:"))
                                    rectangle_side_length2_perimeter = float(input("Enter second side length:"))
                                    rectangle_perimeter_result = rectangle_perimeter(rectangle_side_length1_perimeter,rectangle_side_length2_perimeter)
                                    print ("Rectangle Perimeter:" + str(rectangle_perimeter_result))
                                    #perimeter of rectangle
                                    
                                if perimeter_shape == 'triangle' or perimeter_shape == 'Triangle':
                                    data_valid8 = True
                                    triangle_side_length1_perimeter = float(input("Enter first side length:"))
                                    triangle_side_length2_perimeter = float(input("Enter second side length:"))
                                    triangle_side_length3_perimeter = float(input("Enter third side length:"))
                                    triangle_perimeter_result = triangle_perimeter(triangle_side_length1_perimeter,triangle_side_length2_perimeter,triangle_side_length3_perimeter)
                                    print ("Triangle Perimeter:" + str(triangle_perimeter_result))
                                    #perimeter of triangle
                                    
                                    
                                if perimeter_shape == 'circle' or perimeter_shape == 'Circle':
                                    data_valid8 = True
                                    circle_radius_perimeter = float(input("Enter radius:"))
                                    circle_perimeter_result = circle_perimeter(circle_radius_perimeter)
                                    print ("Circle Perimeter:" + str(circle_perimeter_result))
                                    #perimeter of circle
                                    
                if advanf_needs == 'Averages' or advanf_needs == 'averages' or advanf_needs == 'average':
                    data_valid2 = True
                    
                    data_valid9 = False
                    #this loop checks to make sure user entered in mean or mode
                    while not data_valid9:
                        mean_or_mode_or_median = input("Would you like to calculate Mean or Mode or Median:")
                        
                        if mean_or_mode_or_median == 'Mean' or mean_or_mode_or_median == 'mean':
                            data_valid9 = True
                            #the following is used to ask how mnay numbers the user has and asks them to input it into the array
                            #Then the code will print it to them. 
                            mean_array = []
                            n = int(input("How many numbers do you have: "))
                            for i in range(0, n):
                                ele = int(input("Enter the numbers into the array:"))     
                                mean_array.append(ele)
                            print(mean_array)
                            #my_mean is a def funtion in the top on code
                            mean_result = my_mean(mean_array)
                            print ("Your mean: " + str(mean_result))
                            
                        if mean_or_mode_or_median == 'Mode' or mean_or_mode_or_median == 'mode':
                            data_valid9 = True
                            #the following is used to ask how mnay numbers the user has and asks them to input it into the array
                            #Then the code will print it to them. 
                            mode_array = []
                            n = int(input("How many numbers do you have: "))
                            for i in range(0, n):
                                ele = int(input("Enter the numbers into the array:"))     
                                mode_array.append(ele)
                            print(mode_array)
                            #my_mean is a def funtion in the top on code
                            mode_result = mine_mode(mode_array)
                            if mode_result == -1:
                                print ("This array has no mode")
                            else:
                                print ("Your mode: " + str(mode_result))
                                
                        if mean_or_mode_or_median == 'Median' or mean_or_mode_or_median == 'median':
                            data_valid9 = True
                            #the following is used to ask how mnay numbers the user has and asks them to input it into the array
                            #Then the code will print it to them.
                            median_array = []
                            n = int(input("How many numbers do you have: "))
                            for i in range(0, n):
                                ele = int(input("Enter the numbers into the array:"))     
                                median_array.append(ele)
                            print(median_array)
                            median_result = median(median_array)
                            print("Your Median:" + str(median_result))
    
    #checks if the user would like to use the calculator again, if yes then loops back to the top. 
    check_1 = input("Would you like to use the calculator again? Enter Y to reset:")
    if check_1.upper() == 'Y': 
        continue
    print ("Thank you for using my calculator.")
    break
                              
