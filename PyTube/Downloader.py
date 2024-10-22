import customtkinter as ctk
import tkinter
from tkinter import *
from pytube import YouTube


def down():
    try:
        ytlink = link.get()
        ytobject = YouTube(ytlink, on_progress_callback=save)
        video = ytobject.streams.get_highest_resolution()
        video.download()
        
        nome_video.configure(text=ytobject.title)
        textofinal.configure(text="Download Completo", font=('Arial',24,'bold'))
    except:
        textofinal.configure(text="Erro no Download ou Link Invalido", font=('Arial',24,'bold'))
        
def save(stream,x,bytes_restantes):
    tamanho_total= stream.filesize
    bytes_baixados = tamanho_total-bytes_restantes
    porcentagem_completa = (bytes_baixados/tamanho_total)*100
    por = str(int(porcentagem_completa))
    progresso.configure(text=f"{por}%")
    progresso.update()
    
    barradeprogresso.set(porcentagem_completa/100)
    barradeprogresso.update()

ctk.set_appearance_mode('dark')

janela = ctk.CTk()
janela.geometry('800x400')
janela.title('Youtube Downloader V1.0')

ctk.CTkLabel(janela, text='Youtube Downloader V1.0',
             font=('Arial',30,'bold'),
             text_color='green').pack(pady=10)

link = ctk.CTkEntry(janela, width=650,
                    height=50,placeholder_text='Cole aqui a URL do Vídeo')
link.pack(pady=10)

nome_video = ctk.CTkLabel(janela, text='',
                          font=('Arial',20,'bold'),
                          text_color='green')
nome_video.pack(pady=5)

textofinal = ctk.CTkLabel(janela, text='',
                          font=('Arial',16,'bold'),
                          text_color='white')
textofinal.pack(pady=5)

progresso = ctk.CTkLabel(janela, text='0%',
                          font=('Arial',18,'bold'),
                          text_color='white')
progresso.pack(pady=5)

barradeprogresso = ctk.CTkProgressBar(janela, width=650,
                                      height=25,
                                      progress_color='green')
barradeprogresso.set(0)
barradeprogresso.pack(pady=10)

btn = ctk.CTkButton(janela, text='Download',
                    font=('arial',20,'bold'),
                    fg_color='green',
                    hover_color='darkgreen',command=down)
btn.pack(pady=10)

janela.mainloop()