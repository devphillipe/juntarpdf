import tkinter as tk
from tkinter import filedialog
import PyPDF2

root = tk.Tk()
root.title("PDF Fusion Pro")
root.configure(bg='#87CEEB')

# Define a fonte em negrito
bold_font = ('Arial', 12, 'bold')

# Define a cor dos botões
button_color = '#fff'

pdf_files = []

def open_pdfs():
    files = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
    for file in files:
        pdf_files.append(file)
        listbox.insert(tk.END, file)

def remove_pdf():
    selection = listbox.curselection()
    if selection:
        listbox.delete(selection[0])
        pdf_files.pop(selection[0])

def merge_pdfs():
    merger = PyPDF2.PdfMerger()
    for file in pdf_files:
        merger.append(file)
    save_file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
    if save_file:
        with open(save_file, 'wb') as output_file:
            merger.write(output_file)
    listbox.delete(0, tk.END)
    pdf_files.clear()

# Cria o botão "Abrir PDFs" com a cor personalizada e fonte em negrito
open_button = tk.Button(root, text="Abrir PDFs", bg=button_color, font=bold_font, command=open_pdfs)
open_button.pack(pady=10)

# Cria o campo de lista com a cor personalizada e fonte em negrito
listbox = tk.Listbox(root, bg=button_color, font=bold_font, width=50)
listbox.pack(fill='both', expand=True, padx=10, pady=10)

# Cria o botão "Remover PDF" com a cor personalizada e fonte em negrito
remove_button = tk.Button(root, text="Remover PDF", bg=button_color, font=bold_font, command=remove_pdf)
remove_button.pack(pady=10)

# Cria o botão "Mesclar PDFs" com a cor personalizada e fonte em negrito
merge_button = tk.Button(root, text="Mesclar PDFs", bg=button_color, font=bold_font, command=merge_pdfs)
merge_button.pack(pady=10)

root.mainloop()
