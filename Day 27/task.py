import tkinter as tk

windows = tk.Tk()
windows.title("KM to M Converter")
windows.minsize(500, 300)
windows.config(padx=50, pady=50, bg="#f0f0f0")

my_label = tk.Label(windows, text="Welcome to KM to M Converter", font=("Arial", 24, "bold"), bg="#f0f0f0")
my_label.grid(column=0, row=0, columnspan=2, pady=20)

w_label = tk.Label(windows, text="KM:", font=("Arial", 14), bg="#f0f0f0")
w_label.grid(column=0, row=1, sticky="E")
KM_input = tk.Entry(windows, width=10)
KM_input.grid(column=1, row=1, pady=10)


def button_clicked():
    value = KM_input.get()
    try:
        value = float(value) * 0.621372737
        show_label.config(text=f"{value:.2f} Miles")
    except ValueError:
        show_label.config(text="Invalid input")

button = tk.Button(windows, text="Convert", command=button_clicked, font=("Arial", 14), bg="#4CAF50", fg="white")
button.grid(column=0, row=2, columnspan=2, pady=20)

show_label = tk.Label(windows, text="Miles", font=("Arial", 14), bg="#f0f0f0")
show_label.grid(column=0, row=3, columnspan=2, pady=10)

windows.mainloop()
