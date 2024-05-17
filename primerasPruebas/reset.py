import os
import argparse

tty_device = "/dev/usbtmc2"  

def NOEwrite(tty_fd, msg):
    print(msg)
    try:
        os.write(tty_fd, msg.encode())
        print(f"Mensaje enviado...")
    except OSError as e:
        print(f"Error al enviar el mensaje: {e}")
    finally:
        os.close(tty_fd)

# Abre el descriptor de fichero a un instrumento: devuelve el descriptor de fichero
def NOEopen(tty_path):
    # Abrimos el descriptor de fichero del instrumento
    try:
        tty_fd = os.open(tty_path, os.O_WRONLY)
    except OSError as error:
        print(f"ERROR: No se pudo abrir el dispositivo TTY: {error}")
        exit(1)
    finally:
        return tty_fd

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Programacion sabrosa de osciloscopiote...")
    parser.add_argument("usb_path", help="Ruta al dispositivo")
    parser.add_argument("message", help="Mensajinho")

    args = parser.parse_args()

tty_fd = NOEopen(args.usb_path)
NOEwrite(tty_fd, "*RST\n")