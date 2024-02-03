# Importamos los módulos necesarios
import tkinter as tk
import math
import datetime
import pygame

global segundero
segundero = None
global lienzo
lienzo = None


# Creamos la ventana principal
ventana = tk.Tk()
ventana.title("Reloj del Ratoncito Azul")

# Creamos el lienzo donde dibujaremos el reloj
lienzo = tk.Canvas(ventana, width=300, height=300)
lienzo.pack()
# Creamos una función que reproduce el sonido de tic tac cada segundo
pygame.init()
sonido=pygame.mixer.Sound("tictac.mp3")

def move_hour_and_minute_hands():
    global lienzo
    
    # Borramos las antiguas manecillas
    lienzo.delete("hour_hand", "minute_hand")
    # Obtenemos la hora y los minutos actuales
    hora = datetime.datetime.now().hour
    minuto = datetime.datetime.now().minute

    # Calculamos el ángulo que deben tener las manecillas
    angulo_hora = (hora % 12 + minuto / 60) * math.pi / 6
    angulo_minuto = minuto * math.pi / 30

    # Calculamos las coordenadas de los extremos de las manecillas
    x_hora = 150 + 50 * math.sin(angulo_hora)
    y_hora = 150 - 50 * math.cos(angulo_hora)
    x_minuto = 150 + 75 * math.sin(angulo_minuto)
    y_minuto = 150 - 75 * math.cos(angulo_minuto)

    # Dibujamos las manecillas
    lienzo.create_line(150, 150, x_hora, y_hora, width=3, fill="black", tags="hour_hand")
    lienzo.create_line(150, 150, x_minuto, y_minuto, width=2, fill="black", tags="minute_hand")

    # Llamamos a la función move_hour_and_minute_hands() cada segundo
    ventana.after(1000, move_hour_and_minute_hands)

# Llamamos a la función move_hour_and_minute_hands
move_hour_and_minute_hands()

def update_digital_time():
    global lienzo
    
    # Borramos la hora digital anterior
    lienzo.delete("digital_time")
    # Obtenemos la hora actual
    hora_digital = datetime.datetime.now().strftime("%H:%M:%S")
    #Creamos 
    lienzo.create_rectangle(100, 260, 200, 290, fill="#F0E68C", outline="#F0E68C")
    # Dibujamos la hora digital actualizada
    lienzo.create_text(150, 275, text=hora_digital, font=("Arial", 16), tags="digital_time")

    # Llamamos a la función update_digital_time() cada segundo
    ventana.after(1000, update_digital_time)

# Llamamos a la función update_digital_time
update_digital_time()


def tic_tac():
    if ventana.winfo_exists():
        sonido.play()
        ventana.after(1000, tic_tac)  # Llama a tic_tac después de 1000 ms (1 segundo)

# Configurar el evento de cierre de la ventana
def on_closing():
    ventana.destroy()

ventana.protocol("WM_DELETE_WINDOW", on_closing)
 

# Movemos la manecilla de los segundos cada segundo
def move_segundero():

    global segundero 
    global lienzo
    # Obtenemos los segundos actuales
    segundo = datetime.datetime.now().second

    # Calculamos el ángulo que debe tener la manecilla de los segundos
    angulo_segundo = segundo * math.pi / 30

    # Calculamos las coordenadas del extremo de la manecilla de los segundos
    x_segundo = 150 + 80 * math.sin(angulo_segundo)
    y_segundo = 150 - 80 * math.cos(angulo_segundo)

    # Borramos la manecilla de los segundos anterior
    lienzo.delete(segundero)

    # Dibujamos la manecilla de los segundos actualizada
    segundero = lienzo.create_line(150, 150, x_segundo, y_segundo, width=1, fill="red")

    # Llamamos a la función move_segundero() cada segundo
    ventana.after(1000, move_segundero)



# Llamamos a la función tic_tac
tic_tac()


# Dibujamos el círculo que representa la esfera del reloj
lienzo.create_oval(50, 50, 250, 250, fill="#F0E68C", outline="#F0E68C")

# Cargamos la imagen de ratón gracioso
raton = tk.PhotoImage(file="ratoncito.png")

# Reducimos el tamaño del ratón a un tercio
raton = raton.subsample(3)

# Colocamos la imagen de ratón en el centro del reloj
lienzo.create_image(150, 150, image=raton)


#Dibujamos el secundero
move_segundero()

def calcular_coordenadas(angulo, distancia):
    x = 150 + distancia * math.cos(math.radians(angulo))
    y = 150 + distancia * math.sin(math.radians(angulo))
    return x, y



# Lista de ángulos para los números del reloj
angulos = [270, 300, 330, 0, 30, 60, 90, 120, 150, 180, 210, 240]

# Crear las coordenadas y los números del reloj
for i, angulo in enumerate(angulos):
    x, y = calcular_coordenadas(angulo, 90)
    numero = (i + 11) % 12 + 1  # Ajuste para comenzar en 12
    lienzo.create_text(x, y, text=str(numero), font=("Arial", 16))

# Dibujamos las rayas de los minutos
for i in range(60):
    angulo = i * math.pi / 30
    x1 = 150 +90 * math.sin(angulo)
    y1 = 150 -90 * math.cos(angulo)
    x2 = 150 +100 * math.sin(angulo)
    y2 = 150 -100 * math.cos(angulo)
    lienzo.create_line(x1, y1, x2, y2, width=2, fill="black")









# Iniciamos el bucle principal de la ventana
ventana.mainloop()
