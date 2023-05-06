from tkinter import Entry, Button, Tk, Label, messagebox

import os
import time
from datetime import datetime, time as t


def Desligar():
    # Defina a hora em que deseja desligar o computador
    hora_desligar = entrada.get()
    #hora_desligar = input("Digite a hora em que deseja desligar o computador (hh:mm:ss): ")

    # Converte a hora para um objeto datetime
    hora_desligar = datetime.strptime(hora_desligar, "%H:%M:%S").time()

    # Obtém a hora atual como um objeto time
    hora_atual = datetime.now().time()

    # Calcula o tempo restante até a hora de desligar em segundos
    tempo_restante = (datetime.combine(datetime.today(), hora_desligar) - datetime.combine(datetime.today(), hora_atual)).total_seconds()

    # Espera até a hora definida para desligar o computador
    time.sleep(tempo_restante)
 
    # Desliga o computador
    if os.name == "nt":
        os.system("shutdown /s /t 1")
    elif os.name == "posix":
        os.system("sudo shutdown -h now")
    else:
        print("Sistema operacional não suportado.")

# cria a janela
janela = Tk()
# titulo da janela 
janela.title("Como desligar o pc")
# texto da janela 
texto_explicacao = Label(janela, text="Qual a hora que prefere desligar o pc? ")
# Escolhendo a posição do texto na janela 
# (dica: coluna, linha, enquanto o padx e pady servem pra dar espaço dentro na janela)
texto_explicacao.grid(column=0, row=0, padx=5, pady=10)

texto_explicacao2 = Label(janela, text="(hh:mm:ss): ")
texto_explicacao2.grid(column=0, row=1, padx=2, pady=10)

# Entrada de informacoes (dica: troque o input() pelo .get())
entrada = Entry(width=20)
entrada.grid(column=1, row=1, columnspan=1, padx=10, pady=10)
entrada.focus()

# columnspan, não sei pra que serve

# criando o botao 
# (dica: transformer o codigo em funcao e jogue como parametro dentro do command para funcionar, sem o def)
botao = Button(janela, text= "aperte aqui", command= Desligar)
botao.grid(column=0, row=2, columnspan=2, padx=5, pady=10)

# mantem a janela ligada (mantenha no fim do codigo sempre)
janela.mainloop() 


# Esses são só os comando basicos do tkinter, boa sorte em procurar

