
from datetime import date    
    

def get_todays_date():
    
    ###################
    #
    # This function gets today's current day and month values for later use in
    # the program.
    #
    ###################
    
    todays_date = str(date.today())
    
    current_day = todays_date.split('-')[2]
    current_month= todays_date.split('-')[1]
    
    return current_day, current_month