#1
def number_of_food_groups():
    return 5
print(number_of_food_groups()) #Returns 5, no argument was expressed, and 5 is he only thing being returned. 


#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches()) #Will cause an error, the first function is not defined, so it can't be called.


#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold()) #Return ends the function, so 10 will not be ran.


#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers()) #The return is simply 5, the return statement will end the function 


#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()  
return (x)   #The function is called, so 5 is printed, return ends a function, so x is returned without running


#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3)) #the arguments are both string and cannot be added, answer is 2, 3. 


#7
def concatenate(b,c): #function and parameters
    return str(b)+str(c)  #when function is ran, reurn the strings defined as b + c
print(concatenate(2,5)) #2 and 5 are both returned, they appear together as 25


#8
def number_of_oceans_or_fingers_or_continents(): #function and parameter
    b = 100  #var b = 100
    print(b) #b is printed
    if b < 10: #if loop, b is less than 10
        return 5 #B is 100, so this is ignored
    else: 
        return 10 #Since B is ignored, return 10 and end function
    return 7
print(number_of_oceans_or_fingers_or_continents()) #100 10 is the answer


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c: #(2,3), first argument goes through
        return 7 #first argument returns 7 and ends the function
    else: #the second argument applies here  b(5) is greater than c(3)
        return 14 #2nd arguement is returned, function ended 
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3)) 
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
#third print calls the function twice, each with it's own argument, 7 + 14 is returned and the answer is 21

#10
def addition(b,c):
    return b+c 
    return 10
print(addition(3,5)) #return (b)3+(c)5 =8


#11
b = 500 #variabe b = 500
print(b) #500 is printed 
def foobar(): #a function and parameter are given
    b = 300 #b inside function = 300
    print(b) #within the function, b is printed. b = 300
print(b) #500 is printed
foobar() #foobar is called, printing 300
print(b) #500 is printed
#Final answer will be 500 500 300 500. 300 is only printed when the function is called. 


#12
b = 500 #b is defined
print(b) #500 is printed
def foobar(): #function and parameter given 
    b = 300 #within function, b = 300
    print(b) #300 is printed
    return b #the value 300 is returned to foobar
print(b) #500 is printed 
foobar() #300 is returned to foobar
print(b) #500 is printed 
#Similar to the last question, the value of b is only different inside of the function 


#13
b = 500 #b is equel to 500
print(b) #500 is printed 
def foobar(): #foobar the function and the paramter is set
    b = 300 #b = 300
    print(b) #300 is printed 
    return b #the value of 300 is returned. 
print(b) #500 is printed 
b=foobar() #b is now equal to foobar, and is called. 300is returned 
print(b) #b is now equal to foobar, 300 is retrned  


#14
def foo(): #function foo() <- parameter
    print(1) #1 is printed 
    bar() #regardless of placement, bar is called, so 3 is printed
    print(2) #2 is printed 
def bar():
    print(3)
foo() #1 3 2 is the answer. bar is defined after foo, but that doesn't matter and it is called in foo's function 


#15
def foo():
    print(1) #1 is printed 
    x = bar() #x is defined as the function bar
    print(x) #x is printed. x = bar(), so 3 is printed and 5 is returned, ending that function
    return 10 #10 is returned 
def bar():
    print(3)
    return 5
y = foo()
print(y)
#1 3 5 10