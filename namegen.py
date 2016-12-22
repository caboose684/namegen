#!/usr/bin/env python3

import tkinter as tk
import random
from os import listdir
from os.path import isfile, splitext

def get_lists(working_dir):
    word_files = [f for f in listdir(working_dir) if
        (isfile(f) and
        splitext(f)[1].lower() == '.txt')]
    return word_files

def random_line(filename):
    afile = open(filename)
    line = next(afile)
    for num, aline in enumerate(afile):
        if random.randrange(num + 2): continue
        line = aline
    afile.close()
    return line

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.word_lists = get_lists(".")
        #set up frames
        self.topframe = tk.Frame(self)
        self.topframe.pack(side=tk.TOP,fill=tk.X)
        self.outputframe = tk.Frame(self)
        self.outputframe.pack(side=tk.TOP,fill=tk.X)

        #top frame
        self.firstvar = tk.StringVar(self.topframe)
        self.firstvar.set(self.word_lists[0])
        self.first = tk.OptionMenu(self.topframe, self.firstvar,
                                    *self.word_lists)
        self.first.pack(side=tk.LEFT)

        self.secondvar = tk.StringVar(self.topframe)
        self.secondvar.set(self.word_lists[0])
        self.second = tk.OptionMenu(self.topframe, self.secondvar,
                                    *self.word_lists)
        self.second.pack(side=tk.LEFT)

        self.QUIT = tk.Button(self.topframe)
        self.QUIT.pack(side=tk.RIGHT)
        self.QUIT["text"] = "QUIT"
        self.QUIT["command"] = root.destroy

        self.go = tk.Button(self.topframe)
        self.go.pack(side=tk.RIGHT)
        self.go["text"] = "GO!"
        self.go["command"] = self.say_output
        self.go["width"] = 20
        self.go["background"] = "lightgreen"

        #output frame
        self.output = tk.Text(self.outputframe)
        self.output.pack(side=tk.LEFT)
        self.output["state"] = tk.DISABLED
        self.output["wrap"] = tk.WORD
        self.yscroll = tk.Scrollbar(self.outputframe)
        self.yscroll.pack(side=tk.RIGHT,fill=tk.Y)
        self.yscroll["command"] = self.output.yview
        self.output["yscrollcommand"] = self.yscroll.set

    def say_output(self):
        self.output["state"] = tk.NORMAL
        self.output.delete(1.0, tk.END)
        self.make_names()
        self.output["state"] = tk.DISABLED

    def make_names(self):
        for q in range(20):
            self.output.insert(tk.END,
                random_line(self.firstvar.get())[:-1] + " "
                + random_line(self.secondvar.get())[:-1] + "\n")


root = tk.Tk()
root.title("Name Generator v1.0")
app = Application(master=root)
app.mainloop()