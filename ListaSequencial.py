import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from tkinter import messagebox

class Application(tk.Frame):
    def __init__(self, master=None):
        # master.configure(bg='black')
        super().__init__(master)
        self.master = master
        self.items = []
        self.create_widgets()
        self.prepopulate_list() 
        
    def update_count_label(self):
        count = len(self.items)
        self.count_label.config(text=f"{count} {'elemento' if count == 1 else 'elementos'}")

    def create_widgets(self):
        self.count_label = tk.Label(self.master, text="0 elementos")

        self.count_label.grid(row=1, column=1, columnspan=4, pady=5)

        self.canvas_frame = tk.Frame(self.master)
        self.canvas_frame.grid(row=2, column=1, columnspan=4, sticky="nsew")

        self.canvas = tk.Canvas(self.canvas_frame, width=600, height=100, scrollregion=(0, 0, 2000, 500))
        self.canvas.grid(row=1, column=1, sticky="nsew")

        # self.scrollbar_y = tk.Scrollbar(self.canvas_frame, orient="vertical", command=self.canvas.yview)
        # self.scrollbar_y.grid(row=1, column=2, sticky="ns")

        self.scrollbar_x = tk.Scrollbar(self.master, orient="horizontal", command=self.canvas.xview)
        self.scrollbar_x.grid(row=3, column=1, columnspan=4, sticky="ew")

        # self.canvas.configure(yscrollcommand=self.scrollbar_y.set, xscrollcommand=self.scrollbar_x.set)
        # self.canvas.config(xscrollcommand=self.scrollbar_x.set)

        self.add_button = tk.Button(self.master, text="Adicionar Item", command=self.add_item)
        self.add_button.grid(row=4, column=2, pady=10, padx=50)

        self.remove_by_value_button = tk.Button(self.master, text="Remover Item", command=self.remove_by_value)
        self.remove_by_value_button.grid(row=6, column=2, padx=5, pady=10)

        self.remove_by_index_button = tk.Button(self.master, text="Remover Por Posição", command=self.remove_by_index)
        self.remove_by_index_button.grid(row=7, column=2, padx=5, pady=10)

        self.query_value_entry = tk.Entry(self.master)
        self.query_value_entry.grid(row=4, column=3, padx=5, pady=10)

        self.query_value_button = tk.Button(self.master, text="Consultar Item", command=self.query_by_value)
        self.query_value_button.grid(row=5, column=3, padx=5, pady=10)

        self.query_index_entry = tk.Entry(self.master)
        self.query_index_entry.grid(row=6, column=3, padx=5, pady=10)

        self.query_index_button = tk.Button(self.master, text="Consultar por posição", command=self.query_by_index)
        self.query_index_button.grid(row=7, column=3, padx=5, pady=10)

        self.update_count_label()

        self.items = []

    #pré-popular a lista
    def prepopulate_list(self):
            num_items = simpledialog.askinteger("Quantidade de Itens", "Digite a quantidade de itens na lista:")
            if num_items:
                for i in range(num_items):
                    self.add_empty_item()

    # Adicionei esta função para adicionar um item vazio à lista
    def add_empty_item(self):
        x = len(self.items)
        rect = self.canvas.create_rectangle(x * 100, 0, x * 100 + 100, 100, fill="white", outline="black")
        text = self.canvas.create_text(x * 100 + 50, 50, text="")
        pos_text = self.canvas.create_text(x * 100 + 20, 20, text=f"posição: {x}", anchor="nw")
        self.items.append((rect, text, "", pos_text))
        self.update_count_label()

    def add_item(self):
        item = simpledialog.askstring("Adicionar item", "Digite o item:")
        if item:
            position = simpledialog.askinteger("Adicionar item", "Digite a posição para inserir o item:")
            if position is not None and 0 <= position < len(self.items):
                rect, text, item_value, pos_text = self.items[position]
                if not item_value:
                    self.canvas.itemconfig(text, text=item)
                    self.items[position] = (rect, text, item, pos_text)
                    self.update_count_label()
                else:
                    messagebox.showerror("Erro", "A posição já possui um item. Escolha outra posição.")
            elif position is not None:
                messagebox.showerror("Erro", "Posição inválida. Escolha uma posição dentro do intervalo pré-definido.")


    def remove_by_value(self):
        value = simpledialog.askstring(
            "Remover item", "Digite o valor a ser removido:")
        if value:
            found = False
            empty_position = False
            for i, item in enumerate(self.items):
                if item[2] == value:
                    found = True
                    self.canvas.delete(item[0])
                    self.canvas.delete(item[1])
                    self.canvas.delete(item[3])
                    self.items.pop(i)
                    for j in range(i, len(self.items)):
                        rect, text, item_value, pos_text = self.items[j]
                        self.canvas.move(rect, -100, 0)
                        self.canvas.move(text, -100, 0)
                        self.canvas.move(pos_text, -100, 0)
                        new_pos = self.canvas.itemcget(pos_text, "text")
                        new_pos = f"posição: {int(new_pos.split(': ')[1]) - 1}"
                        self.canvas.itemconfig(pos_text, text=new_pos)
                elif not item[2]:
                    empty_position = True
            self.update_count_label()
            if not found:
                if empty_position:
                    messagebox.showinfo("Remover item", "Valor não encontrado. Há posições vazias.")
                else:
                    messagebox.showinfo("Remover item", "Valor não encontrado.")

    def remove_by_index(self):
        index = simpledialog.askinteger(
            "Remover item", "Digite a posição a ser removida:")
        if index is not None and index >= 0 and index < len(self.items):
            item = self.items[index]
            if item[2]:
                self.canvas.delete(item[0])
                self.canvas.delete(item[1])
                self.canvas.delete(item[3])
                self.items.pop(index)
                for i in range(index, len(self.items)):
                    rect, text, item_value, pos_text = self.items[i]
                    self.canvas.move(rect, -100, 0)
                    self.canvas.move(text, -100, 0)
                    self.canvas.move(pos_text, -100, 0)
                    new_pos = self.canvas.itemcget(pos_text, "text")
                    new_pos = f"posição: {i}"
                    self.canvas.itemconfig(pos_text, text=new_pos)
            else:
                messagebox.showinfo("Remover item", "Não há nenhum elemento para ser removido nesta posição.")
            self.update_count_label()
        elif index is not None:
            self.remove_by_index()

    def query_by_value(self):
        value = self.query_value_entry.get()
        if value:
            found = False
            for i, item in enumerate(self.items):
                rect, text, item_value, pos_text = item
                self.canvas.itemconfig(rect, fill="red")
                self.canvas.update()
                if item_value == value:
                    self.canvas.itemconfig(rect, fill="green")
                    found = True
                    break
                self.canvas.after(600)
                self.canvas.update()
                self.canvas.itemconfig(rect, fill="white")
            self.query_value_entry.delete(0, "end")
            if found:
                print(f"Valor '{value}' encontrado.")
                messagebox.showinfo("Consulta por valor", f"Valor '{value}' encontrado.")
            else:
                print(f"Valor '{value}' não encontrado.")
                messagebox.showinfo("Consulta por valor", f"Valor '{value}' não encontrado.")


    def query_by_index(self):
        index = self.query_index_entry.get()
        if index.isdigit():
            index = int(index)
            if 0 <= index < len(self.items):
                item = self.items[index]
                value = item[2]
                if value:
                    message = f"O valor na posição {index} é {value}."
                else:
                    message = f"Não há nenhum elemento na posição {index}."
            else:
                message = f"A posição {index} não existe."
        else:
            message = "Por favor, digite um número válido para a posição."
        simpledialog.messagebox.showinfo("Consulta por posição", message)


root = tk.Tk()
app = Application(master=root)
app.mainloop()
