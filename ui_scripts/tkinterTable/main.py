import tkinter
from tkTable import TkTable

UI = tkinter.Tk()

names = ['name', 'movie', 'pet']

indexlist = [0, 1, 2]

Source = [['john', 'Spiderman', 'cat'],
          ['malek','Matrix', 'dog']]
# Affect how cells added to Table          
SystemType = 'grid'
# Entry and Labels looks similar in presenting data.
# but Labels is easier for Style Customization and much Pretty for Presentations 
CellType = 'entry'

mytable = TkTable(
    master=UI,
    data=Source,
    header=names,
    index=indexlist,
    geometrysystem=SystemType, 
    celltype=CellType
    )

mytable.pack()

# To Edit cells
# Method mytable.get return a tkinter Variable of the cell.
# That Variable have access to the Widget itself through master attribute
mytable.get(row=0, col=0).master.config(bg='purple')
# result should affect 'john' cell
mytable.get(row=1, col=1).master.config(font=('Segoe UI', 24, 'italic'))
# result should affect 'matrix' cell
mytable.set(row=1,col=2, info='Dogs Are bigger Than Cats')
# result should affect 'Dog' cell


UI.mainloop()