import tkinter
import sqlite3
from tkinter import *
from Welcome_ui import Welcome
from tkinter import messagebox
class CustomWelcome(Welcome):
    print("Welcome Window Opened.")
    pass

    def about_command(self):
        print("About Button Pressed.")
        import aboutus
        self.newwindow = tkinter.Toplevel()
        self.demo=aboutus.CustomAboutus(self.newwindow)
        #newwindow.destroy()
        pass

    def exit_command(self):
        print("Exit Button Pressed.")
        msg = messagebox.askyesno("Exit","Are you sure you want to exit ?", icon='warning')
        if msg:
            print("Welcome Window Closed.")
            quit(0)
        pass

    def login_command(self):
        print("Login Button Pressed.")
        import Login
        self.newwindow = tkinter.Toplevel()
        self.demo=Login.CustomLogin(self.newwindow)
        pass

    def newuser_command(self):
        print("New User Button Pressed.")
        import newuser
        self.newwindow = tkinter.Toplevel()
        self.demo = newuser.CustomNewuser(self.newwindow)
        pass

def main():
    root = Tk()
    demo = CustomWelcome(root)
    root.title('Welcome')
    root.mainloop()

if __name__ == '__main__': main()