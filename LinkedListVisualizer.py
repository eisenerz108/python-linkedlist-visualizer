import tkinter as tk
from Node import Node


class LinkedListVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Linked List Visualizer")
        self.canvas = tk.Canvas(self.root, width=1000, height=400, bg="white")
        self.canvas.pack()

        self.head = None  # Head of the linked list
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
            new_node = Node(data)
            if not self.head:
                self.head = new_node
            else:
                # Traverse to the last node and link the new node
                current = self.head
                while current.next:
                    current = current.next
                current.next = new_node
            self.data_entry.delete(0, tk.END)
            self.update_canvas()

    def reset(self):
        self.head = None
        self.canvas.delete("all")

    def update_canvas(self):
        self.canvas.delete("all")
        x, y = 50, 200
        current = self.head

        while current:
            # Draw node with two compartments
            self.canvas.create_rectangle(x, y, x + 100, y + 30, fill="lightblue")  # Outer rectangle
            self.canvas.create_line(x + 50, y, x + 50, y + 30)  # Divider

            # Display data in the first compartment
            self.canvas.create_text(x + 25, y + 15, text=current.data)

            # Display last 4 digits of the next node's address in the second compartment
            next_address = str(id(current.next))[-4:] if current.next else "None"
            self.canvas.create_text(x + 75, y + 15, text=next_address)

            # Draw arrow to the next node
            if current.next:
                self.canvas.create_line(x + 100, y + 15, x + 150, y + 15, arrow=tk.LAST)

            x += 150  # Adjust spacing between nodes
            current = current.next

