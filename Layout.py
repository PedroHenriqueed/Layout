import customtkinter
from tkinter import font
from PIL import Image

customtkinter.set_appearance_mode("light")

janela = customtkinter.CTk()
janela.grid_rowconfigure(0, weight=1)
janela.grid_columnconfigure(0, weight=1)
janela.geometry("910x700")
janela.title("")
janela.iconbitmap("syngular.ico")
janela.resizable(False,False)

fonte_negrito = customtkinter.CTkFont(family="Arial", size=14, weight="bold")

def clique():
    print("INICIAR")
    print("Bitlocker:", var_bitlocker.get())
    print("Instalação dos Programas:", var_programas.get())
    print("Criação de usuários:", var_usuarios.get())
    print("Gpedit:", var_gpedit.get())
    print("Servidor NTP:", var_ntp.get())
    print("Evidências:", var_evidencias.get())

def combobox_callback(choice):
    print("Senha Administrador:", choice)


imagem_pill2 = Image.open("Syng.png")

imagem2 = customtkinter.CTkImage(light_image=imagem_pill2,size=(490, 490))

Label_imagem2 = customtkinter.CTkLabel(janela, image=imagem2, text="")
Label_imagem2.pack(side="left", expand=True, fill="both")

texto = customtkinter.CTkLabel(janela, text="Configuração das Estações de Trabalho", font=fonte_negrito)
texto.pack(padx=10, pady=10)

AGR = customtkinter.CTkEntry(janela, placeholder_text="Nome do AGR: ")
AGR.pack(padx=10, pady=10)

AR = customtkinter.CTkEntry(janela, placeholder_text="Nome da AR: ")
AR.pack(padx=10, pady=10)

texto_combo = customtkinter.CTkLabel(janela, text="Senha Administradora", font=fonte_negrito)
texto_combo.pack(padx=2, pady=2)

combobox = customtkinter.CTkComboBox(janela, values=["ARs Próprias", "Outras ARs"],
                                     command=combobox_callback, button_color="#6800ff")
combobox.set("ARs Próprias")
combobox.pack(pady=3)

# Frame para switches
frame_switches = customtkinter.CTkFrame(janela, fg_color="transparent")
frame_switches.pack(pady=20)

# Variáveis de estado
var_bitlocker = customtkinter.StringVar(value="off")
var_programas = customtkinter.StringVar(value="off")
var_usuarios = customtkinter.StringVar(value="off")
var_gpedit = customtkinter.StringVar(value="off")
var_ntp = customtkinter.StringVar(value="off")
var_evidencias = customtkinter.StringVar(value="off")

# Lista de switches com suas variáveis
switches = [
    ("Bitlocker", var_bitlocker),
    ("Instalação dos Programas", var_programas),
    ("Criação de usuários", var_usuarios),
    ("Gpedit", var_gpedit),
    ("Servidor NTP", var_ntp),
    ("Evidências", var_evidencias)
]

# Adiciona os switches em grid
for i, (texto, var) in enumerate(switches):
    s = customtkinter.CTkSwitch(frame_switches, text=texto, variable=var,
                                switch_height=20, switch_width=36,
                                progress_color="#6800ff", button_color="#000000", onvalue="on", offvalue="off")
    s.grid(row=i // 2, column=i % 2, padx=20, pady=10, sticky="w")

# Botão
botao = customtkinter.CTkButton(janela, text="INICIAR", fg_color="#6800ff",
                                hover_color="#808080", font=fonte_negrito, command=clique)
botao.pack(padx=10, pady=10)

janela.mainloop()
