import random
import string
import tkinter as tk
from tkinter import messagebox

def gerar_senha(tamanho=8):
    # Define os caracteres possíveis: letras, dígitos e caracteres especiais
    caracteres = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>/?"
    # Gera a senha aleatória
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def mostrar_senha():
    senha = gerar_senha()
    # Cria uma nova janela para exibir a senha
    janela_senha = tk.Toplevel(root)
    janela_senha.title("Senha Gerada")
    label = tk.Label(janela_senha, text=f"Sua senha é:\n{senha}", font=("Arial", 14))
    label.pack(padx=20, pady=20)
    # Opcional: adiciona um botão para copiar a senha para a área de transferência
    def copiar():
        root.clipboard_clear()
        root.clipboard_append(senha)
        messagebox.showinfo("Copiado", "Senha copiada para a área de transferência!")
    botao_copiar = tk.Button(janela_senha, text="Copiar para área de transferência", command=copiar)
    botao_copiar.pack(pady=10)

# Janela principal
root = tk.Tk()
root.title("Gerador de Senha")
root.geometry("300x150")

# Botão para gerar a senha
botao_gerar = tk.Button(root, text="Gerar Senha", command=mostrar_senha, font=("Arial", 12))
botao_gerar.pack(expand=True)

root.mainloop()
