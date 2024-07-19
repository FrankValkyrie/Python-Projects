from tkinter import Label, Tk 
import time

app = Tk() 
app.title("Digital Clock") 
app.geometry("420x150") 
app.resizable(1,1)

text_font= ("Boulder", 69, 'bold')
background = "#5BBCFF"
foreground= "#FFFFFF"
border_width = 30

label = Label(app, font=text_font, bg=background, fg=foreground, bd=border_width) 
label.grid(row=0, column=1)

def digital_clock(): 
   time_live = time.strftime("%H:%M:%S")
   label.config(text=time_live) 
   label.after(200, digital_clock)

digital_clock()
app.mainloop()