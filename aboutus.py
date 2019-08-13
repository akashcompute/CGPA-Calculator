from tkinter import *
from aboutus_ui import Aboutus
class CustomAboutus(Aboutus):
    print("About Us Window Opened.")
    pass

    def close_command(self):
        print("Close Buttton pressed.")
        print("About Us Window Closed.")
        quit(0)
        pass

def main():
    root = Tk()
    demo = CustomAboutus(root)
    root.title('aboutus')
    root.mainloop()

if __name__ == '__main__': main()
