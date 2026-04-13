data = "abc@gmail.com"
userInput = input("Enter your email: ")
#if condition
if data == userInput.lower():
    print("welcome user your email is correct...")
else:
    print("your email is incorrect please try again")
#task if users enters email and by mistake has enters space at last or begining of email it should not show him incorrect email