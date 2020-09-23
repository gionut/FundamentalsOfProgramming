from tkinter import*

#create window
app = Tk()

#Part
part_text = StringVar()
part_label = Label(app, text = 'book Id', font =('bold', 14) , pady = 20)
part_label.grid(row=0, column=0)

app.title('Library')
app.geometry('700x350')

#start app
app.mainloop()

