import tkinter as tk

master = tk.Tk()


################ TEXT WITH IMAGE
# logo = tk.PhotoImage(file="sprite1.png")
#
#
# w2 = tk.Label(root,
#               justify=tk.LEFT,
#               compound = tk.LEFT,
#               text="""At present, only GIF and PPM/PGM
#   formats are supported, but an interface
#   exists to allow additional image file
#   formats to be added easily.""",
#               image=logo,
#               padx=10).pack(side="right")



####################    COLOURED FONT
# tk.Label(root,
#          text="Red text in times font",
#          fg="red",
#          font = "Times").pack()
# tk.Label(root,
#          text="Green text is helvetica font",
#          fg = "light green",
#          bg = "dark green",
#          font = "Helvetica 16 bold italic").pack()
# tk.Label(root,
#          text="Blue text in verdana bold",
#          fg = "blue",
#          bg = "yellow",
#          font = "Verdana 10 bold").pack()


################# COUNTER WITH BUTTON

# counter = 0
# def counter_label(label):
#     def count():
#         global counter
#         counter += 1
#         label.config(text=str(counter))
#         label.after(1000, count)
#     count()
#
# root.title("Counting Seconds")
# label = tk.Label(root, fg="green")
# label.pack()
# counter_label(label)
# button = tk.Button(root, text="stop", width=25, command=root.destroy)
# button.pack()

whatever_you_do = """Whatever you do will be insignificant, but it is
  very important that you do it.\n(Mahatma Gandhi)"""

msg = tk.Message(master, text=whatever_you_do)
msg.config(relief=tk.RIDGE, justify=tk.CENTER, bg="lightgreen", font=('times', 24, 'italic'))
msg.pack()


master.mainloop()
