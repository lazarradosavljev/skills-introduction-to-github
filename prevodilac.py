

import tkinter as tk
from tkinter import messagebox, filedialog
from googletrans import Translator

def translate_text():
    """
    Translates text from English to Serbian and displays the result.
    """
    input_text = input_text_box.get("1.0", tk.END).strip()
    if not input_text:
        messagebox.showwarning("Input Error", "Please enter text to translate.")
        return

    translator = Translator()
    try:
        translation = translator.translate(input_text, src='en', dest='sr')
        output_text_box.config(state=tk.NORMAL)
        output_text_box.delete("1.0", tk.END)
        output_text_box.insert(tk.END, translation.text)
        output_text_box.config(state=tk.DISABLED)
    except Exception as e:
        messagebox.showerror("Translation Error", f"An error occurred: {e}")

def save_translation():
    """
    Saves the translated text to a file in a user-specified folder.
    """
    translated_text = output_text_box.get("1.0", tk.END).strip()
    if not translated_text:
        messagebox.showwarning("Save Error", "No translated text to save.")
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
root.title("English to Serbian Translator")
root.geometry("500x500")
root.resizable(False, False)

# Input label
input_label = tk.Label(root, text="Enter English Text:", font=("Arial", 12))
input_label.pack(pady=10)

# Input text box
input_text_box = tk.Text(root, height=10, width=50, font=("Arial", 12))
input_text_box.pack(pady=10)

# Translate button
translate_button = tk.Button(root, text="Translate to Serbian", font=("Arial", 12), command=translate_text)
translate_button.pack(pady=10)

# Output label
output_label = tk.Label(root, text="Translated Serbian Text:", font=("Arial", 12))
output_label.pack(pady=10)

# Output text box
output_text_box = tk.Text(root, height=10, width=50, font=("Arial", 12), state=tk.DISABLED)
output_text_box.pack(pady=10)

# Save button
save_button = tk.Button(root, text="Save Translation", font=("Arial", 12), command=save_translation)
save_button.pack(pady=10)

# Run the application
root.mainloop()