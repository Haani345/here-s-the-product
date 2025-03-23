import tkinter as tk

def calculate_product():
    try:
        result.set(float(entry1.get()) * float(entry2.get()))
    except ValueError:
        result.set("Invalid Input")

window = tk.Tk()
window.title("Multiply")
window.geometry("400x400")

entry1 = tk.Entry(window)
entry1.pack()
entry2 = tk.Entry(window)
entry2.pack()

tk.Button(window, text="Multiply", command=calculate_product).pack()

result = tk.StringVar()
tk.Label(window, textvariable=result).pack()

window.mainloop()