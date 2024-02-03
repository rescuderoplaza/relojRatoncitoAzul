import tkinter as tk
import math
import datetime
import pygame

class RelojRaton:
    def __init__(self):
        self.segundero = None
        self.lienzo = None

        self.ventana = tk.Tk()
        self.ventana.title("Reloj del Ratoncito Azul")

        self.lienzo = tk.Canvas(self.ventana, width=300, height=300)
        self.lienzo.pack()

        pygame.init()
        self.sonido = pygame.mixer.Sound("tictac.mp3")

        self.move_hour_and_minute_hands()
        self.update_digital_time()
        self.tic_tac()
        self.move_segundero()

        self.ventana.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.lienzo.create_oval(50, 50, 250, 250, fill="#F0E68C", outline="#F0E68C")
        raton = tk.PhotoImage(file="ratoncito.png").subsample(3)
        self.lienzo.create_image(150, 150, image=raton)

        self.set_numbers_clock()
        self.draw_minute_lines()

        self.ventana.mainloop()

    def move_hour_and_minute_hands(self):
        self.lienzo.delete("hour_hand", "minute_hand")
        hora = datetime.datetime.now().hour
        minuto = datetime.datetime.now().minute

        angulo_hora = (hora % 12 + minuto / 60) * math.pi / 6
        angulo_minuto = minuto * math.pi / 30

        x_hora = 150 + 50 * math.sin(angulo_hora)
        y_hora = 150 - 50 * math.cos(angulo_hora)
        x_minuto = 150 + 75 * math.sin(angulo_minuto)
        y_minuto = 150 - 75 * math.cos(angulo_minuto)

        self.lienzo.create_line(150, 150, x_hora, y_hora, width=3, fill="black", tags="hour_hand")
        self.lienzo.create_line(150, 150, x_minuto, y_minuto, width=2, fill="black", tags="minute_hand")

        self.ventana.after(1000, self.move_hour_and_minute_hands)

    def update_digital_time(self):
        self.lienzo.delete("digital_time")
        hora_digital = datetime.datetime.now().strftime("%H:%M:%S")
        self.lienzo.create_rectangle(100, 260, 200, 290, fill="#F0E68C", outline="#F0E68C")
        self.lienzo.create_text(150, 275, text=hora_digital, font=("Arial", 16), tags="digital_time")

        self.ventana.after(1000, self.update_digital_time)

    def tic_tac(self):
        if self.ventana.winfo_exists():
            self.sonido.play()
            self.ventana.after(1000, self.tic_tac)

    def on_closing(self):
        self.ventana.destroy()

    def move_segundero(self):
        segundo = datetime.datetime.now().second
        angulo_segundo = segundo * math.pi / 30
        x_segundo = 150 + 80 * math.sin(angulo_segundo)
        y_segundo = 150 - 80 * math.cos(angulo_segundo)

        self.lienzo.delete(self.segundero)
        self.segundero = self.lienzo.create_line(150, 150, x_segundo, y_segundo, width=1, fill="red")

        self.ventana.after(1000, self.move_segundero)

    def set_numbers_clock(self):
        for i in range(12):
            angulo = (i - 3) * math.pi / 6
            distancia = 90
            x = 150 + distancia * math.cos(angulo)
            y = 150 + distancia * math.sin(angulo)
            numero = (i + 11) % 12 + 1
            self.lienzo.create_text(x, y, text=str(numero), font=("Arial", 16))

    def draw_minute_lines(self):
        for i in range(60):
            angulo = i * math.pi / 30
            x1 = 150 + 90 * math.sin(angulo)
            y1 = 150 - 90 * math.cos(angulo)
            x2 = 150 + 100 * math.sin(angulo)
            y2 = 150 - 100 * math.cos(angulo)
            self.lienzo.create_line(x1, y1, x2, y2, width=2, fill="black")

# Crear una instancia de la clase RelojRaton
reloj = RelojRaton()
