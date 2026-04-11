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
