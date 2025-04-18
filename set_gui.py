import tkinter as tk
from tkinter import messagebox

def parse_set(input_text):
    return set(input_text.strip().split())

def show_result(result):
    result_box.delete(1.0, tk.END)
    result_box.insert(tk.END, result)

def union_sets():
    setA = parse_set(entryA.get())
    setB = parse_set(entryB.get())
    result = setA.union(setB)
    show_result("Union: " + str(result))

def intersection_sets():
    setA = parse_set(entryA.get())
    setB = parse_set(entryB.get())
    result = setA.intersection(setB)
    show_result("Intersection: " + str(result))

def difference_sets():
    setA = parse_set(entryA.get())
    setB = parse_set(entryB.get())
    resultA = setA - setB
    resultB = setB - setA
    show_result(f"A - B: {resultA}\nB - A: {resultB}")

def symmetric_difference_sets():
    setA = parse_set(entryA.get())
    setB = parse_set(entryB.get())
    result = setA.symmetric_difference(setB)
    show_result("Symmetric Difference: " + str(result))

# GUI Setup
window = tk.Tk()
window.title("Set Operations GUI")

tk.Label(window, text="Enter Set A:").grid(row=0, column=0)
entryA = tk.Entry(window, width=40)
entryA.grid(row=0, column=1)

tk.Label(window, text="Enter Set B:").grid(row=1, column=0)
entryB = tk.Entry(window, width=40)
entryB.grid(row=1, column=1)

tk.Button(window, text="Union", command=union_sets).grid(row=2, column=0, pady=5)
tk.Button(window, text="Intersection", command=intersection_sets).grid(row=2, column=1)
tk.Button(window, text="Difference", command=difference_sets).grid(row=3, column=0)
tk.Button(window, text="Symmetric Difference", command=symmetric_difference_sets).grid(row=3, column=1)

tk.Label(window, text="Result:").grid(row=4, column=0)
result_box = tk.Text(window, height=4, width=50)
result_box.grid(row=5, column=0, columnspan=2)

window.mainloop()
