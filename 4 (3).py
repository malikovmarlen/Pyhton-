import datetime
first=datetime.datetime.now().time()
last=datetime.time(17,20,0)
diff=datetime.timedelta(hours=(first.hour-last.hour),minutes=(first.minute-last.minute),seconds=(first.second-last.second))
print(diff)