nome = input("Escreva seu nome:")
idade = int(input("Escreva sua idade:"))
renda = float(input("Escreva sua renda:"))
print("Olá", nome, "com idade",idade,"renda de",renda)

////////////////////////////////////////////////////////////////////////////////////////////

def validador():
    while True:
        try:
            op = int(input("Insira uma opção (1, 2 ou 3): "))
            if op == 1 or op == 2 or op == 3:
                return op
            else:
                print("Erro, digite uma opção correta.")
        except ValueError:
            print("Erro, digite um número válido.")

def main():
    nomes = []  # Lista para armazenar os nomes dos usuários
    while True:
        print("Menu\n1 - Adicionar usuário")
        print("2 - Consultar usuário\n3 - Fazer Compra")
        
        op = validador()  # Obtém a opção do usuário
        
        if op == 1:
            nome = input("Insira o nome: ")
            nomes.append(nome)
        
        elif op == 2:
            nome = input("Localizar usuário, insira o nome: ")
            
            if not nomes:
                print("Lista vazia")
            elif nome in nomes:
                print("Cliente encontrado")
            else:
                print("Cliente não encontrado")
        
        elif op == 3:
            compra = float(input("Insira o valor total dos produtos: "))
            total = 0
            total = total + 0.9 * compra  # Aplica um desconto de 10%
            print(f"Valor a pagar: {total:.2f}")
        
        continuar = input("Deseja continuar? (s/n): ")
        if continuar.lower() != 's':
            break

if __name__ == "__main__":
    main()

////////////////////////////////////////////////////////////////////////////////////////////

import tkinter as tk
from tkinter import messagebox

# Função para validar a opção
def validador():
    try:
        op = int(op_entry.get())
        if op == 1 or op == 2 or op == 3:
            return op
        else:
            messagebox.showerror("Erro", "Opção inválida. Digite 1, 2 ou 3.")
    except ValueError:
        messagebox.showerror("Erro", "Erro: Digite um número válido.")

# Função para adicionar usuário
def adicionar_usuario():
    nome = nome_entry.get()
    if nome:
        nomes.append(nome)
        messagebox.showinfo("Sucesso", f"Usuário {nome} adicionado com sucesso.")
        nome_entry.delete(0, tk.END)  # Limpa o campo de entrada
    else:
        messagebox.showerror("Erro", "Por favor, insira um nome.")

# Função para consultar usuário
def consultar_usuario():
    nome = nome_entry.get()
    if nome:
        if nome in nomes:
            messagebox.showinfo("Sucesso", f"Cliente {nome} encontrado.")
        else:
            messagebox.showerror("Erro", f"Cliente {nome} não encontrado.")
    else:
        messagebox.showerror("Erro", "Por favor, insira o nome do cliente.")

# Função para fazer a compra
def fazer_compra():
    try:
        compra = float(compra_entry.get())
        total = 0
        total = total + 0.9 * compra  # Aplica um desconto de 10%
        messagebox.showinfo("Sucesso", f"Valor a pagar: R$ {total:.2f}")
        compra_entry.delete(0, tk.END)  # Limpa o campo de entrada
    except ValueError:
        messagebox.showerror("Erro", "Erro: Digite um valor válido para a compra.")

# Função principal para mostrar o menu
def mostrar_menu():
    op = validador()
    if op == 1:
        adicionar_usuario()
    elif op == 2:
        consultar_usuario()
    elif op == 3:
        fazer_compra()

# Lista para armazenar os nomes dos usuários
nomes = []

# Configuração da janela principal
root = tk.Tk()
root.title("Sistema de Usuários")

# Labels e campos de entrada
op_label = tk.Label(root, text="Digite uma opção (1, 2 ou 3):")
op_label.pack()

op_entry = tk.Entry(root)
op_entry.pack()

nome_label = tk.Label(root, text="Nome do Usuário:")
nome_label.pack()

nome_entry = tk.Entry(root)
nome_entry.pack()

compra_label = tk.Label(root, text="Valor da Compra:")
compra_label.pack()

compra_entry = tk.Entry(root)
compra_entry.pack()

# Botão para mostrar o menu
menu_button = tk.Button(root, text="Executar", command=mostrar_menu)
menu_button.pack()

# Inicia o loop da interface gráfica
root.mainloop()
