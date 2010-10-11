from Tkinter import *
import tkFileDialog, tkMessageBox
import datetime
from converter import Converter

class App:

    def __init__(self, master):
        
        master.title("Tide ASCII Converter (data source: vannstand.no)")
        
        self.now = datetime.datetime.now()
        label01 = "Convert tide data for ASCII Interpreter"
        Label(master, text=label01).grid(row=0, column=1, sticky=W)
        
        Label(master, text="Input file: ").grid(row=1)
        self.fileloc = Entry(master)
        self.fileloc["width"] = 50
        self.fileloc.focus_set()
        self.fileloc.grid(row=1, column=1)
        
        self.open_file = Button(master, text="Browse...", command=self.browse_file)
        self.open_file.grid(row=1, column=2)
        
        Label(master, text="Adjusment: ").grid(row=3, sticky=N)
        ADJUSTMENTS = [
            ("Adjust by 1 hour", "1"),
            ("Adjust by 2 hours", "2")
        ]
        
        self.adj = StringVar()
        self.adj.set("1") #Initialize
        
        i = 3
        for text, mode in ADJUSTMENTS:
            self.adjustment = Radiobutton(master, text=text, variable=self.adj, value=mode)
            self.adjustment.grid(row=i, column=1, sticky=W)
            i += 1
        
        Label(master, text="Message Logs: ").grid(row=5, sticky=NW)
        self.textarea = Text(master, height=3, width=33)
        scroll = Scrollbar(master, command=self.textarea.yview)
        self.textarea.configure(yscrollcommand=scroll.set)
        self.textarea.grid(row=5, column=1)
        scroll.grid(row=5, column=2, sticky=W)
        
        self.submit = Button(master, text="EXECUTE", command=self.start_processing, fg="red")
        self.submit.grid(row=7, column=0, sticky=E)

    def browse_file(self):
        self.filename = tkFileDialog.askopenfilename(title="Open tide file...")
        self.fileloc.insert(0,self.filename )#set the location to fileloc var
        
    def start_processing(self):
        print "start processing file..."
        try:
            #print self.fileloc.get()
            #print self.adj.get()
            tide = Converter()
            tide.set_input_file(self.fileloc.get())
            tide.set_adjustment(int(self.adj.get()))
            tide.set_output_file("tide_%d%d%d%d%d%d.txt" % (self.now.year, self.now.month, self.now.day, self.now.hour, self.now.minute, self.now.second))
            tide.process_file()
            tide.close()
            self.done_processing()
        except:
            print "Unexpected error",  
            tkMessageBox.showerror("Unexpected Error", sys.exc_info())
        
    def done_processing(self):
        tkMessageBox.showinfo("Successful", "Done! Conversion file created.")
        
        self.textarea.insert(END, "[%d/%d/%d %d:%d:%d] %s %s hour\n" % (self.now.year, self.now.month, self.now.day, self.now.hour, self.now.minute, self.now.second, self.filename, self.adj.get()))
        
root = Tk()
app = App(root)
root.mainloop()