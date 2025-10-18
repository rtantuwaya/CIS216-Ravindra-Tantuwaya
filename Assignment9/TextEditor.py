# Create a simple text editor application. Include vertical and horizontal scrollbars.
# Extend the text editor application by adding File (New and Exit) and Edit 
# (Cut, Copy, and Paste) menus. 
# Also include a context menu for Edit options.
# GUI (Graphical User Interface) applications.

# This import the tkinter module, library for GUI application 

import tkinter as tk

#define a class TextEditor that inherits from tk.Tk, 
#the main window of a tkinter application.

# Create a class for the text editor

class TextEditor(tk.Tk): 
    def __init__(self):
        super().__init__() # initializes the parent tk.Tk class.
        self.title("Text Editor") # sets the window title.
        self.geometry("800x600") # sets the window size to 800 pixels wide and 600 pixels high.

        # This calls a method to add the text box and scrollbars to the window.
        self.create_widgets()
        # Calls the method to create the File and Edit menus at the top of the window.
        self.create_menu()
        # Calls the method 
        self.create_context_menu()

    def create_widgets(self):
# Create a Frame to hold the Text widget and both scrollbars
        frame = tk.Frame(self) # 
        frame.pack(fill=tk.BOTH, expand=True)
        # self refers to the instance of the class.
        # self is the main application window (an instance of tk.Tk).
        # tk.Frame(self) Creates a container widget inside the main window
        # fill=tk.BOTH the fram will expend in both dirction (X and Y)
        # expand=True the frame to grow when the window is resize

# Create vertical scrollbarto the right side of the frame.
        v_scroll = tk.Scrollbar(frame, orient=tk.VERTICAL) 
        v_scroll.pack(side=tk.RIGHT, fill=tk.Y) 
        # orient=tk.VERTICAL sets the scrollbar direction
        # side=tk.RIGHT places it at the right of the frame
        # fill=tk.Y makes it stretch vertically

# Create horizontal scrollbar
        h_scroll = tk.Scrollbar(frame, orient=tk.HORIZONTAL)
        h_scroll.pack(side=tk.BOTTOM, fill=tk.X)
        # orient=tk.HORIZONTAL sets the scrollbar direction
        # side=tk.BOTTOM places it at the bottom of the frame
        # fill=tk.X makes it stretch horizontally

# Create Text widget with both scrollbars
        # self.text_area is a variable (attribute) that stores the Text widget 
        # and attaches it to the class instance

        self.text_area = tk.Text(
            frame,
            wrap=tk.NONE,
            font=("Arail, 12"),
            yscrollcommand=v_scroll.set,
            xscrollcommand=h_scroll.set
        )
        #tk.Text - edit text 
        # wrap=tk.NONE,disables word wrapping
        # font=("Arail, 12") sets the font
        # yscrollcommand=v_scroll.set connects vertical scrollbar to the text area.
        # xscrollcommand=h_scroll.set connects horizontal scrollbar to the text area.

        self.text_area.pack(fill=tk.BOTH, expand=True)
        # pack(fill=tk.BOTH, expand=True) makes the text area expand with the window.
              
# Attach scrollbars to the Text widget
        v_scroll.config(command=self.text_area.yview) # it scrolls the text vertically
        h_scroll.config(command=self.text_area.xview) # it scrolls the text horizontally

        # Bind right-click to show context menu
        self.text_area.bind("<Button-3>", self.show_context_menu)

    def create_menu(self):
        menu_bar = tk.Menu(self)  # Create the menu bar

 # FileMenu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)


 # Edit menu
        edit_menu = tk.Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label="Cut", command=lambda: self.text_area.event_generate("<<Cut>>"))
        edit_menu.add_command(label="Copy", command=lambda: self.text_area.event_generate("<<Copy>>"))
        edit_menu.add_command(label="Paste", command=lambda: self.text_area.event_generate("<<Paste>>"))
        menu_bar.add_cascade(label="Edit", menu=edit_menu)

        # Attach the menu bar to the window
        self.config(menu=menu_bar)

    def create_context_menu(self):
        self.context_menu = tk.Menu(self, tearoff=0)
        self.context_menu.add_command(label="Cut", command=lambda: self.text_area.event_generate("<<Cut>>"))
        self.context_menu.add_command(label="Copy", command=lambda: self.text_area.event_generate("<<Copy>>"))
        self.context_menu.add_command(label="Paste", command=lambda: self.text_area.event_generate("<<Paste>>"))

    def show_context_menu(self, event):
        try:
            self.context_menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.context_menu.grab_release()
    
    def new_file(self):
        # Clear the text area
        self.text_area.delete(1.0, tk.END)

# Run the application
if __name__ == "__main__":
     # This checks if the script is being run directly.
     app = TextEditor() 
     # creates an instance of the GUI.
     app.mainloop() 
     # starts the event loop that keeps your tkinter GUI window open and responsive.
    