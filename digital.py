from tkinter import *
import datetime

def date_time():
    timenow = datetime.datetime.now()
    now_hour = timenow.strftime('%I')
    now_minute = timenow.strftime('%M')
    now_second = timenow.strftime('%S')
    now_ampm = timenow.strftime('%p')
    now_date = timenow.strftime('%d')
    now_month = timenow.strftime('%B')
    now_year = timenow.strftime('%Y')
    now_day = timenow.strftime('%A')

    lab_hr.config(text = now_hour)
    lab_min.config(text = now_minute)
    lab_sec.config(text = now_second)
    lab_ampm.config(text = now_ampm)
    lab_date.config(text = now_date)
    lab_mon.config(text= now_month)
    lab_year.config(text = now_year)
    lab_day.config(text = now_day)

    lab_hr.after(200,date_time)

clock = Tk() # Create object of Tk class
clock.title('Digital Clock')
clock.geometry('1000x500') #This is the width and height of window
clock.config(bg='#9CDBD7')

#Create a label for Hour
lab_hr = Label(clock, text="00", font=("Times New Roman", 60,"bold"), bg='#4768B0', fg="white")
lab_hr.place(x=120, y=50, height=100, width=100)
lab_hr_txt = Label(clock, text="Hour", font=("Times New Roman", 30,"underline"), bg='#4768B0', fg="white")
lab_hr_txt.place(x=120, y=170, height=40, width=100)


#Create a label for Minute
lab_min = Label(clock, text="00", font=("Times New Roman", 60,"bold"), bg='#4768B0', fg="white")
lab_min.place(x=340, y=50, height=100, width=100)
lab_min_txt = Label(clock, text="Min.", font=("Times New Roman", 30,"underline"), bg='#4768B0', fg="white")
lab_min_txt.place(x=340, y=170, height=40, width=100)


#Create a label for Second
lab_sec = Label(clock, text="00", font=("Times New Roman", 60,"bold"), bg='#4768B0', fg="white")
lab_sec.place(x=560, y=50, height=100, width=100)
lab_sec_txt = Label(clock, text="Sec.", font=("Times New Roman", 30,"underline"), bg='#4768B0', fg="white")
lab_sec_txt.place(x=560, y=170, height=40, width=100)


#Create a label for AM/PM
lab_ampm = Label(clock, text="00", font=("Times New Roman", 60,"bold"), bg='#4768B0', fg="white")
lab_ampm.place(x=780, y=50, height=100, width=100)
lab_ampm_txt = Label(clock, text="AM/PM", font=("Times New Roman", 20,"underline"), bg='#4768B0', fg="white")
lab_ampm_txt.place(x=780, y=170, height=40, width=100)


lab_line = Label(clock, text="-----------------------------------------------------------------------------------------------------------------", font=("Times New Roman", 20,"bold"), bg='#9CDBD7', fg="#4768B0")
lab_line.place(x=20, y=230, height=10, width=950)


#************** Create Date, Month Year and Day Data

#Create a label for Date
lab_date = Label(clock, text="00", font=("Times New Roman", 50,"bold"), bg='#4768B0', fg="white")
lab_date.place(x=120, y=280, height=100, width=100)
lab_date_txt = Label(clock, text="Date", font=("Times New Roman", 25,"underline"), bg='#4768B0', fg="white")
lab_date_txt.place(x=120, y=400, height=40, width=100)


#Create a label for Month
lab_mon = Label(clock, text="00", font=("Times New Roman", 20,"bold"), bg='#4768B0', fg="white")
lab_mon.place(x=340, y=280, height=100, width=100)
lab_mon_txt = Label(clock, text="Month", font=("Times New Roman", 25,"underline"), bg='#4768B0', fg="white")
lab_mon_txt.place(x=340, y=400, height=40, width=100)


#Create a label for Year
lab_year = Label(clock, text="00", font=("Times New Roman", 30,"bold"), bg='#4768B0', fg="white")
lab_year.place(x=560, y=280, height=100, width=100)
lab_year_txt = Label(clock, text="Year", font=("Times New Roman", 25,"underline"), bg='#4768B0', fg="white")
lab_year_txt.place(x=560, y=400, height=40, width=100)


#Create a label for Day
lab_day = Label(clock, text="00", font=("Times New Roman", 20,"bold"), bg='#4768B0', fg="white")
lab_day.place(x=780, y=280, height=100, width=100)
lab_day_txt = Label(clock, text="Day", font=("Times New Roman", 25,"underline"), bg='#4768B0', fg="white")
lab_day_txt.place(x=780, y=400, height=40, width=100)





date_time()
clock.mainloop()