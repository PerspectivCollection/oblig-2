#Is a yeare leap year? 
def isLeapYear(year):
    if (0 == year % 4):
        if (0 == year % 100):
            if (0 == year % 400):
                return True   
            else: 
                return False
        else: 
            return True
    else:  
        return False 

print(isLeapYear(2000))


