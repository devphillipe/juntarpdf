import tkinter as tk

root = tk.Tk()
root.title("Exemplo de UI com cores personalizadas")
root.configure(bg='#ADD8E6')

# Define a fonte em negrito
bold_font = ('Arial', 12, 'bold')

# Define a cor dos botões
button_color = '#F5F5F5'

# Cria o botão "Abrir PDFs" com a cor personalizada e fonte em negrito
open_button = tk.Button(root, text="Abrir PDFs", bg=button_color, font=bold_font)
open_button.pack(pady=10)

# Cria o campo de lista com a cor personalizada e fonte em negrito
listbox = tk.Listbox(root, bg=button_color, font=bold_font)
listbox.pack(fill='both', expand=True, padx=10, pady=10)

# Cria o botão "Mesclar PDFs" com a cor personalizada e fonte em negrito
merge_button = tk.Button(root, text="Mesclar PDFs", bg=button_color, font=bold_font)
merge_button.pack(pady=10)

# Cria o botão "Salvar PDF" com a cor personalizada e fonte em negrito
save_button = tk.Button(root, text="Salvar PDF", bg=button_color, font=bold_font)
save_button.pack(pady=10)

root.mainloop()
