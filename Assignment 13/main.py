# main.py
# 1. Imports and Setup
import tkinter as tk
# Tkinter GUI tools
from tkinter import messagebox, simpledialog, scrolledtext
import os
# OS functions for file handling
from wiki_bot import WikiBot
# WikiBot class for sending edits to Wikipedia


# 2. Initialize WikiBot
wiki_bot = WikiBot()
wiki_bot.login()  
# A WikiBot object is created and immediately logged in
# This means the app is ready to send edits to Wikipedia.

# 3. Local Storage Folder

PAGES_DIR = "wiki_pages"  # folder where pages are stored locally
os.makedirs(PAGES_DIR, exist_ok=True)
# A folder named wiki_pages is created if it does not exist.

# 4. User Management

users = {"admin": "1234"}  #
# default users dictionary stores username → password in memory user system
current_user = None
# current_user keeps the logged-in user


# 5. Global Page Variables
current_page_title = None
current_page_content = ""
# track the  working page


# 6. Login Window Class
# this class ask for username/password
# Lets user log in OR create a new user
# Opens the main wiki editor after login
class LoginWindow:
    # 6.1 Constructor (__init__)
    # Shows username + password entry boxes and a Login/Create User button.
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("350x200")

        tk.Label(root, text="Username:").pack(pady=5)
        self.username_entry = tk.Entry(root, width=30)
        self.username_entry.pack(pady=5)

        tk.Label(root, text="Password:").pack(pady=5)
        self.password_entry = tk.Entry(root, show="*", width=30)
        self.password_entry.pack(pady=5)

        tk.Button(root, text="Login / Create User", command=self.login_or_create).pack(pady=10)

    # 6.2 login_or_create()
     # If username exists
        # If username exists
        # If password correct
        # show erro
     # If new username
        # Save new user in users dict
        # Log in
    def login_or_create(self):
        global current_user

        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if not username:
            messagebox.showerror("Error", "Enter username")
            return

        # Existing user login
        if username in users:
            if users[username] == password:
                current_user = username
                messagebox.showinfo("Success", f"Welcome back, {username}!")
                self.launch_main_window()
            else:
                messagebox.showerror("Error", "Incorrect password")
        else:
            # Create new user
            if not password:
                password = simpledialog.askstring(
                    "Create Password", f"Enter password for {username}:", show="*"
                )
                if not password:
                    messagebox.showerror("Error", "Password cannot be empty")
                    return

            users[username] = password
            current_user = username
            messagebox.showinfo("Success", f"User '{username}' created!")
            self.launch_main_window()

    # 6.3 launch_main_window()
    def launch_main_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        MainWindow(self.root)


# 7. Main Window Class
 # This is the main wiki editing interface.

class MainWindow:
    # 7.1 Constructor (__init__)
     # Creates the window layout
    def __init__(self, root):
        self.root = root
        self.root.title("Wiki Editing App")
        self.root.geometry("700x550")

        tk.Label(root, text=f"Logged in as: {current_user}", font=("Arial", 10)).pack(pady=5)

        tk.Label(root, text="Page Title:").pack(pady=5)
        self.page_entry = tk.Entry(root, width=50)
        self.page_entry.pack(pady=5)

        tk.Label(root, text="Content:").pack(pady=5)
        self.text_area = scrolledtext.ScrolledText(root, width=80, height=20)
        self.text_area.pack(pady=5)

        # Action Buttons
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Search", width=12, command=self.search_page).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Edit", width=12, command=self.edit_page).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="Preview", width=12, command=self.preview_page).grid(row=0, column=2, padx=5)
        tk.Button(button_frame, text="Submit (Local)", width=12, command=self.submit_page).grid(row=0, column=3, padx=5)
        tk.Button(button_frame, text="Submit to Wiki", width=14, command=self.submit_to_wiki).grid(row=0, column=4, padx=5)
        tk.Button(button_frame, text="Close", width=12, command=self.close_app).grid(row=0, column=5, padx=5)

    # 8. Search Function LOCAL FILE 
    def search_page(self):
        global current_page_title, current_page_content

        title = self.page_entry.get().strip()
        if not title:
            messagebox.showerror("Error", "Enter a page title")
            return

        filename = os.path.join(PAGES_DIR, f"{title}.txt")

        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as f:
                content = f.read()
        else:
            messagebox.showwarning("Not Found", f"'{title}' not found. Starting a NEW page.")
            content = ""

        current_page_title = title
        current_page_content = content
        self.text_area.delete("1.0", tk.END)
        self.text_area.insert(tk.END, content)

        messagebox.showinfo("Search", f"Page '{title}' loaded.")

    # 9. Edit Function
    def edit_page(self):
        global current_page_content

        if not current_page_title:
            messagebox.showerror("Error", "Search a page first.")
            return

        content = self.text_area.get("1.0", tk.END).strip()
        current_page_content = content
        messagebox.showinfo("Edit", f"Page '{current_page_title}' is ready for editing.")

    # 10. Preview Function
    def preview_page(self):
        if not current_page_title:
            messagebox.showerror("Error", "Search a page first.")
            return

        content = self.text_area.get("1.0", tk.END).strip()
        PreviewWindow(self.root, current_page_title, content)

    # 11. Save Locally
    def submit_page(self):
        global current_page_title

        if not current_page_title:
            messagebox.showerror("Error", "Search a page first.")
            return

        content = self.text_area.get("1.0", tk.END).strip()
        filename = os.path.join(PAGES_DIR, f"{current_page_title}.txt")

        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)

        messagebox.showinfo("Success", f"Page '{current_page_title}' saved locally!")

    # 12. Submit to Wikipedia
    def submit_to_wiki(self):
        global current_page_title, current_page_content

        if not current_page_title:
            messagebox.showerror("Error", "Search a page first.")
            return

        content = self.text_area.get("1.0", tk.END).strip()
        current_page_content = content

        # Always edit in the user's sandbox to avoid protected pages
        wiki_page_title = f"User:{current_user}/Sandbox"

        try:
            wiki_bot.edit_page(wiki_page_title, content, summary=f"Edit from WikiBot by {current_user}")
            messagebox.showinfo("Success", f"Page '{wiki_page_title}' submitted to Wiki successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to submit to Wiki:\n{e}")

    # 13. Close Application
    def close_app(self):
        self.root.quit()

# 14. Preview Window Class
class PreviewWindow:
    def __init__(self, root, title, content):
        self.preview_win = tk.Toplevel(root)
        self.preview_win.title(f"Preview: {title}")
        self.preview_win.geometry("700x500")

        tk.Label(self.preview_win, text=f"Preview of: {title}", font=("Arial", 12)).pack(pady=5)

        text_area = scrolledtext.ScrolledText(self.preview_win, width=80, height=25)
        text_area.pack(pady=5)
        text_area.insert(tk.END, content)
        text_area.config(state=tk.DISABLED)

        tk.Button(self.preview_win, text="Close Preview", command=self.preview_win.destroy).pack(pady=10)


# 15. main() Function
def main():
    root = tk.Tk()
    LoginWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()
