import tkinter

class Aboutus(object):
    _images = []  # Holds image refs to prevent GC

    def __init__(self, root):
        self._images.append(tkinter.PhotoImage('about-us (1).gif',file='about-us (1).gif'))

        # Widget Initialization
        self._frame_1 = tkinter.Frame(root,background="#ffff77",)
        self._labelframe_1 = tkinter.LabelFrame(root,background="#f1fd60",font="{Lucida Sans Unicode} 8 bold",text="License",)
        self._label_4 = tkinter.Label(root,
                                        activebackground="#ffffff",
                                      background="#ffffff",
                                      borderwidth=0,
                                      image="about-us (1).gif",
                                      text="_label_4",)
        self._label_5 = tkinter.Label(root,
                                      activebackground="#fcff7d",
                                      background="#fcff7d",
                                      borderwidth=0,
                                      font="{MS Sans Serif} 10 bold",
                                      text="""CGPA Calculator designed by Akash.
 \uD83D\uDC8C Email ID - akashkrcse1@gmail.com
 \uD83D\uDCDE Phone number - +917004250668
 \uD83C\uDF10 Whats app - +919470589336""",)
        self.close = tkinter.Button(root,
                                    activebackground="#846fff",
                                    background="#846fff",
                                    borderwidth=5,
                                    cursor="hand2",
                                    font="{MS Sans Serif} 8 bold",
                                    text="Close",)
        self._label_1 = tkinter.Label(self._labelframe_1,
                                      activebackground="#fcf861",
                                      background="#fcf861",
                                      justify="left",
                                      text="""All Rights Reserved.

The author and publisher have taken care in the preparation of this software, but make no expressed or implied warranty of any kind and assume no responsibility
for errors or omissions. No liability is assumed for incidenttal or consequential damages in connection with or arising out of the use of the information or programs
contained herein.

This software is protected by copyright, and permission must be obtained from the publisher prior to any prohibited reproduction, storage in a retrieval system, or 
transmission in any form or by any means, electronic, mechanical, photocopying, recording, or likewise.

For more information regarding permissions, write us to or call: +917004250668.""",)

        # widget commands
        self.close.configure(command=self.close_command)

        # Geometry Management
        self._frame_1.grid(in_=root,column=1,row=4,columnspan=1,ipadx=0,ipady=0,padx=0,pady=0,rowspan=1,sticky="news")
        self._labelframe_1.grid(in_=root,column=1,row=3,columnspan=2,ipadx=0,ipady=0,padx=0,pady=0,rowspan=1,sticky="news")
        self._label_4.grid(in_=root,column=1,row=1,columnspan=2,ipadx=0,ipady=0,padx=0,pady=0,rowspan=1,sticky="nsew")
        self._label_5.grid(in_=root,column=1,row=2,columnspan=2,ipadx=0,ipady=0,padx=0,pady=0,rowspan=1,sticky="nsew")
        self.close.grid(in_=root,column=2,row=4,columnspan=1,ipadx=0,ipady=0,padx=0,pady=0,rowspan=1,sticky="nsew")
        self._label_1.grid(in_=self._labelframe_1,column=1,row=1,columnspan=1,ipadx=0,ipady=0,padx=0,pady=0,rowspan=3,sticky="nsew")

        # Resize Behavior
        root.grid_rowconfigure(1, weight=0, minsize=155, pad=0)
        root.grid_rowconfigure(2, weight=0, minsize=40, pad=0)
        root.grid_rowconfigure(3, weight=0, minsize=40, pad=0)
        root.grid_rowconfigure(4, weight=0, minsize=40, pad=0)
        root.grid_columnconfigure(1, weight=0, minsize=662, pad=0)
        root.grid_columnconfigure(2, weight=0, minsize=5, pad=0)
        self._labelframe_1.grid_rowconfigure(1, weight=0, minsize=40, pad=0)
        self._labelframe_1.grid_rowconfigure(2, weight=0, minsize=40, pad=0)
        self._labelframe_1.grid_rowconfigure(3, weight=0, minsize=40, pad=0)
        self._labelframe_1.grid_columnconfigure(1, weight=0, minsize=40, pad=0)