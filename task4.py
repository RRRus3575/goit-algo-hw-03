from datetime  import datetime, timedelta

users = {
    'vova': '2000-12-09',
    'sergey': '1998-09-30',
    'vasy': '1998-04-23',
    'vasyl': '1999-04-25',
    'sanya': '1999-04-28',
    'kiril': '2000-04-26'
}




def get_upcoming_birthdays(users):
    new_users = {}
    current_date = datetime.today().date()
   
    finish_date = current_date + timedelta(days=7)
    

    for user, birthday in users.items():     
        date = datetime.strptime(birthday, '%Y-%m-%d').date()
        now_year_date = date.replace(year=current_date.year)
        

        if current_date <= now_year_date <= finish_date:
            weekday_number = now_year_date.weekday()
            if weekday_number == 5:
                correct_date = now_year_date + timedelta(days=2)
                print('saturday', correct_date)
                new_users[user] = correct_date

            elif weekday_number == 6:
                correct_date= now_year_date + timedelta(days=1)
                print('sunday', correct_date)
                new_users[user] = correct_date
                
            else:
                new_users[user] = date
    sorted_dates_dict = {key: value for key, value in sorted(new_users.items(), key=lambda item: item[1])}
   
    return sorted_dates_dict


print(get_upcoming_birthdays(users))

