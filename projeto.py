from tkinter import *
from tkinter import ttk
import sqlite3


def processa_login(event=None):
    if (
        tela_login_container_2_usuario.get() == "admin"
        and tela_login_container_3_senha.get() == "admin"
    ):
        produtos = busca_produtos()
        for produto in produtos:
            tela_principal_container_3_listagem.insert(
                parent="",
                index=1,
                values=(produto[0], produto[1], produto[2], produto[3]),
            )
        tela_principal.deiconify()
        tela_login.withdraw()
    else:
        aviso["text"] = "Usuário e/ou senha incorreto(s)"
        aviso.pack()


def abre_tela_cadastro_produto():
    tela_cadastro_produto.deiconify()


def busca_produtos():
    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()
    res = cur.execute(
        "select id_produto, nome_produto, unidade_medida, quantidade_estoque from produtos"
    )
    return res.fetchall()


def cadastra_produto():
    params = (
        tela_cadastro_produto_container_2_entrada_1.get(),
        tela_cadastro_produto_container_3_entrada_1.get(),
        tela_cadastro_produto_container_4_entrada_1.get(),
    )
    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()
    cur.execute(
        "insert into produtos (nome_produto, unidade_medida, quantidade_estoque) values (?, ?, ?)",
        params,
    )
    con.commit()
    for filho in tela_principal_container_3_listagem.get_children():
        tela_principal_container_3_listagem.delete(filho)
    produtos = busca_produtos()
    for produto in produtos:
        tela_principal_container_3_listagem.insert(
            parent="", index=1, values=(produto[0], produto[1], produto[2], produto[3])
        )
    tela_cadastro_produto.withdraw()
    tela_cadastro_produto_container_2_entrada_1.delete(0, "end")
    tela_cadastro_produto_container_3_entrada_1.delete(0, "end")
    tela_cadastro_produto_container_4_entrada_1.delete(0, "end")


def edita_produto():
    params = (
        tela_editar_produto_container_2_entrada_1.get(),
        tela_editar_produto_container_3_entrada_1.get(),
        tela_editar_produto_container_4_entrada_1.get(),
        tela_editar_produto_container_1_label_2.cget("text"),
    )
    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()
    cur.execute(
        "update produtos set nome_produto = ?, unidade_medida = ?, quantidade_estoque = ? where id_produto = ?",
        params,
    )
    con.commit()
    for filho in tela_principal_container_3_listagem.get_children():
        tela_principal_container_3_listagem.delete(filho)
    produtos = busca_produtos()
    for produto in produtos:
        tela_principal_container_3_listagem.insert(
            parent="", index=1, values=(produto[0], produto[1], produto[2], produto[3])
        )
    tela_editar_produto.withdraw()
    tela_editar_produto_container_2_entrada_1.delete(0, "end")
    tela_editar_produto_container_3_entrada_1.delete(0, "end")
    tela_editar_produto_container_4_entrada_1.delete(0, "end")


def clique_para_editar(event=None):
    tela_editar_produto.deiconify()
    item = tela_principal_container_3_listagem.item(
        tela_principal_container_3_listagem.focus()
    )
    tela_editar_produto_container_1_label_2.config(text=item["values"][0])
    tela_editar_produto_container_2_entrada_1.delete(0, "end")
    tela_editar_produto_container_2_entrada_1.insert(0, item["values"][1])
    tela_editar_produto_container_3_entrada_1.delete(0, "end")
    tela_editar_produto_container_3_entrada_1.insert(0, item["values"][2])
    tela_editar_produto_container_4_entrada_1.delete(0, "end")
    tela_editar_produto_container_4_entrada_1.insert(0, item["values"][3])


tela_principal = Tk()
tela_login = Toplevel()
tela_cadastro_produto = Toplevel()
tela_editar_produto = Toplevel()
tela_login.bind("<Return>", processa_login)

tela_login_container_1 = Frame(tela_login)
tela_login_container_1["pady"] = 10
tela_login_container_1.pack()
tela_login_container_1_titulo = Label(tela_login_container_1)
tela_login_container_1_titulo["text"] = "Dados do usuário"
tela_login_container_1_titulo.pack()

tela_login_container_2 = Frame(tela_login)
tela_login_container_2["pady"] = 10
tela_login_container_2["padx"] = 100
tela_login_container_2.pack()
tela_login_container_2_label = Label(tela_login_container_2)
tela_login_container_2_label["text"] = "Usuário"
tela_login_container_2_label.pack(side=LEFT)
tela_login_container_2_usuario = Entry(tela_login_container_2)
tela_login_container_2_usuario["width"] = 30
tela_login_container_2_usuario.pack(side=RIGHT)

tela_login_container_3 = Frame(tela_login)
tela_login_container_3["pady"] = 10
tela_login_container_3["padx"] = 100
tela_login_container_3.pack()
tela_login_container_3_label = Label(tela_login_container_3)
tela_login_container_3_label["text"] = "Senha"
tela_login_container_3_label.pack(side=LEFT)
tela_login_container_3_senha = Entry(tela_login_container_3)
tela_login_container_3_senha["width"] = 30
tela_login_container_3_senha["show"] = "*"
tela_login_container_3_senha.pack(side=RIGHT)

tela_login_container_4 = Frame(tela_login)
tela_login_container_4["pady"] = 10
tela_login_container_4.pack()
tela_login_container_4_botao = Button(tela_login_container_4)
tela_login_container_4_botao["text"] = "Entrar"
tela_login_container_4_botao["command"] = processa_login
tela_login_container_4_botao.pack()

tela_login_container_5 = Frame(tela_login)
tela_login_container_5["pady"] = 10
tela_login_container_5.pack()
aviso = Label(tela_login_container_5)

tela_principal_container_1 = Frame(tela_principal)
tela_principal_container_1["pady"] = 10
tela_principal_container_1.pack()
tela_principal_container_1_titulo = Label(tela_principal_container_1)
tela_principal_container_1_titulo["text"] = "Controle de estoque"
tela_principal_container_1_titulo.pack()

tela_principal_container_2 = Frame(tela_principal)
tela_principal_container_2["pady"] = 10
tela_principal_container_2.pack()
tela_principal_container_2 = Button(tela_principal_container_2)
tela_principal_container_2["text"] = "Cadastrar"
tela_principal_container_2["command"] = abre_tela_cadastro_produto
tela_principal_container_2.pack(side=LEFT)

tela_principal_container_3 = Frame(tela_principal)
tela_principal_container_3["pady"] = 10
tela_principal_container_3.pack()
tela_principal_container_3_listagem = ttk.Treeview(tela_principal_container_3)
tela_principal_container_3_listagem["columns"] = (1, 2, 3, 4)
tela_principal_container_3_listagem.heading(1, text="ID do produto")
tela_principal_container_3_listagem.heading(2, text="Nome do produto")
tela_principal_container_3_listagem.heading(3, text="Unidade de medida")
tela_principal_container_3_listagem.heading(4, text="Quantidade em estoque")
tela_principal_container_3_listagem["show"] = "headings"
tela_principal_container_3_listagem.pack()
tela_principal_container_3_listagem.bind("<ButtonRelease-1>", clique_para_editar)

tela_cadastro_produto_container_1 = Frame(tela_cadastro_produto)
tela_cadastro_produto_container_1["pady"] = 10
tela_cadastro_produto_container_1.pack()
tela_cadastro_produto_container_1_titulo = Label(tela_cadastro_produto_container_1)
tela_cadastro_produto_container_1_titulo["text"] = "Cadastro de produto"
tela_cadastro_produto_container_1_titulo.pack()

tela_cadastro_produto_container_2 = Frame(tela_cadastro_produto)
tela_cadastro_produto_container_2["pady"] = 10
tela_cadastro_produto_container_2.pack()
tela_cadastro_produto_container_2_label_1 = Label(tela_cadastro_produto_container_2)
tela_cadastro_produto_container_2_label_1["text"] = "Nome do produto: "
tela_cadastro_produto_container_2_label_1.pack(side=LEFT)
tela_cadastro_produto_container_2_entrada_1 = Entry(tela_cadastro_produto_container_2)
tela_cadastro_produto_container_2_entrada_1["width"] = 30
tela_cadastro_produto_container_2_entrada_1.pack(side=RIGHT)

tela_cadastro_produto_container_3 = Frame(tela_cadastro_produto)
tela_cadastro_produto_container_3["pady"] = 10
tela_cadastro_produto_container_3.pack()
tela_cadastro_produto_container_3_label_1 = Label(tela_cadastro_produto_container_3)
tela_cadastro_produto_container_3_label_1["text"] = "Unidade de medida (un/kg): "
tela_cadastro_produto_container_3_label_1.pack(side=LEFT)
tela_cadastro_produto_container_3_entrada_1 = Entry(tela_cadastro_produto_container_3)
tela_cadastro_produto_container_3_entrada_1["width"] = 30
tela_cadastro_produto_container_3_entrada_1.pack(side=RIGHT)

tela_cadastro_produto_container_4 = Frame(tela_cadastro_produto)
tela_cadastro_produto_container_4["pady"] = 10
tela_cadastro_produto_container_4.pack()
tela_cadastro_produto_container_4_label_1 = Label(tela_cadastro_produto_container_4)
tela_cadastro_produto_container_4_label_1["text"] = "Quantidade em estoque: "
tela_cadastro_produto_container_4_label_1.pack(side=LEFT)
tela_cadastro_produto_container_4_entrada_1 = Entry(tela_cadastro_produto_container_4)
tela_cadastro_produto_container_4_entrada_1["width"] = 30
tela_cadastro_produto_container_4_entrada_1.pack(side=RIGHT)

tela_cadastro_produto_container_5 = Frame(tela_cadastro_produto)
tela_cadastro_produto_container_5["pady"] = 10
tela_cadastro_produto_container_5.pack()
tela_cadastro_produto_container_5 = Button(tela_cadastro_produto_container_5)
tela_cadastro_produto_container_5["text"] = "Cadastrar"
tela_cadastro_produto_container_5["command"] = cadastra_produto
tela_cadastro_produto_container_5.pack(side=LEFT)

tela_editar_produto_container_0 = Frame(tela_editar_produto)
tela_editar_produto_container_0["pady"] = 10
tela_editar_produto_container_0.pack()
tela_editar_produto_container_0_titulo = Label(tela_editar_produto_container_0)
tela_editar_produto_container_0_titulo["text"] = "Edição de produto"
tela_editar_produto_container_0_titulo.pack()

tela_editar_produto_container_1 = Frame(tela_editar_produto)
tela_editar_produto_container_1["pady"] = 10
tela_editar_produto_container_1.pack()
tela_editar_produto_container_1_label_1 = Label(tela_editar_produto_container_1)
tela_editar_produto_container_1_label_1["text"] = "ID do produto: "
tela_editar_produto_container_1_label_1.pack(side=LEFT)
tela_editar_produto_container_1_label_2 = Label(tela_editar_produto_container_1)
tela_editar_produto_container_1_label_2.pack(side=RIGHT)

tela_editar_produto_container_2 = Frame(tela_editar_produto)
tela_editar_produto_container_2["pady"] = 10
tela_editar_produto_container_2.pack()
tela_editar_produto_container_2_label_1 = Label(tela_editar_produto_container_2)
tela_editar_produto_container_2_label_1["text"] = "Nome do produto: "
tela_editar_produto_container_2_label_1.pack(side=LEFT)
tela_editar_produto_container_2_entrada_1 = Entry(tela_editar_produto_container_2)
tela_editar_produto_container_2_entrada_1["width"] = 30
tela_editar_produto_container_2_entrada_1.pack(side=RIGHT)

tela_editar_produto_container_3 = Frame(tela_editar_produto)
tela_editar_produto_container_3["pady"] = 10
tela_editar_produto_container_3.pack()
tela_editar_produto_container_3_label_1 = Label(tela_editar_produto_container_3)
tela_editar_produto_container_3_label_1["text"] = "Unidade de medida (un/kg): "
tela_editar_produto_container_3_label_1.pack(side=LEFT)
tela_editar_produto_container_3_entrada_1 = Entry(tela_editar_produto_container_3)
tela_editar_produto_container_3_entrada_1["width"] = 30
tela_editar_produto_container_3_entrada_1.pack(side=RIGHT)

tela_editar_produto_container_4 = Frame(tela_editar_produto)
tela_editar_produto_container_4["pady"] = 10
tela_editar_produto_container_4.pack()
tela_editar_produto_container_4_label_1 = Label(tela_editar_produto_container_4)
tela_editar_produto_container_4_label_1["text"] = "Quantidade em estoque: "
tela_editar_produto_container_4_label_1.pack(side=LEFT)
tela_editar_produto_container_4_entrada_1 = Entry(tela_editar_produto_container_4)
tela_editar_produto_container_4_entrada_1["width"] = 30
tela_editar_produto_container_4_entrada_1.pack(side=RIGHT)

tela_editar_produto_container_5 = Frame(tela_editar_produto)
tela_editar_produto_container_5["pady"] = 10
tela_editar_produto_container_5.pack()
tela_editar_produto_container_5 = Button(tela_editar_produto_container_5)
tela_editar_produto_container_5["text"] = "Editar"
tela_editar_produto_container_5["command"] = edita_produto
tela_editar_produto_container_5.pack(side=LEFT)

tela_principal.withdraw()
tela_cadastro_produto.withdraw()
tela_editar_produto.withdraw()
tela_principal.mainloop()