import tkinter as tk
window = tk.Tk()

button = tk.Button(text='light on', bg="white", fg="black")
button.pack(pady = 20, padx = 20)

# schijf hier tussen je code
window['bg'] = 'black'

def clickButton(event):
    button.config(text=' light off')
    print ("light is on")
    window['bg'] = 'yellow'

button.bind("<Button-1>", clickButton) #Rechter button (Rightclick)

def clickButton1(event):
    button.config(text=' light on')
    print ("light is off")
    window['bg'] = 'Black'
button.bind("<Button-3>", clickButton1) #Linker button (Leftclick)
# schijf hier tussen je code

window.mainloop()