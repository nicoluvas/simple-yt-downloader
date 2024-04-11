import tkinter 
import customtkinter
from pytube import YouTube

#functions
def download():
    try:
        url = url_var.get()
        ytobj = YouTube(url)
        vid = ytobj.streams.get_highest_resolution().download()
    except Exception as e:
        print("error: ", e)

#system settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

#frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("youtube picker")

#elements
title = customtkinter.CTkLabel(app, text="insert a yt link")
title.pack(padx=10, pady=10)

#input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, placeholder_text="right here", textvariable=url_var)
link.pack(padx=10, pady=10)

#button
btn = customtkinter.CTkButton(app, text="submit", command=download)
btn.pack(padx=10, pady=10)



#runapp function
app.mainloop();