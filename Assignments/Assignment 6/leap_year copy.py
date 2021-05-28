
years = int(input("enter a year: ")) 
if (years % 4) == 0:
   if (years % 100) == 0:
       if (years % 400) == 0:
           print("{0} is a leap year".format(years))
       else:
           print("{0} is not a leap year".format(years))
   else:
       print("{0} is a leap year".format(years))
else:
   print("{0} is not a leap year".format(years)) 
