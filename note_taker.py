import Tkinter
import pickle

root = Tkinter.Tk()
root.geometry("600x400")
root.title("Note taker")

def Enter():
	text_contents = text.get()
	listbox.insert(Tkinter.END, text_contents)
	text.delete(0, Tkinter.END)
	
def Remove():
	listbox.delete(Tkinter.ANCHOR)

def Save():
	f = file("notes.db", "wb")
	notes = listbox.get(0,Tkinter.END)
	pickle.dump(notes,f)
	
def ReturnInsert(event):
	Enter()
	
def DeleteCurrent(event):
	Remove()
	
def CopyToText(event):
	text.delete(0,Tkinter.END)
	
textframe = Tkinter.Frame(root)
listframe = Tkinter.Frame(root)

enter_button = Tkinter.Button(textframe, text="Enter", command=Enter)
remove_button = Tkinter.Button(textframe, text="Remove", command=Remove)
save_button = Tkinter.Button(textframe, text="Save", command=Save)

text = Tkinter.Entry(textframe)

scrollbar = Tkinter.Scrollbar(listframe, orient=Tkinter.VERTICAL)
listbox = Tkinter.Listbox(listframe, yscrollcommand=scrollbar.set, selectmode=Tkinter.EXTENDED)
scrollbar.configure(command=listbox.yview)

text.bind("<Return>", ReturnInsert)
listbox.bind("<Double-Button-3>", DeleteCurrent)
listbox.bind("Double-Button-1>", CopyToText)

text.pack(side=Tkinter.LEFT, fill=Tkinter.X, expand=1)
enter_button.pack(side=Tkinter.LEFT)
remove_button.pack(side=Tkinter.LEFT)
save_button.pack(side=Tkinter.LEFT)
listbox.pack(side=Tkinter.LEFT, fill=Tkinter.BOTH, expand=1)
scrollbar.pack(side=Tkinter.RIGHT, fill=Tkinter.Y)

textframe.pack(fill=Tkinter.X)
listframe.pack(fill=Tkinter.BOTH, expand=1)

try:
	f = file("notes.db", "rb")
	notes = pickle.load(f)
	for item in notes:
		listbox.insert(Tkinter.END, item)
	f.close()
except:
	pass
	
root.mainloop()