import tkinter

class Welcome(object):
    _images = []
    def __init__(self, root):
        self._images.append(tkinter.PhotoImage('lpu.gif', file = 'lpu.gif'))
        self._images.append(tkinter.PhotoImage('Screenshot (115).gif', file = 'Screenshot (115).gif'))

        # Widget Initialization
        self._frame_1 = tkinter.Frame(root,background = "#ffffff",)
        self._label_1 = tkinter.Label(root,
            activebackground = "#ffffff",
            background = "#ffffff",
            borderwidth = 1,
            cursor = "dotbox",
            font = "{MS Sans Serif} 24 bold",
            image = "Screenshot (115).gif",
            text = "CGPA Calculator",)
        self._label_3 = tkinter.Label(root,
            activebackground = "#ffffff",
            background = "#ffffff",
            borderwidth = 0,
            cursor = "arrow",
            image = "lpu.gif",
            text = "_label_3",)
        self._label_4 = tkinter.Label(root,
            activebackground = "#feebcd",
            activeforeground = "#ff0033",
            background = "#feebcd",
            font = "{MS Sans Serif} 13 bold italic",
            foreground = "#ff0033",
            text = "\u00A9 copyright protected 2018-2019",)
        self.login = tkinter.Button(root,
            activebackground = "#c0c5fe",
            background = "#c0c5fe",
            borderwidth = 5,
            cursor = "hand2",
            font = "{Leelawadee UI} 10 bold",
            text = "Login",)
        self.newuser = tkinter.Button(root,
            activebackground = "#c0c5fe",
            background = "#c0c5fe",
            borderwidth = 5,
            cursor = "hand2",
            font = "{Leelawadee UI} 10 bold",
            text = "New User",)
        self._label_2 = tkinter.Label(root,
            activebackground = "#fff4d2",
            background = "#fff4d2",
            borderwidth = 0,
            font = "{MS Sans Serif} 14 bold",
            text = """\uD83D\uDCAE \uD83D\uDCAE \uD83D\uDCAE This project is based on ten (10) point scale as used by most  Colleges of Education. 
Academic excellence is measured using the Grade Point Average (GPA) and Cumulative Grade Point Average (CGPA).
 So it is important that all students have insight on how to calculate their GPA & CGPA so as to be able
 to evaluate their academic performance from time to time and improve themselves by the remarks provided.   \uD83D\uDCAE \uD83D\uDCAE \uD83D\uDCAE  
""",)
        self.about = tkinter.Button(root,
            activebackground = "#c0c5fe",
            background = "#c0c5fe",
            borderwidth = 5,
            cursor = "hand2",
            font = "{Leelawadee UI} 10 bold",
            text = "About",)
        self.exit = tkinter.Button(root,
            activebackground = "#c0c5fe",
            background = "#c0c5fe",
            borderwidth = 5,
            cursor = "hand2",
            font = "{Leelawadee UI} 10 bold",
            text = "Exit",)
        self._label_5 = tkinter.Label(root,
            activebackground = "#fff4d2",
            activeforeground = "#fb001a",
            background = "#fff4d2",
            font = "{MS Sans Serif} 14 bold italic",
            foreground = "#fb001a",
            text = " Made with \u2764  by Akash \uD83D\uDC68\uD83C\uDFFB\u200D ",)

        # widget commands
        self.login.configure(command = self.login_command)
        self.newuser.configure(command = self.newuser_command)
        self.about.configure(command = self.about_command)
        self.exit.configure(command = self.exit_command)

        # Geometry Management
        self._frame_1.grid(in_ = root,column = 5,row = 2,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "news")
        self._label_1.grid(in_ = root,column = 1,row = 1,columnspan = 4,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 2,sticky = "nsew")
        self._label_3.grid(in_ = root,column = 5,row = 1,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self._label_4.grid(in_ = root,column = 5,row = 5,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self.login.grid(in_ = root,column = 2,row = 5,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self.newuser.grid(in_ = root,column = 3,row = 5,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self._label_2.grid(in_ = root,column = 1,row = 3,columnspan = 5,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self.about.grid(in_ = root,column = 1,row = 5,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self.exit.grid(in_ = root,column = 4,row = 5,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self._label_5.grid(in_ = root,column = 1,row = 4,columnspan = 5,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")

        # Resize Behavior
        root.grid_rowconfigure(1, weight = 0, minsize = 84, pad = 0)
        root.grid_rowconfigure(2, weight = 0, minsize = 42, pad = 0)
        root.grid_rowconfigure(3, weight = 0, minsize = 40, pad = 0)
        root.grid_rowconfigure(4, weight = 0, minsize = 36, pad = 0)
        root.grid_rowconfigure(5, weight = 1, minsize = 39, pad = 0)
        root.grid_columnconfigure(1, weight = 0, minsize = 143, pad = 0)
        root.grid_columnconfigure(2, weight = 0, minsize = 147, pad = 0)
        root.grid_columnconfigure(3, weight = 0, minsize = 148, pad = 0)
        root.grid_columnconfigure(4, weight = 0, minsize = 40, pad = 0)
        root.grid_columnconfigure(5, weight = 0, minsize = 40, pad = 0)