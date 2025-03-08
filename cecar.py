import tkinter as tk 
from tkinter import messagebox

def caecar_cipher(text, shift, mode):
    result =""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                result += chr((ord(char)-ord('a') + (shift if mode == 'encrypt' else - shift)) % 26 + ord('a'))

            elif char.isupper():
                result += chr((ord(char) - ord('A') + (shift if mode == 'encrypt' else - shift)) % 26 + ord('A'))
        else:
            result += char
        return
    
def process():
    text = entry_text.get()
    shift = int(entry_shift.get())
    mode = var_mode.get()

    if not text:
        messagebox.showerror("Input Error", "Please enter text to be processed.")
        return

    if mode == 'encrypt':
        result = caecar_cipher(text, shift, 'encrypt')
    else:
        result = caecar_cipher(text, shift, 'decrypt')

    label_result.config(text="Result: "+result)

window = tk.Tk()
window.title("Caecar cipher")

label_text = tk.Label(window, text="Enter Text")
label_text.grid(row=0,column=0)

entry_text=tk.Entry(window, width=100)
entry_text.grid(row=0,column=1)

label_shift = tk.Label(window, text="Enter shift (1-25):")
label_shift.grid(row=1, column=0)

entry_shift = tk.Entry(window, width=100)
entry_shift.grid(row=1, column=1)

var_mode = tk.StringVar(value="encrypt")
radio_encrypt = tk.Radiobutton(window, text="Encrypt",
variable = var_mode, value="encrypt")
radio_encrypt.grid(row=2, column=0)

radio_decrypt = tk.Radiobutton(window, text="Decrypt", variable=var_mode, value="decrypt")
radio_decrypt.grid(row=2, column=1)

button_process = tk.Button(window,text="Process",
command=process)
button_process.grid(row=3, column=0, columnspan=2)

label_result = tk.Label(window, text="Result")
label_result.grid(row=4, column=0, columnspan=2)

window.mainloop()

