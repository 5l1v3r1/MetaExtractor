from PIL import Image, ImageTk
from tkinter import *

from tkinter import *
import tkinter.ttk as ttk
from tkinter import Tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk
from tkinter import filedialog

class _PopuleteGui():

    i=0

    def __init__(self, master, location, metadata_xml, metadata_ord):
        self.master = master
        self.location = location
        self.metadata_xml = metadata_xml
        self.metadata_ord = metadata_ord
        self.textToSave = ""
        print()

    def _pop_image_(self):
        image = Image.open(self.location)
        image = image.resize((300, 250), Image.ANTIALIAS)
        imageEx = ImageTk.PhotoImage(image, master=self.master)

        return imageEx

    def _pop_about_(self):
        ABOUT_TEXT = """

            About


            This tool has been created as a summer project. Its intended 
            purpose is to educate as to what type of information is 
            stored ithin image files.

            This software comes with no guarantee. Use at your own risk.    
            """

        top = Toplevel()
        label = Label(top, text=ABOUT_TEXT, heigh=0, width=60)
        label.configure(background="#ffffff")
        label.pack()

    def _pop_usage_(self):
        USAGE_TEXT = """

            How to use


            Go to File->Open New... and choose the image you want to extract 
            metadata for.

            The data should appear in the "Image Metadata" box in the main 
            window.

            To save the metadata go to File->Save Meta to file... and choose 
            the location and the name you would like to save the data under.

            Under the Filter tab you can choose which type of metadata to display. 

            """
        top = Toplevel()
        label = Label(top, text=USAGE_TEXT, heigh=0, width=65)
        label.configure(background="#ffffff")
        label.pack()

    def _pop_xml_(self, canvas):
        for key, value in self.metadata_xml.items():
            if "0" not in value and "http" not in value:
                l = len(key)
                tab = ""
                if l < 9:
                    tab = "\t\t\t"
                elif l < 20:
                    tab = "\t\t"
                elif l < 30:
                    tab = "\t"
                else:
                    tab = ""

                myText = key + ": " + tab + value
                label = Label(canvas, text=myText)
                canvas.create_window(0, self.i * 22, anchor='nw', window=label, height=15)
                label.configure(background="#ffffff")
                self.textToSave += myText + "\n"
                self.i += 1

        return  self.textToSave

    def _pop_ord_(self, canvas):

        for j in self.metadata_ord:
            label = Label(canvas, text=j)
            canvas.create_window(0, self.i * 22, anchor='nw', window=label, height=15)
            label.configure(background="#ffffff")
            self.textToSave += j + "\n"
            self.i += 1

        return  self.textToSave

    def _save_meta_(self):
        f = filedialog.asksaveasfile(mode='w', defaultextension=".txt", initialfile='METAEX_metadata.txt', )
        text = self.textToSave
        f.write(text)
        f.close()

    # good

    def _open_new_(self):
        # location = askopenfilename(title="Select image for metadata extraction", filetypes=[("Image Files", "*.jpg"), ("Image Files", "*.png")])
        # metadata_ord = ord_meta_handler.handle_meta(imgdata)
        # metadata_xml = xml_meta_handler.handle_meta(imgdata)
        print()