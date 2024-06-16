import customtkinter as ctk

janela = ctk.CTk()
janela.geometry("400x300")
janela.title("Alterar Temas")

temas = [
    {"bg_color": "red", "fg_color": "white"},
    {"bg_color": "blue", "fg_color": "yellow"},
    {"bg_color": "green", "fg_color": "black"},
    {"bg_color": "purple", "fg_color": "pink"},
    {"bg_color": "orange", "fg_color": "blue"},
    {"bg_color": "grey", "fg_color": "white"},
    {"bg_color": "black", "fg_color": "green"},
    {"bg_color": "yellow", "fg_color": "red"},
    {"bg_color": "pink", "fg_color": "brown"},
    {"bg_color": "cyan", "fg_color": "navy"},
]

tema_atual = 0

def alterar_tema():
    global tema_atual
    tema = temas[tema_atual]
    janela.configure(bg=tema["bg_color"])
    label.configure(text_color=tema["fg_color"])
    botao.configure(text_color=tema["fg_color"], fg_color=tema["bg_color"])
    tema_atual = (tema_atual + 1) % len(temas)

label = ctk.CTkLabel(janela, text="Clique no botão para alterar o tema", font=("Arial", 18))
label.pack(pady=20)

botao = ctk.CTkButton(janela, text="Alterar Tema", command=alterar_tema)
botao.pack(pady=20)

alterar_tema()
janela.mainloop()
