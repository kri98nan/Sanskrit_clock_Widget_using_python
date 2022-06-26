import tkinter as tk
import math
import time
import datetime
from PIL import ImageTk,Image

class Win(tk.Tk):
    def __init__(self):
        super().__init__()
        super().overrideredirect(True)
        self._offsetx = 0
        self._offsety = 0
        super().bind("<Button-1>" ,self.clickwin)
        super().bind("<B1-Motion>", self.dragwin)

    def dragwin(self,event):
        x = super().winfo_pointerx() - self._offsetx
        y = super().winfo_pointery() - self._offsety
        super().geometry(f"+{x}+{y}")

    def clickwin(self,event):
        self._offsetx = super().winfo_pointerx() - super().winfo_rootx()
        self._offsety = super().winfo_pointery() - super().winfo_rooty()



root = Win()
width,height=400,400 # set the variables 
c_width,c_height=width,height # canvas width height
d=str(width)+"x"+str(height)
root.geometry(d)
root.attributes('-alpha', 0.83)
c1 = tk.Canvas(root, width=c_width, height=c_height,bg='gray25')    
c1.place(x=0,y=0)
c1.delete('all')
x,y=200,200 # center 
x1,y1,x2,y2=x,y,x,10 # second needle 
r1=140 # dial lines for one minute 
r3 = 170
r4 = 100
in_degree = 0

verses = ["अहम् ब्रह्मास्मि","वसुंधैव कुटुम्वकम्","धर्मो रक्षति रक्षितः","यतो धर्मस्ततो जयः","योगश्चित्तवृत्तिनिरोधः","यत भावो-तत भवति","मा त्यज"]

h=iter(['१२','१','२','३','४','५','६','७','८','९','१॰','११'])
m=iter(['६॰','१','२','३','४','५','६','७','८','९','१॰',
        '११','१२','१३','१४','१५','१६','१७','१८','१९','२॰',
        '२१','२२','२३','२४','२५','२६','२७','२८','२९','३॰',
        '३१','३२','३३','३४','३५','३६','३७','३८','३९','४॰',
        '४१','४२','४३','४४','४५','४६','४७','४८','४९','५॰',
        '५१','५२','५३','५४','५५','५६','५७','५८','५९'])
s=iter(['६॰','१','२','३','४','५','६','७','८','९','१॰',
        '११','१२','१३','१४','१५','१६','१७','१८','१९','२॰',
        '२१','२२','२३','२४','२५','२६','२७','२८','२९','३॰',
        '३१','३२','३३','३४','३५','३६','३७','३८','३९','४॰',
        '४१','४२','४३','४४','४५','४६','४७','४८','४९','५॰',
        '५१','५२','५३','५४','५५','५६','५७','५८','५९'])

hr=['१२','१','२','३','४','५','६','७','८','९','१॰','११']
mn=['६॰','१','२','३','४','५','६','७','८','९','१॰',
        '११','१२','१३','१४','१५','१६','१७','१८','१९','२॰',
        '२१','२२','२३','२४','२५','२६','२७','२८','२९','३॰',
        '३१','३२','३३','३४','३५','३६','३७','३८','३९','४॰',
        '४१','४२','४३','४४','४५','४६','४७','४८','४९','५॰',
        '५१','५२','५३','५४','५५','५६','५७','५८','५९']
se=['६॰','१','२','३','४','५','६','७','८','९','१॰',
        '११','१२','१३','१४','१५','१६','१७','१८','१९','२॰',
        '२१','२२','२३','२४','२५','२६','२७','२८','२९','३॰',
        '३१','३२','३३','३४','३५','३६','३७','३८','३९','४॰',
        '४१','४२','४३','४४','४५','४६','४७','४८','४९','५॰',
        '५१','५२','५३','५४','५५','५६','५७','५८','५९']

now = datetime.datetime.now()
h_in =[]

m_in = []

s_in = []

for i in range(0,60):
    in_radian = math.radians(in_degree) # converting to radian
    if(i%5==0): 
        ratio=0.85 # Long marks ( lines )
        t1=x+r4*math.sin(in_radian) # coordinate to add text ( hour numbers )
        t2=x-r4*math.cos(in_radian) # coordinate to add text ( hour numbers )
        h_1=c1.create_text(t1,t2,fill='White',font="Times 15  bold",text=next(h))
        h_in.append(h_1)
    else:
        ratio = 0.7
    in_degree=in_degree+6
    
for i in range(0,60):
    in_radian = math.radians(in_degree) # converting to radian
    ratio = 0.5
    x2=x+r1*math.sin(in_radian)
    y2=y-r1*math.cos(in_radian)
    m_1 = c1.create_text(x2,y2,fill='White',font="Times 7  bold",text=next(m))
    m_in.append(m_1)
    in_degree=in_degree+6
    
for i in range(0,60):
    in_radian = math.radians(in_degree) # converting to radian
    ratio = 0.5
    x2=x+r3*math.sin(in_radian)
    y2=y-r3*math.cos(in_radian)
    s_1 = c1.create_text(x2,y2,fill='White',font="Times 7  bold",text=next(s))
    s_in.append(s_1)
    in_degree=in_degree+6
    
quote = c1.create_text(200,180,fill='GoldenRod2',font="Times 15  bold",text=verses[(now.day%7)-1])
main_t = c1.create_text(200,220,fill='GoldenRod2',font="Times 15  bold",text=str(hr[now.hour-12])+":"+mn[now.minute]+":"+se[now.second])

def tick():
    hr=['१२','१','२','३','४','५','६','७','८','९','१॰','११']
    mn=['६॰','१','२','३','४','५','६','७','८','९','१॰',
            '११','१२','१३','१४','१५','१६','१७','१८','१९','२॰',
            '२१','२२','२३','२४','२५','२६','२७','२८','२९','३॰',
            '३१','३२','३३','३४','३५','३६','३७','३८','३९','४॰',
            '४१','४२','४३','४४','४५','४६','४७','४८','४९','५॰',
            '५१','५२','५३','५४','५५','५६','५७','५८','५९']
    se=['६॰','१','२','३','४','५','६','७','८','९','१॰',
            '११','१२','१३','१४','१५','१६','१७','१८','१९','२॰',
            '२१','२२','२३','२४','२५','२६','२७','२८','२९','३॰',
            '३१','३२','३३','३४','३५','३६','३७','३८','३९','४॰',
            '४१','४२','४३','४४','४५','४६','४७','४८','४९','५॰',
            '५१','५२','५३','५४','५५','५६','५७','५८','५९']
    now = datetime.datetime.now()
    if now.hour > 12:
        if now.hour == 24:
            hour = 0
        else:
            hour = now.hour -12
    else:
        hour = now.hour
    c1.itemconfig(h_in[hour-1],fill='White',font="Times 15  bold")
    c1.itemconfig(m_in[now.minute-1],fill='White',font="Times 7  bold")
    c1.itemconfig(s_in[now.second-1],fill='White',font="Times 7  bold")
    
    c1.itemconfig(h_in[hour],fill='GoldenRod2',font="Times 20  bold")
    c1.itemconfig(m_in[now.minute],fill='GoldenRod2',font="Times 12  bold")
    c1.itemconfig(s_in[now.second],fill='GoldenRod2',font="Times 12  bold")

    c1.itemconfig(main_t,text=str(hr[now.hour-12])+":"+mn[now.minute]+":"+se[now.second])    
    c1.after(10, tick)

    
    


tick()
root.mainloop()


