import smtp
import db
import datetime as dt
today=dt.datetime.now()
t_d=today.day
t_m=today.month
if(db.Birthdays(t_d,t_m)!=[]):
    for i in range(len(db.Birthdays(t_d,t_m))):
        smtp.mail("happy"+str(db.Birthdays(t_d,t_m)[i][3])+str(db.Birthdays(t_d,t_m)[i][0]),"many more happy return of the day ")

else:
    print("no events today")





