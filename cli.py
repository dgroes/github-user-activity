import sys

# C03: Colores en terminal
ROJO = "\033[0;38;2;227;79;79;49m"
ROJO_B = "\033[1;38;2;227;79;79;49m"
VERDE = "\033[0;38;2;98;243;57;49m"
AMARILLO = "\033[0;38;2;243;228;57;49m"
AMARILLO_I = "\033[3;38;2;243;228;57;49m"
AZUL = "\033[94m"
RESET = "\033[0m"
ROSA_B = "\033[1;38;2;241;129;243;49m"

def main():
    # sys.argv[0] es siempre el nombre del archivo ("main.py")
    # Validamos que se hayan pasado suficientes argumentos
    if len(sys.argv) < 2:
        print(f"{ROSA_B}[GITHUB-ACTIVITY]{RESET}: Para buscar la actividad de un usuario introdusca un username. Uso: python main.py <{AMARILLO_I}username{RESET}>")
        sys.exit(1)

    elif len(sys.argv) > 2:
        print(f"{ROJO_B}[ERROR]{RESET}: El programa solo recibe un parametro. Uso: python main.py <{AMARILLO_I}username{RESET}>")
        sys.exit(1)

    username = sys.argv[1] # Captura del username

    return username
