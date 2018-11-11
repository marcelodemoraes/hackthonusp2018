from tkinter import *
#importando módulo do SQlite
import sqlite3
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

model = train() 

    def train():
        #Abrindo arquivo csv
        data = pd.read_csv('bandeco.csv', header=0)
        data = data.dropna()
        cat_vars=['Periodo','DiaSemana','PratoPrincipal','Vegetariano','Guarnicao','Sobremesa','Fruta',]

        index = []

        for var in cat_vars:
            cat_list='var'+'_'+var
            for word in data[var]:
                if word not in index:
                    index.append(word)
            index.append('|')
            cat_list = pd.get_dummies(data[var], prefix=var)
            data1=data.join(cat_list)
            data=data1
        cat_vars=['Periodo','DiaSemana','PratoPrincipal','Vegetariano','Guarnicao','Sobremesa','Fruta',]
        data_vars=data.columns.values.tolist()
        to_keep=[i for i in data_vars if i not in cat_vars]
        data_final=data[to_keep]
        data_final.columns.values

        X = data_final.loc[:, data_final.columns != 'desperdicio']
        y = data_final.loc[:, data_final.columns == 'desperdicio']


        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
        logreg = LogisticRegression(multi_class= 'multinomial', solver= 'lbfgs')
        logreg.fit(X_train, y_train)
        return logreg

    def prediction(model, ent):
        ent_final = []
        i = 0
        for word in index:
            if word == '|':
                i += 1
            else:
                ent_final.append(int(ent[i] == word))
        ent_final = np.array(ent_final)
        ent_final = ent_final.reshape(1,243)
        y_pred = logreg.predict(ent_final);
        return y_pred[0]



    class Application:
      #declaracao dos espacos de input
        def __init__(self, master=None):


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

            self.vegetInput = Frame(master)
            self.vegetInput["padx"] = 20
            self.vegetInput.pack()

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
      
            self.titulo = Label(self.primeiroContainer, text="Insira o cardápio")#, highlightthickness=0, bg="#a1dbcd")
            self.titulo["font"] = ("Mingzat", 50, "bold underline italic")
            self.titulo.pack()
            
      
            self.diaLabel = Label(self.diaInput,text="Dia da Semana	", font=self.fontePadrao) #fg="#ff3300", bg="#a1dbcd",
            self.diaLabel.pack(side=LEFT)
            
      
            self.dia = Entry(self.diaInput)
            self.dia["width"] = 30
            self.dia["font"] = self.fontePadrao
            self.dia.pack(side=LEFT)
            
            self.refeicaoLabel = Label(self.refeicaoInput,text="Refeição		",  font=self.fontePadrao) #fg="#ff3300", bg="#a1dbcd"
            self.refeicaoLabel.pack(side=LEFT)
      
            self.refeicao = Entry(self.refeicaoInput)
            self.refeicao["width"] = 30
            self.refeicao["font"] = self.fontePadrao
            self.refeicao.pack(side=LEFT)
            
            self.pratoLabel = Label(self.pratoInput,text="Prato principal	", font=self.fontePadrao)#  fg="#ff3300", bg="#a1dbcd",
            self.pratoLabel.pack(side=LEFT)
      
            self.prato = Entry(self.pratoInput)
            self.prato["width"] = 30
            self.prato["font"] = self.fontePadrao
            self.prato.pack(side=LEFT)
      
      
            self.guarniLabel = Label(self.guarniInput, text="Guarnição	", font=self.fontePadrao) #fg="#ff3300", bg="#a1dbcd",
            self.guarniLabel.pack(side=LEFT)
      
            self.guarni = Entry(self.guarniInput)
            self.guarni["width"] = 30
            self.guarni["font"] = self.fontePadrao
            #self.guarni["show"] = "*"
            self.guarni.pack(side=LEFT)
      
            self.sobremesaLabel = Label(self.sobreInput, text="Sobremesa	", font=self.fontePadrao) #fg="#ff3300", bg="#a1dbcd",
            self.sobremesaLabel.pack(side=LEFT)
      
            self.sobremesa = Entry(self.sobreInput)
            self.sobremesa["width"] = 30
            self.sobremesa["font"] = self.fontePadrao
            #self.sobremesa["show"] = "*"
            self.sobremesa.pack(side=LEFT)


            self.vegetLabel = Label(self.vegetInput, text="Vegetariano	", font=self.fontePadrao) #fg="#ff3300", bg="#a1dbcd",
            self.vegetLabel.pack(side=LEFT)
      
            self.veget = Entry(self.sobreInput)
            self.veget["width"] = 30
            self.veget["font"] = self.fontePadrao
            #self.sobremesa["show"] = "*"
            self.veget.pack(side=LEFT)
      
            self.frutaLabel = Label(self.frutaInput, text="Fruta		" , font=self.fontePadrao) #fg="#ff3300", bg="#a1dbcd", 
            self.frutaLabel.pack(side=LEFT)
      
            self.fruta = Entry(self.frutaInput)
            self.fruta["width"] = 30
            self.fruta["font"] = self.fontePadrao
            #self.sobremesa["show"] = "*"
            self.fruta.pack(side=LEFT)
            
            self.autenticar = Button(self.rodaProg)
            self.autenticar["text"] = "Calcular"
            self.autenticar["font"] = ("Calibri", "30", "bold")
            self.autenticar["width"] = 30
            self.autenticar.pack()

            """cor botao"""
            #self.autenticar.configure(highlightbackground="#a1dbcd")
            
            self.autenticar["command"] = self.verificaCardapio
                            
            self.mensagem = Label(self.rodaProg, text="", font=self.fontePadrao)
            self.mensagem.pack()


      
        #Método rodar programa
        def verificaCardapio(self):
            refeicao = self.refeicao.get()
            dia = self.dia.get()
            prato = self.prato.get()
            veget = self.veget.get()
            guarni = self.guarni.get()
            sobremesa = self.sobremesa.get()
            fruta = self.fruta.get()
            ent = [refeicao, dia, prato, veget, guarni, sobremesa, fruta]

            #chama no prog nos mino
            num = prediction(model , ent)
        if num == 1:
            self.mensagem["text"] = "Disperdicio estimado por pessoa entre 0 e 30g (baixo)"
        if num == 2:
            self.mensagem["text"] = "Disperdicio estimado por pessoa entre 31 e 60g (mediano)"
        if num == 3:
            self.mensagem["text"] = "Disperdicio estimado por pessoa acima de 60g (alto)"
        else:
            self.mensagem["text"] = "Cardapio nao encontrado"
       
  
root = Tk()

root.title("Bandeco")
Application(root, model)
root.mainloop()
