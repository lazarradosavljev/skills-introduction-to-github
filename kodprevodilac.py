

import tkinter as tk
from tkinter import messagebox, filedialog
from googletrans import Translator

def translate_message():
    """
    Translates an email message from English to Serbian and displays the result.
    """
    email_text = input_text_box.get("1.0", tk.END).strip()
    if not email_text:
        messagebox.showwarning("Input Error", "Please enter the email message to translate.")
        return

    translator = Translator()
    try:
        translation = translator.translate(email_text, src='en', dest='sr')
        output_text_box.config(state=tk.NORMAL)
        output_text_box.delete("1.0", tk.END)
        output_text_box.insert(tk.END, translation.text)
        output_text_box.config(state=tk.DISABLED)
    except Exception as e:
        messagebox.showerror("Translation Error", f"An error occurred: {e}")

def save_translation():
    """
    Saves the translated email message to a file in a user-specified folder.
    """
    translated_text = output_text_box.get("1.0", tk.END).strip()
    if not translated_text:
        messagebox.showwarning("Save Error", "No translated email message to save.")
        return

    file_path = filedialog.asksaveasfilename(
        title="Save Translation",
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    
    if file_path:
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(translated_text)
            messagebox.showinfo("Success", f"Translation saved to {file_path}")
        except Exception as e:
            messagebox.showerror("Save Error", f"An error occurred while saving: {e}")

# Create the main window
root = tk.Tk()
root.title("Email Translator (English to Serbian)")

# Set the window size to be larger
root.geometry("1600x800")  # Set to double the size as you requested
root.resizable(True, True)  # Allow resizing

# Input label
input_label = tk.Label(root, text="Enter Email Message (English):", font=("Arial", 12))
input_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

# Output label
output_label = tk.Label(root, text="Translated Email Message (Serbian):", font=("Arial", 12))
output_label.grid(row=0, column=1, padx=10, pady=10, sticky="w")

# Input text box
input_text_box = tk.Text(root, height=25, width=70, font=("Arial", 12))
input_text_box.grid(row=1, column=0, padx=10, pady=10)

# Output text box
output_text_box = tk.Text(root, height=25, width=70, font=("Arial", 12), state=tk.DISABLED)
output_text_box.grid(row=1, column=1, padx=10, pady=10)

# Translate button
translate_button = tk.Button(root, text="Translate to Serbian", font=("Arial", 12), command=translate_message)
translate_button.grid(row=2, column=0, columnspan=2, pady=10)

# Save button
save_button = tk.Button(root, text="Save Translated Message", font=("Arial", 12), command=save_translation)
save_button.grid(row=3, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
