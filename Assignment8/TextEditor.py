# Create a simple text editor application. Include vertical and horizontal scrollbars.
import tkinter as tk

class TextEditor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Text Editor")
        self.geometry("800x600")

# Create a Frame to hold the Text widget and both scrollbars
        frame = tk.Frame(self)
        frame.pack(fill=tk.BOTH, expand=True)

# Create vertical scrollbar
        v_scroll = tk.Scrollbar(frame, orient=tk.VERTICAL)
        v_scroll.pack(side=tk.RIGHT, fill=tk.Y)

# Create horizontal scrollbar
        h_scroll = tk.Scrollbar(frame, orient=tk.HORIZONTAL)
        h_scroll.pack(side=tk.BOTTOM, fill=tk.X)

# Create Text widget with both scrollbars
        self.text_area = tk.Text(
            frame,
            wrap=tk.NONE,  # Allow horizontal scrolling
            font=("Arial", 12),
            yscrollcommand=v_scroll.set,
            xscrollcommand=h_scroll.set
        )
        self.text_area.pack(fill=tk.BOTH, expand=True)

# Attach scrollbars to the Text widget
        v_scroll.config(command=self.text_area.yview)
        h_scroll.config(command=self.text_area.xview)


if __name__ == "__main__":
    app = TextEditor()
    app.mainloop()
    