import tkinter
from tkinter import *
import sqlite3
from tkinter import messagebox

class Login(object):
    _images = [] # Holds image refs to prevent GC
    def __init__(self, root):
        self._images.append(tkinter.PhotoImage('icon_lock_key.gif', file = 'icon_lock_key.gif'))

        # Widget Initialization
        self._frame_1 = tkinter.Frame(root,background = "#ffa4a6",)
        self._frame_2 = tkinter.Frame(root,background = "#ffa4a6",)
        self._frame_3 = tkinter.Frame(root,background = "#ffa4a6",)
        self._label_1 = tkinter.Label(root,
            activebackground = "#999999",
            activeforeground = "#000000",
            background = "#999999",
            font = "{MS Sans Serif} 4 bold",
            foreground = "#000000",
            text = "    Provide Correct Login Credentials To Proceed  ",)
        self._label_7 = tkinter.Label(root,
            activebackground = "#ffffff",
            activeforeground = "#990000",
            background = "#ffffff",
            cursor = "umbrella",
            foreground = "#990000",
            image = "icon_lock_key.gif",
            text = "_label_7",)
        self._label_2 = tkinter.Label(root,activebackground = "#ffa4a6",background = "#ffa4a6",font = "{Gill Sans Ultra Bold} 24 bold",text = "Login",)
        self._label_3 = tkinter.Label(root,activebackground = "#ffa4a6",background = "#ffa4a6",font = "{MS Sans Serif} 10 bold",text = " Username  ",)
        self._label_4 = tkinter.Label(root,activebackground = "#ffa4a6",background = "#ffa4a6",font = "{MS Sans Serif} 11 bold",text = "Password",)
        self.password = tkinter.Entry(self._frame_2,insertwidth = 4,width = 50,show="*",)
        self.username = tkinter.Entry(self._frame_1,insertwidth = 4,width = 50,)
        self.cancel = tkinter.Button(root,
            activebackground = "#ff5b5b",
            background = "#ff5b5b",
            borderwidth = 4,
            cursor = "hand2",
            font = "{MS Gothic} 10 bold",
            overrelief = "flat",
            text = "Cancel",)
        self.login = tkinter.Button(root,
            activebackground = "#ff5b5b",
            background = "#ff5b5b",
            borderwidth = 3,
            cursor = "hand2",
            font = "{MS Gothic} 10 bold",
            overrelief = "flat",
            text = "Login",)

        # widget commands
        self.cancel.configure(command = self.cancel_command)
        self.login.configure(command = self.login_command)

        # Geometry Management
        self._frame_1.grid(in_ = root,column = 3,row = 3,columnspan = 2,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "news")
        self._frame_2.grid(in_ = root,column = 3,row = 4,columnspan = 2,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "news")
        self._frame_3.grid(in_  = root,column = 2,row = 5,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 2,sticky = "news")
        self._label_1.grid(in_ = root,column = 1,row = 1,columnspan = 4,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self._label_7.grid(in_ = root,column = 1,row = 2,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 5,sticky = "nsew")
        self._label_2.grid(in_ = root,column = 2,row = 2,columnspan = 3,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self._label_3.grid(in_ = root,column = 2,row = 3,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self._label_4.grid(in_ = root,column = 2,row = 4,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self.password.grid(in_ = self._frame_2,column = 1,row = 1,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "ew")
        self.username.grid(in_ = self._frame_1,column = 1,row = 1,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "ew")
        self.cancel.grid(in_ = root,column = 3,row = 5,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 2,sticky = "nsew")
        self.login.grid(in_ = root,column = 4,row = 5,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 2,sticky = "nsew")

        # Resize Behavior
        root.grid_rowconfigure(1, weight = 1, minsize = 13, pad = 0)
        root.grid_rowconfigure(2, weight = 0, minsize = 70, pad = 0)
        root.grid_rowconfigure(3, weight = 1, minsize = 64, pad = 0)
        root.grid_rowconfigure(4, weight = 1, minsize = 46, pad = 0)
        root.grid_rowconfigure(5, weight = 1, minsize = 24, pad = 0)
        root.grid_rowconfigure(6, weight = 0, minsize = 3, pad = 0)
        root.grid_columnconfigure(1, weight = 0, minsize = 100, pad = 0)
        root.grid_columnconfigure(2, weight = 1, minsize = 113, pad = 0)
        root.grid_columnconfigure(3, weight = 0, minsize = 179, pad = 0)
        root.grid_columnconfigure(4, weight = 0, minsize = 196, pad = 0)
        self._frame_1.grid_rowconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_1.grid_columnconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_2.grid_rowconfigure(1, weight = 0, minsize = 87, pad = 0)
        self._frame_2.grid_columnconfigure(1, weight = 0, minsize = 59, pad = 0)

class CustomLogin(Login):
    print("Login Window Opened.")
    pass

    def cancel_command(self):
        print("Cancel Buttton pressed.")
        print("Login Window Closed.")
        quit(0)
        pass

    def login_command(self):
        try:
            print("Login Buttton pressed.")
            if self.username.get()=="" or self.password.get()=="":
                print("Enter all details before proceeding.")
                messagebox.showerror("Error","Enter all the details before proceeding...!!")
            else:
                ob = sqlite3.connect("database.db")
                cur = ob.cursor()
                list = []
                list2 = []
                pos = 0
                i = 0
                # to retrieve login data from database
                cur.execute("""select * from login;""")
                while True:
                    records = cur.fetchone()
                    if records == None:
                        break
                    if self.username.get() == records[0]:
                        list.append(records[0])
                        list2.append(records)
                        pos = i
                        break
                    i += 1
                print("list=", list)
                if self.username.get() not in list:
                    print("User Does't Exists.")
                    messagebox.showerror("SORRY..!!", "User Doesn't Exists...!!.\n\nPlease add new user and then login.")
                    flag = 1
                else:
                    flag = 0

                if flag == 0:
                    # to retrieve login data from database
                    cur.execute("""select * from login;""")
                    record = cur.fetchall()
                    if self.password.get() == str(record[i][1]):
                        import main
                        self.newwindow = tkinter.Toplevel()
                        self.demo = main.CustomMain(self.newwindow)
                    else:
                        print("Password Did't Matched.")
                        messagebox.showwarning("Failed..!!","Login Failed..!!\n\nEnter correct password.")
                ob.commit()
                ob.close()
        except:
            messagebox.showerror("Error", "Something went wrong..!!!\nPlease contact Admin: +917004250668")
        pass

def main():
    root = Tk()
    demo = CustomLogin(root)
    root.title('Login')
    root.mainloop()

if __name__ == '__main__': main()
