# Logical operators = evaluate multiple conditions (or , and , not)
#                     or = at least one condition must be True
#                     and  = both condations must be True
#                     not = inverts the condition (not False,not True )


# temp = 20
# is_raining = False

# if temp > 35 or temp < 0 or is_raining:
#     print("The outdoor event is cancelled")
# else:
#     print("The outdoor event is still scheduled")


temp = 20
is_sunny = True

if temp >=28 and is_sunny:
    print("it is Hot outside")
elif temp <=0 and is_sunny:
    print("It is Cold OutSide")
elif temp <= 28 and temp > 0 and is_sunny:
    print("It is Warm OutSide")