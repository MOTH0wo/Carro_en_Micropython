from machine import Pin, PWM, UART
import time

# Pines de los motores (Ajustar segun tu configuracion)
IN1 = Pin(5, Pin.OUT)
IN2 = Pin(6, Pin.OUT)
IN3 = Pin(9, Pin.OUT)
IN4 = Pin(10, Pin.OUT)

# PWM para velocidad (frecuencia 1000 Hz)
ENA = PWM(Pin(3), freq=1000)
ENB = PWM(Pin(11), freq=1000)

velocidad = 150  # rango 0-255 (se escalará a 0-1023 para PWM)

# Configuración del Bluetooth serie (UART)
# Ajusta los pines según tu conexión (TX=17, RX=16)
uart = UART(2, baudrate=9600, tx=17, rx=16, timeout=100)

# Función de control de velocidad
def set_velocidad(val):
    # Escala de 0-255 a 0-1023 (duty de PWM)
    duty = int(val * 1023 / 255)
    ENA.duty(duty)
    ENB.duty(duty)

# Movimientos
def adelante():
    set_velocidad(velocidad)      # Resetea ambos motores a la misma velocidad
    IN1.value(1)
    IN2.value(0)
    IN3.value(1)
    IN4.value(0)

def retroceder():
    set_velocidad(velocidad)
    IN1.value(0)
    IN2.value(1)
    IN3.value(0)
    IN4.value(1)

def girar_izquierda():
    set_velocidad(velocidad)
    IN1.value(0)
    IN2.value(1)
    IN3.value(1)
    IN4.value(0)

def girar_derecha():
    set_velocidad(velocidad)
    IN1.value(1)
    IN2.value(0)
    IN3.value(0)
    IN4.value(1)

def diagonal_izquierda_adelante():
    # Motor izquierdo a media velocidad, derecho a velocidad completa
    ENA.duty(int((velocidad // 2) * 1023 / 255))
    ENB.duty(int(velocidad * 1023 / 255))
    IN1.value(1)
    IN2.value(0)
    IN3.value(1)
    IN4.value(0)

def diagonal_derecha_adelante():
    # Motor izquierdo a velocidad completa, derecho a media
    ENA.duty(int(velocidad * 1023 / 255))
    ENB.duty(int((velocidad // 2) * 1023 / 255))
    IN1.value(1)
    IN2.value(0)
    IN3.value(1)
    IN4.value(0)

def diagonal_izquierda_atras():
    ENA.duty(int((velocidad // 2) * 1023 / 255))
    ENB.duty(int(velocidad * 1023 / 255))
    IN1.value(0)
    IN2.value(1)
    IN3.value(0)
    IN4.value(1)

def diagonal_derecha_atras():
    ENA.duty(int(velocidad * 1023 / 255))
    ENB.duty(int((velocidad // 2) * 1023 / 255))
    IN1.value(0)
    IN2.value(1)
    IN3.value(0)
    IN4.value(1)

def detener():
    IN1.value(0)
    IN2.value(0)
    IN3.value(0)
    IN4.value(0)

# Lectura de comandos Bluetooth
def leer_comando():
    if uart.any():
        b = uart.read(1)          # Lee un byte
        if b:
            c = b.decode()        # Convierte a carácter
            if c.isdigit():       # Si es número, se espera una línea con nueva velocidad
                linea = uart.readline()   # Lee hasta '\n'
                if linea:
                    try:
                        nueva_vel = int(linea.decode().strip())
                        global velocidad
                        velocidad = max(100, min(255, nueva_vel))
                        set_velocidad(velocidad)
                        print("Velocidad:", velocidad)
                    except:
                        pass
            else:                 # Comando de una sola letra
                print("Comando:", c)
                if c == 'F':
                    adelante()
                elif c == 'B':
                    retroceder()
                elif c == 'L':
                    girar_izquierda()
                elif c == 'R':
                    girar_derecha()
                elif c == 'G':
                    diagonal_izquierda_adelante()
                elif c == 'I':
                    diagonal_derecha_adelante()
                elif c == 'H':
                    diagonal_izquierda_atras()
                elif c == 'J':
                    diagonal_derecha_atras()
                elif c == 'S':
                    detener()

# Inicialización y bucle principal
set_velocidad(velocidad)

while True:
    leer_comando()
    time.sleep_ms(10)   # Pequeño retardo para no saturar el bucle
