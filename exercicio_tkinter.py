import tkinter as tk

# Listas para armazenar os dados
lista_nomes = []
lista_idades = []
lista_emails = []

# Função para adicionar convidado
def ad():
    valor1 = entrada1.get()
    lista_nomes.append(valor1)
    valor2 = entrada2.get()
    lista_idades.append(valor2)
    valor3 = entrada3.get()
    lista_emails.append(valor3)
    
    alert = tk.Toplevel(root)
    label9 = tk.Label(alert, text="Convidado inserido na lista")
    label9.pack()

    def ok():
        alert.destroy()
        b_ok = tk.Button(alert, text="OK", command=ok)
        b_ok.pack()
        entrada1.delete(0, "end")
        entrada2.delete(0, "end")
        entrada3.delete(0, "end")

    b_ok.pack()

# Função para exibir convidados nas listas
def exi():
    lista1.delete(0, tk.END)
    lista2.delete(0, tk.END)
    lista3.delete(0, tk.END)
    
    for item1 in lista_nomes:
        lista1.insert(tk.END, item1)
    for item2 in lista_idades:
        lista2.insert(tk.END, item2)
    for item3 in lista_emails:
        lista3.insert(tk.END, item3)

# Função para limpar as listas
def limp():
    lista_nomes.clear()
    lista_idades.clear()
    lista_emails.clear()

# Função para localizar um convidado pelo nome
def loc():
    alert1 = tk.Toplevel(root)
    alert1.title("Localizador Convidado")
    valor = entrada4.get()
    
    if valor in lista_nomes:
        label_alert = tk.Label(alert1, text="Convidado Localizado", font=("Arial", 15))
        label_alert.pack()
    else:
        label_alert1 = tk.Label(alert1, text="Convidado Não Localizado", font=("Arial", 15))
        label_alert1.pack()

    def ok():
        alert1.destroy()

    b_alert = tk.Button(alert1, text="OK", font=("Arial", 15), command=ok)
    b_alert.pack()

# Criando a janela principal
root = tk.Tk()
root.title("Convite")
root.geometry("650x550")

# Labels e widgets
label1 = tk.Label(root, text="Convidados", font=("Arial", 15))
label1.grid(row=0, column=0)

label2 = tk.Label(root, text="Nome:", font=("Arial", 15))
label2.grid(row=1, column=0)

entrada1 = tk.Entry(root, font=("Arial", 15))
entrada1.grid(row=1, column=1)

label3 = tk.Label(root, text="Idade:", font=("Arial", 15))
label3.grid(row=2, column=0)

entrada2 = tk.Entry(root, font=("Arial", 15))
entrada2.grid(row=2, column=1)

label4 = tk.Label(root, text="Email:", font=("Arial", 15))
label4.grid(row=3, column=0)

entrada3 = tk.Entry(root, font=("Arial", 15))
entrada3.grid(row=3, column=1)

b_ad = tk.Button(root, text="Adicionar", font=("Arial", 15), command=ad)
b_ad.grid(row=4, column=0)

b_exibir = tk.Button(root, text="Exibir", font=("Arial", 15), command=exi)
b_exibir.grid(row=4, column=1)

b_limpar = tk.Button(root, text="Limpar", font=("Arial", 15), command=limp)
b_limpar.grid(row=4, column=2)

label_loc = tk.Label(root, text="Localizar convidado:", font=("Arial", 15))
label_loc.grid(row=6, column=0)

entrada4 = tk.Entry(root, font=("Arial", 15))
entrada4.grid(row=6, column=1)

b_loc = tk.Button(root, text="Localizar", font=("Arial", 15), command=loc)
b_loc.grid(row=6, column=2)

label5 = tk.Label(root, text="Lista de Convidados", font=("Arial", 15))
label5.grid(row=7, column=1)

label6 = tk.Label(root, text="Nome", font=("Arial", 15))
label6.grid(row=8, column=0)

label7 = tk.Label(root, text="Idade", font=("Arial", 15))
label7.grid(row=8, column=1)

label8 = tk.Label(root, text="Email", font=("Arial", 15))
label8.grid(row=8, column=2)

lista1 = tk.Listbox(root, font=("Arial", 15))
lista1.grid(row=9, column=0)

lista2 = tk.Listbox(root, font=("Arial", 15))
lista2.grid(row=9, column=1)

lista3 = tk.Listbox(root, font=("Arial", 15))
lista3.grid(row=9, column=2)

root.mainloop()
