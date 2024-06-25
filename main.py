import requests as rq
import tkinter as tk
def search():
    city=entry.get()
    api_key="810200664952a46c60505d4f394f411d"
    base_url="https://api.openweathermap.org/data/2.5/weather?"
    url=base_url+"appid="+api_key+"&q="+city+"&units=metric"
    response=rq.get(url).json()
    print(response)
    
    if response['cod']==200:
        var=response['weather'][0]['main']
        temp=response['main']['temp']
        des=response['weather'][0]['description']
        tk.Label(window,text=f"{var}",font=12).pack()
        tk.Label(window,text=f"{des}",font=12).pack()
        tk.Label(window,text=f"{temp}°C",font=("poppins",25,"bold")).pack()
    else:
        tk.Label(window,text=f"not found!",font=15,bg="white").pack()

def humidity():
    city=entry.get()
    api_key="810200664952a46c60505d4f394f411d"
    base_url="https://api.openweathermap.org/data/2.5/weather?"
    url=base_url+"appid="+api_key+"&q="+city+"&units=metric"
    response=rq.get(url).json()
    print(response)
    
    if response['cod']==200:
        humidity=response['main']['humidity']
        visibility=response['visibility']
        tk.Label(window,text=f"humidity:{humidity}\n visibility:{visibility}",font=14).pack()
    else:
        tk.Label(window,text=f"not found!",font=15,bg="white").pack()
def wind():
    city=entry.get()
    api_key="810200664952a46c60505d4f394f411d"
    base_url="https://api.openweathermap.org/data/2.5/weather?"
    url=base_url+"appid="+api_key+"&q="+city+"&units=metric"
    response=rq.get(url).json() 
    print(response)
    if response['cod']==200:
        wind_speed=response['wind']['speed']
        deg=response['wind']['deg']
        
        tk.Label(window,text=f"wind speeds:{wind_speed} m/s \n {deg} degrees",font=15).pack()
    else:
        tk.Label(window,text=f"not found!",font=15,bg="white").pack()

    
def weather():
    city=entry.get()
    api_key="810200664952a46c60505d4f394f411d"
    base_url="https://api.openweathermap.org/data/2.5/weather?"
    url=base_url+"appid="+api_key+"&q="+city+"&units=metric"
    response=rq.get(url).json()
    
    
    print(response)
    if response['cod']==200:
        temp=response['main']['temp']
        feels=response['main']['feels_like']
        max_temp=response['main']['temp_max']
        min_temp=response['main']['temp_min']
        tk.Label(window,text=f"temperature of {city}:{temp}°C\n feels like:{feels}°C\n temp_max:{max_temp}°C\n temp_min:{min_temp}°C",font=15,bg="white").pack()
    else:
        tk.Label(window,text=f"not found!",font=15,bg="white").pack()



            

window=tk.Tk()
window.title("know weather")
window.geometry("700x500")






# window.resizable(False,False)
#black border
title=tk.Label(window,text="The Weather App",font=("Helvetica",20),bg="black",fg='white',width=500,height=2,anchor="se").pack()
title=tk.Label(window,bg="black",fg='white',height=500,width=20).pack(side="left")






#search
l1=tk.Label(window,text="City:",font=50).pack()
search_image=tk.PhotoImage(file="Copy of search.png")
l2=tk.Label(window,image=search_image).pack()
entry=tk.Entry(window,font=("poppins",25,"bold"),bg="#404040",border=0,fg='white')
entry.place(x=225,y=115)
entry.focus()
s_image=tk.PhotoImage(file="copy of search_icon.png")
search_btn=tk.Button(window,image=s_image,borderwidth=0,cursor="hand2",bg="#404040",command=search)
search_btn.place(x=560,y=113)
#icon

icon=tk.PhotoImage(file="copy of logo.png")
icon_image=tk.Label(image=icon)
icon_image.place(x=145,y=200)





#buttons
btn_1=tk.Button(window,text="weather",width=19,command=weather)
btn_1.place(x=0,y=100)
btn_2=tk.Button(window,text="winds",width=19,command=wind)
btn_2.place(x=0,y=200)
btn_3=tk.Button(window,text="humidity",width=19,command=humidity)
btn_3.place(x=0,y=300)





window.mainloop()













