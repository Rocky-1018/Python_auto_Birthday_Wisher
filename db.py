import pandas as pd
def Birthdays(date_day,month_year):
    li=[]
    dbse=pd.read_csv("Birthdays.csv")
    mod_dbbs=dbse.dropna()
    birthdays=mod_dbbs.values
    for i in range(1,len(birthdays)):
        name,date,event=birthdays[i]
        date,month,year=date.split("-")
        if(date_day==int(date) and month_year==int(month)):
            li.append([name,date,month,event])
    return(li)




