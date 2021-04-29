def leap_year(n):

    
    for i in range(2,n):
        if (n % 4) == 0:
            if (n % 400) == 0:
                return True
        return False 
years=[2000, 1994, 1912, 3002, 1700, 1400] 
for i in years:
    if leap_year(i):
        print(i, "is a leap year")
    else:
        print(i, "is not a leap year")




