from Tkinter import *
import tkFileDialog

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        label = Label(frame)
        label.config(text="Convert tide data for ASCII Interpreter")
        label.pack()
        
        self.fileloc = Entry(frame)
        self.fileloc["width"] = 50
        self.fileloc.pack(side=LEFT)
        self.fileloc.focus_set()
        
        self.open_file = Button(frame, text="Open File", command=self.browse_file)
        self.open_file.pack(side=LEFT)
        
        self.newfile = Entry(frame)
        self.newfile["width"] = 50
        self.newfile.pack()
        
        ADJUSTMENTS = [
            ("1 hour", "1"),
            ("2 hour", "2")
        ]
        
        self.adj = StringVar()
        self.adj.set("1") #Initialize
        
        for text, mode in ADJUSTMENTS:
            self.adjustment = Radiobutton(frame, text=text, variable=self.adj, value=mode)
            self.adjustment.pack(anchor=W)
            
        self.submit = Button(frame, text="Start Converting", command=self.start_processing)
        self.submit.pack(side=LEFT)

    def browse_file(self):
        self.filename = tkFileDialog.askopenfilename(title="Enter tide file...")
        self.fileloc.insert(0,self.filename )#set the location to fileloc var
        
    def start_processing(self):
        print "start processing file..."
        print self.fileloc.get()
        print self.adj.get()

root = Tk()
app = App(root)
root.mainloop()