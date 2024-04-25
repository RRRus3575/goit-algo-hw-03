from datetime import datetime




def get_days_from_today(date):
    current_data = datetime.today()
    try:    
        date_datetime = datetime.strptime(date, '%Y-%m-%d')    
        different = current_data - date_datetime
        return different.days
    except:
        return 'This is not a valid format'
   
    



print(get_days_from_today('2024-01'))