# The above code is importing various modules and libraries in Python, such as threading, tkinter,
# keyboard, PIL, pygame, and natsort. It is also defining some functions and creating a GUI using
# tkinter. The code seems to be related to creating a game or an interactive application.
import threading
import tkinter as tk
from tkinter import *
from threading import Thread
import random
import time
import tkinter
import keyboard
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
ventana_alto = 700

#Definir colores
blanco = (255, 255, 255)
negro = (0, 0, 0)
azul = (0, 0, 102)
amarillo = (255, 255, 0)
naranja = "#FF4500"
rosado = "#FF4501"
rojo = (255, 0, 0)
celeste = (255, 19, 0)
tamano_casilla = ventana_ancho // columnas

# The above code is defining several variables and assigning them values. It also initializes an empty
# list called "ListaFantasmas". The purpose of the code is not clear without additional context.
Partida = None
entryNombre= "" 
nombreJugadorActual = ""
pared = 0
alimento = 1
capsula = 2
alimentoComida = 3
vacio = 4

contador = 0

MoverFantasmas= True

ListaFantasmas = []


# Inicializar el score
score = 0

# Función para mostrar el score en la pantalla


running = True

button_width = 100
button_height = 40
button_x = ventana_ancho - button_width - 10  # Alineado a la derecha
button_y = ventana_alto - button_height - 10
button_ins_y = ventana_alto - button_height - 55

# The code defines three classes: Juego, PacMan, and Fantasma, which represent a game, a player
# character, and enemy characters respectively.
class Juego:
    def __init__(self, tablero, nivel, score, Jugador, Fantasmas):
        self.tablero = tablero
        self.nivel = nivel
        self.score = score
        self.Jugador = Jugador
        self.Fantasmas = Fantasmas
        
    def iniciarJuego(self):
        self.score = 0

# The PacMan class represents a PacMan character with attributes for speed, position, and whether it
# has a capsule.
class PacMan:
    def __init__(self,velocidad,posicion_x,posicion_y):
        self.velocidad = velocidad
        self.x = 0 
        self.y = 0
        self.capsula = False

# The class "Fantasma" represents a ghost with attributes such as color, position, and state.
class Fantasma:
    def __init__(self, color):
        self.estado = True  
        self.posicion_x = 18 
        self.posicion_y = 18
        self.anterior = 4 
        self.color = color 
        self.capsula = capsula

    def moverIzquierda(self,tablero,xJugador, yJugador, EstadoCapsula):
        """
        The above code defines four functions that move an object on a game board in different
        directions, checking for collisions with other objects.
        
        :param tablero: The parameter "tablero" represents the game board or grid on which the movement
        of the player and ghosts is taking place. It is a two-dimensional array that stores the state of
        each cell on the board. The values in the array represent different elements such as walls,
        pellets, capsules, and empty
        :param xJugador: The x-coordinate of the player's position on the game board
        :param yJugador: The parameter "yJugador" represents the current y-coordinate of the player's
        position on the game board
        :param EstadoCapsula: EstadoCapsula is a boolean variable that represents the state of a
        power-up capsule. If EstadoCapsula is True, it means that the power-up capsule is active, and if
        it is False, it means that the power-up capsule is not active
        """
        global MoverFantasmas
        next_x = self.posicion_x - 1
        if tablero[self.posicion_y][next_x] in (1, 2, 3, 4):
            self.posicion_x = next_x
            if((next_x == xJugador or self.posicion_x == xJugador) and self.posicion_y == yJugador  and EstadoCapsula == False ):
                MoverFantasmas =False
            elif((next_x == xJugador or self.posicion_x == xJugador) and self.posicion_y == yJugador  and EstadoCapsula == True ):    
                self.estado=False
                ListaFantasmas.append(Fantasma(rojo))

    def moverDerecha(self,tablero,xJugador, yJugador, EstadoCapsula):
        """
        The function `moverDerecha` moves a character to the right on a game board and checks for certain
        conditions.
        
        :param tablero: The "tablero" parameter represents the game board or grid on which the movement of
        the player and ghosts is taking place. It is a two-dimensional list or array where each element
        represents a cell on the board. The values in the cells can be integers representing different
        types of objects or obstacles in the
        :param xJugador: The x-coordinate of the player's position on the board
        :param yJugador: The variable "yJugador" represents the y-coordinate of the player's position on
        the game board
        :param EstadoCapsula: EstadoCapsula is a boolean variable that represents the state of a capsule.
        If EstadoCapsula is True, it means that the capsule is active. If it is False, it means that the
        capsule is not active
        """
        global MoverFantasmas
        next_x = self.posicion_x + 1
        if tablero[self.posicion_y][next_x] in (1, 2, 3, 4):
            self.posicion_x = next_x
            if((next_x == xJugador or self.posicion_x == xJugador) and self.posicion_y == yJugador  and EstadoCapsula == False ):
                MoverFantasmas=False
            elif((next_x == xJugador or self.posicion_x == xJugador) and self.posicion_y == yJugador  and EstadoCapsula == True ):
                self.estado=False
                ListaFantasmas.append(Fantasma(rojo))

    def moverArriba(self,tablero,xJugador, yJugador, EstadoCapsula):
        """
        The function "moverArriba" moves the player character up on the game board and checks for collisions
        with other objects.
        
        :param tablero: The variable "tablero" represents the game board or grid on which the movement of
        the player and ghosts is taking place. It is a two-dimensional array that stores the state of each
        cell on the board
        :param xJugador: The x-coordinate of the player's position on the game board
        :param yJugador: The parameter "yJugador" represents the current y-coordinate of the player's
        position on the game board
        :param EstadoCapsula: EstadoCapsula is a boolean variable that represents the state of a capsule. It
        is used in the condition `EstadoCapsula == False` and `EstadoCapsula == True` to check if the
        capsule is active or not
        """
        global MoverFantasmas
        next_y = self.posicion_y - 1
        if tablero[next_y][self.posicion_x] in (1, 2, 3, 4):
            self.posicion_y = next_y
            if((next_y == xJugador or self.posicion_x == xJugador) and self.posicion_y == yJugador  and EstadoCapsula == False ):
                MoverFantasmas=False
            elif((next_y == xJugador or self.posicion_x == xJugador) and self.posicion_y == yJugador  and EstadoCapsula == True ):    
                self.estado=False
                ListaFantasmas.append(Fantasma(rojo))


    def moverAbajo(self,tablero,xJugador, yJugador, EstadoCapsula):
        """
        The function moves the player down on the game board and checks if the player collides with a
        ghost or a capsule.
        
        :param tablero: The "tablero" parameter represents the game board or grid on which the movement
        of the player and ghosts is taking place. It is a two-dimensional array that stores the state of
        each cell on the board
        :param xJugador: The variable "xJugador" represents the x-coordinate of the player's position on
        the game board
        :param yJugador: The parameter "yJugador" represents the current y-coordinate of the player's
        position on the game board
        :param EstadoCapsula: EstadoCapsula is a boolean variable that represents the state of a power-up
        capsule. It indicates whether the power-up capsule is active (True) or not (False)
        """
        global MoverFantasmas
        next_y = self.posicion_y + 1
        if tablero[next_y][self.posicion_x] in (1, 2, 3,4):
            self.posicion_y = next_y
            if((next_y == xJugador or self.posicion_x == xJugador) and self.posicion_y == yJugador and EstadoCapsula == False):
                MoverFantasmas=False
            elif((next_y == xJugador or self.posicion_x == xJugador) and self.posicion_y == yJugador and EstadoCapsula == True):
                self.estado=False
                ListaFantasmas.append(Fantasma(rojo))

#Inicializa Pygame y carga la música en la función play()
pygame.mixer.init()
def play():
    """
    The above code defines two functions in Python, one to play a song and one to stop the music.
    """
    pygame.mixer.music.load("pacman-song.mp3")
    pygame.mixer.music.play(loops=0)

def stop_music():
    pygame.mixer.music.stop()

def ventana_inicio():
    """
    The function `ventana_inicio` creates a window with the title "Diviértete" and a minimum size of
    480x800 pixels, with a black background.
    """
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
    tituloPrincipal = tk.Label(ventana1, text="PAC-MAN", font=("Courier New", 12, "bold"), background="grey", fg="white")
    tituloPrincipal.place(x=1400, y=25)
    def iniciar(vent):
        """
        The code defines a function that creates a window where the user can enter their name and choose
        a level to start a game.
        
        :param vent: The parameter "vent" is a reference to the window object that is being passed to
        the functions. It is used to close the window after the user enters a valid name and clicks the
        "Aceptar" button
        """
        global entryNombre
        if (str(entryNombre.get())!=""):
            entryNombre =str(entryNombre.get())
            vent.destroy()
            Ventana_juego(1)
        else:
            messagebox.showinfo("Advertencia", "Debe ingresar un nombre valido")

    def iniciar_nivel2(vent):
        """
        The function "iniciar_nivel2" checks if the entry field "entryNombre" is not empty, and if so,
        it assigns the value to a variable, closes the current window, and opens a new window called
        "Ventana_juego" with level 2. If the entry field is empty, it displays a warning message.
        
        :param vent: The parameter "vent" is a reference to a tkinter window object. It is used to close
        the current window (vent.destroy()) and open a new window (Ventana_juego(2))
        """
        global entryNombre
        if (str(entryNombre.get())!=""):
            entryNombre =str(entryNombre.get())
            vent.destroy()
            Ventana_juego(2)
        else:
            messagebox.showinfo("Advertencia", "Debe ingresar un nombre valido")
    
    def ventana_nombre():
        global entryNombre
        ventana1.withdraw()
        nombre = Toplevel()
        nombre.title("Nombre jugador") #nombre de la ventana
        nombre.geometry("400x300") # dimensiones de la ventana
        nombre.configure(background="black") #color del fondo 
        #canvas
        canvasC3 = tkinter.Canvas(nombre, width=300, height=200, borderwidth=0, highlightthickness=0, background="black")
        canvasC3.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        #titulo para identicar que tiene que hacer el jugador 
        titulo4= tkinter.Label(canvasC3, text="Ingrese su nombre:", font=("Courier New", 12), background="black", fg="yellow")
        titulo4.place(x=50, y=20)
        # barra donde se escribe el nombre
        entryNombre= tkinter.Entry(nombre, width=40)
        entryNombre.pack()
        entryNombre.place(x=70, y=150)
        #boton aceptar para ir a la pantalla de juego
        Aceptar_Boton= tkinter.Button(nombre, text= "Nivel 1", command=lambda:iniciar(nombre), fg=("yellow"), bg=("black"))
        Aceptar_Boton.pack(pady=10)
        Aceptar_Boton.place(x=100, y=200)

        Aceptar_Boton= tkinter.Button(nombre, text= "Nivel 2", command=lambda:iniciar_nivel2(nombre), fg=("yellow"), bg=("black"))
        Aceptar_Boton.pack(pady=10)
        Aceptar_Boton.place(x=230, y=200)
    
    def agarrar_nombre():
        """
        The function `agarrar_nombre()` writes the current score and player name to a text file.
        """
        global nombreJugadorActual
        global score
        global Partida
        nombre = nombreJugadorActual
        try:
            with open('data.txt', 'a') as file:  # agrega al txt los datos

                file.write(f'{Partida.score}-{nombre},')
                file.close()
        except:
            with open('data.txt', 'w') as file:  # crea el txt de no existir
                file.write(f'{Partida.score}: {nombre},')


    #Ventana modo inspector
    def abrirventana_inspector():
        """
        The function "abrirventana_inspector" creates a new window called "Ventana Inspector" and
        displays information about the game state, including the score, player name, and the positions
        and states of different ghosts.
        """
        # The above code is creating a new window called "Ventana Inspector" and setting its
        # dimensions and background color. It then creates two canvas widgets within the window, one
        # with a black background and one with a white background. It adds labels and text to display
        # information such as the player's score, player's name, and the matrix of the game board. It
        # also displays information about each ghost (fantasma) in the game, including their position
        # and state.
        ventana1.withdraw()
        ventana8 = Toplevel()
        ventana8.title("Ventana Inspector")
        ventana8.geometry("800x800")
        ventana8.configure(background="black")
        canvasC8 = tk.Canvas(ventana8, width=800, height=680, borderwidth=0, highlightthickness=0, background="black")
        canvasC8.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        canvasC10 = tk.Canvas(ventana8, width=800, height=680, borderwidth=0, highlightthickness=0, background="white")
        canvasC10.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        titulo= tk.Label(canvasC8, text="Inspeccion", fg=("Yellow"), font=("Courier New", 12, "bold"), bg=("black"))
        titulo.place(x=308, y=110)
        ventana8.resizable(height=False, width=False)
        ventana8.update()

        texto= tk.Label(canvasC8, text=f"Puntaje:{Partida.score}",font=("Courier New", 12, "bold"), fg=("white"), bg=("black"), justify=tk.LEFT)
        texto.place(x=35, y=25)

        texto1= tk.Label(canvasC8, text=f"Nombre jugador:{entryNombre}",font=("Courier New", 12, "bold"), fg=("white"), bg=("black"), justify=tk.LEFT)
        texto1.place(x=35, y=5)

        

        etiqueta = tk.Label(canvasC10, text="Matriz:", font=("Courier New", 6, "bold"), fg=("white"), bg=("black"), justify=tk.LEFT)
        etiqueta.pack()

        for fila in Partida.tablero:
            texto_fila = " ".join(map(str, fila))
            fila_label = tk.Label(canvasC10, text=texto_fila,font=("Courier New", 6, "bold"), fg=("white"), bg=("black"), justify=tk.LEFT)
            fila_label.pack()
        
        for FantasmaAux in Partida.Fantasmas:
                global rojo,naranja,rosado, celeste
                if FantasmaAux.color == rojo:
                    Posiciony= FantasmaAux.posicion_y
                    Posicionx= FantasmaAux.posicion_x
                    Estado = FantasmaAux.estado
                    texto1= tk.Label(canvasC8, text=f"Fantasma rojo:\nPosicion en y: {Posiciony}\nPosicion en x: {Posicionx}\nEstado: {Estado}",font=("Courier New", 12, "bold"), fg=("white"), bg=("black"), justify=tk.LEFT)
                    texto1.place(x=35, y=65)
                if FantasmaAux.color == naranja:
                    Posiciony= FantasmaAux.posicion_y
                    Posicionx= FantasmaAux.posicion_x
                    Estado = FantasmaAux.estado
                    texto1= tk.Label(canvasC8, text=f"Fantasma naranja:\nPosicion en y: {Posiciony}\nPosicion en x: {Posicionx}\nEstado: {Estado}",font=("Courier New", 12, "bold"), fg=("white"), bg=("black"), justify=tk.LEFT)
                    texto1.place(x=35, y=155)
                if FantasmaAux.color == celeste:
                    Posiciony= FantasmaAux.posicion_y
                    Posicionx= FantasmaAux.posicion_x
                    Estado = FantasmaAux.estado
                    texto1= tk.Label(canvasC8, text=f"Fantasma celeste:\nPosicion en y: {Posiciony}\nPosicion en x: {Posicionx}\nEstado: {Estado}",font=("Courier New", 12, "bold"), fg=("white"), bg=("black"), justify=tk.LEFT)
                    texto1.place(x=35, y=255)
                if FantasmaAux.color == rosado:
                    Posiciony= FantasmaAux.posicion_y
                    Posicionx= FantasmaAux.posicion_x
                    Estado = FantasmaAux.estado
                    texto1= tk.Label(canvasC8, text=f"Fantasma rosado:\nPosicion en y: {Posiciony}\nPosicion en x: {Posicionx}\nEstado: {Estado}",font=("Courier New", 12, "bold"), fg=("white"), bg=("black"), justify=tk.LEFT)
                    texto1.place(x=35, y=345)

       
        Jugadorx =  Partida.Jugador.x
        Jugadory =  Partida.Jugador.y
        JugadorEs = Partida.Jugador.capsula 

        texto9= tk.Label(canvasC8, text=f"Jugador:\nPosicion en y: {Jugadory}\nPosicion en x: {Jugadorx}\nCapsula: {JugadorEs}",font=("Courier New", 12, "bold"), fg=("white"), bg=("black"), justify=tk.LEFT)
        texto9.place(x=35, y=440)


        

            
           
        
        #Botón de back Ventana Inspector
        def back():
            """
            The function "back" creates a button labeled "Back" that, when clicked, destroys the window
            named "ventana8".
            """
            ventana8.destroy()
  
        botonBack = tk.Button(ventana8, text="Back", command= back, font=("Courier New", 12, "bold"), fg=("white"), bg=("black"), width=8)
        botonBack.pack()
        botonBack.place(x=650, y=420)


    #Ventana JUEGO
    def Ventana_juego(nivel):
        """
        The function "Ventana_juego" creates a game window using the Pygame library and also creates a
        separate Tkinter window for an inspector mode.
        
        :param nivel: The parameter "nivel" represents the level of the game. It is used in the function
        "Ventana_juego" to determine the difficulty or complexity of the game
        """
        pygame.init()
        ventana = pygame.display.set_mode((ventana_ancho, ventana_alto))
        pygame.display.set_caption("PacMan")
        font = pygame.font.Font(None, 36)
        clock = pygame.time.Clock()
        
        # Crear otra ventana de Tkinter
        ventana_inspector = Toplevel()
        ventana_inspector.title("Modo Inspector")
        # Establecer la geometría con las coordenadas de posición
        ventana_inspector.geometry(f"150x55+{252}+{2}")
        ventana_inspector.configure(background="black")
        ventana_inspector.resizable(height=False, width=False)
        
        boton7 = tk.Button(ventana_inspector, text="Inspector", command=abrirventana_inspector,font=("Courier New", 16, "bold"), fg=("yellow"), bg=("black"))
        boton7.pack()
        boton7.place(x=10, y=10)

        
        #Funcion para dibujar tablero de juego
        """
            The function "show_score" draws a rectangle on the screen and displays the current score in
            yellow color.
            """
        
        global Partida
        def show_score():
            
           # The above code is drawing a rectangle on a pygame window. The rectangle is positioned at
           # coordinates (0, 600) with a width of 300 and a height of 100. The color of the rectangle
           # is black.
            pygame.draw.rect(ventana, negro, (0 , 600, 300, 100))
            score_text = font.render(f"Score: {Partida.score}", True, amarillo)
            
            ventana.blit(score_text, (10, 600))
            
            
        def nombre():
            """
            The function "nombre" sets the global variable "nombreJugadorActual" to the value of the
            entry "entryNombre" and displays the player's name on the screen.
            """
            global nombreJugadorActual
            if(entryNombre != ""):
                NombreJugador = str(entryNombre)
                nombreJugadorActual = str(entryNombre)
            juganombre = font.render(f"Jugador: {NombreJugador}", True, amarillo)
            ventana.blit(juganombre, (10, 620))

       
       
        tableroJuego = [
                [4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 2, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 3, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                [2, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1],
                [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 2, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],

                    ]
        

        # The above code is creating a PacMan game. It creates a PacMan player object and a list of
        # ghost objects. Depending on the level, it adds different types of ghosts to the list. Then,
        # it creates a game object and initializes it with the game board, level, score, player
        # object, and list of ghost objects. Finally, it starts the game by calling the `Juego`
        # function twice with the same parameters.
        Jugador = PacMan(0, 0, 0)
        ListaFantasmas = []
        if nivel == 2:
            ListaFantasmas.append(Fantasma(rojo))
            ListaFantasmas.append(Fantasma(naranja))
        ListaFantasmas.append(Fantasma(rojo))
        ListaFantasmas.append(Fantasma(naranja))
        ListaFantasmas.append(Fantasma(rosado))
        ListaFantasmas.append(Fantasma(celeste))
        Partida = Juego(tableroJuego,1,0, Jugador, ListaFantasmas)
        Partida = Juego(tableroJuego,1,0, Jugador, ListaFantasmas)

        def mover(fantasma,velocidad):
            """
            The function `mover` moves a ghost character randomly on a game board until a certain
            condition is met, and then prints a message indicating the end of the game.
            
            :param fantasma: The "fantasma" parameter represents an instance of a ghost object in a game.
            It is used to control the movement of the ghost
            :param velocidad: The "velocidad" parameter represents the speed at which the ghost moves. It
            is a measure of the time delay between each movement of the ghost. The smaller the value of
            "velocidad", the faster the ghost moves
            """
            global MoverFantasmas
            global Partida
            # The above code is a Python while loop that controls the movement of ghosts in a game.
            while MoverFantasmas and fantasma.estado:
                try:
                    time.sleep(velocidad)
                    direccion = random.choice(["izquierda", "derecha", "arriba", "abajo"])
                    
                    if direccion == "izquierda":
                        fantasma.moverIzquierda(Partida.tablero,Partida.Jugador.x, Partida.Jugador.y, Partida.Jugador.capsula)
                    elif direccion == "derecha":
                        fantasma.moverDerecha(Partida.tablero, Partida.Jugador.x, Partida.Jugador.y, Partida.Jugador.capsula)
                    elif direccion == "arriba":
                        fantasma.moverArriba(Partida.tablero, Partida.Jugador.x, Partida.Jugador.y, Partida.Jugador.capsula)
                    elif direccion == "abajo":
                        fantasma.moverAbajo(Partida.tablero, Partida.Jugador.x, Partida.Jugador.y, Partida.Jugador.capsula)
                except Exception as e:
                    # Maneja la excepción aquí, por ejemplo, imprime un mensaje de error
                    print(f"Error en el hilo: {e}")
            fantasma.estado = False
            contadorFantasmasVivos = 0
            for FantasmaAux in Partida.Fantasmas:
                if FantasmaAux.estado:
                    contadorFantasmasVivos += 1

            if MoverFantasmas == False and contadorFantasmasVivos == 0:
                
                
                print("Se acabo el juego")
                           
                
                

        # The above code is creating a thread for each ghost in the "Partida.Fantasmas" list. It sets
        # the speed of the thread based on the color of the ghost. Then it starts the execution of
        # each thread. After that, it loads an image of a player and scales it to a specific size.
        for fantasma in Partida.Fantasmas:
            # Crea un objeto de hilo
            veloc= 0.5
            if fantasma.color==rojo:
                veloc=0.25
            hilo = threading.Thread(target=mover,args=(fantasma,veloc))

            # Inicia la ejecución del hilo
            hilo.start()

            

        jugador_imagen = pygame.image.load("jugador.png") 
        jugador_imagen = pygame.transform.scale(jugador_imagen, (tamano_casilla, tamano_casilla))

       
            
        #Funcion para dibujar tablero de juego
        def dibujar_tablero():
            """
            The function `dibujar_tablero()` draws a game board using different shapes and colors based
            on the values in the `Partida.tablero` array.
            """
           # The above code is drawing different shapes on a Pygame window based on the values in the
           # `Partida.tablero` array. It uses nested loops to iterate over each element in the array
           # and draws a rectangle or a circle based on the value of the element. The color and size
           # of the shapes vary depending on the value.
            for fila in range(filas):
                for columna in range(columnas):
                    if Partida.tablero[fila][columna]==0:
                        pygame.draw.rect(ventana, azul, (columna * tamano_casilla, fila * tamano_casilla, tamano_casilla, tamano_casilla))
                    elif Partida.tablero[fila][columna]==1:
                        x = columna * tamano_casilla + tamano_casilla // 2
                        y = fila * tamano_casilla + tamano_casilla // 2
                        radio = tamano_casilla // 4
                        pygame.draw.rect(ventana, negro, (columna * tamano_casilla, fila * tamano_casilla, tamano_casilla, tamano_casilla))
                        pygame.draw.circle(ventana, amarillo, (x, y), radio)
                    elif Partida.tablero[fila][columna]==2:
                        x = columna * tamano_casilla + tamano_casilla // 2
                        y = fila * tamano_casilla + tamano_casilla // 2
                        radio = tamano_casilla // 2
                        pygame.draw.rect(ventana, negro, (columna * tamano_casilla, fila * tamano_casilla, tamano_casilla, tamano_casilla))
                        pygame.draw.circle(ventana, blanco, (x, y), radio)
                    elif Partida.tablero[fila][columna]==3:
                        x = columna * tamano_casilla + tamano_casilla // 2
                        y = fila * tamano_casilla + tamano_casilla // 2
                        radio = tamano_casilla // 3
                        pygame.draw.rect(ventana, negro, (columna * tamano_casilla, fila * tamano_casilla, tamano_casilla, tamano_casilla))
                        pygame.draw.circle(ventana, naranja, (x, y), radio)
                    elif Partida.tablero[fila][columna]==4:
                        pygame.draw.rect(ventana, negro, (columna * tamano_casilla, fila * tamano_casilla, tamano_casilla, tamano_casilla))
                    
                    
                
            # The above code is rendering the player and the ghosts on the game window. It first sets
            # the position of the player using the `topleft` attribute of the player's rectangle.
            # Then, it loads the image of each ghost based on its color and scales it to the size of a
            # game tile. The position of each ghost is set using the `topleft` attribute of its
            # rectangle. Finally, the player and the ghosts are blitted onto the game window using the
            # `blit()` function.
            jugador_rect = jugador_imagen.get_rect()
            jugador_rect.topleft = (Jugador.x * tamano_casilla, Jugador.y * tamano_casilla)
            ventana.blit(jugador_imagen, jugador_rect.topleft)

            for fantasmaR in Partida.Fantasmas:
                fantasma_Aux = pygame.image.load("rojo.png")
                if fantasmaR.color == rosado:
                    fantasma_Aux = pygame.image.load("rosado.png")
                elif fantasmaR.color == naranja:
                    fantasma_Aux = pygame.image.load("naranja.png")
                elif fantasmaR.color == celeste:
                    fantasma_Aux = pygame.image.load("celeste.png")
                elif fantasmaR.color == blanco:
                    fantasma_Aux = pygame.image.load("blanco.png")
                    
                fantasma_Aux = pygame.transform.scale(fantasma_Aux, (tamano_casilla, tamano_casilla))
                fantasma = fantasma_Aux.get_rect()
                fantasma.topleft = (fantasmaR.posicion_x * tamano_casilla, fantasmaR.posicion_y * tamano_casilla)
                ventana.blit(fantasma_Aux, fantasma.topleft)    
             
        # Funcion para boton regresar del juego
        def boton_regresar():
            """
            The function `boton_regresar` is a part of a larger program that includes a game board and a
            button to return to a previous window.
            """
             # Alineado en la parte inferior
            pygame.draw.rect(ventana, negro, (button_x, button_y, button_width, button_height))
            font = pygame.font.Font(None, 25)
            button_text = font.render("Regresar", True, amarillo)
            text_rect = button_text.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2))
            ventana.blit(button_text, text_rect.topleft)
        

       # The above code is an infinite loop that listens for events in a Pygame window. If the event
       # type is pygame.QUIT, it quits the Pygame window and exits the program. If all the values in
       # the Partida.tablero are not equal to 1, it displays a "Juego Ganado" message in the center of
       # the window, waits for 2 seconds, quits the Pygame window, and brings the ventana1 window to
       # the front. If the event type is pygame.MOUSEBUTTONDOWN and the mouse click is within the
       # specified button coordinates, it quits the Pygame window and brings
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if all(all(valor !=2 for valor in fila) for fila in Partida.tablero):     
                    fuente = pygame.font.Font(None, 36)
                    mensaje = fuente.render("¡Juego Ganado!", True, blanco)
                    ventana.blit(mensaje, (ventana_ancho // 2 - mensaje.get_width() // 2, ventana_alto // 2 - mensaje.get_height() // 2))
                    pygame.display.flip()
                    time.sleep(2)
                    pygame.quit()
                    ventana1.deiconify()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if (button_x <= event.pos[0] <= button_x + button_width and button_y <= event.pos[1] <= button_y + button_height):
                        # Regresar a la Ventana1
                        pygame.quit()
                        ventana1.deiconify()

                # Regresar a la Ventana
                pygame.display.flip()
                clock.tick(10)

                
                #Control de movimiento de Pac-Man
               # The above code is checking for key presses in the pygame window. If the up arrow key
               # is pressed and the player's y-coordinate is greater than 0 and the value in the game
               # board at the position above the player is not 0, then it performs certain actions
               # based on the value in the game board at that position. If the value is 1, it updates
               # the game board, increases the score by 2, and calls the function "agarrar_nombre()".
               # If the value is 2, it updates the game board and sets the player's "capsula"
               # attribute to
                keys = pygame.key.get_pressed()
            global MoverFantasmas
            if keys[pygame.K_UP] and Jugador.y > 0 and Partida.tablero[Jugador.y - 1][Jugador.x] != 0:
                
                if Partida.tablero[Jugador.y - 1][Jugador.x] == 1:
                    Partida.tablero[Jugador.y - 1][Jugador.x] = 4
                    Partida.score+=2
                    agarrar_nombre()
                    
                elif Partida.tablero[Jugador.y - 1][Jugador.x] == 2:
                    Partida.tablero[Jugador.y - 1][Jugador.x] = 4
                    Jugador.capsula = True  # Suponiendo que hay una variable en la clase Jugador para representar si la cápsula está activa

                    #Definir una función para cambiar la cápsula a False después de 10 segundos
                    def desactivar_capsula():
                        time.sleep(10)
                        Jugador.capsula = False

                    # Iniciar un hilo para ejecutar la función desactivar_capsula
                   # The above code is creating a new thread called "hilo_capsula" and starting it.
                   # The thread is executing the function "desactivar_capsula". After starting the
                   # thread, the code iterates over a list called "ListaFantasmas" and checks if each
                   # "fantasma" object has the attribute "capsula" set to True. If it does, the code
                   # sets the "capsula" attribute of that "fantasma" object to False.
                    hilo_capsula = Thread(target=desactivar_capsula)
                    hilo_capsula.start()
                    for fantasma in ListaFantasmas:
                        if fantasma.capsula:
                            fantasma.capsula = False

                # The code is checking if the value at the position (Jugador.y - 1, Jugador.x) in the
                # Partida.tablero (game board) is equal to 3. If it is, then it updates the value at
                # that position to 4, increments the Partida.score by 4, and calls the function
                # agarrar_nombre().
                elif Partida.tablero[Jugador.y - 1][Jugador.x] == 3:
                    Partida.tablero[Jugador.y - 1][Jugador.x] = 4 
                    Partida.score+=4 
                    agarrar_nombre()
                
                # The above code is updating the position of a player in a game. It subtracts 1 from
                # the player's y-coordinate. Then, it checks if any of the ghosts in the game have the
                # same x and y coordinates as the player. If a ghost is found at the player's position
                # and the player does not have a power-up capsule, a variable called MoverFantasmas is
                # set to False. If a ghost is found at the player's position and the player has a
                # power-up capsule, the ghost's state is set to False and a new ghost is added to a
                # list called
                Jugador.y -= 1
                for FantasmaAux in Partida.Fantasmas:
                    if FantasmaAux.posicion_x == Jugador.x and FantasmaAux.posicion_y == Jugador.y  and Jugador.capsula == False :
                        MoverFantasmas=False
                        
                    elif FantasmaAux.posicion_x == Jugador.x and FantasmaAux.posicion_y == Jugador.y  and Jugador.capsula == True :
                       FantasmaAux.estado=False
                       ListaFantasmas.append(Fantasma(rojo))
           # The above code is checking if the down arrow key is pressed and if the player's
           # y-coordinate is less than 39 and if the tile below the player on the game board is not
           # equal to 0. If these conditions are met, the code checks the value of the tile below the
           # player. If the value is 1, it changes the value to 4, increases the score by 2, and calls
           # the function "agarrar_nombre()". If the value is 2, it changes the value to 4 and sets
           # the player's "capsula" attribute to True.
            if keys[pygame.K_DOWN] and Jugador.y < 39  and Partida.tablero[Jugador.y + 1][Jugador.x] != 0:
                
                if Partida.tablero[Jugador.y + 1][Jugador.x] == 1:
                    Partida.tablero[Jugador.y + 1][Jugador.x] = 4
                    Partida.score+=2
                    agarrar_nombre()
               
                elif Partida.tablero[Jugador.y + 1][Jugador.x] == 2:
                    Partida.tablero[Jugador.y + 1][Jugador.x] = 4
                    Jugador.capsula = True  # Suponiendo que hay una variable en la clase Jugador para representar si la cápsula está activa

                         # Definir una función para cambiar la cápsula a False después de 10 segundos
                    def desactivar_capsula():
                        """
                        The function "desactivar_capsula" waits for 10 seconds and then sets the
                        "capsula" attribute of the "Jugador" object to False.
                        """
                        time.sleep(10)
                        Jugador.capsula = False

                    # Iniciar un hilo para ejecutar la función desactivar_capsula
                   # The above code is creating a new thread called "hilo_capsula" and starting it.
                   # The thread is executing the function "desactivar_capsula". After starting the
                   # thread, the code iterates over a list called "ListaFantasmas" and checks if each
                   # "fantasma" object has the attribute "capsula" set to True. If it does, the code
                   # sets the "capsula" attribute of that "fantasma" object to False.
                    hilo_capsula = Thread(target=desactivar_capsula)
                    hilo_capsula.start()
                    for fantasma in ListaFantasmas:
                        if fantasma.capsula:
                            fantasma.capsula = False
                    #Setear el capsula del jugador en true
                    #e iniciamos un hilo sleep 10 segundos y cambia otra vez la capsula a false

                # The above code is checking if the value at the position (Jugador.y + 1, Jugador.x)
                # in the Partida.tablero (game board) is equal to 3. If it is, then it sets the value
                # at that position to 4, increments the Partida.score by 4, and calls the function
                # agarrar_nombre().
                elif Partida.tablero[Jugador.y + 1][Jugador.x] == 3:
                    Partida.tablero[Jugador.y + 1][Jugador.x] = 4
                    Partida.score+=4
                    agarrar_nombre()
                    
                Jugador.y += 1

                # The above code is iterating through a list of ghosts in a game called "Partida". It
                # checks if the position of each ghost matches the position of the player (Jugador)
                # and if the player has a capsule (Jugador.capsula). If the player does not have a
                # capsule, the variable "MoverFantasmas" is set to False. If the player does have a
                # capsule, the state of the ghost (FantasmaAux.estado) is set to False and the ghost
                # is added to a list called "ListaFantasmas".
                for FantasmaAux in Partida.Fantasmas:
                    if FantasmaAux.posicion_x == Jugador.x and FantasmaAux.posicion_y == Jugador.y  and Jugador.capsula == False :
                       MoverFantasmas=False
                    elif FantasmaAux.posicion_x == Jugador.x and FantasmaAux.posicion_y == Jugador.y  and Jugador.capsula == True :
                       FantasmaAux.estado=False
                       ListaFantasmas.append(Fantasma(rojo))
            # The above code is checking if the left arrow key is pressed, the player's x-coordinate
            # is greater than 0, and the value in the game board at the player's current y-coordinate
            # and x-coordinate minus 1 is not equal to 0. If these conditions are met, the code
            # performs different actions based on the value in the game board at the new position.
            if keys[pygame.K_LEFT] and Jugador.x > 0 and Partida.tablero[Jugador.y][Jugador.x - 1] != 0:
                
                if Partida.tablero[Jugador.y][Jugador.x - 1] == 1:
                    Partida.tablero[Jugador.y][Jugador.x - 1] = 4
                    Partida.score+=2
                    agarrar_nombre()
                    
                elif Partida.tablero[Jugador.y][Jugador.x - 1] == 2:
                    Partida.tablero[Jugador.y][Jugador.x - 1] = 4
                    Jugador.capsula = True  # Suponiendo que hay una variable en la clase Jugador para representar si la cápsula está activa

                    # Definir una función para cambiar la cápsula a False después de 10 segundos
                    def desactivar_capsula():
                        time.sleep(10)
                        Jugador.capsula = False

                    # Iniciar un hilo para ejecutar la función desactivar_capsula
                    hilo_capsula = Thread(target=desactivar_capsula)
                    hilo_capsula.start()
                    for fantasma in ListaFantasmas:
                        if fantasma.capsula:
                            fantasma.capsula = False
                    #Setear el capsula del jugador en true
                    #e iniciamos un hilo sleep 10 segundos y cambia otra vez la capsula a false
                    

               # The above code is checking if the value at the position (Jugador.y, Jugador.x - 1) in
               # the Partida.tablero list is equal to 3. If it is, then it sets the value at that
               # position to 4, increments the Partida.score by 4, and calls the function
               # agarrar_nombre().
                elif Partida.tablero[Jugador.y][Jugador.x - 1] == 3:
                    Partida.tablero[Jugador.y][Jugador.x - 1] = 4
                    Partida.score+=4
                    agarrar_nombre()
                    
                # The code is checking for keyboard input to move the player character (Jugador) to
                # the left or right. If the player character collides with a ghost character
                # (FantasmaAux), the behavior depends on whether the player character has a power-up
                # (capsula) or not. If the player character has a power-up, the ghost character is
                # removed from the game (FantasmaAux.estado=False). If the player character does not
                # have a power-up, the game ends (MoverFantasmas=False). Additionally, if the player
                # character moves onto a specific tile (Partida.tablero[Jugador
                Jugador.x -= 1
                for FantasmaAux in Partida.Fantasmas:
                    if FantasmaAux.posicion_x == Jugador.x  and FantasmaAux.posicion_y == Jugador.y and Jugador.capsula == False :
                       MoverFantasmas=False
                    elif FantasmaAux.posicion_x == Jugador.x and FantasmaAux.posicion_y == Jugador.y and Jugador.capsula == True :
                       FantasmaAux.estado=False
                       ListaFantasmas.append(Fantasma(rojo))

            if keys[pygame.K_RIGHT] and Jugador.x < 35 and Partida.tablero[Jugador.y][Jugador.x + 1] != 0:
                
                if Partida.tablero[Jugador.y][Jugador.x + 1] == 1:
                    Partida.tablero[Jugador.y][Jugador.x + 1] = 4
                    Partida.score+=2
                    
                elif Partida.tablero[Jugador.y][Jugador.x + 1] == 2:
                    Partida.tablero[Jugador.y][Jugador.x + 1] = 4
                    Jugador.capsula = True  # Suponiendo que hay una variable en la clase Jugador para representar si la cápsula está activa

                         # Definir una función para cambiar la cápsula a False después de 10 segundos
                    def desactivar_capsula():
                        time.sleep(10)
                        Jugador.capsula = False

                    # Iniciar un hilo para ejecutar la función desactivar_capsula
                    hilo_capsula = Thread(target=desactivar_capsula)
                    hilo_capsula.start()
                    for fantasma in ListaFantasmas:
                        if fantasma.capsula:
                            fantasma.capsula = False
                    #Setear el capsula del jugador en true
                    #e iniciamos un hilo sleep 10 segundos y cambia otra vez la capsula a false

                elif Partida.tablero[Jugador.y][Jugador.x + 1] == 3:
                    Partida.tablero[Jugador.y][Jugador.x + 1] = 4
                    Partida.score+=4
                    
                Jugador.x += 1
                for FantasmaAux in Partida.Fantasmas:
                    if FantasmaAux.posicion_x == Jugador.x and FantasmaAux.posicion_y == Jugador.y and Jugador.capsula == False :
                       MoverFantasmas=False
                    elif FantasmaAux.posicion_x == Jugador.x and FantasmaAux.posicion_y == Jugador.y and Jugador.capsula == True :
                       FantasmaAux.estado=False
                       ListaFantasmas.append(Fantasma(rojo))

            boton_regresar()
            
        
                # Controlar la velocidad de actualización
            clock.tick(5)

            show_score()
            nombre() 
            dibujar_tablero()
            pygame.display.update()



            #Soluciono el error del boton y pausa el juego cuando abrimos la ventana inspector
            ventana_inspector.update()
        

    
    
    def abrirventana3():
        """
        The function "abrirventana3" opens a new window titled "Salon de la fama" with a black
        background.
        """
        menuRank = Tk()
        menuRank.title('Salon de la fama')
        fondo = Canvas(menuRank, width=800, height=500, border=0, bg='black')
        fondo.pack()

           
        # Regresar a la ventana principal
        def regresa():
            """
            The function "regresa" is used to destroy a menu window and display the main window, and it
            also creates a button to go back to the main window.
            """
            menuRank.destroy()
            ventana1.deiconify()
         #boton regresar
        botonRegre = tkinter.Button(fondo, text="❌", command=regresa)
        botonRegre.pack()
        botonRegre.place(x=30 , y=30)

        # The above code is trying to open a file named 'data.txt' and read its contents. It then
        # splits the contents by comma and prints them. It sorts the contents in descending order
        # using the natsorted function. It then creates a table on the screen displaying the top 5
        # scores from the sorted list. Each score is displayed in a separate label with its
        # corresponding position.
        try: #trata de abrir el domcunento con los puntajes y los recrea en la pantalla una tabla de los mejores
            file = open('data.txt','r')
            read = file.read().split(',')
            print(read)
            top= natsorted(read,reverse=True)
            print(top)
            puesto1 = Label(fondo,text=f'1) {top[0]}',width=15, height=1,font=('Courier New', 21, 'italic', 'bold'),bg='black',fg='yellow')
            puesto1.place(x=320, y=25)
            puesto2 = Label(fondo,text=f'2) {top[1]}',width=15, height=2, font=('Courier New', 21, 'italic', 'bold'),bg='black',fg='yellow')
            puesto2.place(x=320, y=100)
            puesto3 = Label(fondo,text=f'3) {top[2]}', width=15, height=2, font=('Courier New', 21, 'italic', 'bold'),bg='black',fg='yellow')
            puesto3.place(x=320, y=200)
            puesto4 = Label(fondo,text=f'4) {top[3]}', width=15, height=2, font=('Courier New', 21, 'italic', 'bold'),bg='black',fg='yellow')
            puesto4.place(x=320, y=300)
            puesto5 = Label(fondo,text=f'5) {top[4]}', width=15, height=2, font=('Courier New', 21, 'italic', 'bold'),bg='black',fg='yellow')
            puesto5.place(x=320, y=400)

        except:
            None

        menuRank.mainloop()
        
        
    
    #Fución abrir ventana de Configuración
    def abrirventana4():
        """
        The function "abrirventana4" opens a new window titled "Ventana 4" with a specific size,
        background color, and a canvas with a label for "Sonido".
        """
        ventana1.withdraw()
        ventana4 = Toplevel()
        ventana4.title("Ventana 4")
        ventana4.geometry("800x480")
        ventana4.configure(background="black")
        canvasC4 = tk.Canvas(ventana4, width=800, height=680, borderwidth=0, highlightthickness=0, background="black")
        canvasC4.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        titulo= tk.Label(canvasC4, text="Sonido", font=("Courier New", 16, "bold"), background="black", fg="yellow")
        titulo.place(x=330 ,y=170)
        ventana4.resizable(height=False, width=False)
        

        # Botón de play
        botonP = Button(ventana4, text="Play", font=("Courier New", 12, "bold"), command=play, fg=("yellow"), bg=("black"), width=8)
        botonP.pack()
        botonP.place(x=500, y=300)
        
        # Botón de stop music
        botonBack = tk.Button(ventana4, text="Stop Music", font=("Courier New", 12, "bold"), command=stop_music, fg=("yellow"), bg=("black"), width=12)
        botonBack.pack()
        botonBack.place(x=600, y=300)

        #Botón de back Ventana Configuración
        def back():
            ventana4.destroy()
            ventana1.deiconify()
  
        botonBack = tk.Button(ventana4, text="Back", command= back, font=("Courier New", 12, "bold"), fg=("yellow"), bg=("black"), width=8)
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
    
        titulo= tk.Label(canvasC4, text="Controles", font=("Courier New", 15, "bold"), fg=("yellow"), bg=("black"))
        titulo.place(x=310, y=120)
        ventana5.resizable(height=False, width=False)

        texto= tk.Label(canvasC4, text="Mover hacia arriba: W "
                                        "\nMover hacia abajo: X" 
                                        "\nMover hacia la derecha: D"
                                        "\nMover hacia la izquierda: A"
                                        
                                ,font=("Courier New", 12, "bold"), fg=("yellow"), bg=("black"), justify=tk.LEFT)
        texto.place(x=50, y=180)

        image= Image.open("Teclado1.png")
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

        botonBack = tk.Button(ventana5, text="Back", command= back, fg=("yellow"), font=("Courier New", 12, "bold"), bg=("black"), width=8)
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
        titulo= tk.Label(canvasC4, text="Informacion Personal", fg=("yellow"), font=("Courier New", 12, "bold"), bg=("black"))
        titulo.place(x=308, y=110)
        ventana6.resizable(height=False, width=False)
        
        
         #informacion de la ventana
        titulo2=tkinter.Label(canvasC4, text= "\nProgramadores:"
                                            "\n Joselyn María Salas Ramírez"
                                            " \n Edad: 19 años"
                                            "\n Carnet: 2023210441."
                                            "\n"
                                            "\n Ian Yoel Gómez Oses"
                                            " \n Edad: 18 años"
                                            "\n Carnet: 2023216136."
                              , font=("Courier New", 12), fg= "yellow", bg="black")
        titulo2.place(x=250, y=200)
        
   
    
    #Botón de back Ventana "Acerca de"
        def back():
            ventana6.destroy()
            ventana1.deiconify()
            
        botonBack = tk.Button(ventana6, text="Back", font=("Courier New", 12, "bold"), command= back, fg=("white"), bg=("black"), width=8 )
        botonBack.pack()
        botonBack.place(x=650, y=420)
        
        abrirventana6.mainloop()

    
    #Botones Principales VENTANA 1
   # The above code is creating a GUI (Graphical User Interface) using the Tkinter library in Python.
   # It creates a window (ventana1) and adds several buttons to it. Each button has a specific text,
   # font, color, and command associated with it. The commands are functions that will be executed
   # when the buttons are clicked. The buttons are placed at specific coordinates on the window using
   # the place() method. Finally, the mainloop() function is called to start the event loop and
   # display the window.
    boton1 = tk.Button(ventana1, text="Jugar", command=ventana_nombre,font=("Courier New", 16, "bold"), fg=("yellow"), bg=("black"))
    boton1.place(x=353, y=50)
    boton2 = tk.Button(ventana1, text="Música",command=abrirventana4, font=("Courier New", 16, "bold"), fg=("yellow"), bg=("black"))
    boton2.place(x=300, y=420)
    boton3 = tk.Button(ventana1, text="Ayuda", command=abrirventana5, font=("Courier New", 14, "bold"), fg=("yellow"), bg=("black"))
    boton3.place(x=30, y=420)
    boton4 = tk.Button(ventana1, text="Mejores Puntajes",command=abrirventana3, font=("Courier New", 16, "bold"), fg=("yellow"), bg=("black"))
    boton4.place(x=280, y=110)
    boton5 = tk.Button(ventana1, text="Acerca de", command=abrirventana6, font=("Courier New", 14, "bold"), fg=("yellow"), bg=("black"))
    boton5.place(x=650, y=420)
    
    ventana1.mainloop() 
ventana_inicio()
