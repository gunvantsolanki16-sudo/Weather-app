from tkinter import*
from tkinter import  ttk
import requests
import os


def data_get():
    
    city = city_name.get()
    url = f"https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=e0eaee1a84b8d75f5c3c52dbeab6148f"
    response = requests.get(url)
    data = response.json()
    w1_label1.config(text=data["weather"][0]["main"])
    w2_label1.config(text=data["weather"][0]["description"].capitalize())
    # The API uis returning in kelvin so i converted it into degree celcius.
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)) + " °C")
    pre_label1.config(text=str(data["main"]["pressure"])+ " hPa") 


win = Tk()
win.title("Weather app by Gunvant 🌥️ ")
win.config(bg = "lightblue")
win.geometry("500x570")


name_label = Label(win,text="Weather App",
                   font=("Time New Roman",35,"bold"))
name_label.place(x=25,y=50,height=50,width=450)


city_name = StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand",
             "Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu",
             "Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu",
             "Lakshadweep","National Capital Territory of Delhi","Puducherry"]
combo_box = ttk.Combobox(win,text="Weather App",values=list_name,
                   font=("Time New Roman",20,"bold"),textvariable=city_name)
combo_box.place(x=25,y=120,height=50,width=450)


w1_label = Label(win,text="Weather Climate",          # this is  my 1st label
                   font=("Time New Roman",20))
w1_label.place(x=25,y=260,height=50,width=210)
w1_label1 = Label(win,text="",          # this is  my 1st label second box
                   font=("Time New Roman",20))
w1_label1.place(x=250,y=260,height=50,width=210)


w2_label = Label(win,text="Weather Description",          # this is  my 2nd label
                   font=("Time New Roman",17))
w2_label.place(x=25,y=330,height=50,width=210)
w2_label1 = Label(win,text="",          # this is  my 2nd label second box
                   font=("Time New Roman",17))
w2_label1.place(x=250,y=330,height=50,width=210)


temp_label = Label(win,text="Temperature",          # this is  my 3rd label
                   font=("Time New Roman",20))
temp_label.place(x=25,y=400,height=50,width=210)
temp_label1 = Label(win,text="",          # this is  my 3rd label second box
                   font=("Time New Roman",20))
temp_label1.place(x=250,y=400,height=50,width=210)


pre_label = Label(win,text="Pressure",          # this is  my 4th label
                   font=("Time New Roman",20))
pre_label.place(x=25,y=470,height=50,width=210)
pre_label1 = Label(win,text="",          # this is  my 4th label second box
                   font=("Time New Roman",20))
pre_label1.place(x=250,y=470,height=50,width=210)


done_button = Button(win,text="Done",
                   font=("Time New Roman",20,"bold"),command=data_get)
done_button.place(y=190,height=50,width=100,x=200)


win.mainloop()