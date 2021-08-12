import tkinter as tk
from tkinter import messagebox as msg
from tkinter.ttk import Notebook

#pip install requests
import requests

#Toda vez que quiser fazer um frame é so chamar essa classe
#passando um tk.Frame dela
class LanguageTab(tk.Frame):
    def _init_(self, master, lang_name, lang_code):
        super()._init_(master)

        self.lang_name = lang_name
        self.lang_code = lang_code

        self.translation_var = tk.StringVar(self)
        self.translation_var.set("")

        self.translated_label = tk.Label(self, textvar=self.translation_var, bg="lightgrey", fg="black")

        self.copy_button = tk.Button(self, text="Copiar", command=self.copy_to_clipboard)
        self.copy_button.pack(side=tk.BOTTOM, fill=tk.X)
        self.translated_label.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def copy_to_clipboard(self):
        root = self.winfo_toplevel()
        root.clipboard_clear()
        root.clipboard_append(self.translation_var.get())
        msg.showinfo("Área de transferência", "Copiado com sucesso!!")

# Janela Principal
class TranslateBook(tk.Tk):
    def _init_(self):
        super()._init_()

        self.title("Tradutor tabajara pro Jacson")
        self.geometry("500x300")

        self.menu = tk.Menu(self, bg="lightgrey", fg="black")

        self.languages_menu = tk.Menu(self.menu, tearoff=0, bg="lightgrey", fg="black")
        self.languages_menu.add_command(label="Nova", command=self.show_new_language_popup)
        self.languages_menu.add_command(label="Português",
                                        command=lambda: self.add_new_tab(LanguageTab(self, "Portugues", "pt")))

        self.menu.add_cascade(label="Líguas", menu=self.languages_menu)

        self.config(menu=self.menu)

        self.notebook = Notebook(self)

        self.language_tabs = []

        english_tab = tk.Frame(self.notebook)

        self.translate_button = tk.Button(english_tab, text="Traduzir", command=self.translate)
        self.translate_button.pack(side=tk.BOTTOM, fill=tk.X)

        self.english_entry = tk.Text(english_tab, bg="white", fg="black")
        self.english_entry.pack(side=tk.TOP, expand=1)

        self.notebook.add(english_tab, text="Inglês")

        self.notebook.pack(fill=tk.BOTH, expand=1)

    # Função de tradução
    def translate(self, text=None):
        if len(self.language_tabs) < 1:
            msg.showerror("Sem Lingua", "Sem linguas selecionadas. Adicione uma do menu!!")
            return

        if not text:
            text = self.english_entry.get(1.0, tk.END).strip()

        url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl={}&tl={}&dt=t&q={}"

        try:
            # para cada tab de linguas faço uma requisição ao site e volta um r (response) com um json que pego a palavra
            # e seto para dentro da variavel traduzida para apresentar no frame
            for language in self.language_tabs:
                full_url = url.format("en", language.lang_code, text)
                r = requests.get(full_url)
                r.raise_for_status()
                translation = r.json()[0][0][0]
                language.translation_var.set(translation)
        except Exception as e:
            msg.showerror("Tradução falhou!!", str(e))
        else:
            msg.showinfo("Traduzido com sucesso", "O texto foi traduzido com sucesso")

    # Método que adiciona uma nova aba
    def add_new_tab(self, tab):
        self.language_tabs.append(tab)
        self.notebook.add(tab, text=tab.lang_name)

        try:
            self.languages_menu.entryconfig(tab.lang_name, state="disabled")
        except:
            pass

    def show_new_language_popup(self):
        # Cria aqui uma classe para adicionar uma nova lingua
        return ""


if _name_ == "_main_":
    # Crio a janela principal
    translatebook = TranslateBook()
    # Crio a aba de italiano
    italian_tab = LanguageTab(translatebook, "Italiano", "it")
    # Crio a aba de frances
    # Descomente para ver
    #french_tab = LanguageTab(translatebook, "Frances", "fr")

    # Adiciona a aba na janela principal já de inicio
    translatebook.add_new_tab(italian_tab)
    # Descomente essa também
    # translatebook.add_new_tab(french_tab)

    # Inicial a janela principal
    translatebook.mainloop()