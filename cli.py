import sys
def main():
    # sys.argv[0] es siempre el nombre del archivo ("main.py")
    # Validamos que se hayan pasado suficientes argumentos
    if len(sys.argv) < 1:
        print("[GITHUB-ACTIVITY]: Para buscar la actividad de un usuario introdusca un username. Uso: python main.py <username>")
        return

    elif len(sys.argv) > 2:
        print("[ERROR]: El programa solo recibe un parametro. Uso: python main.py <username>")
        return
    username = sys.argv[1] # Captura del username

    return username
