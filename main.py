import tkinter as tk
from LinkedListVisualizer import LinkedListVisualizer


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

if __name__ == "__main__":
    root = tk.Tk()
    app = LinkedListVisualizer(root)
    root.mainloop()
