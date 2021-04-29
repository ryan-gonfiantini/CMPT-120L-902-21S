def leap_year(year):
    """
    - Add code in the defined function to figure out whether or not the given year is a leap year or not. 
    
    - Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100, but these centurial years are leap years if they are exactly divisible by 400. For example, the years 1700, 1800, and 1900 are not leap years, but the years 1600 and 2000 are. - Wikipedia
    
    - Take in a parameter called year and return “Is a leap year” or “Not a leap year”
    """
    # Write your code here. 


num = int(input("enter a year: ")) 
if (num % 4) == 0:
   if (num % 100) == 0:
       if (num % 400) == 0:
           print("{0} is a leap year".format(num))
       else:
           print("{0} is not a leap year".format(num))
   else:
       print("{0} is a leap year".format(num))
else:
   print("{0} is not a leap year".format(num)) 