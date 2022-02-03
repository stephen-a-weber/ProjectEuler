import calendar
import datetime

 
 
f=datetime.date(1901,1,1)
 
 
sundays=0
while True:
  f=f+datetime.timedelta(days=1)
  if f.year==2001:
      break
  
  if f.day==1 and f.weekday()==6:
      sundays+=1
   
print sundays

  
