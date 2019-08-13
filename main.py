import tkinter
from tkinter import *
from tkinter import messagebox
import sqlite3
grade1 = []
grade1point=[]
credit1 = []
grade2 = []
grade2point=[]
credit2 = []
class Main(object):
    _images = [] # Holds image refs to prevent GC
    def __init__(self, root):
        self._images.append(tkinter.PhotoImage('Screenshot_(117).gif', file = 'Screenshot_(117).gif'))
        self._images.append(tkinter.PhotoImage('Screenshot_(119).gif', file = 'Screenshot_(119).gif'))

        # Widget Initialization
        self._labelframe_3 = tkinter.LabelFrame(root,background = "#fafdb3",font = "{MS Sans Serif} 8 bold",foreground = "#000000",text = "Student Details",)
        self._frame_1 = tkinter.Frame(root,background = "#ffffae",)
        self._frame_2 = tkinter.Frame(root,background = "#ffffb0",)
        self._frame_3 = tkinter.Frame(root,background = "#ffffb0",)
        self._frame_4 = tkinter.Frame(root,background = "#ffffb0",)
        self._frame_5 = tkinter.Frame(root,background = "#ffffb0",)
        self._frame_6 = tkinter.Frame(root,background = "#ffffb0",)
        self._frame_7 = tkinter.Frame(root,background = "#ffffb0",)
        self._frame_8 = tkinter.Frame(root,background = "#ffffb0",)
        self._frame_9 = tkinter.Frame(root,background = "#ffffb0",)
        self._frame_10 = tkinter.Frame(root,background = "#ffffb0",)
        self._frame_11 = tkinter.Frame(root,background = "#ffffb0",)
        self._frame_12 = tkinter.Frame(root,background = "#ffffb0",)
        self._frame_13 = tkinter.Frame(root,background = "#ffffb0",)
        self._frame_14 = tkinter.Frame(root,background = "#ffffb0",)
        self._frame_15 = tkinter.Frame(root,background = "#ffffb0",)
        self._frame_16 = tkinter.Frame(root,background = "#ffffb0",)
        self._frame_17 = tkinter.Frame(root,background = "#ffffb0",)
        self._frame_18 = tkinter.Frame(root,background = "#ffffb0",)
        self._frame_20 = tkinter.Frame(root,background = "#ffffb0",)
        self._frame_24 = tkinter.Frame(root,background = "#ffffa4",)
        self._frame_22 = tkinter.Frame(root,background = "#ffffa4",)
        self._frame_23 = tkinter.Frame(root,background = "#ffffa4",)
        self._frame_25 = tkinter.Frame(root,background = "#ffffa4",)
        self._frame_26 = tkinter.Frame(root,background = "#ffffa4",)
        self._frame_27 = tkinter.Frame(root,background = "#ffffa4",)
        self._frame_28 = tkinter.Frame(root,background = "#ffffa4",)
        self._frame_29 = tkinter.Frame(root,background = "#ffffa4",)
        self._frame_30 = tkinter.Frame(root,background = "#ffffa4",)
        self._frame_32 = tkinter.Frame(root,background = "#ffffa4",)
        self._frame_33 = tkinter.Frame(root,background = "#ffffa4",)
        self._frame_34 = tkinter.Frame(root,background = "#ffffa4",)
        self._frame_35 = tkinter.Frame(root,background = "#ffffa4",)
        self._frame_42 = tkinter.Frame(root,background = "#ffffa4",)
        self._frame_43 = tkinter.Frame(root,background = "#ffffa4",)
        self._frame_44 = tkinter.Frame(root,background = "#ffffa4",)
        self._frame_45 = tkinter.Frame(root,background = "#ffffa4",)
        self._frame_46 = tkinter.Frame(root,background = "#ffffa4",)
        self._label_1 = tkinter.Label(root,activebackground = "#ffffff",activeforeground = "#cccccc",background = "#ffffff",font = "{MS Sans Serif} 9",
            foreground = "#cccccc",image = "Screenshot_(117).gif",justify = "right",text = "_label_1",)
        self._label_2 = tkinter.Label(root,activebackground = "#ff8f59",background = "#ff8f59",
            text = """\uD83D\uDCAE \uD83D\uDCAE \uD83D\uDCAE This project is based on ten (10) point scale as used by most  Colleges of Education. 
Academic excellence is measured using the Grade Point Average (GPA) and Cumulative Grade Point Average (CGPA).
 So it is important that all students have insight on how to calculate their GPA & CGPA so as to be able
 to evaluate their academic performance from time to time and improve themselves by the remarks provided.   \uD83D\uDCAE \uD83D\uDCAE \uD83D\uDCAE """,)
        self._label_3 = tkinter.Label(root,activebackground = "#c89191",background = "#c89191",font = "{MS Sans Serif} 8 bold",
            text = "Before proceeding kindly see the instructions on rightmost corner, will be overwritten later by remarks afte calculating CGPA.",)
        self._label_5 = tkinter.Label(self._labelframe_3,activebackground = "#fafdb3",background = "#fafdb3",font = "{MS Sans Serif} 8 bold",text = "Name:",)
        self.name = tkinter.Entry(self._labelframe_3,width = 25,)
        self._label_6 = tkinter.Label(self._labelframe_3,activebackground = "#fafdb3",background = "#fafdb3",font = "{MS Sans Serif} 8 bold",
            text = "    Registration number :",)
        self.regno = tkinter.Entry(self._labelframe_3,width = 25,)
        self._label_10 = tkinter.Label(root,activebackground = "#ffffff",background = "#ffffff",image = "Screenshot_(119).gif",text = "_label_10",)
        self._label_12 = tkinter.Label(self._frame_1,activebackground = "#ffffae",activeforeground = "#ff0000",background = "#ffffae",
            font = "{MS Sans Serif} 8 bold",foreground = "#ff0000",text = " First Semester :",)
        self._label_13 = tkinter.Label(root,activebackground = "#b87070",background = "#b87070",font = "{MS Sans Serif} 8 bold",text = "Course Title",)
        self._label_14 = tkinter.Label(root,activebackground = "#b87070",background = "#b87070",font = "{MS Sans Serif} 8 bold",text = "Course Code",)
        self._label_16 = tkinter.Label(root,activebackground = "#b87070",background = "#b87070",font = "{MS Sans Serif} 8 bold",text = "Credit",)
        self._label_20 = tkinter.Label(root,activebackground = "#b87070",background = "#b87070",font = "{MS Sans Serif} 8 bold",text = "Grade Obtained",)
        self.firstsub1 = tkinter.Entry(self._frame_2,justify = "center",width = 35,)
        self.firstcourse1 = tkinter.Entry(self._frame_3,justify = "center",width = 10,)
        self.firstcredit1 = tkinter.Entry(self._frame_4,justify = "center",width = 0,)
        self.firstgrade1 = tkinter.Entry(self._frame_5,justify = "center",width = 0,)
        self.firstsub2 = tkinter.Entry(self._frame_6,justify = "center",width = 35,)
        self.firstcourse2 = tkinter.Entry(self._frame_7,justify = "center",width = 10,)
        self.firstcredit2 = tkinter.Entry(self._frame_8,justify = "center",width = 0,)
        self.firstgrade2 = tkinter.Entry(self._frame_9,justify = "center",width = 0,)
        self.firstsub3 = tkinter.Entry(self._frame_10,justify = "center",width = 35,)
        self.firstcourse3 = tkinter.Entry(self._frame_11,justify = "center",width = 10,)
        self.firstcredit3 = tkinter.Entry(self._frame_12,justify = "center",width = 0,)
        self.firstgrade3 = tkinter.Entry(self._frame_13,justify = "center",width = 0,)
        self.firstsub4 = tkinter.Entry(self._frame_14,justify = "center",width = 35,)
        self.firstcourse4 = tkinter.Entry(self._frame_15,justify = "center",width = 10,)
        self.firstcredit4 = tkinter.Entry(self._frame_16,justify = "center",width = 0,)
        self.firstgrade4 = tkinter.Entry(self._frame_17,justify = "center", width = 0,)
        self.firsttgpa = tkinter.Button(root,
            activebackground = "#c4c4ff",
            background = "#c4c4ff",
            borderwidth = 5,
            cursor = "hand2",
            font = "{MS Sans Serif} 8 bold",
            text = "Calculate TGPA",)
        self.firsttgpavalue = tkinter.Label(root,
            activebackground = "#ffffb0",
            activeforeground = "#ff0000",
            background = "#ffffb0",
            font = "{MS Sans Serif} 17 bold",
            foreground = "#ff0000",
            text = 0.00,)
        self._label_22 = tkinter.Label(root,activebackground = "#b66b6b",background = "#b66b6b",font = "{MS Sans Serif} 8 bold",text = "Grade",)
        self._label_24 = tkinter.Label(root,activebackground = "#b66b6b",background = "#b66b6b",font = "{MS Sans Serif} 8 bold",text = "Grade Point",)
        self._label_25 = tkinter.Label(root,activebackground = "#d7ffd7",background = "#d7ffd7",font = "{MS Sans Serif} 8 bold",text = "O (Outstanding)",)
        self._label_39 = tkinter.Label(self._frame_20,
            activebackground = "#ffffae",
            activeforeground = "#ff0000",
            background = "#ffffae",
            font = "{MS Sans Serif} 8 bold",
            foreground = "#ff0000",
            text = " Second Semester :",)
        self._label_47 = tkinter.Label(root,activebackground = "#d7ffd7",background = "#d7ffd7",font = "{MS Sans Serif} 8 bold",padx = 0,pady = 0,text = 10,)
        self._label_48 = tkinter.Label(root,activebackground = "#d7ffd7",background = "#d7ffd7",font = "{MS Sans Serif} 8 bold",padx = 0,pady = 0,text = "A+",)
        self._label_49 = tkinter.Label(root,activebackground = "#d7ffd7",background = "#d7ffd7",font = "{MS Sans Serif} 8 bold",padx = 0,pady = 0,text = 9,)
        self._label_50 = tkinter.Label(root,activebackground = "#d7ffd7",background = "#d7ffd7",font = "{MS Sans Serif} 8 bold",padx = 0,pady = 0,text = "A",)
        self._label_51 = tkinter.Label(root,activebackground = "#d7ffd7",background = "#d7ffd7",font = "{MS Sans Serif} 8 bold",padx = 0,pady = 0,text = 8,)
        self._label_52 = tkinter.Label(root,activebackground = "#d7ffd7",background = "#d7ffd7",font = "{MS Sans Serif} 8 bold",padx = 0,pady = 0,text = "B+",)
        self._label_53 = tkinter.Label(root,activebackground = "#d7ffd7",background = "#d7ffd7",font = "{MS Sans Serif} 8 bold",padx = 0,pady = 0,text = 7,)
        self._label_54 = tkinter.Label(root,activebackground = "#d7ffd7",background = "#d7ffd7",font = "{MS Sans Serif} 8 bold",padx = 0,pady = 0,text = "B",)
        self._label_55 = tkinter.Label(root,activebackground = "#d7ffd7",background = "#d7ffd7",font = "{MS Sans Serif} 8 bold",padx = 0,pady = 0,text = 6,)
        self._label_56 = tkinter.Label(root,activebackground = "#d2ffd2",background = "#d2ffd2",font = "{MS Sans Serif} 8 bold",padx = 0,pady = 0,text = "C+",)
        self._label_57 = tkinter.Label(root,activebackground = "#d2ffd2",background = "#d2ffd2",font = "{MS Sans Serif} 8 bold",padx = 0,pady = 0,text = 5,)
        self._label_58 = tkinter.Label(root,activebackground = "#d2ffd2",background = "#d2ffd2",font = "{MS Sans Serif} 8 bold",padx = 0,pady = 0,text = "C",)
        self._label_59 = tkinter.Label(root,activebackground = "#d2ffd2",background = "#d2ffd2",font = "{MS Sans Serif} 8 bold",padx = 0,pady = 0,text = 4,)
        self._label_11 = tkinter.Label(self._frame_24,activebackground = "#b87070",background = "#b87070",font = "{MS Sans Serif} 8 bold",text = "Course Title",)
        self._label_15 = tkinter.Label(self._frame_24,activebackground = "#b87070",background = "#b87070",font = "{MS Sans Serif} 8 bold",text = "Course Code",)
        self._label_17 = tkinter.Label(self._frame_24,activebackground = "#b87070",background = "#b87070",font = "{MS Sans Serif} 8 bold",text = "Credit",)
        self._label_18 = tkinter.Label(self._frame_24,activebackground = "#b87070",background = "#b87070",font = "{MS Sans Serif} 8 bold",text = "Grade Obtained",)
        self._label_4 = tkinter.Label(root,activebackground = "#d2ffd2",background = "#d2ffd2",font = "{MS Sans Serif} 8 bold",padx = 0,pady = 0,text = "E (Reappear)",)
        self._label_8 = tkinter.Label(root,
            activebackground = "#d2ffd2",
            background = "#d2ffd2",
            font = "{MS Sans Serif} 8 bold",
            padx = 0,
            pady = 0,
            text = "G (Backlog)",
        )
        self._label_9 = tkinter.Label(root,
            activebackground = "#d2ffd2",
            background = "#d2ffd2",
            font = "{MS Sans Serif} 8 bold",
            padx = 0,
            pady = 0,
            text = "  I (Result Incomplete)",
        )
        self._label_19 = tkinter.Label(root,
            activebackground = "#d2ffd2",
            background = "#d2ffd2",
            font = "{MS Sans Serif} 8 bold",
            padx = 0,
            pady = 0,
            text = "F (Fail)",
        )
        self._label_26 = tkinter.Label(root,
            activebackground = "#d2ffd2",
            background = "#d2ffd2",
            font = "{MS Sans Serif} 8 bold",
            padx = 0,
            pady = 0,
            text = 0,
        )
        self._label_27 = tkinter.Label(root,
            activebackground = "#d2ffd2",
            background = "#d2ffd2",
            font = "{MS Sans Serif} 8 bold",
            padx = 0,
            pady = 0,
            text = 0,
        )
        self._label_28 = tkinter.Label(root,
            activebackground = "#d2ffd2",
            background = "#d2ffd2",
            font = "{MS Sans Serif} 8 bold",
            padx = 0,
            pady = 0,
            text = 0,
        )
        self._label_29 = tkinter.Label(root,
            activebackground = "#d2ffd2",
            background = "#d2ffd2",
            font = "{MS Sans Serif} 8 bold",
            padx = 0,
            pady = 0,
            text = 0,
        )
        self.secondtgpa = tkinter.Button(root,
            activebackground = "#b9b9ff",
            background = "#b9b9ff",
            borderwidth = 5,
            cursor = "hand2",
            font = "{MS Sans Serif} 5 bold",
            text = "Calculate TGPA",
        )
        self.secondtgpavalue = tkinter.Label(root,
            activebackground = "#ffffb3",
            activeforeground = "#ff0000",
            background = "#ffffb3",
            font = "{MS Sans Serif} 17 bold",
            foreground = "#ff0000",
            text = 0.00,
        )
        self.secondsub1 = tkinter.Entry(self._frame_22,
            justify = "center",
            width = 35,
        )
        self.secondcourse1 = tkinter.Entry(self._frame_23,
            justify = "center",
            width = 10,
        )
        self.secondcredit1 = tkinter.Entry(self._frame_25,
            justify = "center",
            width = 0,
        )
        self.secondgrade1 = tkinter.Entry(self._frame_26,
            justify = "center",
            width = 0,
        )
        self.secondsub2 = tkinter.Entry(self._frame_27,
            justify = "center",
            width = 35,
        )
        self.secondcourse2 = tkinter.Entry(self._frame_28,
            justify = "center",
            width = 10,
        )
        self.secondcredit2 = tkinter.Entry(self._frame_29,
            justify = "center",
            width = 0,
        )
        self.secondgrade2 = tkinter.Entry(self._frame_30,
            justify = "center",
            width = 0,
        )
        self.secondsub3 = tkinter.Entry(self._frame_34,
            justify = "center",
            width = 35,
        )
        self.secondcourse3 = tkinter.Entry(self._frame_33,
            justify = "center",
            width = 10,
        )
        self.secondcredit3 = tkinter.Entry(self._frame_32,
            justify = "center",
            width = 0,
        )
        self.secondgrade3 = tkinter.Entry(self._frame_42,
            justify = "center",
            width = 0,
        )
        self.secondsub4 = tkinter.Entry(self._frame_43,
            justify = "center",
            width = 35,
        )
        self.secondcourse4 = tkinter.Entry(self._frame_44,
            justify = "center",
            width = 10,
        )
        self.secondcredit4 = tkinter.Entry(self._frame_45,
            justify = "center",
            width = 0,
        )
        self.secondgrade4 = tkinter.Entry(self._frame_46,
            justify = "center",
            width = 0,
        )
        self.cgpa = tkinter.Button(root,
            activebackground = "#ff6464",
            background = "#ff6464",
            borderwidth = 5,
            cursor = "hand2",
            font = "{Times New Roman Baltic} 17 bold",
            text = "Calculate CGPA",
        )
        self._label_31 = tkinter.Label(root,
            activebackground = "#e0c2c2",
            activeforeground = "#333333",
            background = "#e0c2c2",
            font = "{MS Sans Serif} 10 bold italic",
            foreground = "#333333",
            text = "Made with \u2764  by Akash					\u00A92018-2019",
        )
        self._label_7 = tkinter.Label(root,
            activebackground = "#c89191",
            background = "#c89191",
            font = "{MS Sans Serif} 8 bold",
            text = """PLease find your CGPA and Remarks and
 take steps for improvements""",
        )
        self.open = tkinter.Button(root,
            activebackground = "#c4c0fe",
            background = "#c4c0fe",
            borderwidth = 5,
            cursor = "hand2",
            font = "{Franklin Gothic Heavy} 12",
            text = "Open",
        )
        self.save = tkinter.Button(root,
            activebackground = "#c4c0fe",
            background = "#c4c0fe",
            borderwidth = 5,
            cursor = "hand2",
            font = "{Franklin Gothic Heavy} 12",
            text = "Save",
        )
        self._label_23 = tkinter.Label(root,
            activebackground = "#c89191",
            activeforeground = "#000000",
            background = "#c89191",
            font = "{MS Gothic} 10 bold",
            foreground = "#000000",
            text = "Grade Point Consideration	",
        )
        self._label_32 = tkinter.Label(root,
            activebackground = "#ceffff",
            background = "#ceffff",
            font = "{Wide Latin} 17",
            text = """Your
 CGPA
 is :""",
        )
        self.cgpavalue = tkinter.Label(root,
            activebackground = "#ceffff",
            activeforeground = "#ff0000",
            background = "#ceffff",
            font = "{MS Sans Serif} 30 bold",
            foreground = "#ff0000",
            text = 0.00,
        )
        self.remark = tkinter.Label(root,
            activebackground = "#ff2f2f",
            background = "#ff2f2f",
            font = "{MS Sans Serif} 8 bold",
            text = "Instructions",
        )
        self.remarkvalue = tkinter.Label(root,
            activebackground = "#000000",
            activeforeground = "#ffffff",
            background = "#000000",
            font = "{MS Sans Serif} 8 bold",
            foreground = "#ffffff",
            justify = "left",
            text = """
Follow the instructions
********************************************************
1. Enter reg no and open, if found, name
and all course details will be displayed, if not
2. Enter all the details like name, reg no and
course details, then Save.
3. Enter credits of each subjects and grade
obtained in that subject for each semester.
4. Calculate TGPA for both semesters.
5. Finally Press CGPA.
6. CGPA is calculated using the formula given.
The grade point considered is for LPU students.
7. CGPA will be displayed along with helpful
remarks which will guide students for their
improvements in CGPA for better future.

********************************************************""",
        )

        # widget commands
        self.firsttgpa.configure(
            command = self.firsttgpa_command
        )
        self.secondtgpa.configure(
            command = self.secondtgpa_command
        )
        self.cgpa.configure(
            command = self.cgpa_command
        )
        self.open.configure(
            command = self.open_command
        )
        self.save.configure(
            command = self.save_command
        )


        # Geometry Management
        self._labelframe_3.grid(
            in_ = root,
            column = 1,
            row = 3,
            columnspan = 4,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "news"
        )
        self._frame_1.grid(
            in_ = root,
            column = 1,
            row = 4,
            columnspan = 4,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "news"
        )
        self._frame_2.grid(
            in_ = root,
            column = 1,
            row = 6,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "news"
        )
        self._frame_3.grid(
            in_ = root,
            column = 2,
            row = 6,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "news"
        )
        self._frame_4.grid(
            in_ = root,
            column = 3,
            row = 6,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "news"
        )
        self._frame_5.grid(
            in_ = root,
            column = 4,
            row = 6,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "news"
        )
        self._frame_6.grid(
            in_ = root,
            column = 1,
            row = 7,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "news"
        )
        self._frame_7.grid(
            in_ = root,
            column = 2,
            row = 7,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "news"
        )
        self._frame_8.grid(
            in_ = root,
            column = 3,
            row = 7,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "news"
        )
        self._frame_9.grid(
            in_ = root,
            column = 4,
            row = 7,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "news"
        )
        self._frame_10.grid(
            in_ = root,
            column = 1,
            row = 8,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "news"
        )
        self._frame_11.grid(
            in_ = root,
            column = 2,
            row = 8,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "news"
        )
        self._frame_12.grid(
            in_ = root,
            column = 3,
            row = 8,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "news"
        )
        self._frame_13.grid(
            in_ = root,
            column = 4,
            row = 8,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "news"
        )
        self._frame_14.grid(
            in_ = root,
            column = 1,
            row = 9,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "news"
        )
        self._frame_15.grid(
            in_ = root,
            column = 2,
            row = 9,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "news"
        )
        self._frame_16.grid(
            in_ = root,
            column = 3,
            row = 9,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "news"
        )
        self._frame_17.grid(
            in_ = root,
            column = 4,
            row = 9,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "news"
        )
        self._frame_18.grid(
            in_ = root,
            column = 1,
            row = 10,
            columnspan = 2,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "news"
        )
        self._frame_20.grid(
            in_ = root,
            column = 1,
            row = 11,
            columnspan = 4,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "news"
        )
        self._frame_24.grid(
            in_ = root,
            column = 1,
            row = 12,
            columnspan = 4,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "news"
        )
        self._frame_22.grid(
            in_ = root,
            column = 1,
            row = 13,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "news"
        )
        self._frame_23.grid(
            in_ = root,
            column = 2,
            row = 13,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "news"
        )
        self._frame_25.grid(
            in_ = root,
            column = 3,
            row = 13,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "news"
        )
        self._frame_26.grid(
            in_ = root,
            column = 4,
            row = 13,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "news"
        )
        self._frame_27.grid(
            in_ = root,
            column = 1,
            row = 14,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "news"
        )
        self._frame_28.grid(
            in_ = root,
            column = 2,
            row = 14,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "news"
        )
        self._frame_29.grid(
            in_ = root,
            column = 3,
            row = 14,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "news"
        )
        self._frame_30.grid(
            in_ = root,
            column = 4,
            row = 14,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "news"
        )
        self._frame_32.grid(
            in_ = root,
            column = 3,
            row = 15,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "news"
        )
        self._frame_33.grid(
            in_ = root,
            column = 2,
            row = 15,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "news"
        )
        self._frame_34.grid(
            in_ = root,
            column = 1,
            row = 15,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "news"
        )
        self._frame_35.grid(
            in_ = root,
            column = 1,
            row = 17,
            columnspan = 2,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "news"
        )
        self._frame_42.grid(
            in_ = root,
            column = 4,
            row = 15,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "news"
        )
        self._frame_43.grid(
            in_ = root,
            column = 1,
            row = 16,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "news"
        )
        self._frame_44.grid(
            in_ = root,
            column = 2,
            row = 16,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "news"
        )
        self._frame_45.grid(
            in_ = root,
            column = 3,
            row = 16,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "news"
        )
        self._frame_46.grid(
            in_ = root,
            column = 4,
            row = 16,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "news"
        )
        self._label_1.grid(
            in_ = root,
            column = 1,
            row = 1,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 2,
            sticky = "nsew"
        )
        self._label_2.grid(
            in_ = root,
            column = 2,
            row = 1,
            columnspan = 8,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "nsew"
        )
        self._label_3.grid(
            in_ = root,
            column = 2,
            row = 2,
            columnspan = 8,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "nsew"
        )
        self._label_5.grid(
            in_ = self._labelframe_3,
            column = 1,
            row = 1,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "e"
        )
        self.name.grid(
            in_ = self._labelframe_3,
            column = 2,
            row = 1,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "ew"
        )
        self._label_6.grid(
            in_ = self._labelframe_3,
            column = 3,
            row = 1,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "e"
        )
        self.regno.grid(
            in_ = self._labelframe_3,
            column = 4,
            row = 1,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "ew"
        )
        self._label_10.grid(
            in_ = root,
            column = 8,
            row = 3,
            columnspan = 2,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 2,
            sticky = "nsew"
        )
        self._label_12.grid(
            in_ = self._frame_1,
            column = 1,
            row = 1,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "w"
        )
        self._label_13.grid(
            in_ = root,
            column = 1,
            row = 5,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "nsew"
        )
        self._label_14.grid(
            in_ = root,
            column = 2,
            row = 5,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "nsew"
        )
        self._label_16.grid(
            in_ = root,
            column = 3,
            row = 5,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "nsew"
        )
        self._label_20.grid(
            in_ = root,
            column = 4,
            row = 5,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "nsew"
        )
        self.firstsub1.grid(
            in_ = self._frame_2,
            column = 1,
            row = 1,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "ew"
        )
        self.firstcourse1.grid(
            in_ = self._frame_3,
            column = 1,
            row = 1,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "ew"
        )
        self.firstcredit1.grid(
            in_ = self._frame_4,
            column = 1,
            row = 1,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "ew"
        )
        self.firstgrade1.grid(
            in_ = self._frame_5,
            column = 1,
            row = 1,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "ew"
        )
        self.firstsub2.grid(
            in_ = self._frame_6,
            column = 1,
            row = 1,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "ew"
        )
        self.firstcourse2.grid(
            in_ = self._frame_7,
            column = 1,
            row = 1,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "ew"
        )
        self.firstcredit2.grid(
            in_ = self._frame_8,
            column = 1,
            row = 1,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "ew"
        )
        self.firstgrade2.grid(
            in_ = self._frame_9,
            column = 1,
            row = 1,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "ew"
        )
        self.firstsub3.grid(
            in_ = self._frame_10,
            column = 1,
            row = 1,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "ew"
        )
        self.firstcourse3.grid(
            in_ = self._frame_11,
            column = 1,
            row = 1,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "ew"
        )
        self.firstcredit3.grid(
            in_ = self._frame_12,
            column = 1,
            row = 1,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "ew"
        )
        self.firstgrade3.grid(
            in_ = self._frame_13,
            column = 1,
            row = 1,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "ew"
        )
        self.firstsub4.grid(
            in_ = self._frame_14,
            column = 1,
            row = 1,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "ew"
        )
        self.firstcourse4.grid(
            in_ = self._frame_15,
            column = 1,
            row = 1,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "ew"
        )
        self.firstcredit4.grid(
            in_ = self._frame_16,
            column = 1,
            row = 1,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "ew"
        )
        self.firstgrade4.grid(
            in_ = self._frame_17,
            column = 1,
            row = 1,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "ew"
        )
        self.firsttgpa.grid(
            in_ = root,
            column = 3,
            row = 10,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "nsew"
        )
        self.firsttgpavalue.grid(
            in_ = root,
            column = 4,
            row = 10,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "nsew"
        )
        self._label_22.grid(
            in_ = root,
            column = 5,
            row = 5,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "nsew"
        )
        self._label_24.grid(
            in_ = root,
            column = 6,
            row = 5,
            columnspan = 2,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "nsew"
        )
        self._label_25.grid(
            in_ = root,
            column = 5,
            row = 6,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "nsew"
        )
        self._label_39.grid(
            in_ = self._frame_20,
            column = 1,
            row = 1,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "w"
        )
        self._label_47.grid(
            in_ = root,
            column = 6,
            row = 6,
            columnspan = 2,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "nsew"
        )
        self._label_48.grid(
            in_ = root,
            column = 5,
            row = 7,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "nsew"
        )
        self._label_49.grid(in_ = root,column = 6,row = 7,columnspan = 2,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self._label_50.grid(in_ = root,column = 5,row = 8,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self._label_51.grid(in_ = root,column = 6,row = 8,columnspan = 2,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self._label_52.grid(in_ = root,column = 5,row = 9,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self._label_53.grid(in_ = root,column = 6,row = 9,columnspan = 2,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self._label_54.grid(in_ = root,column = 5,row = 10,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self._label_55.grid(in_ = root,column = 6, row = 10, columnspan = 2, ipadx = 0, ipady = 0, padx = 0, pady = 0,rowspan = 1,sticky = "nsew")
        self._label_56.grid(in_ = root,column = 5,row = 11,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self._label_57.grid(in_ = root,column = 6,row = 11,columnspan = 2,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self._label_58.grid(in_ = root,column = 5,row = 12,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self._label_59.grid(in_ = root,column = 6,row = 12,columnspan = 2,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self._label_11.grid(in_ = self._frame_24,column = 1,row = 1,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self._label_15.grid(in_ = self._frame_24,column = 2,row = 1,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self._label_17.grid(in_ = self._frame_24,column = 3,row = 1,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self._label_18.grid(in_ = self._frame_24,column = 4,row = 1,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self._label_4.grid(in_ = root,column = 5,row = 13,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self._label_8.grid(in_ = root,column = 5,row = 15,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self._label_9.grid(in_ = root,column = 5,row = 16,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self._label_19.grid(in_ = root,column = 5,row = 14,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self._label_26.grid(in_ = root,column = 6,row = 13,columnspan = 2,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self._label_27.grid(in_ = root,column = 6,row = 14,columnspan = 2,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self._label_28.grid(in_ = root,column = 6,row = 15,columnspan = 2,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self._label_29.grid(in_ = root,column = 6,row = 16,columnspan = 2,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self.secondtgpa.grid(in_ = root,column = 3,row = 17,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self.secondtgpavalue.grid(in_ = root,column = 4,row = 17,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self.secondsub1.grid(in_ = self._frame_22,column = 1,row = 1,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "ew")
        self.secondcourse1.grid(in_ = self._frame_23,column = 1,row = 1,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "ew")
        self.secondcredit1.grid(in_ = self._frame_25,column = 1,row = 1,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "ew")
        self.secondgrade1.grid(in_ = self._frame_26,column = 1,row = 1,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "ew")
        self.secondsub2.grid(in_ = self._frame_27,column = 1,row = 1,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "ew")
        self.secondcourse2.grid(in_ = self._frame_28,column = 1,row = 1,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "ew")
        self.secondcredit2.grid(in_ = self._frame_29,column = 1,row = 1,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "ew")
        self.secondgrade2.grid(in_ = self._frame_30,column = 1,row = 1,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "ew")
        self.secondsub3.grid(in_ = self._frame_34,column = 1,row = 1,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "ew")
        self.secondcourse3.grid(in_ = self._frame_33,column = 1,row = 1,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "ew")
        self.secondcredit3.grid(in_ = self._frame_32,column = 1,row = 1,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "ew")
        self.secondgrade3.grid(in_ = self._frame_42,column = 1,row = 1,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "ew")
        self.secondsub4.grid(in_ = self._frame_43,column = 1,row = 1,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "ew")
        self.secondcourse4.grid(in_ = self._frame_44,column = 1,row = 1,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "ew")
        self.secondcredit4.grid(in_ = self._frame_45,column = 1,row = 1,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "ew")
        self.secondgrade4.grid(in_ = self._frame_46,column = 1,row = 1,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "ew")
        self.cgpa.grid(in_ = root,column = 5,row = 17,columnspan = 3,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 2,sticky = "nsew")
        self._label_31.grid(in_ = root,column = 1,row = 18,columnspan = 4,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self._label_7.grid(in_ = root,column = 8,row = 5,columnspan = 2,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 2,sticky = "nsew")
        self.open.grid(in_ = root,column = 5,row = 3,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self.save.grid(in_ = root,column = 6,row = 3,columnspan = 2,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self._label_23.grid(in_ = root,column = 5,row = 4,columnspan = 3,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self._label_32.grid(in_ = root,column = 8,row = 7,columnspan = 2,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 3,sticky = "nsew")
        self.cgpavalue.grid(in_ = root,column = 8,row = 10,columnspan = 2,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 2,sticky = "nsew")
        self.remark.grid(in_ = root,column = 8,row = 12,columnspan = 2,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self.remarkvalue.grid(in_ = root,column = 8,row = 13,columnspan = 2,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 6,sticky = "nsew")

        # Resize Behavior
        root.grid_rowconfigure(1, weight = 1, minsize = 54, pad = 0)
        root.grid_rowconfigure(2, weight = 0, minsize = 7, pad = 0)
        root.grid_rowconfigure(3, weight = 1, minsize = 12, pad = 0)
        root.grid_rowconfigure(4, weight = 0, minsize = 5, pad = 0)
        root.grid_rowconfigure(5, weight = 0, minsize = 6, pad = 0)
        root.grid_rowconfigure(6, weight = 1, minsize = 6, pad = 0)
        root.grid_rowconfigure(7, weight = 0, minsize = 40, pad = 0)
        root.grid_rowconfigure(8, weight = 0, minsize = 40, pad = 0)
        root.grid_rowconfigure(9, weight = 0, minsize = 40, pad = 0)
        root.grid_rowconfigure(10, weight = 0, minsize = 40, pad = 0)
        root.grid_rowconfigure(11, weight = 0, minsize = 40, pad = 0)
        root.grid_rowconfigure(12, weight = 0, minsize = 5, pad = 0)
        root.grid_rowconfigure(13, weight = 1, minsize = 35, pad = 0)
        root.grid_rowconfigure(14, weight = 0, minsize = 40, pad = 0)
        root.grid_rowconfigure(15, weight = 0, minsize = 40, pad = 0)
        root.grid_rowconfigure(16, weight = 0, minsize = 40, pad = 0)
        root.grid_rowconfigure(17, weight = 0, minsize = 40, pad = 0)
        root.grid_rowconfigure(18, weight = 0, minsize = 1, pad = 0)
        root.grid_columnconfigure(1, weight = 0, minsize = 241, pad = 0)
        root.grid_columnconfigure(2, weight = 1, minsize = 158, pad = 0)
        root.grid_columnconfigure(3, weight = 1, minsize = 125, pad = 0)
        root.grid_columnconfigure(4, weight = 1, minsize = 116, pad = 0)
        root.grid_columnconfigure(5, weight = 0, minsize = 5, pad = 0)
        root.grid_columnconfigure(6, weight = 0, minsize = 71, pad = 0)
        root.grid_columnconfigure(7, weight = 0, minsize = 50, pad = 0)
        root.grid_columnconfigure(8, weight = 0, minsize = 44, pad = 0)
        root.grid_columnconfigure(9, weight = 0, minsize = 189, pad = 0)
        self._frame_1.grid_rowconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_1.grid_columnconfigure(1, weight = 0, minsize = 68, pad = 0)
        self._frame_10.grid_rowconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_10.grid_columnconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_11.grid_rowconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_11.grid_columnconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_12.grid_rowconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_12.grid_columnconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_13.grid_rowconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_13.grid_columnconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_14.grid_rowconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_14.grid_columnconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_15.grid_rowconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_15.grid_columnconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_16.grid_rowconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_16.grid_columnconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_17.grid_rowconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_17.grid_columnconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_2.grid_rowconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_2.grid_columnconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_20.grid_rowconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_20.grid_columnconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_22.grid_rowconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_22.grid_columnconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_23.grid_rowconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_23.grid_columnconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_24.grid_rowconfigure(1, weight = 0, minsize = 5, pad = 0)
        self._frame_24.grid_columnconfigure(1, weight = 0, minsize = 240, pad = 0)
        self._frame_24.grid_columnconfigure(2, weight = 0, minsize = 181, pad = 0)
        self._frame_24.grid_columnconfigure(3, weight = 0, minsize = 175, pad = 0)
        self._frame_24.grid_columnconfigure(4, weight = 1, minsize = 67, pad = 0)
        self._frame_25.grid_rowconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_25.grid_columnconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_26.grid_rowconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_26.grid_columnconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_27.grid_rowconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_27.grid_columnconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_28.grid_rowconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_28.grid_columnconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_29.grid_rowconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_29.grid_columnconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_3.grid_rowconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_3.grid_columnconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_30.grid_rowconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_30.grid_columnconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_32.grid_rowconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_32.grid_columnconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_33.grid_rowconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_33.grid_columnconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_34.grid_rowconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_34.grid_columnconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_4.grid_rowconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_4.grid_columnconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_42.grid_rowconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_42.grid_columnconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_43.grid_rowconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_43.grid_columnconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_44.grid_rowconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_44.grid_columnconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_45.grid_rowconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_45.grid_columnconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_46.grid_rowconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_46.grid_columnconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_5.grid_rowconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_5.grid_columnconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_6.grid_rowconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_6.grid_columnconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_7.grid_rowconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_7.grid_columnconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_8.grid_rowconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_8.grid_columnconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_9.grid_rowconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_9.grid_columnconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._labelframe_3.grid_rowconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._labelframe_3.grid_columnconfigure(1, weight = 0, minsize = 14, pad = 0)
        self._labelframe_3.grid_columnconfigure(2, weight = 0, minsize = 17, pad = 0)
        self._labelframe_3.grid_columnconfigure(3, weight = 0, minsize = 56, pad = 0)
        self._labelframe_3.grid_columnconfigure(4, weight = 0, minsize = 138, pad = 0)

class CustomMain(Main):
    print("Main Window Opened.")
    pass
    print("Login Successful")
    messagebox.showinfo("Success", u"Login Successful..!!!\u263A\u263A\u263A")

    def firsttgpa_command(self, ):
        try:
            print("Semester1 TGPA Button Pressed.")
            list = ['O', 'o', 'A+', 'a+', 'A', 'a', 'B+', 'b+', 'B', 'b', 'C+', 'c+', 'c', 'C', 'E', 'e', 'F', 'f', 'g',
                    'G', 'I', 'i']
            num = [1,2,3,4,5,6,7,8,9,0]
            if (self.firstgrade1.get() in list) and (self.firstgrade2.get() in list) and (self.firstgrade3.get() in list) and \
            (self.firstgrade4.get() in list) and (int(self.firstcredit1.get()) in num) and (int(self.firstcredit2.get()) in num) and \
            (int(self.firstcredit3.get()) in num) and (int(self.firstcredit4.get()) in num):

                a1, b1, c1, d1 = self.firstcredit1.get(), self.firstcredit2.get(), self.firstcredit3.get(), self.firstcredit4.get()
                credit1.append(int(a1))
                credit1.append(int(b1))
                credit1.append(int(c1))
                credit1.append(int(d1))
                print(credit1)
                e1, f1, g1, h1 = self.firstgrade1.get(), self.firstgrade2.get(), self.firstgrade3.get(), self.firstgrade4.get()
                e1 = e1.upper()
                grade1.append(e1)
                f1 = f1.upper()
                grade1.append(f1)
                g1 = g1.upper()
                grade1.append(g1)
                h1 = h1.upper()
                grade1.append(h1)
                print(grade1)
                y = 0
                while (y < 4):
                    if (grade1[y] == "O"):
                        number = 10
                        grade1point.append(number)
                    elif (grade1[y] == "A+"):
                        number = 9
                        grade1point.append(number)
                    elif (grade1[y] == "A"):
                        number = 8
                        grade1point.append(number)
                    elif (grade1[y] == "B+"):
                        number = 7
                        grade1point.append(number)
                    elif (grade1[y] == "B"):
                        number = 6
                        grade1point.append(number)
                    elif (grade1[y] == "C+"):
                        number = 5
                        grade1point.append(number)
                    elif (grade1[y] == "C"):
                        number = 4
                        grade1point.append(number)
                    elif (grade1[y] == "D+"):
                        number = 3
                        grade1point.append(number)
                    elif (grade1[y] == "D"):
                        number = 2
                        grade1point.append(number)
                    elif (grade1[y] == "E"):
                        number = 0
                        grade1point.append(number)
                    y = y + 1
                print(grade1point)
                i = 0
                self.tgpa1, first_part1, second_part1 = 0.00, 0, 0
                while (i < 4):
                    first_part1 += credit1[i] * grade1point[i]
                    second_part1 += credit1[i]
                    i = i + 1
                self.tgpa1 = first_part1 / second_part1
                self.tgpa1 = "{:.2f}".format(self.tgpa1)
                print(self.tgpa1)
                self.firsttgpavalue["text"] = self.tgpa1
            else:
                messagebox.showinfo("Information","Please choose credit and grades from following values only.\n\n Grades = [ 'O' , 'o' , 'A+' , 'a+' , 'A' , 'a' , 'B+' , 'b+' , 'B' , 'b' , 'C+' , 'c+' , 'c' , 'C' , 'E' , 'e' , 'F' , 'f' , 'g' ,'G' , 'I' , 'i' ]\n\nCredits = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 0 ]")
        except:
            messagebox.showerror("Error", "Something went wrong..!!!\nPlease contact Admin: +917004250668")
        pass

    def secondtgpa_command(self):
        try:
            print("Semester2 TGPA Button Pressed.")
            list = ['O', 'o', 'A+', 'a+', 'A', 'a', 'B+', 'b+', 'B', 'b', 'C+', 'c+', 'c', 'C', 'E', 'e', 'F', 'f', 'g','G', 'I', 'i' ]
            num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
            if (self.firstgrade1.get() in list) and (self.firstgrade2.get() in list) and (self.firstgrade3.get() in list) and\
                (self.firstgrade4.get() in list) and (int(self.firstcredit1.get()) in num) and (int(self.firstcredit2.get()) in num) and \
                                                       (int(self.firstcredit3.get()) in num) and (int(self.firstcredit4.get()) in num):
                a2, b2, c2, d2 = self.secondcredit1.get(), self.secondcredit2.get(), self.secondcredit3.get(), self.secondcredit4.get()
                credit2.append(int(a2))
                credit2.append(int(b2))
                credit2.append(int(c2))
                credit2.append(int(d2))
                print(credit2)
                e2, f2, g2, h2 = self.secondgrade1.get(), self.secondgrade2.get(), self.secondgrade3.get(), self.secondgrade4.get()
                e2 = e2.upper()
                grade2.append(e2)
                f2 = f2.upper()
                grade2.append(f2)
                g2 = g2.upper()
                grade2.append(g2)
                h2 = h2.upper()
                grade2.append(h2)
                print(grade2)
                z = 0
                while (z < 4):
                    if (grade2[z] == "O"):
                        number = 10
                        grade2point.append(number)
                    elif (grade2[z] == "A+"):
                        number = 9
                        grade2point.append(number)
                    elif (grade2[z] == "A"):
                        number = 8
                        grade2point.append(number)
                    elif (grade2[z] == "B+"):
                        number = 7
                        grade2point.append(number)
                    elif (grade2[z] == "B"):
                        number = 6
                        grade2point.append(number)
                    elif (grade2[z] == "C+"):
                        number = 5
                        grade2point.append(number)
                    elif (grade2[z] == "C"):
                        number = 4
                        grade2point.append(number)
                    elif (grade2[z] == "D+"):
                        number = 3
                        grade2point.append(number)
                    elif (grade2[z] == "D"):
                        number = 2
                        grade2point.append(number)
                    elif (grade2[z] == "E"):
                        number = 0
                        grade2point.append(number)
                    z = z + 1
                print(grade2point)
                j = 0
                self.tgpa2, first_part2, second_part2 = 0.00, 0, 0
                while (j < 4):
                    first_part2 += credit2[j] * grade2point[j]
                    second_part2 += credit2[j]
                    j = j + 1
                self.tgpa2 = first_part2 / second_part2
                self.tgpa2 = "{:.2f}".format(self.tgpa2)
                print(self.tgpa2)
                self.secondtgpavalue["text"] = self.tgpa2
                print("tgpa1=", self.tgpa1)
                print("tgpa2=", self.tgpa2)
            else:
                messagebox.showinfo("Information",
                                    "Please choose credit and grades from following values only.\n\n Grades = [ 'O' , 'o' , 'A+' , 'a+' , 'A' , 'a' , 'B+' , 'b+' , 'B' , 'b' , 'C+' , 'c+' , 'c' , 'C' , 'E' , 'e' , 'F' , 'f' , 'g' ,'G' , 'I' , 'i' ]\n\nCredits= [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 0 ]")
        except:
            messagebox.showerror("Error", "Something went wrong..!!!\nPlease contact Admin: +917004250668")
        pass

    def cgpa_command(self, ):
        try:
            print("CGPA Button Pressed.")
            if self.name.get()=="" and self.firstcredit1.get()=="" and self.firstcredit2.get()=="" and self.firstcredit3.get()=="" and\
                    self.firstcredit4.get()=="" and self.secondcredit1.get()=="" and self.secondcredit2.get()=="" and self.secondcredit3.get()=="" and\
                    self.secondcredit4.get()=="" and self.firstgrade1.get()=="" and self.firstgrade2.get()=="" and self.firstgrade3.get()=="" and\
                    self.firstgrade4.get()=="" and self.secondgrade1.get()=="" and self.secondgrade2.get()=="" and self.secondgrade3.get()=="" and\
                    self.secondgrade4.get()=="":
                messagebox.showwarning("Warning..!!","Provide all required details\nthen Proceed.")
            else:
                self.cgp = (float(self.firsttgpavalue['text']) + float(self.secondtgpavalue['text'])) / 2
                self.cgp = "{:.2f}".format(self.cgp)
                self.cgpavalue['text'] = str(self.cgp)

                #remarks
                self.remark["text"] = "Remarks"
                if float(self.cgpavalue['text']) > 9 and float(self.cgpavalue['text']) <=10:
                    self.remarkvalue["text"] = u"""******************************************************
        
Dear """+self.name.get()+""",
    
Your performance is outstanding. You should
maintain the same performance for the best 
future.
You are well going.
All the best for your future and remember to 
keep working hard always...!!! \u263A\u263A\u263A
    
******************************************************"""
                elif float(self.cgpavalue['text']) > 8 and float(self.cgpavalue['text']) <= 9:
                    self.remarkvalue["text"]=u"""******************************************************
        
Dear """+self.name.get()+""",
    
Your performance is Excellent.
Try to make some more improvement in order to
grap the position in the first.
Overall performance is excellent.
All the best for your future and remember to 
keep working hard always...!!! \u263A\u263A\u263A
    
******************************************************"""
                elif float(self.cgpavalue['text']) > 7 and float(self.cgpavalue['text']) <= 8:
                    self.remarkvalue["text"]=u"""******************************************************
        
    Dear """+self.name.get()+""",
        
    Your performance is Very Good.
    But you still need to work hard in order to have
    a good future. So do some more efforts. Do new
    experiments in studies so that you can grab the
    first position. 
    All the best for your future and remember to 
    keep working hard always...!!! \u263A\u263A\u263A 
        
    ******************************************************"""
                elif float(self.cgpavalue['text']) > 6 and float(self.cgpavalue['text']) <= 7:
                    self.remarkvalue["text"]=u"""******************************************************
        
Dear """+self.name.get()+""",
    
Your performance is just Good.
you need to work hard in order to have a good
future. It's neither good nor bad.
You can do much better than this. Just focus 
on your studies.
All the best for your future and remember to 
Keep working hard always...!!! \u263A\u263A\u263A 
    
******************************************************"""
                elif float(self.cgpavalue['text']) > 5 and float(self.cgpavalue['text']) <= 6:
                    self.remarkvalue["text"] =u"""******************************************************
        
Dear """+self.name.get()+""",
    
Your performance is Fair.
Lots of hard work is required. You have to make
your goals. Just implement your qualities and
utilise it well.
Just focus on your studies.
All the best for your future and remember to 
keep working hard always...!!! \u263A\u263A\u263A 

******************************************************"""
                elif float(self.cgpavalue['text']) > 4 and float(self.cgpavalue['text']) <= 5:
                    self.remarkvalue["text"] =u"""******************************************************
        
Dear """+self.name.get()+""",
    
Your performance is Below Average.
You are just passed. you need to work hard for 
improvement.
Just be serious and focus on your studies.
Much improvements and hard work is required.
All the best for your future and remember to 
keep working hard always...!!! \u263A\u263A\u263A 
    
******************************************************"""
                elif float(self.cgpavalue['text']) <= 4:
                    self.remarkvalue["text"] =u"""******************************************************
Dear """+self.name.get()+""",        

        
You have Failed.
You are not giving sufficient time for your 
studies as per required. Just think about goals
and start studying.
Or else you will surely gonna spoil your future.
Be serious and focus on your studies.
Much improvements and hard work is required.
All the best for your future...!!! \u263A\u263A\u263A 
        
******************************************************"""
        except:
            messagebox.showerror("Error", "Something went wrong..!!!\nPlease contact Admin: +917004250668")
        pass

    def open_command(self):
        try:
            print("Open Button Pressed.")
            ob = sqlite3.connect("database.db")
            cur = ob.cursor()
            list=[]
            list2=[]
            pos=0
            i=0
            #to retrieve student data from database
            cur.execute("""select * from studentdetails;""")
            while True:
                records = cur.fetchone()
                if records == None:
                    break
                if self.regno.get() == str(records[0]):
                    list.append(str(records[0]))
                    list2.append(records)
                    pos = i
                    break
                i+=1
            print("list=",list)
            if self.regno.get() not in list:
                messagebox.showerror("Error", "SORRY..!!\nData not found.\n\nPlease fill the details and Save.")
                flag=1
            else:
                self.regno.delete(0, END)
                self.regno.insert(0,str(list2[pos][0]))
                self.name.delete(0, END)
                self.name.insert(0,list2[pos][1])
                flag=0
            ob.commit()
            ob.close()

            if flag==0:
                obc = sqlite3.connect("database.db")
                curr = obc.cursor()
                # to retrieve course data from database
                curr.execute("""select * from coursedetails;""")
                record = curr.fetchall()
                for i in range(0,len(record)):
                    if self.regno.get() == str(record[i][0]):
                        self.firstsub1.delete(0, END)
                        self.firstsub1.insert(0, record[i][1])
                        self.firstcourse1.delete(0, END)
                        self.firstcourse1.insert(0, record[i][2])
                        self.secondsub1.delete(0, END)
                        self.secondsub1.insert(0, record[i][3])
                        self.secondcourse1.delete(0, END)
                        self.secondcourse1.insert(0, record[i][4])

                        self.firstsub2.delete(0, END)
                        self.firstsub2.insert(0, record[i+1][1])
                        self.firstcourse2.delete(0, END)
                        self.firstcourse2.insert(0, record[i+1][2])
                        self.secondsub2.delete(0, END)
                        self.secondsub2.insert(0, record[i+1][3])
                        self.secondcourse2.delete(0, END)
                        self.secondcourse2.insert(0, record[i+1][4])

                        self.firstsub3.delete(0, END)
                        self.firstsub3.insert(0, record[i+2][1])
                        self.firstcourse3.delete(0, END)
                        self.firstcourse3.insert(0, record[i+2][2])
                        self.secondsub3.delete(0, END)
                        self.secondsub3.insert(0, record[i+2][3])
                        self.secondcourse3.delete(0, END)
                        self.secondcourse3.insert(0, record[i+2][4])

                        self.firstsub4.delete(0, END)
                        self.firstsub4.insert(0, record[i+3][1])
                        self.firstcourse4.delete(0, END)
                        self.firstcourse4.insert(0, record[i+3][2])
                        self.secondsub4.delete(0, END)
                        self.secondsub4.insert(0, record[i+3][3])
                        self.secondcourse4.delete(0, END)
                        self.secondcourse4.insert(0, record[i+3][4])
                        break
                obc.commit()
                obc.close()
        except:
            messagebox.showerror("Error", "Something went wrong..!!!\nPlease contact Admin: +917004250668")
        pass

    def save_command(self):
        try:
            print("Save button Pressed.")
            ob = sqlite3.connect("database.db")
            cur = ob.cursor()
            # to create tables
            # cur.execute("""create table coursedetails(regno numeric, titlefirst char, codefirst char, titlesecond char, codesecond char);""")
            # cur.execute("""create table studentdetails(regno numeric, name char);""")
            list=[]
            if self.name.get()=="" or self.firstsub1.get()=="" or self.firstsub2.get()=="" or self.firstsub3.get()=="" or\
                    self.firstsub4.get()=="" or self.secondsub1.get()=="" or self.secondsub2.get()=="" or self.secondsub3.get()=="" or\
                    self.secondsub4.get()=="" or self.firstcourse1.get()=="" or self.firstcourse2.get()=="" or self.firstcourse3.get()=="" or\
                    self.firstcourse4.get()=="" or self.secondcourse1.get()=="" or self.secondcourse2.get()=="" or self.secondcourse3.get()=="" or\
                    self.secondcourse4.get()=="":
                print("Enter data before saving.")
                messagebox.showerror("Error..!!", "Enter all required data before saving..!!!")
            else:
                cur.execute("""select * from studentdetails;""")
                while True:
                    value = cur.fetchone()
                    if value == None:
                        break
                    if self.regno.get() == str(value[0]):
                        list.append(str(value[0]))
                print("list=",list)
                if self.regno.get() in list:
                    print("Data already present.")
                    messagebox.showerror("Error", "SORRY..!!\nData already present.\nPress Open Button instead.")
                else:
                    # to insert data into coursedetails table
                    cur.execute("""insert into coursedetails(regno, titlefirst, codefirst, titlesecond, codesecond) values(?,?,?,?,?)""",
                        (int(self.regno.get()), self.firstsub1.get(), self.firstcourse1.get(), self.secondsub1.get(),self.secondcourse1.get()))
                    cur.execute("""insert into coursedetails(regno, titlefirst, codefirst, titlesecond, codesecond) values(?,?,?,?,?)""",
                        (int(self.regno.get()), self.firstsub2.get(), self.firstcourse2.get(), self.secondsub2.get(),self.secondcourse2.get()))
                    cur.execute("""insert into coursedetails(regno, titlefirst, codefirst, titlesecond, codesecond) values(?,?,?,?,?)""",
                        (int(self.regno.get()), self.firstsub3.get(), self.firstcourse3.get(), self.secondsub3.get(),self.secondcourse3.get()))
                    cur.execute("""insert into coursedetails(regno, titlefirst, codefirst, titlesecond, codesecond) values(?,?,?,?,?)""",
                        (int(self.regno.get()), self.firstsub4.get(), self.firstcourse4.get(), self.secondsub4.get(),self.secondcourse4.get()))

                    # to insert data into studentdetails table
                    cur.execute("""insert into studentdetails(regno, name) values(?,?)""",(int(self.regno.get()), self.name.get()))
                    print("Data Saved Successfully.")
                    messagebox.showinfo("Saved", "Data Saved Successfully..!!!")
                ob.commit()
                ob.close()
        except:
            messagebox.showerror("Error", "Something went wrong..!!!\nPlease contact Admin: +917004250668")
        pass

def main():
    root = Tk()
    demo = CustomMain(root)
    root.title('main')
    root.mainloop()

if __name__ == '__main__': main()