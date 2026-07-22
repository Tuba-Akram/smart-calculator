def welcome():
    print("Welcome to Smart Calculator!")
def addition(a,b):
    return a + b
def substraction(a,b):
    return a - b
def multiplication(a,b,c):
    return a*b*c
def division(a,b):
    return a /b
def square(number):
    return number**2
def cube(number):
    return number**3
def bigger(a,b,c):
    return max(a,b,c)
def smallest(a,d):
    return min(a,d)
def even_odd(number):
    if number % 2==0:
        print("Even")
    else:
        print("Odd")
def student_grade(marks):
    if marks >=90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    elif marks >= 50:
        return "E"
    else:
        return "FAIL"
welcome()
print(student_grade(90))
print(student_grade(89))
print(substraction(450,100))
print(division(20,2))
print(multiplication(8,2,10))
print(square(40))
print(cube(9))
print(bigger(30,100,70))
print(smallest(4,7))
even_odd(60)