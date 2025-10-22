import tkinter as tk

def calculate_miles_to_km():
    result_value["text"] = round(float(num_input.get()) * 1.6)

window = tk.Tk()
window.title("Mile to Kilometer Converter")
window.config(padx=20, pady=20)

#Labels
miles = tk.Label(text="Miles")
km = tk.Label(text="Km")
is_equal_to = tk.Label(text="Is equal to")
result_value = tk.Label(text=0)

#Button
calculate_button = tk.Button(text="Calculate", command=calculate_miles_to_km)

#Input
num_input = tk.Entry(width=10)
num_input.focus()

#Grid
is_equal_to.grid(row=1, column=0)
num_input.grid(row=0, column=1)
result_value.grid(row=1, column=1)
calculate_button.grid(row=2, column=1)
miles.grid(row=0, column=2)
km.grid(row=1, column=2)

window.mainloop()