from datetime import datetime 

# take input from user
birthdate_str=input("Enter your birthdate (YYYY-MM-DD)")

# convert String to date
birthdate=datetime.strptime(birthdate_str,"%Y-%m-%d")

#get todays date
today=datetime.today()

# calcluate age
age=today.year -birthdate.year

# Adjust if birthday hast occured yet this year
if(today.month,today.day) < (birthdate.month,birthdate.day):
    age -=1 

print("your age is: ",age ,"years")
    