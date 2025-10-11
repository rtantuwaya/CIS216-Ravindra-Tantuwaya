# Create a Hello World GUI application.
# This appication creates a simple window that dispay "Hello World!"

import tkinter as tk
# Import the tkinter module which is used to create GUI application


def main():
# Created and run the Hellow World 

    root = tk.Tk()
# Create the main window (root of the GUI)

    root.title("Hellow World")
# Set the title of the window

    root.geometry("300x100")
# Set the size of the window (width and height)


    label = tk.Label(root, text="Hello World", font=("Arial", 20))
# Create a label widget with the text "Hello World"
# font=("Arial", 20) Set the font to Arial with size 20

    label.pack(pady=20)
# Place the label in the window with padding on Y-axis


    root.mainloop()
# Start the main loop which keeps the window open

if __name__ == "__main__":
    main()

# Check if the script is being run directly (not imported)