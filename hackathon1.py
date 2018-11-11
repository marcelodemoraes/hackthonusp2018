from tkinter import *
#importando módulo do SQlite
import sqlite3


class Application:
  #declaracao dos espacos de input
    def __init__(self, master=None):

        """self.window=Tk()
        self.configure(background="#a1dbcd")
        self.title("Bandeco")"""

        self.fontePadrao = ("Waree", 25, "bold italic")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 30
        self.primeiroContainer.pack()
        
        self.diaInput = Frame(master)
        self.diaInput["padx"] = 20
        self.diaInput.pack()
        
        self.refeicaoInput = Frame(master)
        self.refeicaoInput["padx"] = 20
        self.refeicaoInput.pack()
         
        self.pratoInput = Frame(master)
        self.pratoInput["padx"] = 20
        self.pratoInput.pack()
  
        self.guarniInput = Frame(master)
        self.guarniInput["padx"] = 20
        self.guarniInput.pack()

        self.sobreInput = Frame(master)
        self.sobreInput["padx"] = 20
        self.sobreInput.pack()
    
        self.frutaInput = Frame(master)
        self.frutaInput["padx"] = 20
        self.frutaInput.pack()
        
        self.kcalInput = Frame(master)
        self.kcalInput["padx"] = 20
        self.kcalInput.pack()
        
        self.rodaProg = Frame(master)
        self.rodaProg["pady"] = 20
        self.rodaProg.pack()
  
  # dados de input
  
        self.titulo = Label(self.primeiroContainer, text="Insira o cardápio")
        self.titulo["font"] = ("Mingzat", 50, "bold underline italic")
        self.titulo.pack()
  
        self.diaLabel = Label(self.diaInput,text="Dia da Semana",  fg="#ff3300", bg="#a1dbcd", font=self.fontePadrao)
        self.diaLabel.pack(side=LEFT)
  
        self.dia = Entry(self.diaInput)
        self.dia["width"] = 30
        self.dia["font"] = self.fontePadrao
        self.dia.pack(side=LEFT)
        
        self.refeicaoLabel = Label(self.refeicaoInput,text="Refeição         ",  fg="#ff3300", bg="#a1dbcd", font=self.fontePadrao)
        self.refeicaoLabel.pack(side=LEFT)
  
        self.refeicao = Entry(self.refeicaoInput)
        self.refeicao["width"] = 30
        self.refeicao["font"] = self.fontePadrao
        self.refeicao.pack(side=LEFT)
        
        self.pratoLabel = Label(self.pratoInput,text="Prato principal ",  fg="#ff3300", bg="#a1dbcd", font=self.fontePadrao)
        self.pratoLabel.pack(side=LEFT)
  
        self.prato = Entry(self.pratoInput)
        self.prato["width"] = 30
        self.prato["font"] = self.fontePadrao
        self.prato.pack(side=LEFT)
  
  
        self.guarniLabel = Label(self.guarniInput, text="Guarnição       ",  fg="#ff3300", bg="#a1dbcd", font=self.fontePadrao)
        self.guarniLabel.pack(side=LEFT)
  
        self.guarni = Entry(self.guarniInput)
        self.guarni["width"] = 30
        self.guarni["font"] = self.fontePadrao
        #self.guarni["show"] = "*"
        self.guarni.pack(side=LEFT)
  
        self.sobremesaLabel = Label(self.sobreInput, text="Sobremesa     ",  fg="#ff3300", bg="#a1dbcd", font=self.fontePadrao)
        self.sobremesaLabel.pack(side=LEFT)
  
        self.sobremesa = Entry(self.sobreInput)
        self.sobremesa["width"] = 30
        self.sobremesa["font"] = self.fontePadrao
        #self.sobremesa["show"] = "*"
        self.sobremesa.pack(side=LEFT)
  
        self.frutaLabel = Label(self.frutaInput, text="Fruta              " , fg="#ff3300", bg="#a1dbcd", font=self.fontePadrao)
        self.frutaLabel.pack(side=LEFT)
  
        self.fruta = Entry(self.frutaInput)
        self.fruta["width"] = 30
        self.fruta["font"] = self.fontePadrao
        #self.sobremesa["show"] = "*"
        self.fruta.pack(side=LEFT)
        
        self.kcalLabel = Label(self.kcalInput, text="Kcal               ",  fg="#ff3300", bg="#a1dbcd", font=self.fontePadrao)
        self.kcalLabel.pack(side=LEFT)
  
        self.kcal = Entry(self.kcalInput)
        self.kcal["width"] = 30
        self.kcal["font"] = self.fontePadrao
        #self.sobremesa["show"] = "*"
        self.kcal.pack(side=LEFT)
        
        self.autenticar = Button(self.rodaProg)
        self.autenticar["text"] = "Autenticar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar.pack()

        """cor botao"""
        self.autenticar.configure(background="#a1dbcd")
        self.autenticar["command"] = self.verificaCardapio
        		
        self.mensagem = Label(self.rodaProg, text="", font=self.fontePadrao)
        self.mensagem.pack()


  
    #Método rodar programa
    def verificaCardapio(self):
        prato = self.prato.get()
        guarni = self.guarni.get()
        sobremesa = self.sobremesa.get()
        fruta = self.fruta.get()
        
        #chama no prog nos mino
        num = 3
        if num == 1:
            self.mensagem["text"] = "Disperdicio estimado por pessoa entre 0 e 30g (baixo)"
        if num == 2:
            self.mensagem["text"] = "Disperdicio estimado por pessoa entre 31 e 60g (mediano)"
        if num == 3:
            self.mensagem["text"] = "Disperdicio estimado por pessoa acima de 60g (alto)"
        else:
            self.mensagem["text"] = "Cardapio nao encontrado"
       
  
root = Tk()
root.configure(background="#a1dbcd")
root.title("Bandeco")
Application(root)
root.mainloop()
