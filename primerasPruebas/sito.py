import os
import argparse

def NOEwrite(tty_fd, msg):
    try:
        os.write(tty_fd, msg.encode())
        print("Mensaje enviado...")
    except OSError as e:
        print(f"Error al enviar el mensaje: {e}")

def NOEread(tty_fd, num_bytes):
    try:
        data = os.read(tty_fd, num_bytes)
        print(f"Datos recibidos: {data.decode()}")
        return data
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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Programacion sabrosa de osciloscopiote...")
    parser.add_argument("usb_path", help="Ruta al dispositivo")
    parser.add_argument("message", help="Mensajinho")
    parser.add_argument("num_bytes", type=int, help="Número de bytes a leer")

    args = parser.parse_args()

    tty_fd = NOEopen(args.usb_path)
    
    # Escribir el mensaje en el dispositivo TTY
    NOEwrite(tty_fd, "*IDN?\n")
    
    # Leer datos del dispositivo TTY
    data = NOEread(tty_fd, 90)
    
    # Cerrar el descriptor de archivo
    NOEclose(tty_fd)
