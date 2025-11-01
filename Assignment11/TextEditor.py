# Create a simple text editor application. Include vertical and horizontal scrollbars.
# Extend the text editor application by adding File (New and Exit) and Edit 
# (Cut, Copy, and Paste) menus. 
# Also include a context menu for Edit options.
# GUI (Graphical User Interface) applications.
# Extend the text editor application by adding 
# Open, Save, and Save As options to the File menu. 
# Add a Format menu and implement font and/or color
# Extend the text editor application by adding a custom About dialog box.


# This import the tkinter module, library for GUI application 

import tkinter as tk
from tkinter import filedialog, colorchooser, font

# filedialog is submodule inside of tkinter package
# colorchooser is submodule inside of tkinter package
# font is submodule inside of tkinter package
 
#define a class TextEditor that inherits from tk.Tk,  
#the main window of a tkinter application.

# Create a class for the text editor

class TextEditor(tk.Tk): 
    def __init__(self): # This define the constructor for TextEditor class
        super().__init__() # calls the constructor of the parent class tk.Tk.
        self.current_file = None # create instance variable current_file and set to None.
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

# Text
        self.text_area = tk.Text(   #tk.Text - edit text 
            frame,
            wrap=tk.NONE,           # wrap=tk.NONE,disables word wrapping
            font=("Arail, 12"),     # font=("Arail, 12") sets the font
            yscrollcommand=v_scroll.set,
     # yscrollcommand=v_scroll.set connects vertical scrollbar to the text area.
            xscrollcommand=h_scroll.set 
     # xscrollcommand=h_scroll.set connects horizontal scrollbar to the text area.
        )
        
       
        self.text_area.pack(fill=tk.BOTH, expand=True)
           # pack(fill=tk.BOTH, expand=True) makes the text area expand with the window.
              
# Attach scrollbars to the Text widget
        v_scroll.config(command=self.text_area.yview) # it scrolls the text vertically
        h_scroll.config(command=self.text_area.xview) # it scrolls the text horizontally

        # Bind right-click to show context menu
        self.text_area.bind("<Button-3>", self.show_context_menu)

    def create_menu(self):
        menu_bar = tk.Menu(self)  
        # tk.Menu Create the menu bar object
        # self refers to the main window tk.Frame                       

 # FileMenu
        file_menu = tk.Menu(menu_bar, tearoff=0) 
        # Create a submenu named file_menu(varaible), will under "File" in the menu bar
        # Create another object this one is submenu of the manu_bar
        # tearoff is predifined inTkinter - Enables/disables detechable menuus
        # tearoff=0, User cannot detach the munu from the window 
       

        file_menu.add_command(label="New",      command=self.new_file) 
        # add_command() is predifened method of Menu - Adds clickable menu item
        # label predifned in Tkinter - Sets the text of the menu item
        # command is a predifined in Tkinter - set the finction to run the click 

        file_menu.add_command(label="Open",     command=self.open_file)
        file_menu.add_command(label="Save",     command=self.save_file)
        file_menu.add_command(label="Save As",  command=self.save_as_file)
        file_menu.add_separator()
        # add_separator() is predfined method of the Tkinter Menu widget class
        file_menu.add_command(label="Exit",     command=self.quit)
        # self.quit to claose the application
        menu_bar.add_cascade(label="File", menu=file_menu)
        # add_cascade is predifined method - Add the submenu (file_nemu)
        # under the label "File" on the menu bar

 # Create the "Edit" menu
        edit_menu = tk.Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label="Cut", command=lambda: self.text_area.event_generate("<<Cut>>"))
        # command= lambda: self.text_area.event_generate("<<Cut>>") when user click "Cut"
        # execute that lambda function
        # text_area - is a variable (attribute)
        # Inside the lambda: self.text_area.event_generate("<<Cut>>") 
        # triggers a built-in virtual event on text_area
        # event_generate is a method on Tkinter widget
        edit_menu.add_command(label="Copy", command=lambda: self.text_area.event_generate("<<Copy>>"))
        edit_menu.add_command(label="Paste", command=lambda: self.text_area.event_generate("<<Paste>>"))
        menu_bar.add_cascade(label="Edit", menu=edit_menu)


 # Format menu
        format_menu = tk.Menu(menu_bar, tearoff=0)

        format_menu.add_command(label="Font", command=self.choose_font)
        # command=self.choose_font sets the method choose_font class
        # to be invoked when the menu item is selected

        format_menu.add_command(label="Text Color", command=self.choose_color)
        # command=self.choose_color sets the method choose_color to be invoked when selected.

        menu_bar.add_cascade(label="Format", menu=format_menu)
        # menu=format_menu links the submenu to created
        # when the user click "Format" on the menu bar - format_menu appears
        
        self.config(menu=menu_bar)
        # Attach the menu bar to the window (self)

 # Help menu
        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about_dialog)
        menu_bar.add_cascade(label="Help", menu=help_menu)

        self.config(menu=menu_bar )

    def create_context_menu(self):
        self.context_menu = tk.Menu(self, tearoff=0)
        self.context_menu.add_command(label="Cut", command=lambda: self.text_area.event_generate("<<Cut>>"))
        self.context_menu.add_command(label="Copy", command=lambda: self.text_area.event_generate("<<Copy>>"))
        self.context_menu.add_command(label="Paste", command=lambda: self.text_area.event_generate("<<Paste>>"))

    def new_file(self):
        # Clear the text area
        self.text_area.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        # askopebfilename is a function that comes from the filedialog module
        # filetypes is parameter name ("Text file is a label and .txt type)
        if file_path:
            with open(file_path, "r", encoding="utf-8") as file:
                # with keyword open
                content = file.read()
                # Read the entire file and store in the varable content
            self.text_area.delete(1.0, tk.END)
            # this clear the text box
            self.text_area.insert(tk.END, content)
             # this inserts the content
            self.current_file = file_path
            self.title(f"Text Editor - {file_path}")

    def save_file(self):
        """Save current file; if none, prompt Save As"""
        if self.current_file: # check if file already exists
            with open(self.current_file, "w", encoding="utf-8") as file:
                #open the file for writing
                file.write(self.text_area.get(1.0, tk.END))
                # Write the text area content to the file
        else: #if file does not exit
            self.save_as_file()

    def save_as_file(self):
        #Prompt user to choose a new file path and save content
        file_path = filedialog.asksaveasfilename(
             defaultextension=".txt",
             filetypes = [("Text File", "*.txt"), ("All Files", "*.*")]) # ask the user where to save
        if file_path: # check if user provided a file name
            with open(file_path, "w", encoding="utf-8") as file: # open file for writing
                file.write(self.text_area.get(1.0, tk.END)) 
            self.current_file = file_path # Update the current file path
            self.title(f"Text Editor - {file_path}") #update the window title

    def choose_font(self):
        font_window = tk.Toplevel(self) # Create a new window
        font_window.title("Choose Font") # set the window title
        font_window.geometry("450x250") # set wundow size

 #Main frame to organize left (font list) and right (font size)
        main_frame = tk.Frame(font_window) 
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Left side : font family list
        left_frame = tk.Frame(main_frame)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

 # Create a list of available font families
        tk.Label(left_frame, text="Font Family:").pack(pady=5) # Add a label for font family
        families = list(font.families()) # returns all available font families
        font_listbox = tk.Listbox(left_frame, height=8) # create a scrollable list showing 5 items at a time
        for f in families: # for loop adds each font family to the listbox with insert(tk.END, f)
            font_listbox.insert(tk.END, f)
        font_listbox.pack(fill=tk.BOTH, expand=True) # makes the list stretch to fill the window

  # Right side: font size controls
        right_frame = tk.Frame(main_frame) 
        right_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10)

#  Add a label and spinbox for font size
        tk.Label(right_frame, text="Font Size:").pack(pady=5) # Font Size
        font_size_var = tk.IntVar(value=12) # create a variable to store the selected size, defaulting 12
        size_spinbox = tk.Spinbox(right_frame, from_=8, to=72, textvariable=font_size_var, width=5) # lets the user choose a number between 8 and 72
        size_spinbox.pack() # position the spinbox in the popup

# Define the function to apply the font
        def apply_font():
            selected_font = font_listbox.get(tk.ACTIVE) # gets the currently selected font family from the listbox
            selected_size = font_size_var.get() # retrives the selected size from the spinbox
            self.text_area.config(font=(selected_font, selected_size)) # updates the font of the main text editor
            font_window.destroy() # closes the popup window

        tk.Button(font_window, text="Apply", command=apply_font).pack(pady=10) # created a button labeled "Apply"

    def choose_color(self): # define a method 
        color_code = colorchooser.askcolor(title="Choose text color") # open the color chooser dialog
        if color_code[1]: # check if a color was chosen
           self.text_area.config(fg=color_code[1]) # apply the color to the text area


    def show_context_menu(self, event):
        try:
            self.context_menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.context_menu.grab_release()

# Add a custom About dialog box.
    def show_about_dialog(self):
         about_window = tk.Toplevel(self)
         about_window.title("About Text Editor")
         about_window.geometry("450x250")
         about_window.resizable(False, False)
         about_window.transient(self)
         

         tk.Label(about_window, text="Simple Text Editor", font=("Arial", 16, "bold")).pack(pady=10)
         tk.Label(about_window, text="Version 1.0", font=("Arial", 12)).pack()
         tk.Label(
             about_window,
             text="Add a Help menu with a custom About dialog box",
             justify="center",
             padx=20
         ).pack(pady=10)

         tk.Button(about_window, text="OK", command=about_window.destroy).pack(pady=10)


# Run the application
if __name__ == "__main__":
     # This checks if the script is being run directly. 
     app = TextEditor() 
     # creates an instance of the GUI.
     app.mainloop() 
     # starts the event loop that keeps your tkinter GUI window open and responsive.
    