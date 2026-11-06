#Typecasting = The process of converting a variable from one data type to another 
#              str(), int(), float(), bool()

Name = "Aman Bhagat";
age = 16;
gpa = 8.9;
is_student = True;


#type() is funcations to know the data type are String, Integer, float, boolen
#Eample: print(type(Name)) 
#Output:-<class 'str'>

#Conveting Int to String

age = str(age);
print(age); #Output: 16
print(type(age)); #Output: <class 'str'>

#Conveting float to int

gpa = int(gpa);
print(gpa); #Output:- 8
print(type(gpa)); #Output:- <class 'int'>

#Conveting String  to boolen

# In the Boolen if Any Data type is Empty it return to the False other wise True
Name = bool(Name);
print(age);


