#Variable = A Container for a value (string, integer, float, boolean)
#           A Variable behaves as if it was the value it contains

#Strings
first_name = "Aman Bhagat";
Email = "amanbhagat.webcorevision@gmail.com";

print(first_name)
# Output: Aman Bhagat
print("first_name")
# Output: first_name

#f-string: Formatted string literals
print(f"Your Name is:- {first_name}");
#Output:- Your Name is:- Aman Bhagat
print(f"Your Email is: - {Email}");
#Output:- Your Email is: - amanbhagat.webcorevision@gmail.com

#------------------------------------------------------------------------------------------------------

#Integer

age = 16;
std = 11;
num_of_students = 120;

print(f"You age {age} Years ols.");
#Output:- You age 16 Years ols
print(f"You are Studing in {std}th class.");
#Output:- You are Studing in 11th class.
print(f"Number of Students In your class is {num_of_students}.");
#Output:- Number of Students In your class is {num_of_students}.

#-------------------------------------------------------------------------------------------------------

#Float

price = 10.99;
gpa = 8.9;
distance = 5.5;

print(f"The price is: ${price}.");
#Output:- The price is $10.99.
print(f"Your GPA is: {gpa}.");
#Output:- Your GPA is: 8.9.
print(f"You ran {distance}km.");
#Output:- You ran 5.5Km.

#--------------------------------------------------------------------------------------------------------

#boolean

is_student = True;

print(f"Are you Student?: {is_student}");