import calendar
m,d,y = map(int,input().split())
b = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
print(b[calendar.weekday(y,m,d)])