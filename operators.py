#arithematic operators + - * / ** % //
x,y = 5,2
z = x + y
print(z)
print(x - y)
print(x * y)
x = x**y
print(x,y,z)
x = 7
y = 2
z = x/y
print(z)
z = x%y
print(z)
z = 5//2
print(z)
print(int(5/2))
print(7/2)
print(7//2)

#comparision operators == >= <= != > <
print(5 == 5)
print(5 == 4)
z = 5 >= 4
print(z)
print( 1 != 0)
print(5 > 5)

#logical operators and or not 
x = 5
y = 4
z = 2
result = x >= y and y >=z
print("printing and condition")
print(result)
print(x > y and y < z)
print(x < y and y > z)
print(x < y and y < z)

#or 
print("or condition...")
print( x > y or y > z)
print( x > y or y < z)
print( x < y or y > z)
print(x < y or y < z)

print("not condition....")
print(not(True))
print(not(x > y))
print(not(x < y))

result = not(x > y and y < z)
print(result)


#bitwise and 
print(5&4)

#assignment operators = += -= *=
x = 5
x = 5*2+4
x = 5
x += 2 # x = x + 2


# += -= *= %= **/ num1 = 10
num = 5
# num = num + 2
num += 2
num -= 2
print(num)

#membership operator
l = [1,2,3,4,5,7]
print (5 in l)
print(6 in l)
name = "aashiq"
print('q' in name)
print('m' not in name)

#identity operoter
a = [1,2,3]
b = a
c = [1,2,3]
print(a,b,c)
print(a is b)
print(a is c)
print( a is not c)


result = 2+4*3
#precidence (), ** , * / // %, + -, comparison oper..., not, and , or, assignment oper
print("precidence......")
result = 4-(2+2)
print(result)
result = 4 - 2**2
print(result)
result = 4*2**2/2 # 4*4/2
print(result)
result = 4+2*2**2/2
print(result)

print(5 + 2 > 5-2 )

print( not(5 > 4 and 5 < 3 or 5<2))