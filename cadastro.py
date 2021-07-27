from tkinter import *
import modules

root = Tk()
db = modules.InserirDados()
#Funções

def extrairDados(): #Fará a extração dos dados inseridos nos campos do sistema
    data_produto = {
        "nome": e_nome.get(),
        "descricao": e_desc.get(),
        "categoria": e_cate.get(),
        "preco": e_prec.get()
    }
    
    #Os dados somente serão inseridos no banco de dados se, no mínimo,
    #o campo nome esteja preenchido. Então:
    if data_produto["nome"] == "":
        label_warning = Label(root, text="*WARNING: Preencha o campo nome")
        label_warning.grid(row=4, column=1)
    else:
        print(data_produto)
        db.insert_into(data_produto)
    

#Elementos
label_nome = Label(root, text="Nome: ",)
label_desc = Label(root, text="Descrição: ")
label_cate = Label(root, text="Categoria: ")
label_prec = Label(root, text="Preço: ")

e_nome = Entry(root)
e_desc = Entry(root)
e_cate = Entry(root)
e_prec = Entry(root)

submmit = Button(root, text="Submit", command=extrairDados)

#Exposição

label_nome.grid(row=0)
e_nome.grid(row=0, column=1)

label_desc.grid(row=1)
e_desc.grid(row=1, column=1)

label_cate.grid(row=2)
e_cate.grid(row=2, column=1)

label_prec.grid(row=3)
e_prec.grid(row=3, column=1)

submmit.grid(row=4)

#Mainloop

root.mainloop()