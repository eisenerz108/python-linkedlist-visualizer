import tkinter as tk
class LinkedListVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Linked List Visualizer")
        self.canvas = tk.Canvas(self.root, width=800, height=400, bg="white")
        self.canvas.pack()

        self.linked_list = []
        self.setup_gui()

    def setup_gui(self):
        # Input field
        self.data_entry = tk.Entry(self.root)
        self.data_entry.pack(side=tk.LEFT, padx=10)

        # Add Node Button
        add_btn = tk.Button(self.root, text="Add Node", command=self.add_node)
        add_btn.pack(side=tk.LEFT, padx=10)

        # Reset Button
        reset_btn = tk.Button(self.root, text="Reset", command=self.reset)
        reset_btn.pack(side=tk.LEFT, padx=10)

    def add_node(self):
        data = self.data_entry.get()
        if data:
            self.linked_list.append(data)
            self.data_entry.delete(0, tk.END)
            self.update_canvas()

    def reset(self):
        self.linked_list = []
        self.canvas.delete("all")

    def update_canvas(self):
        self.canvas.delete("all")
        x, y = 50, 200
        for data in self.linked_list:
            # Draw node
            self.canvas.create_rectangle(x, y, x + 50, y + 30, fill="lightblue")
            self.canvas.create_text(x + 25, y + 15, text=data)

            # Draw arrow
            x += 70
            if data != self.linked_list[-1]:
                self.canvas.create_line(x - 20, y + 15, x, y + 15, arrow=tk.LAST)

