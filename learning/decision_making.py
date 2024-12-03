
########################################decision making in python#####################################



# Decision Making Practice #1
# Using the variables num1 and num2, which are fed with user input (just like in the provided code), create a flow control structure that compares the values of the variables, and returns a result according to the case:

# "num1 is greater than num2"

# "num2 is greater than num1"

# "num1 and num2 are equal"

# You must display the value of the user input instead of num1 and num2.
# num1 = input("Enter a number:")
# num2 = input("Enter another number:")

# f"{num1} is greater than {num2}"
# "num2 is greater than num1"
# "num1 and num2 are equal"

print ("Hello!")
num_1 = input ("Type in a number ")
num_2= input ("Type another number ")

if num_1 == num_2:
    print ("They are equal numbers")

if num_1 > num_2:
    print (f"{num_1} is greater than {num_2}")
else:
    print (f"{num_2} is greater than {num_1}")

# Decision Making Practice #2
# The laws of a certain country establish that an adult can drive if they are of legal age (18 years or older), and have a driver's license.

# Create a conditional structure to check if a 16-year-old without a license can drive, and display the corresponding result on the screen:

# "You can drive"

# "You can't drive yet. You must be 18 years old and have a license"

# "You can't drive. You need to have a license"

# Use the code base already provided to set up the appropriate flow control structure and check those conditions.
age = 16
has_license = False

if age==18 and has_license:
    print("you can drive")
elif age< 18 or has_license:
    print("you can't drive yet. you must be 18 years old and have a license")
else:
    print("you can't drive. you need to have a license")

# "You can drive"

# "You can't drive yet. You must be 18 years old and have a license"

# "You can't drive. You need to have a license"

# Decision Making Practice #3
# To access a certain job, the candidate must be able to program in Python and speak French.

# Create a conditional structure to evaluate a candidate given these conditions, and display the corresponding message on the screen:

# "You meet the requirements to apply"

# "To apply, you need to know how to program in Python and speak French"

# "To apply, you need to speak French"

# "To apply, you need to know how to program in Python"

# Use the code already provided to set up the appropriate flow control structure and check those conditions. Evaluate a candidate who knows French, but does not know how to program in Python.


speak_french = True
knows_python = False

print ("Fill out the application requirements")
basic_french = input ("Can you speak French? Only answer True or False.")
python = input ("Do you know how to program in Python? Answer True or False.")
if python== "True" and basic_french == "True":



"You meet the requirements to apply"

"To apply, you need to know how to program in Python and speak French"

"To apply, you need to speak French"

"To apply, you need to know how to program in Python"



# Decision Making Practice #4
# Enter your name
name = input("what is your name?:")
print(name)
# Enter your relatives name
rel_name= input("enter the name of a relative:")
print(rel_name)
# Enter your age
age= int (input ("how old are you?:"))
print(age)

# If age is less than 20 print i am young
if age < 20:
    print("i am young")
else:
    print("not young")
# If age is less than 30 then print iam vicenarian
if age < 30:
    print("i am a vicenarian")
else:
    print("not a vicenarian")
# If age is less than 40 then print i am a tricenarian
if age < 40:
    print("i am a tricenarian")
else:
    print("not a tricenarian")
# If age is less than 50 then print I am quadragenarian
if age < 50:
    print("i am a quadragenarian")
else:
    print("not a quadragenarian")

    
# Decision Making Practice #5
# ask the user for their age
# if the user's  is between 18 - 21 , print they can vote, other wise print better luck next time.


#######################decision making challenge#####################
# Challenge: Determine if a user is eligible to vote, drink, or retire based on their age.
# The program prompts the user for their age and outputs their eligibility.

# Prompt the user for age


# Check conditions for voting, drinking, and retirement