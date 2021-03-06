
import sys
import subprocess
import os
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from pathlib import Path
import webbrowser

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import pakstongui_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Arduino_Beats_Triggerer__ (root)
    pakstongui_support.init(root, top)
    root.mainloop()

w = None
def create_Arduino_Beats_Triggerer__(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Arduino_Beats_Triggerer__ (w)
    pakstongui_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Arduino_Beats_Triggerer__():
    global w
    w.destroy()
    w = None
from pygame import *
import serial


def demomode(args):
    if isinstance( args, KeyboardEvent ):
        print( args.key_code )
        if args.current_key == 'A' and args.event_type == 'key down' and 'Lcontrol' in args.pressed_key:
            print( "Ctrl + A was pressed" )
        elif args.current_key == 'Q' and args.event_type == 'key down' and 'Lcontrol' in args.pressed_key:
            hk.stop()
            print( 'Quitting.' )



c=1

class Arduino_Beats_Triggerer__:
    fname = None
    Comportnum=None

    newdotblend = None
    numberframe = None
    startframe = None
    endframe = None
    timeint = None
    b=0
    def showstatus(self,a):
        self.Entry3.insert( END, a )





    def playsound1(self,b):
        mixer.music.load( "1.wav" )
        mixer.music.play()
        self.Entry3.insert( END, "playing tone" )
        print( mixer.music.get_busy )


        #while mixer.music.get_busy():
            #time.Clock().tick( 10 )

    def stopsound1(self,b):
        mixer.music.stop()
        self.Entry3.insert( END, "playing tone" )

    def startloop(self):
        mixer.init()
        COM1=str(self.Comportnum)
        COM="COM"+COM1
        print(COM)
        self.Entry1.insert( END, "playing tone" )
        #print('COM3')
        #ser = serial.Serial('COM3', 9600, timeout=.1 )
        ser = serial.Serial( COM, 9600, timeout=.1 )
        print( "connecting to arduino" )
        while 1:
          try:
             a = ser.readline().strip()
             a = (a.decode( 'utf-8' ))
             print(a)
             if int( a )!= 0:
                 print( a )

                 self.b = self.b + int( a )
                 print( "value of b %s" % self.b )

                 if self.b % 2 == 0:
                      self.stopsound1( self.b)
                 else:
                      self.playsound1(self.b )
          except ValueError:
             pass

    def aboutus(self):
        self.aboutuss = messagebox.askquestion( "Know us",
                                                "To know more about us and our projects visit www.engineerthoughts.com, press yes to visit our site" )
        print( self.aboutuss )
        if self.aboutuss == "yes":
            webbrowser.open( 'www.engineerthoughts.com', new=0 )
        else:
            pass


    def helpp(self):
        self.help=messagebox.showinfo("Help","Enter the music wav file and click the USB/comport of the ardunio connected also make sure the serial signal from the arduino is 1 and 0 not any other values and baud rate is 9600")


    def submitt(self):
        try:
            msgg = messagebox.showinfo( "Dialogbox", "Press ok to connect to COM PORT" )

            self.Comportnum=self.Entry2.get()
            self.Comportnum=int(self.Comportnum)
            print(self.Comportnum)
            os.chdir( self.fname )
            if msgg:

                pass
                self.startloop()
            else:
                exit()

        except ValueError:
            dem=messagebox.showwarning("Alert","Enter the COM port value in Interger ")
        except TypeError:
            messagebox.showwarning("Alert","Browse the location of the wav please and continue")
        except FileNotFoundError:
            messagebox.showerror("Alert","You have entered COM is not responding , try entering correct COM port or unplug and plug microcontroller")
        except WindowsError:
            messagebox.showerror("Alert","there is no device in the comport, try entering after plugging the device")

    def browsemusic(self):
        self.fname = askopenfilename( filetypes=(("All files", "*.*"),
                                                 ("wav", "*.wav"),
                                                 ("ogg", "*.ogg")) )
        print(self.fname)
        lastoccr= self.fname.rfind('/')
        total=len(self.fname)
        print(lastoccr)
        print(total)
        self.fname=self.fname[:(lastoccr)]
        print(self.fname)
        if self.fname:
            try:
                print("""here it comes: self.settings["template"].set(fname)""")
                self.Entry1.insert(END, self.fname)
            except:                     # <- naked except is a bad idea
                showerror("Open Source File", "Failed to read file\n'%s'" % self.fname)
            return

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family {Segoe UI Light} -size 19 -weight bold "  \
            "-slant italic -underline 0 -overstrike 0"
        font11 = "-family {Segoe UI} -size 14 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font12 = "-family {Segoe UI} -size 17 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 16 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("958x658+565+142")
        top.title("Arduino Beats Triggerer Electronics drums ")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.01, rely=0.05, relheight=0.93, relwidth=0.96)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=915)

        self.Frame2 = Frame(self.Frame1)
        self.Frame2.place(relx=0.01, rely=0.02, relheight=0.15, relwidth=0.97)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(background="#d9d9d9")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")
        self.Frame2.configure(width=885)

        self.Label2 = Label(self.Frame2)
        self.Label2.place(relx=0.17, rely=0.11, height=71, width=644)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#80ffff")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font10)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Arduino Beats Triggerer by N.Aranganathan''')
        self.Label2.configure(width=644)

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.02, rely=0.21, height=76, width=432)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Browse the location of the wav files''')

        self.Entry1 = Entry(self.Frame1)
        self.Entry1.place(relx=0.51, rely=0.24, relheight=0.06, relwidth=0.3)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")

        self.Button1 = Button(self.Frame1)
        self.Button1.place(relx=0.85, rely=0.24, height=43, width=96)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#ff8080")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Browse''')
        self.Button1.configure(command=self.browsemusic)

        self.Label3 = Label(self.Frame1)
        self.Label3.place(relx=0.02, rely=0.34, height=26, width=552)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font11)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Enter the COM port of the Microcontroller connected''')

        self.Entry2 = Entry(self.Frame1)
        self.Entry2.place(relx=0.64, rely=0.34, relheight=0.06, relwidth=0.16)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(selectbackground="#c4c4c4")
        self.Entry2.configure(selectforeground="black")

        self.Button2 = Button(self.Frame1)
        self.Button2.place(relx=0.66, rely=0.42, height=43, width=136)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Submit''')
        self.Button2.configure(command=self.submitt)

        self.Button3 = Button(self.Frame1)
        self.Button3.place(relx=0.83, rely=0.43, height=43, width=136)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''clear''')

        self.Button4 = Button(self.Frame1)
        self.Button4.place(relx=0.07, rely=0.43, height=43, width=136)
        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''Help''')
        self.Button4.configure(command=self.helpp)

        self.Entry3 = Entry(self.Frame1)
        self.Entry3.place(relx=0.48, rely=0.6, relheight=0.06, relwidth=0.31)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(highlightbackground="#d9d9d9")
        self.Entry3.configure(highlightcolor="black")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(selectbackground="#c4c4c4")
        self.Entry3.configure(selectforeground="black")


        self.Label4 = Label(self.Frame1)
        self.Label4.place(relx=0.32, rely=0.57, height=64, width=121)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font=font12)
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Status''')

        self.Label5 = Label(self.Frame1)
        self.Label5.place(relx=0.27, rely=0.73, height=44, width=375)
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font=font12)
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''Engineer Thoughts''')
        self.Label5.configure(width=375)

        self.Label6 = Label(self.Frame1)
        self.Label6.place(relx=0.38, rely=0.81, height=26, width=190)
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''www.engineerthoughts.com''')

        self.Button5 = Button(self.Frame1)
        self.Button5.place(relx=0.38, rely=0.86, height=33, width=176)
        self.Button5.configure(activebackground="#d9d9d9")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#d9d9d9")
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''visit us''')
        self.Button5.configure(width=176)
        self.Button5.configure(command=self.aboutus)







if __name__ == '__main__':
    vp_start_gui()




