import datetime

date = datetime.date.today() - datetime.timedelta(days = 1617)
print(date.strftime('%Y-%m-%d %H:%M:%S'))