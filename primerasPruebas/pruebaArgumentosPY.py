import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Enviar un mensaje a un dispositivo TTY.")
    parser.add_argument("tty_device", help="Ruta al dispositivo TTY")
    parser.add_argument("message", help="Mensaje a enviar")

    args = parser.parse_args()

print("Aqui estamos operativos" + args.tty_device)