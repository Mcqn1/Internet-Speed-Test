from tkinter import *
import speedtest
import speedtest as speedtest 
def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download()/(10**6),3)) + "Mbps" 
    up = str(round(sp.upload()/(10**6),3)) + "Mbps"
    l_down.config(text=down)
    l_up.config(text=up)
    
sp=Tk()
sp.title(" Internet Speed Test")
sp.geometry("700x700")
sp.config(bg="Blue")
l= Label(sp,text="Internet Speed Test", font=("Time New Roman",30,"bold"),bg="blue",fg="White")
l.place(x=60,y=30,width=580,height=50)
l= Label(sp,text="Download Speed", font=("Time New Roman",30,"bold"),bg="blue",fg="white")
l.place(x=90,y=130,width=500,height=50)
l_down= Label(sp,text="00", font=("Time New Roman",30,"bold"),bg="blue",fg="white")
l_down.place(x=60,y=230,width=580,height=50) 
l= Label(sp,text="Upload Speed", font=("Time New Roman",30,"bold"),bg="blue",fg="white")
l.place(x=60,y=330,width=580,height=50) 
l_up= Label(sp,text="00", font=("Time New Roman",30,"bold"),bg="blue",fg="white")
l_up.place(x=60,y=430,width=580,height=50) 
 
Button = Button(sp,text="Check Speed",font=("Time New Roman",30,"bold"),relief=RAISED,bg="Red",command=speedcheck)
Button.place(x=60,y=630,width=580,height=50)






sp.mainloop()