############### TODO
# write func description


from datetime import date    
    

def get_todays_date():
    
    todays_date = str(date.today())
    
    current_day = todays_date.split('-')[2]
    current_month= todays_date.split('-')[1]
    current_year= todays_date.split('-')[0]
    
    return current_day, current_month, current_year