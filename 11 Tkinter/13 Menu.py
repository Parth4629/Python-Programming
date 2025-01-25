from tkinter import * 
  
top = Tk()
top.geometry("300x300")  
menubar = Menu(top)  

# file

file = Menu(menubar, tearoff=0)  
file.add_command(label="New Text File       Ctrl+N")  
file.add_command(label="New File...          Ctrl+Alt+Windows+N")  
file.add_command(label="New Window")  

file.add_separator()

file.add_command(label="Open File...")  
file.add_command(label="Open Folder...")
file.add_command(label="Open Workspace from File...")
file.add_command(label="Open Recent")  

file.add_separator()  
  
file.add_command(label="Exit", command=top.quit)  
  
menubar.add_cascade(label="File", menu=file)

# edit
  
edit = Menu(menubar, tearoff=0)  
edit.add_command(label="Undo")    
edit.add_command(label="Redo")

edit.add_separator()  

edit.add_command(label="Cut")
edit.add_command(label="Copy")  
edit.add_command(label="Paste")

edit.add_separator()

edit.add_command(label="Find")
edit.add_command(label="Replace") 

  
menubar.add_cascade(label="Edit", menu=edit)  

# Selection

selection = Menu(menubar, tearoff=0) 

selection.add_command(label="Select All")
selection.add_command(label="Expand Selection") 
selection.add_command(label="Shrink Selection")

selection.add_separator()

selection.add_command(label="Copy Line Up")
selection.add_command(label="Copy Line Down")
selection.add_command(label="Move Line Up")
selection.add_command(label="Move Line Down")
selection.add_command(label="Duplicate Selection")

menubar.add_cascade(label="Selection", menu=selection)  

# View

View = Menu(menubar, tearoff=0)

View.add_command(label="Command Palette...")
View.add_command(label="Open View...")

View.add_separator()

View.add_command(label="Appearance")
View.add_command(label="Editor Layout")

menubar.add_cascade(label="View", menu=View)

#Go

Go = Menu(menubar, tearoff=0) 

Go.add_command(label="Back")
Go.add_command(label="Forward")
Go.add_command(label="Last Edit Location")

Go.add_separator()

Go.add_command(label="Switch Editor")
Go.add_command(label="Switch Group")

Go.add_separator()

Go.add_command(label="Go to File...")
Go.add_command(label="Go to Symbol in Workspace...")

menubar.add_cascade(label="Go", menu=Go)

# Run

Run = Menu(menubar, tearoff=0)

Run.add_command(label="Start Debugging")
Run.add_command(label="Run Without Debugging")
Run.add_command(label="Stop Debugging")
Run.add_command(label="Restart Debugging")

Run.add_separator()

Run.add_command(label="Open Configurations")
Run.add_command(label="Add Configurations")

menubar.add_cascade(label="Run", menu=Run)

top.config(menu=menubar)  
top.mainloop()  