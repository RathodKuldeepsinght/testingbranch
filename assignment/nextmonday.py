from datetime import datetime,timedelta

today=datetime.today()

# weeekdays(): Monday =0, sunday =6
days_ahead = 0 - today.weekday()+7

# if today is monday,go to  next monday 
if days_ahead ==0:
    days_ahead=7

next_monday=today + timedelta(days=days_ahead)
print("next monday is on : ", next_monday.strftime("%y-%m-%d"))
