import customtkinter 
from tkinter import Canvas, Frame, Scrollbar
from PIL import Image

customtkinter.set_appearance_mode("light")

janela = customtkinter.CTk()
janela.geometry("700x800")

# Definindo a variável switch_var
switch_var = customtkinter.StringVar(value="off")

# Frame principal para o TextBox à esquerda
frame_principal = customtkinter.CTkFrame(janela)
frame_principal.pack(fill="both", expand=True, padx=10, pady=10, side="left")

customtkinter_textbox = customtkinter.CTkTextbox(frame_principal, activate_scrollbars=False)
customtkinter_textbox.pack(fill="both", expand=True)

# Conteúdo de exemplo para o TextBox
for i in range(20):
    customtkinter_textbox.insert("end", f"Conteúdo de teste {i}\n")

# Canvas para conter a área rolável à direita
canvas = Canvas(janela, width=300)
canvas.pack(side="right", fill="both", expand=True)

# Scrollbar vertical
scrollbar = Scrollbar(janela, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

# Frame dentro do canvas para os widgets
frame_direita = Frame(canvas)
canvas.create_window((0, 0), window=frame_direita, anchor="nw")
frame_direita.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Adicionando widgets ao frame direito
texto = customtkinter.CTkLabel(frame_direita, text="Configuração das Estações de Trabalho")
texto.pack(padx=10, pady=10)

AGR = customtkinter.CTkEntry(frame_direita, placeholder_text="Nome do AGR: ")
AGR.pack(padx=10, pady=10)

AR = customtkinter.CTkEntry(frame_direita, placeholder_text="Nome da AR: ")
AR.pack(padx=10, pady=10)

combobox = customtkinter.CTkComboBox(frame_direita, values=["ARs Próprias", "Outras ARs"], command=lambda x: print(f"Senha Administrador: {x}"), button_color="#6800ff")
combobox.set("ARs Próprias")
combobox.pack(pady=10)

# Adicionando switches ao frame direito
switches = [
    "Bitlocker", "Instalação dos Programas", "Criação de usuários", "Gpedit", "Servidor NTP", "Evidências"
]

for switch_texto in switches:
    switch = customtkinter.CTkSwitch(frame_direita, text=switch_texto, command=lambda: print(switch_texto), variable=switch_var, onvalue="on", offvalue="off", progress_color="#6800ff", button_color="#000000")
    switch.pack(pady=5)

# Botão de iniciar
botao = customtkinter.CTkButton(frame_direita, text="INICIAR", fg_color="#6800ff", hover_color="#808080", command=lambda: print("INICIAR"))
botao.pack(padx=10, pady=10)

# Configurar a rolagem
canvas.configure(yscrollcommand=scrollbar.set)
janela.mainloop()
