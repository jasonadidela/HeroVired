# write a program idf a user is eligible to enter our class or not. UserId should be in between 5 to 10

print("Enter your User Name")

var = int(input("User Name: "))

# if (5<=var >= 10):

#     print ("User is valid")

# else:

#     print ("user is invalid")

eligible = "eligible" if 5<=var<10 else "not eligible"

print(eligible)
