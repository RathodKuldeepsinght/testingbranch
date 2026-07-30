from datetime import datetime

# define deadline
deadline=datetime(2026,12,31)

# todays date
today=datetime.today()

# Calaculate diffrence
remaining_days=(deadline - today).days

print("Days left until deadline: ",remaining_days)