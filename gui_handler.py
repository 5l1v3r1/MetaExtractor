import base, cr, info_handler
from tkinter import *
import tkinter.ttk as ttk
from tkinter import Tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk
from tkinter import filedialog

textToSave = ""



class _GUI():

    def __init__(self, metadata_ord, metadata_xml, location, filename):
        self.metadata_ord = metadata_ord
        self.metadata_xml = metadata_xml
        self.location = location
        self.filename = filename
        self.textToSave = ""

        self._mainGuiInterface()


    def _mainGuiInterface(self):

        master = Tk()
        master.title("MetaEx: Image Metadata Extraction Tool")
        master.configure(background="#ffffff")
        master.pack_propagate(0)
        master.geometry('1120x540')

        pop = info_handler._PopuleteGui(master, self.location, self.metadata_xml, self.metadata_ord)

        # ----MENU----
        menubar = Menu(master)
        menubar.configure(background="#ffffff")

        # create a pulldown menu, and add it to the menu bar
        filemenu = Menu(menubar, tearoff=0)
        filemenu.configure(background="#ffffff")
        filemenu.add_command(label="Open New...", command=pop._open_new_)
        filemenu.add_command(label="Save Meta to file...", command=pop._save_meta_)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=master.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        # create more pulldown menus
        spidermenu = Menu(menubar, tearoff=0)
        spidermenu.configure(background="#ffffff")
        spidermenu.add_command(label="URL", command=cr.cra)
        menubar.add_cascade(label="Crawl", menu=spidermenu)

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.configure(background="#ffffff")
        helpmenu.add_command(label="About", command=pop._pop_about_)
        helpmenu.add_command(label="How to use", command=pop._pop_usage_)
        menubar.add_cascade(label="Help", menu=helpmenu)

        # display the menu
        master.config(menu=menubar)

        # ----LEFT----
        left = Frame(master, width=200, height=500, highlightthickness=0, bg="#ffffff")
        left.grid(row=0, column=0, padx=10, pady=2, sticky=N + S)

        logo = Label(left, text="MetaEx", fg="#00695C", bg="#ffffff", font="Verdana 30 bold", underline=True)
        logo.grid(row=0, column=0, padx=10, pady=30)

        image = pop._pop_image_()
        Label(left, image=image).grid(row=1, column=0, padx=10, pady=15)

        Label(left, text="Other Information", font="Verdana 11 bold", fg="#00695C", bg="#ffffff", pady=10).grid(row=2, column=0, sticky="nw")

        extra_information = "Filename: " + self.filename
        info = Label(left, text=extra_information, font="Verdana 10 ", bg="#ffffff", fg="#00897B")
        info.grid(row=3, column=0, sticky="nw")

        extra_information2 = "Path: " + self.location
        info2 = Label(left, text=extra_information2, font="Verdana 10 ", bg="#ffffff", fg="#00897B")
        info2.grid(row=4, column=0, sticky="nw")

        # ----RIGHT----
        right = Frame(master, bg="#ffffff", highlightthickness=0, highlightbackground="#ffffff", width=500, height=500)
        right.grid(row=0, column=2, padx=50, pady=2, sticky="ns")

        intro = Label(right, text="Image Metadata", fg="#ffffff", bg="#1ba1e2", font="Verdana 10 bold", height=2, width=70)
        intro.grid(row=0, column=0, padx=10, pady=20)

        table = Frame(right, bg="#ffffff", highlightthickness=0, highlightbackground="#ffffff", width=500, height=400)
        table.grid(row=1, column=0, padx=10, pady=0, sticky="ns")

        canvas = Canvas(table, width=600, height=440, background="#ffffff", highlightbackground="#ffffff")
        scrolly = Scrollbar(table, orient='vertical', command=canvas.yview)

        self.textToSave += pop._pop_xml_(canvas)
        self.textToSave += pop._pop_ord_(canvas)


        canvas.configure(scrollregion=canvas.bbox('all'), yscrollcommand=scrolly.set, background="#ffffff")
        # canvas.config(width=600, height=440)
        canvas.pack(fill='both', expand=True, side='left')
        scrolly.configure(bg="#ffffff")
        scrolly.pack(fill='y', side='right')


        master.mainloop()






# def gui(metadata_ord, metadata_xml, location, filename):
#
#     textToSave = ""
#
#     CMAIN = "#ffffff"  #a5d6a7"
#     CDARKER = "#024016" # #1ba1e2
#     CLOGO="#00695C"
#
#
#
#     master = Tk()
#     master.title("MetaEx: Image Metadata Extraction Tool")
#     master.configure(background=CMAIN)
#     master.pack_propagate(0)
#     master.geometry('1120x540')
#
#     # ----MENU----
#     menubar = Menu(master)
#     menubar.configure(background="#ffffff")
#
#     # create a pulldown menu, and add it to the menu bar
#     filemenu = Menu(menubar, tearoff=0)
#     filemenu.configure(background="#ffffff")
#     filemenu.add_command(label="Open New...", command=openFile)
#     filemenu.add_command(label="Save Meta to file...", command=saveFile)
#     filemenu.add_separator()
#     filemenu.add_command(label="Exit", command=master.quit)
#     menubar.add_cascade(label="File", menu=filemenu)
#
#     # create more pulldown menus
#     editmenu = Menu(menubar, tearoff=0)
#     editmenu.configure(background="#ffffff")
#     editmenu.add_command(label="URL", command=cr.cra)
#     menubar.add_cascade(label="Crawl", menu=editmenu)
#
#     helpmenu = Menu(menubar, tearoff=0)
#     helpmenu.configure(background="#ffffff")
#     helpmenu.add_command(label="About", command=about)
#     helpmenu.add_command(label="How to use", command=usage)
#     menubar.add_cascade(label="Help", menu=helpmenu)
#
#     # display the menu
#     master.config(menu=menubar)
#
#     # ----LEFT----
#     left = Frame(master, width=200, height=500, highlightthickness=0, bg=CMAIN)
#     left.grid(row=0, column=0, padx=10, pady=2, sticky=N + S)
#
#     logo = Label(left, text="MetaEx", fg=CLOGO, bg=CMAIN, font="Verdana 30 bold", underline=True)
#     logo.grid(row=0, column=0, padx=10, pady=30)
#
#     image = Image.open(location)
#     image = image.resize((300, 250), Image.ANTIALIAS)
#     imageEx = ImageTk.PhotoImage(image, master=master)
#     Label(left, image=imageEx).grid(row=1, column=0, padx=10, pady=15)
#
#     Label(left, text="Other Information", font="Verdana 11 bold", fg="#00695C", bg=CMAIN, pady=10).grid(row=2, column=0, sticky="nw")
#
#     extra_information = "Filename: " + filename
#     info = Label(left, text=extra_information, font="Verdana 10 ", bg=CMAIN, fg="#00897B")
#     info.grid(row=3, column=0, sticky="nw")
#
#     extra_information2 = "Path: " + location
#     info2 = Label(left, text=extra_information2, font="Verdana 10 ", bg=CMAIN, fg="#00897B")
#     info2.grid(row=4, column=0, sticky="nw")
#
#     # ----MIDDLE----
#     # separator = ttk.Separator(master, orient="vertical")
#     # separator.grid(row=0, column=1, sticky="sn", rowspan=2)
#
#     # ----RIGHT----
#     right = Frame(master, bg=CMAIN, highlightthickness=0, highlightbackground=CMAIN, width=500, height=500)
#     right.grid(row=0, column=2, padx=50, pady=2, sticky="ns")
#
#     intro = Label(right, text="Image Metadata", fg="#ffffff", bg="#1ba1e2", font="Verdana 10 bold", height=2, width=70)
#     intro.grid(row=0, column=0, padx=10, pady=20)
#
#
#
#     table = Frame(right, bg=CMAIN, highlightthickness=0, highlightbackground=CMAIN, width=500, height=400)
#     table.grid(row=1, column=0, padx=10, pady=0, sticky="ns")
#
#     canvas = Canvas(table, width=600, height=440, background=CMAIN, highlightbackground=CMAIN)
#     scrolly = Scrollbar(table, orient='vertical', command=canvas.yview)
#
#     i = 0
#     for key, value in metadata_xml.items():
#         if "0" not in value and "http" not in value:
#             l = len(key)
#             tab = ""
#             if l < 9:
#                 tab = "\t\t\t"
#             elif l < 20:
#                 tab = "\t\t"
#             elif l < 30:
#                 tab = "\t"
#             else:
#                 tab = ""
#
#             myText = key + ": " + tab + value
#             label = Label(canvas, text=myText)
#             canvas.create_window(0, i * 22, anchor='nw', window=label, height=15)
#             label.configure(background=CMAIN)
#             textToSave += myText + "\n"
#             i += 1
#
#     for j in metadata_ord:
#         label = Label(canvas, text=j)
#         canvas.create_window(0, i * 22, anchor='nw', window=label, height=15)
#         label.configure(background=CMAIN)
#         textToSave += j + "\n"
#         i += 1
#
#     canvas.configure(scrollregion=canvas.bbox('all'), yscrollcommand=scrolly.set, background=CMAIN)
#     # canvas.config(width=600, height=440)
#     canvas.pack(fill='both', expand=True, side='left')
#     scrolly.configure(bg="#ffffff")
#     scrolly.pack(fill='y', side='right')
#
#     master.mainloop()
