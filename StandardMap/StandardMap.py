"""
Created on Sat May 28 21:22:26 2016

@author: Milos Adamovic
"""
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
import math

LARGE_FONT= ("Verdana", 12)

def exitProgram():
    global app
    print ("Quit Button pressed")
    app.quit()
    app.destroy()

def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg, font=LARGE_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="OK", command = popup.destroy)
    B1.pack()
    popup.mainloop()

class ChirikovStandardMap(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Chirikov Standard Map")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)


        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Save settings", command = lambda: popupmsg("Jos nije moguce!"))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=exitProgram)
        menubar.add_cascade(label="File", menu=filemenu)

        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Pomoc", command = lambda: popupmsg("Pomoc!"))
        menubar.add_cascade(label="Pomoc", menu=helpmenu)

        tk.Tk.config(self, menu=menubar)

        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, GraphPage):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Chirikov Standard Map", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = ttk.Button(self, text="Graph Page",
                            command=lambda: controller.show_frame(GraphPage))
        button.pack()

        button1 = ttk.Button(self, text="Quit",command=exitProgram)
        button1.pack(side=tk.BOTTOM)

        def callk():
            return mk.get()

        def callpoints():
            return pointsvalue.get()
    
        def calliterations():
            return iterationsvalue.get()

        def Chirikovstandardmap(ks,numPoints,numIterations):
            for i in range(1,numPoints):
                t=np.zeros((2,numIterations))
                q=t[0,:]
                p=t[1,:]
                #Izabrati pocetne vrednosti parametara p i q, random odabir
                q[0]=np.random.rand()*2*math.pi
                p[0]=np.random.rand()*2*math.pi
                for n in range(1,numIterations):
                    p[n]=(p[n-1]+ks*math.sin(q[n-1]))%(2*math.pi)
                    q[n]=(q[n-1]+p[n])%(2*math.pi)
                plt.plot(q/(2*math.pi),p/(2*math.pi),'b.',ms=1)
            plt.title('Chirikov map')
            plt.xlabel(r'$\frac{q}{2\pi}$')
            plt.ylabel(r'$\frac{p}{2\pi}$')
            plt.show()
            #plt.gcf().canvas.draw()
            #fig = plt.figure()
            #canvas = FigureCanvasTkAgg(fig, self)
            #canvas.show()
            #canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)
            
        #def saveclick():
            #a=plt.show()

        def myplot():
            myk = eval(callk())
            mypoints = eval(callpoints())
            myiterations = eval(calliterations())
            Chirikovstandardmap(myk,mypoints,myiterations)

        klabel=ttk.Label(self,text="Unesite vrednost K: ")
        klabel.pack()
        klabel.place(x=20,y=100)

        mk=ttk.Entry(self)
        mk.bind("<Return>")
        mk.pack()
        mk.place(x=200,y=100)

        
        pointsvalue=ttk.Label(self,text="Unesite broj pocetnih tacaka: ")
        pointsvalue.pack()
        pointsvalue.place(x=20,y=150)

        pointsvalue=ttk.Entry(self)
        pointsvalue.bind("<Return>")
        pointsvalue.pack()
        pointsvalue.place(x=200,y=150)

        iterationslabel=ttk.Label(self,text="Unesite broj iteracija: ")
        iterationslabel.pack()
        iterationslabel.place(x=20,y=200)

        iterationsvalue=ttk.Entry(self)
        iterationsvalue.bind("<Return>")
        iterationsvalue.pack()
        iterationsvalue.place(x=200,y=200)


        plotButton=ttk.Button(self,text='Plot',command=myplot,width=6)
        plotButton.pack(pady=40,padx=40)

        #graphButton=ttk.Button(self,text='Graph',command=saveclick,width=6)
        #graphButton.pack(pady=20,padx=20)
        


        
class GraphPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button2 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button2.pack()

        button3 = ttk.Button(self, text="Quit",command=exitProgram)
        button3.pack(side=tk.BOTTOM)

        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
       
       

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        

app = ChirikovStandardMap()
app.geometry("1000x500")
app.mainloop()
