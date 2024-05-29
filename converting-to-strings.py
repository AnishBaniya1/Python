#Converting to Strings
myNumber=5
print(type(myNumber))
myNumberAsString=str(myNumber)
print(type(myNumberAsString))

from datetime import date
myDate=date.today()
myDateAsString=str(myDate)
print("Today Date:" + myDateAsString)

myDateAsString=str(date.today())
print("Today Date:" + myDateAsString)

myDate=date.today()
print("Today date:" ,(myDate))# if+ use then str is must otherwise just use, for printing

print("Today date:" + str(date.today()))

print("Today date:", date.today())
