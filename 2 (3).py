import datetime
yesterday = datetime.date.today() - datetime.timedelta(1)
today = datetime.date.today()
tomorrow = datetime.date.today() + datetime.timedelta(1)
print(yesterday)
print(today)
print(tomorrow)