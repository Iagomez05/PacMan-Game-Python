import tkinter as tk
from tkinter import *
from threading import Thread
import random
import time
from PIL import ImageTk, Image
from tkinter import Toplevel
import pygame
import sys
import natsort
from tkinter import font, PhotoImage
from natsort import natsorted
import tkinter as tk
from tkinter import messagebox
import math

#Variabes globales
window = None

#Constantes
filas = 40
columnas = 36
ventana_ancho = 540
ventana_alto = 600

#Definir colores
blanco = (255, 255, 255)
negro = (0, 0, 0)
azul = (0, 0, 102)
amarillo = (255, 255, 0)
naranja = "#FF4500"
rojo = (255, 0, 0)
tamano_casilla = ventana_ancho // columnas

Partida = None

pared = 0
alimento = 1
capsula = 2
alimentoComida = 3
vacio = 4


class Juego:
    def __init__(self, tablero,  nivel, score, x, y ):
        self.tablero = tablero
        self.nivel = nivel
        self.score = score
        self.x = x
        self.y = y
        
    def iniciarJuego(self):
        self.score = 0
        #instancia un jugador

class PacMan:
    def __init__(self,velocidad):
        self,velocidad = velocidad

class Fantasma:
    def __init__(self, color):
        self.estado = True  
        self.posicion_x = 0 
        self.posicion_y = 0  
        self.color = color 


#Inicializa Pygame y carga la música en la función play()
pygame.mixer.init()
def play():
    pygame.mixer.music.load("musica.mp3")
    pygame.mixer.music.play(loops=0)

def stop_music():
    pygame.mixer.music.stop()

#Abre la ventana principal
def ventana_inicio():
    global window
    ventana1 = tk.Tk()
    ventana1.title("Diviértete")
    ventana1.minsize(height=480, width=800)
    ventana1.configure(background="black") #Color del tk
    
    #Fondo ventana_principal
    fondo = tk.PhotoImage(file="Fondo PAC-MAN.png")
    fondo_label = tk.Label(ventana1, image=fondo)
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)
    ventana1.resizable(height=False, width=False)
    
    #Titulo Ventana Principal
    tituloPrincipal = tk.Label(ventana1, text="ROBOTS", font=("Courier New", 12, "bold"), background="grey", fg="white")
    tituloPrincipal.place(x=1400, y=25)
    
    #Ventana JUEGO
    def Ventana_juego():
        global ventana_alto
        global ventana_ancho
        pygame.init()
        ventana = pygame.display.set_mode((ventana_ancho, ventana_alto))
        pygame.display.set_caption("PacMan")
        
        #Funcion para dibujar tablero de juego
        global Partida
        tableroJuego = [[2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                        [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                        [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                        [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [2, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1],
                        [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                        [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                        [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],

                            ]
        
        Partida = Juego(tableroJuego,1,0, 0, 0)
            
        #Funcion para dibujar tablero de juego
        def dibujar_tablero():
            for fila in range(filas):
                for columna in range(columnas):
                    if Partida.tablero[fila][columna]==0:
                        pygame.draw.rect(ventana, azul, (columna * tamano_casilla, fila * tamano_casilla, tamano_casilla, tamano_casilla))
                    elif Partida.tablero[fila][columna]==1:
                        x = columna * tamano_casilla + tamano_casilla // 2
                        y = fila * tamano_casilla + tamano_casilla // 2
                        radio = tamano_casilla // 4
                        pygame.draw.circle(ventana, amarillo, (x, y), radio)
                    elif Partida.tablero[fila][columna]==2:
                        x = columna * tamano_casilla + tamano_casilla // 2
                        y = fila * tamano_casilla + tamano_casilla // 2
                        radio = tamano_casilla // 2
                        pygame.draw.circle(ventana, blanco, (x, y), radio)
                    elif Partida.tablero[fila][columna]==3:
                        x = columna * tamano_casilla + tamano_casilla // 2
                        y = fila * tamano_casilla + tamano_casilla // 2
                        radio = tamano_casilla // 3
                        pygame.draw.circle(ventana, naranja, (x, y), radio)
                    elif Partida.tablero[fila][columna]==4:
                        pygame.draw.rect(ventana, negro, (columna * tamano_casilla, fila * tamano_casilla, tamano_casilla, tamano_casilla))
                    
                    # Dibujar el objeto Pac-Man
                    x = Partida.x * tamano_casilla + tamano_casilla // 2
                    y = Partida.y * tamano_casilla + tamano_casilla // 2
                    radio = tamano_casilla // 4
                    pygame.draw.circle(ventana, rojo, (x, y), radio)

                    
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                #Control de movimiento de Pac-Man
                keys = pygame.key.get_pressed()
                if keys[pygame.K_UP]:
                    next_y = Partida.y - 1
                    if Partida.tablero[next_y][Partida.x] in (1, 2, 3):
                        Partida.y = next_y
                if keys[pygame.K_DOWN]:
                    next_y = Partida.y + 1
                    if Partida.tablero[next_y][Partida.x] in (1, 2, 3):
                        Partida.y = next_y
                if keys[pygame.K_LEFT]:
                    next_x = Partida.x - 1
                    if Partida.tablero[Partida.y][next_x] in (1, 2, 3):
                        Partida.x = next_x
                if keys[pygame.K_RIGHT]:
                    next_x = Partida.x + 1
                    if Partida.tablero[Partida.y][next_x] in (1, 2, 3):
                        Partida.x = next_x

            dibujar_tablero()
            pygame.display.update()
    
    
    #Ventana de mejores puntajes
    def abrirventana3():
        ventana1.withdraw()
        ventana3 = Toplevel()
        ventana3.title("Mejores Puntajes")
        ventana3.geometry("800x480")
        ventana3.configure(background="black")
        canvasC3 = tk.Canvas(ventana3, width=800, height=680, borderwidth=0, highlightthickness=0, background="black")
        canvasC3.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        titulo= tk.Label(canvasC3, text="Mejores Puntuaciones", font=("Times New Roman", 17), background="black", fg="white")
        titulo.place(x=290, y=120)
        ventana3.resizable(height=False, width=False)
        
        texto= tk.Label(canvasC3, text="Jeff: 1500pts "
                                        "\nJose: 1000pts" 
                                        "\nIan: 950pts"

                                        
                                ,font=("Courier New", 17, "bold"), fg=("white"), bg=("black"), justify=tk.LEFT)
        texto.place(x=50, y=180)
    
        #Botón back de Mejores Puntajes        
        def back():
            ventana3.destroy()
            ventana1.deiconify()
        botonBack = tk.Button(ventana3, text="Back", command= back,  font=("Courier New", 12, "bold"), fg=("white"), bg=("black"), width=8)
        botonBack.pack()
        botonBack.place(x=650, y=420)
        
    
    #Fución abrir ventana de Configuración
    def abrirventana4():
        ventana1.withdraw()
        ventana4 = Toplevel()
        ventana4.title("Ventana 4")
        ventana4.geometry("800x480")
        ventana4.configure(background="black")
        canvasC4 = tk.Canvas(ventana4, width=800, height=680, borderwidth=0, highlightthickness=0, background="black")
        canvasC4.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        titulo= tk.Label(canvasC4, text="Sonido", font=("Courier New", 16, "bold"), background="black", fg="white")
        titulo.place(x=330 ,y=170)
        ventana4.resizable(height=False, width=False)

        # Botón de play
        botonP = Button(ventana4, text="Play", font=("Courier New", 12, "bold"), command=play, fg=("white"), bg=("black"), width=8)
        botonP.pack()
        botonP.place(x=500, y=300)
        
        # Botón de stop music
        botonBack = tk.Button(ventana4, text="Stop Music", font=("Courier New", 12, "bold"), command=stop_music, fg=("white"), bg=("black"), width=12)
        botonBack.pack()
        botonBack.place(x=600, y=300)

        #Botón de back Ventana Configuración
        def back():
            ventana4.destroy()
            ventana1.deiconify()
  
        botonBack = tk.Button(ventana4, text="Back", command= back, font=("Courier New", 12, "bold"), fg=("white"), bg=("black"), width=8)
        botonBack.pack()
        botonBack.place(x=650, y=420)

        abrirventana4.mainloop()


    #Fución abrir ventana de Ayuda
    def abrirventana5():
        ventana1.withdraw()
        ventana5 = Toplevel()
        ventana5.title("Ventana 3")
        ventana5.geometry("800x480")
        ventana5.configure(background="white")
        canvasC4 = tk.Canvas(ventana5, width=800, height=680, borderwidth=0, highlightthickness=0, background="black")
        canvasC4.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    
        titulo= tk.Label(canvasC4, text="Controles", font=("Courier New", 15, "bold"), fg=("white"), bg=("black"))
        titulo.place(x=310, y=120)
        ventana5.resizable(height=False, width=False)

        texto= tk.Label(canvasC4, text="Mover hacia arriba: W "
                                        "\nMover hacia abajo: X" 
                                        "\nMover hacia la derecha: D"
                                        "\nMover hacia la izquierda: A"
                                        
                                ,font=("Courier New", 12, "bold"), fg=("white"), bg=("black"), justify=tk.LEFT)
        texto.place(x=50, y=180)

        image= Image.open("Teclado.png")
        image = image.resize((500,150))
        img = ImageTk.PhotoImage(image)
        yo_img = Label(canvasC4, image=img)
        yo_img.pack()
        yo_img.place(x=110, y=405)

        #Botón de back Ventana Ayuda
        #The above code creates a button in a tkinter window that, when clicked, closes the current
        #window and opens another window.
        
        def back():
            ventana5.destroy()
            ventana1.deiconify()

        botonBack = tk.Button(ventana5, text="Back", command= back, fg=("white"), font=("Courier New", 12, "bold"), bg=("black"), width=8)
        botonBack.pack()
        botonBack.place(x=650, y=420)

        abrirventana5.mainloop()
        
    #Fución abrir ventana "Acerca de"
    #The function "abrirventana6" opens a new window called "Acerca de" with personal information and
    #a back button.
    def abrirventana6():
        ventana1.withdraw()
        ventana6 = Toplevel()
        ventana6.title("Ventana 3")
        ventana6.geometry("800x480")
        ventana6.configure(background="black")
        canvasC4 = tk.Canvas(ventana6, width=800, height=680, borderwidth=0, highlightthickness=0, background="black")
        canvasC4.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        titulo= tk.Label(canvasC4, text="Informacion Personal", fg=("white"), font=("Courier New", 12, "bold"), bg=("black"))
        titulo.place(x=308, y=110)
        ventana6.resizable(height=False, width=False)
    
    #Botón de back Ventana "Acerca de"
        def back():
            ventana6.destroy()
            ventana1.deiconify()
            
        botonBack = tk.Button(ventana6, text="Back", font=("Courier New", 12, "bold"), command= back, fg=("white"), bg=("black"), width=8 )
        botonBack.pack()
        botonBack.place(x=650, y=420)
        
        abrirventana6.mainloop()

    
    
    #Botones Principales VENTANA 1
    boton1 = tk.Button(ventana1, text="Jugar", command=Ventana_juego,font=("Courier New", 16, "bold"), fg=("white"), bg=("black"))
    boton1.place(x=240, y=60)
    boton2 = tk.Button(ventana1, text="Configuración",command=abrirventana4, font=("Courier New", 16, "bold"), fg=("white"), bg=("black"))
    boton2.place(x=185, y=217)
    boton3 = tk.Button(ventana1, text="Ayuda", command=abrirventana5, font=("Courier New", 14, "bold"), fg=("white"), bg=("black"))
    boton3.place(x=75, y=420)
    boton4 = tk.Button(ventana1, text="Mejores Puntajes",command=abrirventana3, font=("Courier New", 16, "bold"), fg=("white"), bg=("black"))
    boton4.place(x=170, y=140)
    boton5 = tk.Button(ventana1, text="Acerca de", command=abrirventana6, font=("Courier New", 14, "bold"), fg=("white"), bg=("black"))
    boton5.place(x=350, y=420)
    
    ventana1.mainloop() 
ventana_inicio()





