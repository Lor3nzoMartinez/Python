import tkinter as tk

HEIGHT = 300
WIDTH = 500

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='#CCE1E9')
canvas.pack()

frame = tk.Frame(root, bg='#a1a0a0')
frame.place(relx=0.5, rely=0.05, relwidth=0.95, relheight=0.1, anchor='n')

frame2 = tk.Frame(root, bg='#EEE7E4')
frame2.place(relx=0.5, rely=0.20, relwidth=0.95, relheight=0.75, anchor='n')

button = tk.Button(frame, text="Submit", bg='#EEE7E4', fg='#000000')
button.place(relx=0.693, rely=0.09, relwidth=0.29, relheight=0.80)

entry = tk.Entry(frame, bg='white')
entry.place(relx=0.01, rely=0.085, relwidth=0.66, relheight=0.80)

label = tk.Label(frame, text='Name', bg='light grey')
label.place(relx=0.475, rely=0.125, relwidth=0.2, relheight=0.75)

root.mainloop()
