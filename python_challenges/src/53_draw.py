'''Create a program that allows users to draw on a canvas using a GUI'''

import tkinter as tk

def draw_on_canvas():
    root = tk.Tk()
    root.title("Draw on Canvas")
    
    canvas = tk.Canvas(root, width=400, height=400, bg="white")
    canvas.pack()

    def draw(event):
        x, y = event.x, event.y
        canvas.create_oval(x-2, y-2, x+2, y+2, fill="black")

    canvas.bind("<B1-Motion>", draw)

    root.mainloop()

# Example usage
draw_on_canvas()
