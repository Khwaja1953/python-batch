#elif
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible for driving manual car....")
elif age >= 16:
    print("You are eligible for driving automatic car...")
elif age >=10:
    print("You are eligible for driving cycle....s")
else:
    print("You are not eligible for driving....")

x = False
if x == True:
    print("Hello world....")
    print("Ok world")
print("Bye world")

#nested condition using only if else
age = int(input("Enter your new age: "))
if age >=18:
    print("You are eligible for driving manual car....")
else:
    if age >= 16:
        print("You are eligible for driving automatic car...")
    else:
        if age >= 10:
            print("You are eligible for driving cycle....s")
        else:
            print("You are not eligible for driving....")

#task: using if else check even odd number
num = int(input("Enter a number: "))
if num%2 == 0:
    print("This is even number")
else:
    print("This is odd number")