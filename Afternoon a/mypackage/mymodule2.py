def Leapyear(l,U):
    for year in range(l,U+1):
        if year%400==0 or (year%100!=0 and year%4==0):
            print(year,"leapyear")
        else:
            print(year,"non leap year")
            
            

class Myclass:
    '''
       This is leap year file
    '''
    def Leapyear(l,U):
        for year in range(l,U+1):
            if year%400==0 or (year%100!=0 and year%4==0):
                 print(year,"leapyear")
            else:
                 print(year,"non leap year")
            
                
        
        
            