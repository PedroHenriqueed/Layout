import customtkinter
from tkinter import font
from tkinter import *
from PIL import Image

customtkinter.set_appearance_mode("light")

janela = customtkinter.CTk()
janela.grid_rowconfigure(0, weight=1)
janela.grid_columnconfigure(0, weight=1)
janela.geometry("900x700")
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

#IMAGEM
imagem_pill2 = Image.open("Syng.png")
img  = Image.open("Syngular.png")

imagem2 = customtkinter.CTkImage(light_image=imagem_pill2,size=(550, 500))

Label_imagem2 = customtkinter.CTkLabel(janela, image=imagem2, text="")
Label_imagem2.place(x=0,y=50)

#FRAME
frame = customtkinter.CTkFrame(master=janela, width=420, height=900)
frame.pack(side=RIGHT)

#FRAME IMAGEM
img = customtkinter.CTkImage(light_image=img,size=(150, 150))

Label_img = customtkinter.CTkLabel(master=frame,image=img, text="")
Label_img.place(x=140,y=0)

#FRAME WIDGETS
texto = customtkinter.CTkLabel(master=frame, text="Configuração das Estações de Trabalho", font=fonte_negrito, width=300)
texto.place(x=50, y=10)

AGR = customtkinter.CTkEntry(master=frame, placeholder_text="Nome do AGR: ")
AGR.place(x=118, y=60)

AR = customtkinter.CTkEntry(master=frame, placeholder_text="Nome da AR: ")
AR.place(x=118, y=120)

texto_combo = customtkinter.CTkLabel(master=frame, text="Senha Administradora", font=fonte_negrito)
texto_combo.place(x=110, y=160)

combobox = customtkinter.CTkComboBox(master=frame, values=["ARs Próprias", "Outras ARs"],
 command=combobox_callback, button_color="#6800ff")
combobox.set("ARs Próprias")
combobox.place(x=118,y=190)

# Frame para switches
frame_switches = customtkinter.CTkFrame(master=frame, fg_color="transparent")
frame_switches.place(x=0,y=250)

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
botao = customtkinter.CTkButton(master=frame, text="INICIAR", fg_color="#6800ff",
                                hover_color="#808080", font=fonte_negrito, command=clique)
botao.place(x=118, y=420)

janela.mainloop()
