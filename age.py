# JTSK-350112
# a5_5.py
# Chetan Sharma
# c.sharma@jacobs-university.de


from datetime import date
print("If you want to enter your date of birth in form of dd-mm-yyyy, Select format 1.\n if you want to enter the date in form of yyyy-mm-dd select format 2")
i=int(input("Please select format: "))
if i==1:
    i2=input("Enter the date of birth in the format selected above: ")
    day,month,year=map(int, i2.split('-'))
    print("Your age is:",((date.today()-(date(year,month,day))).days//365),"years")
elif i==2:
    i3=input("Enter the date of birth in the format selected above: ")
    year,month,day=map(int, i3.split('-'))
    print("Your age is:", ((date.today()-(date(year,month,day))).days)//365,"years")
    

