from datetime import date, timedelta

# get today's date
dt = date.today()
# get datetime after 2 weeks
add_dt = dt + timedelta(days=14)
print(add_dt.strftime('%Y %m %d'))


dt = date.today()
for i in range(0, 9):
    dt = dt + timedelta(days=14)
    print(dt)
