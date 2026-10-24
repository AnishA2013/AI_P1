# Greeting
print("Hello, I am an AI here to ask you some questions!")

# Questions
name = input("What is your name?")
print("Nice to meet you " + name + "!")



mood = input(" How are you feeling? (good/bad/okay) ")
if mood.lower() == "good":
    print(" That is nice to hear!")

elif mood.lower() == "bad":
    print(" I am sorry to hear that. I hope you feel better soon!")

elif mood.lower() == "okay":
    print(" I hope your day gets better!")

else:
    print(" I am not sure how to respond to that, but I hope you have a good day!")



age = int(input("How old are you?"))
if age >= 0 and age <= 12:
    print("You are a child!")
elif age >= 13 and age <= 17:
    print("You are a teenager!")
elif age >= 18 and age <= 64:
    print("You are an adult!")
elif age >= 65:
    print("You are a senior citizen!")


# End Conversation
print("Thank you for answering my questions! Have a great day!")