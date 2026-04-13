s = "helLo worlD welocome To our class. apple"
#captalize
print(s.capitalize())
print(s)
s = s.capitalize()
print(s)
s = 'hello usEr hoW are YoU'
print(s.title())
print(s.upper())
print(s.lower())
s = "HellO World"
print(s.istitle())
print(s.center(15,"*"))
s = "hello my name is ashiq, ashiq  live in south kashmir, ashiq is an HR"
# s.count(str,start,stop)
print(s.count("ashiq",-30,-1))
s = "hello HR how are you, Hey Hr how are you doing , thankyou hR, good hr asjfsdjhr"
print("No. of time HR comes in stirng is ",s.upper().count(" HR "))
s = "hello world"
print(s.endswith("ello world"))
print(s.startswith("hello"))
img = "ashiq.pdf"
print(img.endswith("png") or img.endswith("jpeg"))

s = "Hello world how are you today are you ok  are you guys ok"
print(s.find("are"))
print(s.rfind("are"))
print(s.count("are"))
print(s.find("are",17))

print("using find ",s.find("ashiq"))
# print("using index ",s.index("ashiq")) #will generate error if not found

print("end of program for today")

s = "hELLO wORLD THANK YOU"
print(s.swapcase())
print(s)
print(s.upper().isupper())# "HELLO WORLD ...".isuper()
#replace...
s = 'hello world'
s = s.replace("world","aashiq")
print(s)
s = "........hello world......"
print(s)
print(s.strip("."))
print(s.rstrip("."))
#split
s = "hello world how are you"
print(s.split(" "))
s = 'hello world'
print(s.partition(" "))
s = "hello world how are you"
print(s.split("world"))
print(s.partition("world"))
print(s.partition(" "))
print(s.rpartition(" "))

s1 = "hello "
s2 = "world"
print(s1+s2)#concatanation
print(s1*3)
s = "hello world how are you today are ...r"
print("good" in s)
print("cat" not in s)
print("length of string is ",len(s))
print(len("hello"))
print(s[len(s) - 1])
s1 = "abc@gmail.com"
s2 = "Abc@gmail.com"
print(s1.lower() == s2.lower())