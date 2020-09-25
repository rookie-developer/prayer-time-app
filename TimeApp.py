import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
import requests


#this is where i send the http requests and retrieve the data from https://api.aladhan.com/v1/calendarByCity

def format_response1(times):
    timings = times['data'][0]['timings']
    return timings['Fajr']

def format_response2(times):
    timings = times['data'][0]['timings']
    return timings['Sunrise']

def format_response3(times):
    timings = times['data'][0]['timings']
    return timings['Dhuhr']

def format_response4(times):
    timings = times['data'][0]['timings']
    return timings['Asr']

def format_response5(times):
    timings = times['data'][0]['timings']
    return timings['Maghrib']

def format_response6(times):
    timings = times['data'][0]['timings']
    return timings['Isha']


def get_city(city):
    payload = {'city':city , 'country':'algeria' , 'method':3 , 'month':8 , 'year':2020 }
    x = requests.get('https://api.aladhan.com/v1/calendarByCity',params = payload)
    times = x.json()

    label11['text'] = format_response1(times)
    label12['text'] = format_response2(times)
    label13['text'] = format_response3(times)
    label14['text'] = format_response4(times)
    label15['text'] = format_response5(times)
    label16['text'] = format_response6(times)



root = tk.Tk()

##this is the geometry of the window
root.geometry("1280x780")

#root.configure(bg='#FFD77D')

#this is where the background image was put
background_image = ImageTk.PhotoImage(Image.open('ramadan.png'))
background_label = tk.Label(root,image=background_image)
background_label.place(relwidth='1',relheight='1',x=0,y=0)

#this is the cuntainer for the button (emplacement)
#canvas = tk.Canvas(root,height=HEIGHT,width=WIDTH,bg='#FFD77D')
#canvas.pack()

##color a part of the window
#frame = tk.Frame(root,bg="#FFD77D")
#frame.place(width="1600",height="500")

frame=tk.Frame(root,bg="black")
frame.place(relwidth="0.6",relheight="0.2",relx="0.2",rely="0.35")

label11=tk.Label(root,bg="white",font=('Centry',23),anchor=W)
label11.place(relwidth="0.07",relheight="0.1",relx="0.7",rely="0.45")

label12=tk.Label(root,bg="white",font=('Centry',23),anchor=W)
label12.place(relwidth="0.07",relheight="0.1",relx="0.6",rely="0.45")

label13=tk.Label(root,bg="white",font=('Centry',23),anchor=W)
label13.place(relwidth="0.07",relheight="0.1",relx="0.5",rely="0.45")

label14=tk.Label(root,bg="white",font=('Centry',23),anchor=W)
label14.place(relwidth="0.07",relheight="0.1",relx="0.4",rely="0.45")

label15=tk.Label(root,bg="white",font=('Centry',23),anchor=W)
label15.place(relwidth="0.07",relheight="0.1",relx="0.3",rely="0.45")

label16=tk.Label(root,bg="white",font=('Centry',23),anchor=W)
label16.place(relwidth="0.07",relheight="0.1",relx="0.2",rely="0.45")

#making a label

labelx = tk.Label(root,text="ادخل منطقتك",bg='#FFD77D')
labelx.pack()

#making a barre for you to type in
entry = tk.Entry(root,font='450')
entry.pack()


#this is for the buttons
button = tk.Button(root,text="الحصول على المواقيت",bg="green",fg="yellow",height='3',command=lambda: get_city(entry.get()))#,command=lambda: get_weather(entry.get()))
button.pack()


label1 = tk.Label(root,text="الفجر",relief=SUNKEN,bg="green",fg="yellow")
label1.place(relwidth="0.07",relheight="0.1",relx="0.7",rely="0.35")

label2 = tk.Label(root,text="الصبح",relief=SUNKEN,bg="green",fg="yellow")
label2.place(relwidth="0.07",relheight="0.1",relx="0.6",rely="0.35")

label3 = tk.Label(root,text="الظهر",relief=SUNKEN,bg="green",fg="yellow")
label3.place(relwidth="0.07",relheight="0.1",relx="0.5",rely="0.35")

label4 = tk.Label(root,text="العصر",relief=SUNKEN,bg="green",fg="yellow")
label4.place(relwidth="0.07",relheight="0.1",relx="0.4",rely="0.35")

label5 = tk.Label(root,text="المغرب",relief=SUNKEN,bg="green",fg="yellow")
label5.place(relwidth="0.07",relheight="0.1",relx="0.3",rely="0.35")

label6 = tk.Label(root,text="العشاء",relief=SUNKEN,bg="green",fg="yellow")
label6.place(relwidth="0.07",relheight="0.1",relx="0.2",rely="0.35")

label7 = tk.Label(root,text="المواقيت",relief=SUNKEN,bg="green",fg="yellow")
label7.place(relwidth="0.07",relheight="0.1",relx="0.77",rely="0.45")

#this is the main loop of the programme
root.mainloop()
