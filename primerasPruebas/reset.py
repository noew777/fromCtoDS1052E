import os
import time
import argparse

tty_device = "/dev/usbtmc2"  

def NOEwrite(tty_fd, msg):
    try:
        os.write(tty_fd, msg.encode())
    except OSError as e:
        print(f"Error al enviar el mensaje: {e}")

def NOEread(tty_fd, num_bytes):
    try:
        data = os.read(tty_fd, num_bytes)
        return data.decode()
    except OSError as e:
        print(f"Error al leer los datos: {e}")
        return None

def NOEopen(tty_path):
    try:
        tty_fd = os.open(tty_path, os.O_RDWR)
        return tty_fd
    except OSError as error:
        print(f"ERROR: No se pudo abrir el dispositivo TTY: {error}")
        exit(1)

def NOEclose(tty_fd):
    try:
        os.close(tty_fd)
    except OSError as e:
        print(f"Error al cerrar el descriptor de archivo: {e}")

# # # # # # # # MAIN # # # # # # # #  
tty_fd = NOEopen("/dev/usbtmc2")
NOEwrite(tty_fd, "*IDN?\n")
print(NOEread(tty_fd, 90))
NOEclose(tty_fd)