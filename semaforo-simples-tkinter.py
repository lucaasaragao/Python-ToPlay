import tkinter as tk
import time

class SemaforoApp:
    def __init__(self, master):
        self.master = master
        master.title("Semáforo")

        self.canvas = tk.Canvas(master, width=200, height=400, bg='gray')
        self.canvas.pack()

        # Criando os círculos (luzes do semáforo)
        self.vermelho = self.canvas.create_oval(50, 50, 150, 150, fill="gray")
        self.amarelo = self.canvas.create_oval(50, 160, 150, 260, fill="gray")
        self.verde = self.canvas.create_oval(50, 270, 150, 370, fill="gray")

        # Botão de controle
        self.botao = tk.Button(master, text="Iniciar", command=self.toggle)
        self.botao.pack(pady=10)

        self.ativo = False

    def toggle(self):
        if not self.ativo:
            self.ativo = True
            self.botao.config(text="Parar")
            self.ciclo()
        else:
            self.ativo = False
            self.botao.config(text="Iniciar")

    def ciclo(self):
        if not self.ativo:
            self.apagarLuzes()
            return

        self.acenderLuz("vermelho")
        self.master.after(5000, lambda: self.acenderLuz("verde"))
        self.master.after(10000, lambda: self.acenderLuz("amarelo"))
        self.master.after(13000, self.ciclo)

    def acenderLuz(self, cor):
        self.apagarLuzes()
        if cor == "vermelho":
            self.canvas.itemconfig(self.vermelho, fill="red")
        elif cor == "amarelo":
            self.canvas.itemconfig(self.amarelo, fill="yellow")
        elif cor == "verde":
            self.canvas.itemconfig(self.verde, fill="green")

    def apagarLuzes(self):
        self.canvas.itemconfig(self.vermelho, fill="gray")
        self.canvas.itemconfig(self.amarelo, fill="gray")
        self.canvas.itemconfig(self.verde, fill="gray")

# Executa a aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = SemaforoApp(root)
    root.mainloop()
